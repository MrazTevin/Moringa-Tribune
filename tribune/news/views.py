from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render
# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
          <body>
            <h1>{date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
            # To convert date object to find exact day
    day = convert_dates(date)
    html = f'''
        <html>
          <body>
            <h1>News for {day} {date.day}-{date.month}-{date.year}
          </body>
        </html>
        '''
    return HttpResponse(html)

def convert_dates(dates):
    # function to get weekday number for dates

    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturdaay',"Sunday"]

    # returning actual day of the week
    day = days[day_number]

    return day

def past_days_news(request,past_date):
    
        # convert data from string Url
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    
    except ValueError:
        # Raise 404 error when ValueError is thrown

        raise Http404()
    
    
    day = convert_dates(date)
    html = f'''
      <html>
        <body>
          <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
          </body>
      </html>
         '''
    
    return HttpResponse(html)
    



