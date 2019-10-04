# urls.py
# ...
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
router.register('choices', PollViewSet, base_name='choises')
router.register('votes', PollViewSet, base_name='votes')




urlpatterns = [
    # ...
]

urlpatterns += router.urls