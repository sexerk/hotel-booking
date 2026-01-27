from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import Room, Booking



def create_room(description, price):
    """Создать новый номер отеля"""
    if price <= 0:
        raise ValidationError("Цена должна быть больше нуля")

    return Room.objects.create(
        description=description,
        price=price
    )


def delete_room_with_bookings(room_id):
    """Удалить номер и все его бронирования"""
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return True


def get_rooms_list(sort_by='created_at', order='asc'):
    """Получить отсортированный список номеров"""
    direction = '' if order == 'asc' else '-'
    if sort_by not in ['price', 'created_at']:
        sort_by = 'created_at'

    return Room.objects.all().order_by(f"{direction}{sort_by}")



def create_booking(room_id, date_start, date_end):
    """Создать бронь для конкретного номера"""
    room = get_object_or_404(Room, id=room_id)

    if date_start >= date_end:
        raise ValidationError("Дата начала должна быть раньше даты окончания")

    return Booking.objects.create(
        room=room,
        date_start=date_start,
        date_end=date_end
    )


def delete_booking(booking_id):
    """Удалить конкретную бронь"""
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return True


def get_bookings_for_room(room_id):
    """Получить список броней номера, отсортированный по дате начала"""
    return Booking.objects.filter(room_id=room_id).order_by('date_start')