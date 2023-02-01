from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet, api_group, api_group_detail

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token,
         name='api_token'),
    path('api/v1/groups/', api_group),
    path('api/v1/groups/<int:pk>/', api_group_detail)

]
