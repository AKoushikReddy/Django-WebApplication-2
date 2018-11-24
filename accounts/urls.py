from django.urls import path
from .views import register_user, edit_user
from .views import change_pass, update_profile, home
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Login URL
    # Url for all users, First displayed page.
    path("welcome/", LoginView.as_view(template_name="accounts/home.html")),

    path('home/', home, name="home"),

    # Logout  URL Redirecting to Login URL
    path("logout/", LogoutView.as_view(next_page='/welcome'), name="logout"),

    # Registration Form URL
    path("register/", register_user, name="register"),

    # Edit Account information  Form URL
    path("edit_info/", edit_user, name="edit_info"),
    # Change Password
    path("edit_pass/", change_pass, name="edit_pass"),

    # UserProfile Link
    path("profile/", update_profile, name="profile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
