from django.urls import path
from app import views

app_name = 'elib'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('borrow_history/', views.borrow_history, name='borrow_history'),
    path('contactus/', views.contact_us, name='contact_us'),

    path('search/', views.search, name='search'),
    path('goto/', views.GotoView.as_view(), name='goto'),

    #book details
    path('book_details/<int:book_id>/', views.book_details, name='book_details'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),

    #personal page
    path('personal_page/', views.personal_page, name='personal_page'),

    #recommend
    path('recommends/',views.recommends,name='recommends'),
]
