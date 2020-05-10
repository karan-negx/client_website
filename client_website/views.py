from django.views.generic import View
from django.shortcuts import render
import logging
_logger = logging.getLogger(__name__)


class HomeView(View):

    def get(self,request, *args, **kwargs):
        return render(request,"home/index.html")


