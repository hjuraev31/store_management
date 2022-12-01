from django.urls import path, re_path
from . views import home, getDetails, add_truck, create_product, update_product, getDetailsTest, send_report, truck_data, bmonth, delete_view, bday

urlpatterns = [
    path('home/', home, name='home'),
    path('addt/', add_truck, name='add_truck'),
    path('detail/<int:pk>/', getDetails, name='detail'),
    path('create_product/', create_product, name='create_product'),
    path('update_product/<int:pk>/', update_product, name="update_product"),
    path('send_report/', send_report, name='send_report'),
    path('truck_data/<int:pk>/', truck_data, name='truck_data'),
    path('bdm/<int:pk>/<str:month>/<str:year>/', bmonth, name='bdm'),
    path('delete/<int:pk>/', delete_view, name='delete'),
    path('bday/<int:pk>/<int:day>/<str:month>/<str:year>/', bday, name='bday'),
    path('test/<int:pk>/', getDetailsTest, name='test'),
]
