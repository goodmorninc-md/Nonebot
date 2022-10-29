import requests
if __name__ == "__main__":
	# url = "https://devapi.qweather.com/v7/weather/now?location=101210111&key=5a24fe6e617640f39f103a268b8bfe6f"
	# headers = {"User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 105.0.0.0Safari /537.36Edg /105.0.1343.50"}
	# response = requests.get(url = url,verify=False,json=True)
	# text = eval(response.text)
	# print(text["now"])
	# url2 = "https://geoapi.qweather.com/v2/city/lookup?location=钱塘&key=5a24fe6e617640f39f103a268b8bfe6f"
	# response2 = requests.get(url=url2, verify=False, json=True)
	# print(response2.text)
	content = {'obsTime': '2022-10-05T20:36+08:00', 'temp': '16', 'feelsLike': '13',
			  'icon': '305', 'text': '小雨', 'wind360': '77', 'windDir': '东北风', 'windScale': '3', 'windSpeed': '18', 'humidity': '88', 'precip': '0.0', 'pressure': '1018', 'vis': '15', 'cloud': '91', 'dew': '14'}
	print(content["icon"])
	print(content["text"])