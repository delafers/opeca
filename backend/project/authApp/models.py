from django.db import models



class UsersEmails(models.Model):
    id = models.IntegerField("unique id mail", unique=True, primary_key=True, max_length=16)
    email = models.CharField("email", max_length=128)

class Post(models.Model):
    theme = models.CharField(verbose_name="Заголовок", max_length=511)
    img = models.ImageField(upload_to="media/")


class File(models.Model):
    name = models.CharField(verbose_name="File name", max_length=255)
    file = models.FileField(upload_to="media/mediacia/")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, verbose_name='Post', related_name='files')

    def __str__(self):
        return self.name


class Ref(models.Model):
    name = models.CharField(verbose_name="ref name",  max_length=255)
    ref = models.CharField(max_length=511)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, verbose_name='Post', related_name='refs')


class Post2(models.Model):
    theme = models.CharField(verbose_name="Заголовок вложенного поста", max_length=511)
    img = models.ImageField(upload_to="media/", null=True)
    parent = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, verbose_name='ParentPost', related_name='children')


class File2(models.Model):
    name = models.CharField(verbose_name="File name", max_length=255)
    file = models.FileField(upload_to="media/mediacia/")
    post2 = models.ForeignKey('Post2', on_delete=models.CASCADE, null=True, verbose_name='Post2', related_name='files')

    def __str__(self):
        return self.name


class Ref2(models.Model):
    name = models.CharField(verbose_name="ref name",  max_length=255)
    ref = models.CharField(max_length=511)
    post2 = models.ForeignKey('Post2', on_delete=models.CASCADE, null=True, verbose_name='Post2', related_name='refs')
