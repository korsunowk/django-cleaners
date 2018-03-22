from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from customers.models import Customer
from cleaners.models import Cleaner
from assignment import settings

from .models import Booking
from .forms import BookingForm

# Create your views here.


class BookingCreation(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'

    def form_valid(self, form):
        new_data = form.cleaned_data
        free_cleaner = Cleaner.objects.filter(towns=new_data.get('towns'))\
            .exclude(booking__date=new_data.get('date'))

        if free_cleaner.exists():
            customer_exist = Customer.objects.filter(
                phone_number=new_data.get('phone_number')).exists()
            cleaner = free_cleaner.first()

            if customer_exist:
                customer = Customer.objects.get(
                    phone_number=new_data.get('phone_number'))
            else:
                customer = Customer.objects.create(
                    first_name=new_data.get('first_name'),
                    last_name=new_data.get('last_name'),
                    phone_number=new_data.get('phone_number')
                )
            Booking.objects.create(
                customer=customer,
                cleaner_id=cleaner.pk,
                date=new_data.get('date')
            )
            cleaner_name = "{0} {1}".format(cleaner.first_name,
                                            cleaner.last_name)
            messages.success(
                request=self.request,
                message=settings.SUCCESS_BOOKING_MESSAGE % cleaner_name)

            return redirect(to=reverse_lazy('bookings:new'))

        messages.error(request=self.request,
                       message=settings.FAILED_BOOKING_MESSAGE)
        return super(BookingCreation, self).form_invalid(form)
