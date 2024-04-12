from django.db import models

# Create your models here.
class Naviagtion_bar(models.Model):
    name=models.CharField(max_length=100)
    icon=models.ImageField(upload_to='media/',default='')
    url=models.URLField()
class meta:
    db_table="Navigation_bar"

class Home_carousel(models.Model):
    image=models.ImageField(upload_to='media/')
    class meta:
        db_table="Home_carousel"


class Contact(models.Model):
      Name=models.CharField(max_length=100)
      Email=models.EmailField(max_length = 500)
      Phonenumber=models.BigIntegerField()
      Message=models.TextField()
      Subject=models.CharField(max_length=1000)
class Meta:
    db_table="Contact"  



###############################      flights_data       ##########################################

# Create your models here.
class flights_offercards(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100,default=None)
    image=models.ImageField(upload_to="images/")
    logo=models.ImageField(upload_to="images/",default=None)
    url=models.URLField(default="")
class Meta:
    db_table="flights_offercards"

class flights_kotak_offer(models.Model):
    image=models.ImageField(upload_to="media/")
    # logo=models.ImageField(upload_to="media/")
    text=models.CharField(max_length=100)
    text1=models.CharField(max_length=100)

    class Meta:
        db_table="flights_kotak_offer"

class flights_kotak_terms(models.Model):
    terms=models.TextField()
    condition=models.TextField(default="")

    class Meta:
        db_table="flights_kotak_terms"

class flights_policy(models.Model):
    content=models.TextField()
    class Meta:
        db_table="flights_policy"

class flights_policy1(models.Model):
    content1=models.TextField()
    class Meta:
        db_table="flights_policy1"
    
class flights_kotak_offer1(models.Model):
    image1=models.ImageField(upload_to="media/")
    category=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="flights_kotak_offer1"

### first booking ###

class flight_offer_first(models.Model):
    image=models.ImageField(upload_to="images/")
    content=models.CharField(max_length=255)
class Meta:
    db_table="flight_offer_first"
        
class flight_offer_first1(models.Model):
    title=models.CharField(max_length=255,default=None)
    content=models.TextField()
class Meta:
    db_table="flight_offer_first1"


### .....Yes Bank offer_cards Detailes   models

class card1_offers(models.Model):
    logo1=models.ImageField(upload_to="images/",null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True,blank=True)
    logo2=models.ImageField(upload_to="images/",null=True,blank=True)
    title=models.CharField(max_length=400)
    content=models.CharField(max_length=500)
class Meta:
    db_table="card1_offers"

class card1_offerdetailes(models.Model):
    type=models.CharField(max_length=200,null=True,blank=True)
    PromoCode=models.CharField(max_length=400)
    offer=models.CharField(max_length=300)
    Applicable_on=models.CharField(max_length=400)
class Meta:
    db_table="card1_offerdetailes"

class card1_terms_conditions(models.Model):
    title=models.CharField(max_length=400,null=True,blank=True)
    content=models.TextField()
class Meta:
    db_table="card1_terms_conditions"    

## FAQ ##    
    
class faqs(models.Model):
    id=models.IntegerField(primary_key=True)
    question=models.CharField(max_length=250)
    answer=models.TextField()

class Meta:
    db_table='flightfaqs'    

##...refundcrads...##

class Zero_cancellation_offer(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images/")
    content1=models.CharField(max_length=200)
    content2=models.CharField(max_length=200)
    logo1=models.ImageField(upload_to="images/",blank=True)
    logo2=models.ImageField(upload_to="images/",blank=True)
class Meta:
    db_table="Zero_cancellation_offer"


class Zero_cancellation_terms(models.Model):
    title=models.CharField(max_length=200,blank=True)
    content=models.TextField()
class Meta:
    db_table="Zero_cancellation_terms"     

#....why choose us.....#
    
class why_choose(models.Model):
    image=models.ImageField(upload_to="images/") 
    content=models.CharField(max_length=200)
class Meta:
    db_table="why_choose"


#...questions...#
    
class choosing_content(models.Model):
    question=models.CharField(max_length=100)
    answer=models.TextField()

    class Meta:
        db_table="choosing_content"    

#....icici...#
        
class icic_offer(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images/")
    content1=models.CharField(max_length=250)
    content2=models.CharField(max_length=250)
    logo1=models.ImageField(upload_to="images/",blank=True)
    logo2=models.ImageField(upload_to="images/",blank=True)
class Meta:
    db_table="icic_offer"


class icic_terms(models.Model):
    title=models.CharField(max_length=200,blank=True)
    content=models.TextField()
class Meta:
    db_table="icic_terms"        
    
##....SBI Card Offer.....#

class sbiimage(models.Model):
    image=models.ImageField(upload_to="images/")
    class Meta:
        db_table="sbiimage"
        
class sbioffer(models.Model):
    type=models.CharField(max_length=100)
    offer=models.CharField(max_length=200)
    min_amt=models.CharField(max_length=100)
    Promo_Code=models.CharField(max_length=100)
class Meta:
    db_table="sbioffer"

class sbiterms(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
class Meta:
    db_table="sbiterms"    


class hdfc_logo(models.Model):
    title=models.ImageField(upload_to="images/")
class Meta:
    db_table="hdfc_logo"
    
class hdfc_offer(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
class Meta:
    db_table="hdfc_offer"    

class flight_offers7(models.Model):
   photo=models.ImageField(upload_to="images/")
   heading=models.CharField(max_length=100,default='')
   content=models.CharField(max_length=100,default='')
   title=models.CharField(max_length=100,default='')
   point = models.TextField(help_text="Enter product info on a new line.",default='')
   
class Meta:
    db_table="flight_offers7"



class flight_offers8(models.Model):
   heading=models.CharField(max_length=100,default='')
   photo1=models.ImageField(upload_to="media/")
   title=models.CharField(max_length=100,default='')
   description=models.CharField(max_length=100,default='') 
class Meta:
    db_table="flight_offers8"
 

 ##.....................Hotels..................##
    
from django.db import models

# Create your models here.
class hotel_cards(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    image=models.ImageField(upload_to="media/")
    url=models.URLField(default="")
    class Meta:
        db_table="hotel_cards"

class hotel_quary(models.Model):
    ques=models.TextField()
    ans=models.TextField()
    class Meta:
        db_table="hotel_quary"    

class hotel_FAQItem(models.Model):
    question = models.TextField()
    answer = models.TextField()    
    class Meta:
        db_table="hotel_FAQItem"

#...axis_offer...#
    

class hotel_axisoffer(models.Model):
    image=models.ImageField(upload_to="media/")
    
    class Meta:
        db_table="hotel_axisoffer"


class hotel_axispolicy(models.Model):
    content=models.TextField()
    content1=models.TextField()
    content2=models.TextField()
    content3=models.TextField()
    content4=models.TextField(default="")

    class Meta:
        db_table="hotel_axispolicy"

    
class hotel_axisoffer1(models.Model):
    product=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_axisoffer1"


#...icici...#
        
class hotel_icicioffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_icicioffer"


class hotel_icicipolicy(models.Model):
    content=models.TextField()
    content1=models.TextField()
    content2=models.TextField()
    content3=models.TextField()
    content4=models.TextField(default="")

    class Meta:
        db_table="hotel_icicipolicy"

    
class hotel_icicioffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_icicioffer1"
        
#...HSBC...#

class hotel_hsbcoffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_hsbcoffer"


class hotel_hsbcpolicy(models.Model):
    data=models.TextField()
    data1=models.TextField()
    data2=models.TextField()
    data3=models.TextField()
    data4=models.TextField()

    class Meta:
        db_table="hotel_hsbcpolicy"

    
class hotel_hsbcoffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_hsbcoffer1"     

#...SBI...#

class hotel_sbioffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_sbioffer"


class hotel_sbipolicy(models.Model):
    cnt=models.TextField()
    cnt1=models.TextField()
    cnt2=models.TextField()
    cnt3=models.TextField()
    cnt4=models.TextField()

    class Meta:
        db_table="hotel_sbipolicy"

    
class hotel_sbioffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_sbioffer1"                                           

#...KOTAK...#


class hotel_kotakoffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_kotakoffer"


class hotel_kotakpolicy(models.Model):
    cntnt=models.TextField()
    cntnt1=models.TextField()
    cntnt2=models.TextField()
    cntnt3=models.TextField()

    class Meta:
        db_table="hotel_kotakpolicy"

    
class hotel_kotakoffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_kotakoffer1"                                                           

#.....BOB......#
        
class hotel_boboffer(models.Model):
    photo=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    cpncode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_boboffer"


class hotel_bobpolicy(models.Model):
    term=models.TextField()
    term1=models.TextField()
    term2=models.TextField()
    term3=models.TextField()

    class Meta:
        db_table="hotel_bobpolicy"

    
class hotel_boboffer1(models.Model):
    category=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_boboffer1"                                                           
  


#...FEDERAL...#


class hotel_federaloffer(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=100)
    couponcode=models.CharField(max_length=100)
    class Meta:
        db_table="hotel_federaloffer"


class hotel_federalpolicy(models.Model):
    cntnt=models.TextField()
    cntnt1=models.TextField()
    

    class Meta:
        db_table="hotel_federalpolicy"

    
class hotel_federaloffer1(models.Model):
    applicable=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)

    class Meta:
        db_table="hotel_federaloffer1"                                                                               