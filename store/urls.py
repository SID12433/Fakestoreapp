from django.urls import path
from rest_framework.routers import DefaultRouter
from store import views
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("category",views.CategoryView,basename="category")
router.register("products",views.ProductView,basename="product")

urlpatterns = [
    path("token/",ObtainAuthToken.as_view()),
    path("register/",views.UserCreationView.as_view())
 
]+router.urls
