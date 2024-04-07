from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('rarities/', views.RarityList.as_view(), name='rarities_index'),
    path('rarities/<int:pk>/', views.RarityDetail.as_view(), name='rarities_detail'),
    path('rarities/create/', views.RarityCreate.as_view(), name='rarities_create'),
    path('rarities/<int:pk>/update/', views.RarityUpdate.as_view(), name='rarities_update'),
    path('rarities/<int:pk>/delete/', views.RarityDelete.as_view(), name='rarities_delete'),
    path('finches/<int:finch_id>/assoc_rarity/<int:rarity_id>', views.assoc_rarity, name='assoc_rarity'),
]

