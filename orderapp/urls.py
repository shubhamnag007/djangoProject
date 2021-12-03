from django. urls import path
from orderapp import views
urlpatterns=[

    path('add-order',views.add_order, name='add_order'),
    path('orders',views.order_list, name='order_list')

]