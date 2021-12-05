# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4AQfIAQzYAQHoAQH4AQKIAgGoAgO4AvTIm_IFwAIB&sid=eae1a774e77c394c5e69703d37e033a3&sb=1&src=searchresults&src_elem=sb&error_url=https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4AQfIAQzYAQHoAQH4AQKIAgGoAgO4AvTIm_IFwAIB;sid=eae1a774e77c394c5e69703d37e033a3;tmpl=searchresults;city=-2109472;class_interval=1;dest_id=-2109472;dest_type=city;dr_ps=IDR;dtdisc=0;from_idr=1;ilp=1;inac=0;index_postcard=0;label_click=undef;offset=0;postcard=0;room1=A%2CA;sb_price_type=total;shw_aparth=1;slp_r_match=0;srpvid=7df1609ef03a0103;ss_all=0;ssb=empty;sshis=0;top_ufis=1&;&sr_autoscroll=1&ss=Rishīkesh&is_ski_area=0&ssne=Rishīkesh&ssne_untouched=Rishīkesh&city=-2109472&checkin_year=2020&checkin_month=3&checkin_monthday=4&checkout_year=2020&checkout_month=3&checkout_monthday=5&group_adults=2&group_children=0&no_rooms=1&from_sf=1'

response=requests.get(url,headers=headers)


soup=BeautifulSoup(response.content,'lxml')

#print(soup.select('.a-carousel-card')[0].get_text())

for item in soup.select('.sr_property_block'):
	try:
		print('----------------------------------------')
		print(item.select('.sr-hotel__name')[0].get_text().strip())
		print(item.select('.hotel_name_link')[0]['href'])
		print(item.select('.bui-review-score__badge')[0].get_text().strip())
		print(item.select('.bui-review-score__text')[0].get_text().strip())
		print(item.select('.bui-review-score__title')[0].get_text().strip())
		print(item.select('.hotel_image')[0]['data-highres'])
 
		print(item.select('.bui-price-display__value')[0].get_text().strip())

		print('----------------------------------------')
	except Exception as e:
		#raise e
		print('')