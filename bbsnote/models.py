from django.db import models

class Board(models.Model): #게시글모델
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self): #객체를호출하면 제목에 내용으로 나타내 주겠다
        return self.subject

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


