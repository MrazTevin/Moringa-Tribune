from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render
# Create your views here.


def news_today(request):
    date = dt.date.today()
            # To convert date object to find exact day
 
    return render(request, 'all-news/today-news.html', {"date":date,})

# View Function to present news form past days
def past_days_news(request,past_date):
    
       
    try:
         # convert data from string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    
    except ValueError:
        # Raise 404 error when ValueError is thrown

        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(news_today)
    return render(request, 'all-news/past-news.html', {"date": date})
    



