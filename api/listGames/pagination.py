from rest_framework import pagination
from rest_framework.response import Response
import math

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': math.ceil(self.page.paginator.count/50),
            'results': data
        })