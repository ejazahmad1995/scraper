from django.shortcuts import render
import requests


# Create your views here.
def scrape(request):
    page = requests.get('http://www.google.com')
    # soup = BeautifulSoup(page.text, 'html.parser')

    link_address = ['www.google.com']

    # for link in soup.find_all('a'):
    return render(request, template_name='result.html', context={'link_address': link_address})
