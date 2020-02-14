from reservations import views as reservation_views
from django.urls import path


app_name = "reservations"

urlpatterns = [
    path(
        "create/<int:room>/<int:year>-<int:month>-<int:day>",
        reservation_views.create,
        name="create",
    ),
    path("<int:pk>", reservation_views.ReservationDetailView.as_view(), name="detail",),
    path("<int:pk>/<str:verb>/", reservation_views.edit_reservation, name="edit",),
]

