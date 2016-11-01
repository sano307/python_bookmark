from django.shortcuts import render

from django.views.generic import ListView, DetailView       # 제네틱 뷰 사용
from bookmark.models import Bookmark        # 테이블 조회

# Create your views here.

# --- ListView


class BookmarkLV(ListView):     # 레코드 리스트
    model = Bookmark

# --- DetailView


class BookmarkDV(DetailView):   # 특정 레코드에 대한 상세 정보
    model = Bookmark