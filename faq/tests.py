# from django.test import TestCase

# # Create your tests here.
# import pytest
# from faq.models import FAQ

# @pytest.mark.django_db
# def test_faq_model_auto_translate():
#     faq = FAQ.objects.create(question="How does caching work?", answer="It stores data temporarily.")
    
#     print("Generated Hindi:", faq.question_hi)
#     print("Generated Bengali:", faq.question_bn)

#     assert faq.question_hi is not None
#     assert faq.question_bn is not None
#     assert "कैशिंग" in faq.question_hi  # Looser check for Hindi
#     assert "ক্যাশিং" in faq.question_bn or "ক্যাচিং" in faq.question_bn  # Looser check for Bengali

# # from rest_framework.test import APIClient
# # import pytest

# # @pytest.mark.django_db
# # def test_faq_api():
# #     client = APIClient()

# #     # Create test FAQ
# #     FAQ.objects.create(question="What is Django?", answer="A web framework.")

# #     # Fetch default FAQs (English)
# #     response = client.get("/api/faqs/")
# #     assert response.status_code == 200
# #     assert "What is Django?" in response.json()[0]["question"]

# #     # Fetch FAQs in Hindi
# #     response = client.get("/api/faqs/?lang=hi")
# #     assert response.status_code == 200
# #     assert "Django क्या है?" in response.json()[0]["question"]


import pytest
from faq.models import FAQ
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_faq_model_auto_translate():
    """
    Test that the FAQ model automatically translates the question field
    into Hindi and Bengali upon creation.
    """
    faq = FAQ.objects.create(question="How does caching work?", answer="It stores data temporarily.")
    
    # Debugging prints (can be removed later)
    print("Generated Hindi:", faq.question_hi)
    print("Generated Bengali:", faq.question_bn)
    
    # Ensure translations exist
    assert faq.question_hi is not None
    assert faq.question_bn is not None
    
    # Validate translations (adjust if translation output varies)
    assert "कैशिंग कैसे काम करता है?" in faq.question_hi  # Hindi translation check
    assert "ক্যাচিং কীভাবে কাজ করে?" in faq.question_bn  # Bengali translation check

@pytest.mark.django_db
def test_faq_api():
    """
    Test the FAQ API endpoint to ensure it returns correct responses
    in different languages.
    """
    client = APIClient()

    # Create test FAQ entry
    FAQ.objects.create(question="What is Django?", answer="A web framework.")

    # Fetch default FAQs (English)
    response = client.get("/api/faqs/")
    assert response.status_code == 200
    print("Response JSON:", response.json())  # Debug print
    assert "What is Django?" in response.json()[0]["question"]

    # Fetch FAQs in Hindi
    response = client.get("/api/faqs/?lang=hi")
    assert response.status_code == 200
    print("Response in Hindi:", response.json())  # Debug print
    # Now checking 'translated_question' instead of 'question'
    assert "Django क्या है?" in response.json()[0]["translated_question"]

    # Fetch FAQs in Bengali
    response = client.get("/api/faqs/?lang=bn")
    assert response.status_code == 200
    print("Response in Bengali:", response.json())  # Debug print
    # Check for the actual Bengali translation
    assert "জ্যাঙ্গো কী?" in response.json()[0]["translated_question"]
