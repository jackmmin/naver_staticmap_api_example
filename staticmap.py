# 인터넷창으로 좌표지역 보기

import requests
from bs4 import BeautifulSoup
import webbrowser

# 클이언트 ID
client_id = '발급받은 client id를 입력하세요.'
# 클라이언트 KEY
client_key = '발급받은 client key를 입력하세요.'

# geocode url
geocode_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
# static map url
staticmap_url = 'https://naveropenapi.apigw.ntruss.com/map-static/v2/raster'

query = input("주소지를 입력하세요 : ")

# query : 찾을 주소의 한글명
# X-NCP-APIGW-API-KEY-ID : 클라이언트 아이디
# X-NCP-APIGW-API-KEY : 클라이언트 키
geocode_query = '?' + 'query=' + query + '&X-NCP-APIGW-API-KEY-ID=' + client_id + '&X-NCP-APIGW-API-KEY=' + client_key

geo_url = geocode_url + geocode_query
geo_result = requests.get(geo_url).text
result_x_sta = geo_result.find('"x"')+5
result_x_end = geo_result.find('"y"')-2
result_x = geo_result[result_x_sta:result_x_end]

result_y_sta = geo_result.find('"y"')+5
result_y_end = geo_result.find('"distance"')-2
reuslt_y = geo_result[result_y_sta:result_y_end]

# w : 표시할 지도의 가로
# h : 표시할 지도의 세로
# center : 좌표
# X-NCP-APIGW-API-KEY-ID : 클라이언트 아이디
# X-NCP-APIGW-API-KEY : 클라이언트 키
staticmap_query = '?' + 'w=300&h=300' + '&center=' + result_x + ',' + reuslt_y + '&level=14' +'&X-NCP-APIGW-API-KEY-ID=' + client_id + '&X-NCP-APIGW-API-KEY=' + client_key
static_url = staticmap_url + staticmap_query
webbrowser.open(static_url)
