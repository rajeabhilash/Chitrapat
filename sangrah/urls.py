from django.urls import path, include
from sangrah.views import index, movie_list,movie_detail

app_name = "sangrah"

urlpatterns = [
    path(route='', view=index, name="home"), # type: ignore
    path(route='movies/', view=movie_list, name="movie_list"), # type: ignore
    path(route='movie/<int:id>', view=movie_detail, name="movie_detail"), # type: ignore
]
