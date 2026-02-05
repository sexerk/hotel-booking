from django.urls import path

from . import views

urlpatterns = [
    # Номера
    path("rooms/add", views.add_room),
    path("rooms/list", views.get_rooms),
    path("rooms/delete/<int:room_id>", views.delete_room),
    # Бронирования
    path("bookings/create", views.add_booking),
    path("bookings/list", views.get_bookings),
    path("bookings/delete/<int:booking_id>", views.delete_booking),
]
