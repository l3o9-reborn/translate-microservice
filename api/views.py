from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pydantic import BaseModel
import argostranslate.translate

class TranslateAPIView(APIView):
    def post(self, request):
        text = request.data.get("text")
        source = request.data.get("source")
        target = request.data.get("target")
        
        if not text or not source or not target:
            return Response({"error": "text, source, and target are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            translated = argostranslate.translate.translate(text, source, target)
            return Response({"translatedText": translated})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
