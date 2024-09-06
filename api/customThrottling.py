from rest_framework.throttling import SimpleRateThrottle
from rest_framework.exceptions import Throttled


class CustomThrottle(SimpleRateThrottle):
    scope = 'No_of_requests'

    def get_cache_key(self, request, view):
        # Throttle based on client IP
        return self.get_ident(request)

    # Override the throttled method to return a custom message
    def throttled(self, request, wait):
        custom_message = f"You cannot send more then 3 requests in a minute. Please wait {wait} seconds before trying again."
        raise Throttled(detail=custom_message)
        