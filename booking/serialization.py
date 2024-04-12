from rest_framework import serializers
from .models import *
class TaxiFareSerializer(serializers.Serializer):
    dep_lat = serializers.FloatField()
    dep_lng = serializers.FloatField()
    arr_lat = serializers.FloatField()
    arr_lng = serializers.FloatField()


class Navigationdata(serializers.ModelSerializer):
    class Meta:
        model=Naviagtion_bar
        fields='__all__'
class Carouseldata(serializers.ModelSerializer):
    class Meta:
        model=Home_carousel
        fields='__all__'


########################  flights    ################################
        
from rest_framework import serializers
from .models import *

class flights_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_offercards
        fields="__all__"

class kotak_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_offer
        fields="__all__"

class kotakterms_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_terms
        fields="__all__" 

class kotakpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_policy
        fields="__all__" 

class kotakpolicy1_serialization(serializers.ModelSerializer):
    class Meta:
        model=flights_policy1
        fields="__all__"

class kotak_serialization1(serializers.ModelSerializer):
    class Meta:
        model=flights_kotak_offer1
        fields="__all__"        

## first booking ##

class flight_firstser(serializers.ModelSerializer):
    class Meta:
        model=flight_offer_first
        fields="__all__"

class flight_first1ser(serializers.ModelSerializer):
    class Meta:
        model=flight_offer_first1
        fields="__all__"


# ..................card1 serialization Yes Bank....................
class card1_offers_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_offers
        fields="__all__"

class card1_offerdetailes_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_offerdetailes
        fields="__all__"

class card1_terms_conditions_serialization(serializers.ModelSerializer):
    class Meta:
        model=card1_terms_conditions
        fields="__all__"

## FAQ ##
        
class flightfaqs_serialization(serializers.ModelSerializer):
    class Meta:
        model=faqs
        fields='__all__'   
        
#................100% Refund card...........

from .models import  Zero_cancellation_offer,Zero_cancellation_terms

class ZC_offer_serialization(serializers.ModelSerializer):
    class Meta:
        model=Zero_cancellation_offer
        fields="__all__"

class zc_terms_serialization(serializers.ModelSerializer):
    class Meta:
        model=Zero_cancellation_terms
        fields="__all__"           

#....why choose us...#

class why_chooseser(serializers.ModelSerializer):
    class Meta:
        model=why_choose
        fields="__all__"

#....question...#
        
class content_serialization(serializers.ModelSerializer):
    class Meta:
        model=choosing_content
        fields="__all__"

#....icic...#
        
class icic_serialization(serializers.ModelSerializer):
    class Meta:
        model=icic_offer
        fields="__all__"

class icici_serialization(serializers.ModelSerializer):
    class Meta:
        model=icic_terms
        fields="__all__"    

#...................sbi card......................

class sbiimage_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbiimage
        fields="__all__"

class sbioffer_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbioffer
        fields="__all__"

class sbiterms_serialization(serializers.ModelSerializer):
    class Meta:
        model=sbiterms
        fields="__all__"            

#...................hdfc card......................
        
class hdfc_logoser(serializers.ModelSerializer):
    class Meta:
        model=hdfc_logo
        fields="__all__"             
class hdfc_offerser(serializers.ModelSerializer):
    class Meta:
        model=hdfc_offer
        fields="__all__"         
      
#......................HOTELS...........................#
        
from .models import *
from rest_framework import serializers



class cardsserializationclass(serializers.ModelSerializer):
    class Meta:
        model=hotel_cards
        fields='__all__'

#...Axis...#

class hotel_axis_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_axisoffer
        fields="__all__"



class hotel_axispolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_axispolicy
        fields="__all__" 

class hotel_axisserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_axisoffer1
        fields="__all__"        

#...icici...#
        
class hotel_icici_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicioffer
        fields="__all__"



class hotel_icicipolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicipolicy
        fields="__all__" 

class hotel_iciciserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_icicioffer1
        fields="__all__"           

#...HSBC...#

class hotel_hsbc_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcoffer
        fields="__all__"



class hotel_hsbcpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcpolicy
        fields="__all__" 

class hotel_hsbcserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_hsbcoffer1
        fields="__all__"                 

#...SBI....#
        
class hotel_sbi_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbioffer
        fields="__all__"



class hotel_sbipolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbipolicy
        fields="__all__" 

class hotel_sbiserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_sbioffer1
        fields="__all__"                 

#...KOTAK...#
        

class hotel_kotak_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakoffer
        fields="__all__"



class hotel_kotakpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakpolicy
        fields="__all__" 

class hotel_kotakserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_kotakoffer1
        fields="__all__"         

#.....BOB.....#
        

class hotel_bob_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_boboffer
        fields="__all__"

class hotel_bobpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_bobpolicy
        fields="__all__" 

class hotel_bobserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_boboffer1
        fields="__all__"           


#...FEDERAL...#  


class hotel_federal_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_federaloffer
        fields="__all__"



class hotel_federalpolicy_serialization(serializers.ModelSerializer):
    class Meta:
        model=hotel_federalpolicy
        fields="__all__" 

class hotel_federalserialization1(serializers.ModelSerializer):
    class Meta:
        model=hotel_federaloffer1
        fields="__all__"                               