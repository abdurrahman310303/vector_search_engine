"""
URL configuration for vector_search project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from search import views
from search.ui_views import dashboard, document_search, image_search, system_status

urlpatterns = [
    # Web UI Routes
    path('', dashboard, name='dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('document-search/', document_search, name='document_search'),
    path('image-search/', image_search, name='image_search'),
    path('system-status/', system_status, name='system_status'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Text Document Endpoints
    path('ingest/', views.ingest_document, name='ingest_document'),
    path('search/', views.search_documents, name='search_documents'),
    path('keyword_search/', views.keyword_search, name='keyword_search'),
    path('hybrid_search/', views.hybrid_search, name='hybrid_search'),
    path('rebuild_index/', views.rebuild_index, name='rebuild_index'),
    path('index_stats/', views.index_stats, name='index_stats'),
    
    # Image Search Endpoints
    path('ingest_image/', views.ingest_image, name='ingest_image'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('search_images_by_text/', views.search_images_by_text, name='search_images_by_text'),
    path('search_images_by_image/', views.search_images_by_image, name='search_images_by_image'),
    path('hybrid_image_search/', views.hybrid_image_search, name='hybrid_image_search'),
    path('image_index_stats/', views.image_index_stats, name='image_index_stats'),
    path('validate_system/', views.validate_system, name='validate_system'),
    
    # Image Serving Endpoints
    path('media/<path:path>', views.serve_image, name='serve_image'),
    path('image/<int:image_id>/', views.serve_file_image, name='serve_file_image'),
    
    # Legacy endpoints for backward compatibility
    path('ingest_legacy/', views.ingest_document, name='ingest_legacy'),
    path('search_legacy/', views.search_documents, name='search_legacy'),
    path('hybrid_search_legacy/', views.hybrid_search, name='hybrid_search_legacy'),
    path('keyword_search_legacy/', views.keyword_search, name='keyword_search_legacy'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
