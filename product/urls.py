from django.urls import path,include
from .views import *
# from django.conf.urls.static import static
# from django.conf import settings



urlpatterns = [
    path('', index, name='index'),
    path('addproduct', product_post, name='product_post'),
    path('addcategory', category_post, name='category_post'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)




