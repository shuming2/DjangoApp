from django.db import models
import django.utils.timezone as timezone
import uuid


class Question(models.Model):
    question_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text


class User(models.Model):
    session = models.UUIDField(default=uuid.uuid4())
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.session)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.answer_text



