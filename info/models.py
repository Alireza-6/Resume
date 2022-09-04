from django.db import models


def image_upload_path():
    result = 'profile'
    return result


class SiteSetting(models.Model):
    copyright_text = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.copyright_text}'


class PersonalInfo(models.Model):
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    about_me = models.TextField()
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    profile_image = models.ImageField(upload_to=image_upload_path())
    phone = models.CharField(max_length=11)
    linkedin = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Badge(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, null=True)
    description_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Skill(Badge):
    order = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Familiarity(Badge):
    pass

    def __str__(self):
        return f'{self.name}'


class Worked(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
