# mysite
Pre-development Web untuk kebutuhan web aplikasi atau website berbasis python django, jika belum faham apa itu django silahkan baca tutorialnya disini https://docs.djangoproject.com/en/1.11/intro/tutorial01/. <br/><br /> Folder environment bernama env, cara menggunakannya seperti berikut : https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv

# requirements
OS Ubuntu 16.04 Xenial,
python 3.5.2,
virtualenv 15.1.0,
django 1.11,

# web server
Instal uwsgi terlebih dahulu seperti tutorial berikut ini : http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html, lalu instal nginx seperti tutorial berikut ini : https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04

Download config uwsgi_param jika tidak tersedia di project, silahkan download disini : https://github.com/nginx/nginx/blob/master/conf/uwsgi_params