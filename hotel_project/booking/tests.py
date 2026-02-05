from django.test import TestCase

from .services import create_booking, create_room  # Исправленные имена здесь


class HotelBookingTest(TestCase):
    def setUp(self):
        """Создаем тестовые данные"""
        # Используем новое имя функции: create_room
        self.room = create_room(description="Стандартный двухместный", price=3000.00)

    def test_room_creation(self):
        """Проверяем создание номера"""
        self.assertEqual(self.room.description, "Стандартный двухместный")
        self.assertEqual(float(self.room.price), 3000.00)

    def test_booking_creation(self):
        """Проверяем создание брони через сервис"""
        booking = create_booking(
            room_id=self.room.id, date_start="2026-05-10", date_end="2026-05-15"
        )
        self.assertEqual(booking.room.id, self.room.id)
        self.assertEqual(str(booking.date_start), "2026-05-10")
