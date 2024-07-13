from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats import views
from cats.views import cat_detail, cat_list, CatViewSet


router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   # path('cats/', cat_list),
   # path('cats/<int:pk>/', cat_detail),

   # path('cats/', views.APICat.as_view()),
   # path('cats/<int:pk>/', views.APICatDetail.as_view()),

   # path('cats/', views.CatList.as_view()),
   # path('cats/<int:pk>/', views.CatDetail.as_view()),

   path('', include(router.urls)),
]


