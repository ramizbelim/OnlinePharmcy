from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('basic', views.basic, name='basic'),
    path("viewdata", views.viewdata, name="viewdata"),
    path("checkuser", views.checklogin, name="checkuser"),
    path('about', views.about, name='about'),
    path("logout", views.logout, name="logout"),
    path("cp", views.cp, name="cp"),
    path("completeprofile", views.completeprofile, name="completeprofile"),
    path('login/', views.signin, name='login'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path("submitcontact", views.submitcontact, name="submitcontact"),
    path('acc', views.account, name='acc'),
    path("categorywiseproduct/<int:pcid>", views.categorywiseproduct, name="categorywiseproduct"),
    path("subcategorywiseproduct/<int:pscid>", views.subcategorywiseproduct, name="subcategorywiseproduct"),
    path("single/<int:myid>", views.productView, name="ProductDetail"),
    path('shop', views.shop, name='shop'),
    path("addtocart", views.addtocart, name="addtocart"),
    path('cart', views.Cart, name='cart'),
    path('wishlist', views.wishlists, name='wishlist'),
    path("addtowishlist/<int:awid>", views.addtowishlist, name="addtowishlist"),
    path("removewish/<int:dwid>", views.removewish, name="removewish"),
    path("removeitem/<int:did>", views.RemoveFromCart, name="RemoveFromCart"),
    path("order-complete", views.OrderComplete, name="OrderComplete"),
    path("yourordersingle/<int:yoid>", views.yourordersingle, name="yourordersingle"),
    path("verifypayment", views.verifypayment, name="verifypayment"),
    path("submitreview", views.SubmitReview, name="SubmitReview"),

]