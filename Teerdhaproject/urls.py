"""
URL configuration for Teerdhaproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from booking import views,hotel_views,flight_views,bus_views,cab_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teerdha_page',views.teerdha_page),

    path('calculate-fare/',views.TaxiFareAPIView.as_view(), name='calculate_fare'),
    path('add_navigation_list/',views.add_navigation_list.as_view(),name="add_navigation_list"),
    path('Table_navigation_list/',views.Table_navigation_list.as_view(),name="Table_navigation_list"),
    path('Navigationlist/',views.Navigationlist.as_view(),name="Navigationlist"),
    path('Update_navigation_list/<int:pk>',views.Update_navigation_list.as_view(),name="Update_navigation_list"),
    path('Remove_navigation_list/<int:pk>',views.Remove_navigation_list.as_view(),name="Remove_navigation_list"),
    path('add_carousel_list/',views.add_carousel_list.as_view(),name="add_carousel_list"),
    path('Table_carousel_list/',views.Table_carousel_list.as_view(),name="Table_carousel_list"),
    path('Carousel_list/',views.Carousel_list.as_view(),name="Carousel_list"),
    path('Update_carousel_list/<int:pk>',views.Update_carousel_list.as_view(),name="Update_carousel_list"),
    path('Remove_carousel_list/<int:pk>',views.Remove_carousel_list.as_view(),name="Remove_carousel_list"),
    path('Carousel_home/',views.Carousel_home,name="Carousel_home"),
    path('bus_form/',bus_views.bus_form,name="bus_form"),
    path('footer/',views.footer,name="footer"),



##################     flight ####################################################



    path('flight_home/',flight_views.flightsapi.as_view()),
    path('flight_update/<int:pk>/',flight_views.flight_update.as_view()),
    path('',flight_views.flights),
    # path('',include(router.urls)),

    ## kotak_offercard ##

    path('kotak_api/',flight_views.kotak_api.as_view()),
    path('kotak_update/<int:pk>/',flight_views.kotak_update.as_view()),

    path('kotak_api1/',flight_views.kotak_api1.as_view()),
    path('kotak_update1/<int:pk>/',flight_views.kotak_update1.as_view()),

    
    path('kotakterms_api/',flight_views.kotakterms_api.as_view()),
    path('kotakterms_update/<int:pk>/',flight_views.kotakterms_update.as_view()),

    path('kotakpolicy_api/',flight_views.kotakpolicy_api.as_view()),
    path('kotakpolicy_update/<int:pk>/',flight_views.kotakpolicy_update.as_view()),

    path('kotakpolicy_api1/',flight_views.kotakpolicy_api1.as_view()),
    path('kotakpolicy_update1/<int:pk>/',flight_views.kotakpolicy_update1.as_view()),
    path('kotak/',flight_views.kotak),

## first booking ##

    path('flight_offerfirst_lc/',flight_views.flight_offerfirst_lc.as_view()),
    path('flight_offerfirst_rud/<int:pk>/',flight_views.flight_offerfirst_rud.as_view()),
    path('flight_offerfirst1_lc/',flight_views.flight_offerfirst1_lc.as_view()),
    path('flight_offerfirst1_rud/<int:pk>/',flight_views.flight_offerfirst1_rud.as_view()),
    path('flight_offer_1/',flight_views.flight_offer_1),

#.........FAQ.........#

    path('faqsapi/',flight_views.faqsapi.as_view()),
    path('faq_update/<int:pk>/',flight_views.faq_update.as_view()),
    # path('faq_home/',flight_views.faq_home),

# ..............yes_bank_offercard1...............
    path('card1_offer/',flight_views.card1_offerapi.as_view()),
    path('card1_offerdet/',flight_views.card1_offerdetailesapi.as_view()),
    path('card1_offerterms/',flight_views.card1_offer_termsapi.as_view()),
    path('yes_bank_offercard/',flight_views.yes_bank_offercard),

    path('card1offerup/<int:pk>/',flight_views.card1_offerup.as_view()),
    path('card1offerdetailesup/<int:pk>/',flight_views.card1_offerdetailes_up.as_view()),
    path('card1offertermsup/<int:pk>/',flight_views.card1_offerterms_up.as_view()),

#....refund....#
    path('zero_offer/',flight_views.zc_offerapi.as_view()),
    path('zero_terms/',flight_views.zc_termsapi.as_view()),

    path('zero_offerup/<int:pk>/',flight_views.zc_offer_update.as_view()),
    path('zero_termsup/<int:pk>/',flight_views.zc_terms_update.as_view()),
    
    path('zerocancellation/',flight_views.zerocancellation),

#...why choose us....#

    path('why_choose_lc/',flight_views.why_choose_lc.as_view()),
    path('why_choose_rud/<int:pk>/',flight_views.why_choose_rud.as_view()),
    # path('why_choose_us/',flight_views.why_choose_us),

#....question...#

    path('choose_us/',flight_views.choose_us.as_view()),
    path('whychooseus/<int:pk>/',flight_views.whychooseus.as_view()),  

#.... icic....#

    path('icic_offer/',flight_views.icic_offerapi.as_view()),
    path('icic_terms/',flight_views.icic_termsapi.as_view()),

    path('icic_offer_update/<int:pk>',flight_views.icic_offer_update.as_view()),
    path('icic_terms_update/<int:pk>',flight_views.icic_terms_update.as_view()),
    
    path('icic/',flight_views.icic),

#...Sbi_offer....#

    path('sbi_image/',flight_views.sbiimageapi.as_view()),
    path('sbi_offer/',flight_views.sbiofferapi.as_view()),
    path('sbi_terms/',flight_views.sbitermsapi.as_view()),


    path('sbi_image_up/<int:pk>/',flight_views.sbiimage_up.as_view()),
    path('sbi_offer_up/<int:pk>',flight_views.sbioffer_up.as_view()),
    path('sbi_terms_up/<int:pk>',flight_views.sbiterms_up.as_view()),
    
    path('sbi/',flight_views.sbi),    

#########     HDFC      ################
    path('hdfc_logo_lc/',flight_views.hdfc_logo_lc.as_view()),
    path('hdfc_logo_rud/<int:pk>',flight_views.hdfc_logo_rud.as_view()),
    path('hdfc_offer_lc/',flight_views.hdfc_offer_lc.as_view()),
    path('hdfc_offer_rud/<int:pk>',flight_views.hdfc_offer_rud.as_view()),
    path('hdfc_offer_card/',flight_views.hdfc_offer_card),
    path('flight_offers_card_page_2/',flight_views.flight_offers_card_page_2),


##....................HOTELS.............##

    path('hotelform/',hotel_views.hotelform,name="hotelform"),
    path('cardsapi/',hotel_views.cardsapi.as_view(),name='cardsapi'),
    path('cardsapi2/<int:pk>/',hotel_views.cardsapi2.as_view(),name='cardsapi2'),

    #...Hotel_quary..#

    path('hotel_cardsreg/',hotel_views.hotel_cardsreg),
    path('hotel_cardstb/',hotel_views.hotel_cardstb),
    path('hotel_cardsup/<int:id>',hotel_views.hotel_cardsup,name="hotel_cardsup"),
    path('hotel_cardsedit/<int:id>',hotel_views.hotel_cardsedit,name="hotel_cardsedit"),
    path('hotel_cardsdelete/<int:id>',hotel_views.hotel_cardsdelete,name="hotel_cardsdelete"),

    path('hotel_faqreg/',hotel_views.hotel_faqreg),
    path('hotel_faqtab/',hotel_views.hotel_faqtab),
    path('hotel_faqupdate/<int:id>',hotel_views.hotel_faqupdate,name="hotel_faqupdate"),
    path('hotel_faqedit/<int:id>',hotel_views.hotel_faqedit,name="hotel_faqedit"),
    path('hotel_faqdelete/<int:id>',hotel_views.hotel_faqdelete,name="hotel_faqdelete"),
    
    #...HOtel_Axis...#

    path('hotel_axisform/',hotel_views.hotel_axisform,name="hotel_axisform"),
    path('axis_api/',hotel_views.axis_api.as_view(),name='axis_api'),
    path('axis_update/<int:pk>/',hotel_views.axis_update.as_view(),name='axis_update'),
    path('axis_api1/',hotel_views.axis_api1.as_view(),name='axis_api1'),
    path('aixs_update1/<int:pk>/',hotel_views.aixs_update1.as_view(),name='aixs_update1'),
    path('axispolicy_api/',hotel_views.axispolicy_api.as_view(),name='axispolicy_api'),
    path('axispolicy_update/<int:pk>/',hotel_views.axispolicy_update.as_view(),name='axispolicy_update'),

    #....Hotel_icici...#
    
    path('hotel_iciciform/',hotel_views.hotel_iciciform,name="hotel_iciciform"),
    path('icici_api/',hotel_views.icici_api.as_view(),name='icici_api'),
    path('icici_update/<int:pk>/',hotel_views.icici_update.as_view(),name='icici_update'),
    path('icici_api1/',hotel_views.icici_api1.as_view(),name='icici_api1'),
    path('icici_update1/<int:pk>/',hotel_views.icici_update1.as_view(),name='icici_update1'),
    path('icicipolicy_api/',hotel_views.icicipolicy_api.as_view(),name='icicipolicy_api'),
    path('icicipolicy_update/<int:pk>/',hotel_views.icicipolicy_update.as_view(),name='icicipolicy_update'),

    #...Hotel_HSBC...#

    path('hotel_hsbcform/',hotel_views.hotel_hsbcform,name="hotel_hsbcform"),
    path('hsbc_api/',hotel_views.hsbc_api.as_view(),name='hsbc_api'),
    path('hsbc_update/<int:pk>/',hotel_views.hsbc_update.as_view(),name='hsbc_update'),
    path('hsbc_api1/',hotel_views.hsbc_api1.as_view(),name='hsbc_api1'),
    path('hsbc_update1/<int:pk>/',hotel_views.hsbc_update1.as_view(),name='hsbc_update1'),
    path('hsbcpolicy_api/',hotel_views.hsbcpolicy_api.as_view(),name='hsbcpolicy_api'),
    path('hsbcpolicy_update/<int:pk>/',hotel_views.hsbcpolicy_update.as_view(),name='hsbcpolicy_update'),

    #...Hotel_SBI...#

    path('hotel_sbiform/',hotel_views.hotel_sbiform,name="hotel_sbiform"),
    path('sbi_api/',hotel_views.sbi_api.as_view(),name='sbi_api'),
    path('sbi_update/<int:pk>/',hotel_views.sbi_update.as_view(),name='sbi_update'),
    path('sbi_api1/',hotel_views.sbi_api1.as_view(),name='sbi_api1'),
    path('sbi_update1/<int:pk>/',hotel_views.sbi_update1.as_view(),name='sbi_update1'),
    path('sbipolicy_api/',hotel_views.sbipolicy_api.as_view(),name='sbipolicy_api'),
    path('sbipolicy_update/<int:pk>/',hotel_views.sbipolicy_update.as_view(),name='sbipolicy_update'),

    #...Hotel_KOTAK...#

    path('hotel_kotakform/',hotel_views.hotel_kotakform,name="hotel_kotakform"),
    path('hotel_kotakapi/',hotel_views.hotel_kotakapi.as_view(),name='hotel_kotakapi'),
    path('hotel_kotakupdate/<int:pk>/',hotel_views.hotel_kotakupdate.as_view(),name='hotel_kotakupdate'),
    path('hotel_kotakapi1/',hotel_views.hotel_kotakapi1.as_view(),name='hotel_kotakapi1'),
    path('hotel_kotakupdate1/<int:pk>/',hotel_views.hotel_kotakupdate1.as_view(),name='hotel_kotakupdate1'),
    path('hotel_kotakpolicyapi/',hotel_views.hotel_kotakpolicyapi.as_view(),name='hotel_kotakpolicyapi'),
    path('hotel_kotakpolicyupdate/<int:pk>/',hotel_views.hotel_kotakpolicyupdate.as_view(),name='hotel_kotakpolicyupdate'),

    #.....BOB.....#

    path('hotel_bobform/',hotel_views.hotel_bobform,name="hotel_bobform"),
    path('hotel_bobapi/',hotel_views.hotel_bobapi.as_view(),name='hotel_bobapi'),
    path('hotel_bobupdate/<int:pk>/',hotel_views.hotel_bobupdate.as_view(),name='hotel_bobupdate'),
    path('hotel_bobapi1/',hotel_views.hotel_bobapi1.as_view(),name='hotel_bobapi1'),
    path('hotel_bobupdate1/<int:pk>/',hotel_views.hotel_bobupdate1.as_view(),name='hotel_bobupdate1'),
    path('hotel_bobpolicyapi/',hotel_views.hotel_bobpolicyapi.as_view(),name='hotel_bobpolicyapi'),
    path('hotel_bobpolicyupdate/<int:pk>/',hotel_views.hotel_bobpolicyupdate.as_view(),name='hotel_bobpolicyupdate'),


    #...Hotel_FEDERAL...#

    path('hotel_federalform/',hotel_views.hotel_federalform,name="hotel_federalform"),
    path('federal_api/',hotel_views.federal_api.as_view(),name='federal_api'),
    path('federal_update/<int:pk>/',hotel_views.federal_update.as_view(),name='federal_update'),
    path('federal_api1/',hotel_views.federal_api1.as_view(),name='federal_api1'),
    path('federal_update1/<int:pk>/',hotel_views.federal_update1.as_view(),name='federal_update1'),
    path('federalpolicy_api/',hotel_views.federalpolicy_api.as_view(),name='federalpolicy_api'),
    path('federalpolicy_update/<int:pk>/',hotel_views.federalpolicy_update.as_view(),name='federalpolicy_update'),


   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
