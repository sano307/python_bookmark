from __future__ import unicode_literals # Python 2.x 지원용

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Bookmark( models.Model ):
    # 최대 길이 100byte, 공백과 null 값을 가질 수도 있다.
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    # 객체를 문자열로 표현
    def __str__(self):
        return self.title