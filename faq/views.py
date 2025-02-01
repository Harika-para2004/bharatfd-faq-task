from django.shortcuts import render

# Create your views here.
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'request': request})
        cache.set(cache_key, serializer.data, timeout=3600)  # Cache for 1 hour
        return Response(serializer.data)
