from django.utils.deprecation import MiddlewareMixin
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime
from api.models import CustomUser

class UpdateIPAddressMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            ip = x_forwarded_for.split(',')[-1].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')           
            if request.user.last_login_ip != ip:
                request.user.last_login_ip = ip
                request.user.save()


class JWTAuthenticationMiddleware:
    """
    Custom middleware to decode JWT token and set request.user before views are called.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get token from Authorization header
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return self.get_response(request)
        
        try:
            # Token should start with 'Bearer '
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]  # Extract token
            else:
                raise AuthenticationFailed('Invalid token format')

            # Decode the token using the same secret key as in SimpleJWT
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            # Get the user ID from the decoded token
            user_id = decoded_token.get('user_id')

            if not user_id:
                raise AuthenticationFailed('Token does not contain user id')

            # Set the user to request.user
            user = CustomUser.objects.get(id=user_id)
            request.user = user
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('Error decoding token')
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('User not found')

        # Continue processing the request
        response = self.get_response(request)
        return response
