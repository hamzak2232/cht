from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_prompt', 'chatbot_response', 'timestamp_prompt', 'timestamp_response')
    search_fields = ('user_prompt', 'chatbot_response')
