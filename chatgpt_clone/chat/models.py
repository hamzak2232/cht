from django.db import models

class Chat(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    role = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessage(models.Model):
    user_prompt = models.TextField()
    chatbot_response = models.TextField()
    timestamp_prompt = models.DateTimeField(auto_now_add=True)
    timestamp_response = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id} - User Prompt: {self.user_prompt}"

