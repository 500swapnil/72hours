#+TITLE:  OneStopShop
#+DATE: 30th April,2017
#+SETUPFILE: theme-bigblow.setup
* TEAM MEMBERS: 
- MRIDUL NAGPAL (mridulnagpal07@gmail.com)
- PALASH AGARWAL(konnectpalash@gmail.com)
- SWAPNIL GUPTA (500swapnil@gmail.com)
- VIVEK KAUSHAL (vivek.kaushal@outlook.com)

* Overview
A one stop shopping portal for those who want to buy/sell products.

* Goals
The basic goal, and our motive behind building this web-application is to provide a portal to users
which enables them to sell applications and also provides them the option to browse products, on the 
lines of quikr.com.

* Features
- =User can create account.=
- =User can Sign-In.=
- =Create Ads for Items to Sell.=
- =Browse through categories to see ads for items on sale.=
- =Contact Seller to negotiate for item price.=
- =User can search items according to category.=
- =User can remove posted ads.=

* Application Structure

[[https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=72hours.xml#R5VlNj5swEP01HBsBhpAcd5Nte6m00lZqe%2FTCBNwCRsb52l%2FfIZgEcLYkKXRVNocIP%2BzBfu8xHicGWSS7T4Jm0RceQGzYZrAzyNKw7Zk3xe8C2JeAY1olEAoWlFANeGIvoEBToWsWQN7oKDmPJcuaoM%2FTFHzZwKgQfNvstuJx86kZDUEDnnwa6%2Bg3FshILcs1T%2FhnYGFUPdky1Z1n6v8KBV%2Bn6nmGTVaHT3k7oVUs1T%2BPaMC3NYg8GGQhOJflVbJbQFxQW9FWjvv4yt3jvAWk8pIBdjlgQ%2BO1WrpXtCO%2BFrmaodxXrEjYYdD7SCYxAhZeCsjZC30%2BdDCxnXGWygP37r3hLhGha8nzUt9iAI1ZmOJ1DKsi1AaEZEj7nYIlzxDNM%2BqzNPxaNJYfHETULLE37F5dqXXkD20JPAEp9thFDbBNUg5Rlpy6ZXN70neqRIlq0lZCUeWo8Bj4xCpeKGLPk0w0kjVqIQ3uCt9iK%2BUpNFkue0OgebZz7bXFuWcWV2ECYirZphn%2B3IrVEx4LmWvUkia1hLRIy9FOPqhRdTd2BJq14kgqQpBanAP%2Fx1VfJIl7lSR%2BTPOc%2Bf%2BbKmaDzGOOulqVeUeg%2FmSZarJkgv8sMvy4clGL0arZYYw%2BctHsL3MRrlDsvxcUTxy7av%2Bo33wEwXBaIJQOl74nuMUffFRzwlu9OsSyekpoblNoLISGenWqKY85pRGrlYnadF6qC%2FE6AvWoi15iJTTFAnKS7ceV1TRSiZ7WZgOlNeu6Gmsc7m%2BXRze7f7g6y3I0XUa5o2uUekTz%2FlBbuvUOitm29zXibvW%2BFqhH7%2BvV7DqHsZ2rNUJN798537vK%2BX%2BsZsmsUc1OTLffgtZ624p2Nm%2Bo1FtFS4Y7DFYOGXVea50EtQPCpbo4TkegHnXRTxoSkgx5gJHlNo1UW89t3kC57cpfDcfhfq8v97cD9eh%2BvaLNJZLgj9z67lSzvjOU9d9DQTvv2Edvtf6QG7Je0CYsFEgDT0fu%2FjO%2F0PaU%2BLF5%2BruvFOX0lyp5%2BA0%3D][Application Structure]]

* Implementation

** Django
This project of one stop shop portal has been implemented using Django.Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source. Django was designed to help developers take applications from concept to completion as quickly as possible.Django takes security seriously and helps developers avoid many common security mistakes. Some of the busiest sites on the Web leverage Django's ability to quickly and flexibly scale.

*** Official *Django Documentation* [[https://docs.djangoproject.com/en/1.11/][here]].   
** Backend
*** Setting up web server
#+BEGIN_SRC python
  import os
  import sys

  if __name__ == "__main__":
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
      try:
          from django.core.management import execute_from_command_line
      except ImportError:
          # The above import may fail for some other reason. Ensure that the
          # issue is really that Django is missing to avoid masking other
          # exceptions on Python 2.
          try:
              import django
          except ImportError:
              raise ImportError(
                  "Couldn't import Django. Are you sure it's installed and "
                  "available on your PYTHONPATH environment variable? Did you "
                  "forget to activate a virtual environment?"
              )
          raise
      execute_from_command_line(sys.argv)

#+END_SRC

*** Signup
#+BEGIN_SRC python
  class UserForm(forms.Form):
      name = forms.CharField(max_length=100, label='',
                  widget=forms.TextInput(
              attrs={'placeholder': 'Name'}
                  ))
      email = forms.EmailField(max_length=100, label='', 
                  widget=forms.TextInput(
              attrs={'placeholder': 'Email Address'}
                  ))
      password = forms.CharField(label='', widget=forms.PasswordInput(
                  attrs={'placeholder': 'Password'}
                  ))
#+END_SRC

User will sign-up using name,email and password and then once registered user will login using registered name and password to make it simple for user.

** Post-Ad
User will send an mail to admin to post ad so that admin has the power to accept or reject that ad in order to secure website from useless ads.
We have a mail-to option for this purpose.
** Search Items
#+BEGIN_SRC python
  def search(request):
      if request.method == 'POST':
          name = "Search Results"
          items_all = Item.objects.all()
          search = request.POST.get('search')
          for item in items_all:
              if search in item.title:
                  items.append(item)
          if items:
              return render(request, 'category.html', {'items':items, 'name':name, 'error':""})    
          else:
              return render(request, 'category.html', {'items':items, 'name':name, 'error':"No search results"})

#+END_SRC
* Deployment
To Deploy python apps, we use nginx as a reverse proxy server. We use uWSGI with nginx to deploy python apps like flask. Insight about WSGI - Web Server Gateway Interface (WSGI) is a specification for simple and universal interface between web servers and web applications. 

** Basic uWSGI installation
#+BEGIN_SRC 
pip install uwsgi
#+END_SRC

** Basic nginx
*** Install nginx
#+BEGIN_SRC 
sudo apt-get install nginx
sudo /etc/init.d/nginx start    # start nginx
#+END_SRC

*** Configure nginx for our site
Now we will configure nginx for our site 72hours.We will need uwsgi_params file, which is available in the =nginx= directory of the uWSGI distribution.

*** Deploying static file
Before running nginx, we have to collect all Django static files in the static folder. 
#+BEGIN_SRC 
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
#+END_SRC

Then we will run 
#+BEGIN_SRC 
python manage.py collectstatic
#+END_SRC

*** Basic nginx test
Now we should restart nginx to check that media files are being served correctly.
#+BEGIN_SRC 
sudo /etc/init.d/nginx restart
#+END_SRC
