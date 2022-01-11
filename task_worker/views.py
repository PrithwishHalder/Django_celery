from django.shortcuts import render
from django.http import HttpResponse
from .task import send_email_task
from django.core.mail import send_mail
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(max_workers=10)


async def send_email_aync(sender,loop):
    # time.sleep(5)
    time1 = time.time()
    await loop.run_in_executor(_executor, send_email_task(sender))
    print("Async. Time taken : " + str(time.time() - time1))

# Create your views here.
def index(request):
    time1 = time.time()
    send_email_task.delay("halderprithwish@gmail.com")
    send_email_task.delay("haldarprithwish@gmail.com")
    return HttpResponse("Celery. Time taken : " + str(time.time() - time1))

async def async_view(request):
  time1 = time.time()
  loop = asyncio.get_event_loop()
  l=loop.create_task(send_email_aync("halderprithwish@gmail.com", loop))
  return HttpResponse("Async. Time taken : " + str(time.time() - time1))

def default(request):
    time1 = time.time()
    send_email_task("halderprithwish@gmail.com")
    return HttpResponse("Default. Time taken : " + str(time.time() - time1))