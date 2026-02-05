from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer


@api_view(["POST"])
def add_room(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        room = serializer.save()
        return Response({"room_id": room.id})  # Возвращает ID как в требовании
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return Response({"status": "deleted"})


@api_view(["GET"])
def get_rooms(request):
    """Список номеров с сортировкой по цене или дате"""
    sort_by = request.GET.get("sort_by", "created_at")  # По умолчанию по дате
    order = request.GET.get("order", "asc")

    prefix = "" if order == "asc" else "-"

    rooms = Room.objects.all().order_by(f"{prefix}{sort_by}")
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_booking(request):
    data = request.data.copy()
    if "room_id" in data:
        data["room"] = data["room_id"]

    serializer = BookingSerializer(data=data)
    if serializer.is_valid():
        booking = serializer.save()
        return Response({"booking_id": booking.id})
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return Response({"status": "deleted"})


@api_view(["GET"])
def get_bookings(request):
    room_id = request.GET.get("room_id")
    if not room_id:
        return Response({"error": "room_id is required"}, status=400)

    bookings = Booking.objects.filter(room_id=room_id).order_by("date_start")

    result = [
        {"booking_id": b.id, "date_start": b.date_start, "date_end": b.date_end}
        for b in bookings
    ]
    return Response(result)
