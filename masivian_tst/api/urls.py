from rest_framework import routers

from .views import BinaryTreeViewSet

router = routers.SimpleRouter()
router.register(r'bt', BinaryTreeViewSet)
urlpatterns = []
urlpatterns += router.urls
