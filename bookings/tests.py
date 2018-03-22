from django.test import TestCase, Client
from django.core.urlresolvers import reverse_lazy
from decimal import Decimal

from towns.models import Town
from cleaners.models import Cleaner
from customers.models import Customer
from .models import Booking


class BookingTestCase(TestCase):
    """
    TestCase for testings sign up customer with creation a booking
    """
    def setUp(self):
        """
        Initialize testings data
        """
        self.town = Town.objects.create(name='New York')

        self.cleaners = list()
        self.client = Client()

        self.first_test_date = '2010-12-12 12:12'
        self.second_test_date = '2011-11-11 11:11'

        for i in range(2):
            new_cleaner = Cleaner.objects.create(
                first_name='Cleaner %d' % i,
                last_name='Cleaner %d' % i,
                quality_score=Decimal(i)
            )
            new_cleaner.towns.add(self.town)
            self.cleaners.append(new_cleaner)

    def test_bookings(self):
        """
        Test first sign up with creation a booking,
        test second sign up with creation a booking with another Cleaner,
        test failed new creation a booking, cause doesn't have a free cleaner
        :return: 
        """
        test_data = {
            'first_name': 'Customer 1',
            'last_name': 'Customer 2',
            'phone_number': '111111111',
            'date': self.first_test_date,
            'towns': self.town.pk
        }
        response = self.client.post(reverse_lazy('bookings:new'),
                                    data=test_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Customer.objects.count(), 1)

        self.client.post(reverse_lazy('bookings:new'),
                         data=test_data)
        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(Customer.objects.count(), 1)

        response = self.client.post(reverse_lazy('bookings:new'),
                                    data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('messages' in response.context)
