import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "jSD6yPYWFBOFE0kaWwUyLxK5u8yQP2cR"

while True:
	orig = input('Introduzca Ciudad de origen: ')
	if orig == 's':
		print('Saliendo del programa')
		break
	dest = input('Ciudad de Destino: ')
	if dest == 's':
                print('Saliendo del programa')
                break
	url = main_api + urllib.parse.urlencode({'key': key, 'from':orig, 'to':dest, 'unit':'k'})
	json_data = requests.get (url) .json()
	json_status = json_data ['info'] ['statuscode']
	if json_status == 0:
		print ('Llamada de ruta exitosa. Entregando informacion: ')
	print ('=============================================')
	print ('Distancia desde ' + orig + ' hasta ' + dest)
	print ('Duración del viaje ' + (json_data['route']['formattedTime']))
	print ('Kilometros : ' + str('{:.1f}' .format(json_data['route']['distance'])))
	print ('=============================================')
	print ('Instrucciones para llegar a ' + dest + ' :\n')
	for each in json_data['route']['legs'][0]['maneuvers']:
		print(each['narrative'] + ' (' + str('{:.1f}'.format(each['distance'])) + ' km)')
	print ('=============================================\n')


