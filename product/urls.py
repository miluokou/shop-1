#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

app_name = 'product'

urlpatterns = [
    url('',index,name='index'), #主页
]