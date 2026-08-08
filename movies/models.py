from django.db import models


class Movie(models.Model):

    CATEGORY = [
        ('Action','Action'),
        ('Sci-Fi','Sci-Fi'),
        ('Horror','Horror'),
        ('Comedy','Comedy'),
        ('Marvel','Marvel'),
        ('Thriller','Thriller'),
    ]


    title = models.CharField(max_length=200)

    year = models.CharField(max_length=10)

    genre = models.CharField(
        max_length=100,
        choices=CATEGORY
    )

    story = models.TextField()

    poster = models.ImageField(
        upload_to="posters/"
    )

    video = models.FileField(
        upload_to="videos/",
        blank=True
    )


    def __str__(self):
        return self.title
