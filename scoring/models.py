from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    score_a = models.IntegerField()
    score_b = models.IntegerField()
    score_c = models.IntegerField()
    score_d = models.IntegerField()

    def __str__(self):
        return self.question_text

class UserResponse(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)  # Stores 'A', 'B', 'C', or 'D'
    score = models.IntegerField()

    def __str__(self):
        return f"User {self.user_id} - Question {self.question.id} - Answer {self.answer}"