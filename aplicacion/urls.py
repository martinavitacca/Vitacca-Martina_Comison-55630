from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import * 

urlpatterns = [
    path('', home, name="home"), 
    path('seinen/', seinen, name="seinen"),
    path('shounen/', shounen, name="shounen"),
    path('manhwa/', manhwa, name="manhwa"),
    path('shoujo/', shoujo, name="shoujo"),
    path('about/', about, name="about"),
  
    # CRUD Class Based View of review
    path('review/', ReviewList.as_view(), name="review"),
    path('add_review/', ReviewCreate.as_view(), name="add_review"),
    path('edit_review/<int:pk>/', ReviewUpdate.as_view(), name="edit_review"),
    path('delete_review/<int:pk>/', ReviewDelete.as_view(), name="delete_review"),

    # Update/Delete
    path('update_seinen/<seinen_id>/', updateSeinen, name="update_seinen"),
    path('delete_seinen/<int:pk>/', SeinenDelete.as_view(), name="delete_seinen"),
    path('update_shounen/<shounen_id>/', updateShounen, name="update_shounen"),
    path('delete_shounen/<int:pk>/', ShounenDelete.as_view(), name="delete_shounen"),
    path('update_manhwa/<manhwa_id>/', updateManhwa, name="update_manhwa"),
    path('delete_manhwa/<int:pk>/', ManhwaDelete.as_view(), name="delete_manhwa"),
    path('update_shoujo/<shoujo_id>/', updateShoujo, name="update_shoujo"),
    path('delete_shoujo/<int:pk>/', ShoujoDelete.as_view(), name="delete_shoujo"),

    # CRUD Manga custom entry
    path('manga/', manga, name="manga"),
    path('add_manga/', createManga, name="add_manga"),
    path('edit_manga/<int:pk>/', MangaUpdate.as_view(), name="edit_manga"),
    path('delete_manga/<int:pk>/', MangaDelete.as_view(), name="delete_manga"),


    # Login/Logout/Register
    path('login/', user_login, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),


    # Edit profile/avatar
    path('edit_profile/', editUserProfile, name="edit_profile"),
    path('add_avatar/', addAvatar, name="add_avatar"),


    # Searcher
    path('found_seinen/', searchSeinen, name="found_seinen"),
    path('found_shounen/', searchShounen, name="found_shounen"),
    path('found_manhwa/', searchManhwa, name="found_manhwa"),
    path('found_shoujo/', searchShoujo, name="found_shoujo"),
]