# Uncomment the imports before you add the code
# from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    # login
    path('login', views.login_user, name='login'),

    # logout (nếu có)
    path('logout', views.logout_user, name='logout'),

    # dealers
    path('get_dealers', views.get_dealerships, name='get_dealers'),

    # reviews
    path('reviews', views.get_reviews, name='reviews'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
