from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer
# from django.core.mail import send_mail

@api_view(['POST'])
def post_create_contact(request):
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the contact to the database
            # subject = "Contact Received"
            # message_body = "We have received your message. We will get back to you within 2 business days."
            # from_email = '"Contact-JKDaily" <hi@jkdaily.in>'
            # recipient_email = serializer.validated_data.get('email', '')
            # send_mail(subject, message_body, from_email, [recipient_email], fail_silently=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
