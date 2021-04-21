from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('room_list/', views.roomListView, name="RoomListView"),
    path('booking_list/', views.BookingList.as_view(), name="BookingList"),
    path('room/<category>/', views.RoomDetailView.as_view(), name="RoomDetailView"),
    path('booking/cancel/<pk>/', views.CancelBookingView.as_view(), name="CancelBookingView"),
    path('register/', views.register, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_user, name="logout"),
    # path('room_detail/<int:pk>', views.RoomDetailView.as_view(), name="room_detail_view"), # miro shit

]

# from django.urls import path
# from .views import BookingListView, RoomDetailView, CancelBookingView, CheckoutView, success_view, cancel_view, BookingFormView, contact_us
# app_name = 'hotel'

# urlpatterns = [
#     path('', BookingFormView.as_view(), name='BookingFormView'),
#     path('booking_list/', BookingListView.as_view(), name='BookingListView'),
#     path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
#     path('booking/cancel/<pk>', CancelBookingView.as_view(),
#          name='CancelBookingView'),
#     path('checkout/', CheckoutView.as_view(), name='CheckoutView'),
#     path('success/', success_view, name='success_view'),
#     path('cancel/', cancel_view, name='cancel_view'),
#     path('contact-us/', contact_us, name="contact_us")

# ]