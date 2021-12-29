from django.urls import path, include
from django.urls.resolvers import URLPattern

from app.views import CategoryOperation, Exception404notFound


urlpatterns = [
    # Exceptions URL
    path("warning/", Exception404notFound.as_view(), name="warning"),

    # Currency URL
    # path("currency/<int:shop_id>/", )

    # Category URl
    path("category/<int:shop_id>", CategoryOperation.as_view(), name="category-view"),
    path("update-category/<int:shop_id>/<int:id>/", CategoryOperation.as_view(), name="update-category"),
]