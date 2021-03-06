from django.urls import path
from . import views

urlpatterns = [
    #======BLOG_URLs======
    #list of posts
    path('', views.post_list, name='post_list'),
    # path('', views.post_list.as_view(), name='post_list'),

    #CREATE
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #RETRIEVE
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    #UPDATE
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #DELETE
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    
    #======COMMENT_URLs======
    #CREATE
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #UPDATE
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    #DELETE
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]