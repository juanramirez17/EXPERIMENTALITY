# EXPERIMENTALITY
## Contenido
### ESP8266_mqtt_DHT11 : Programación del wemos D1 mini, para conectarse a red Wifi, suscribirse a un topic y publicar los datos sensados por el sensor DHT11.
### flask_mqtt_mysql : Programa para suscribirse al topic al que se envia los datos sensados por el DHT11. Recibe los datos y los almacena en mySQL.
### flask_mqtt_mysql_plot: Realiza lo mismo que el programa de la carpeta "flask_mqtt_mysql", pero adicionalmente la presenta en tiempo real en un pagina web.
### load_and_clean_data: Contiene la carpeta "datos", donde estan toda los datos del clima obtenidos de SIATA, estos datos son limpiados y ordenados en el programa clean_data.py. La salida de este programa será el archivo "Temperature_2013_01_01__2017_05_31.csv" que contiene todo los datos limpios.
### describe_data: Contiene el programa que resumen informacón de los datos "Temperature_2013_01_01__2017_05_31.csv" , por ejemplo, la temperatura promedio por año, mes, dia.
### predictive_model: Contiene 2 programas que permiten predecir la temperatura para 7 días a partir de una fecha determinada. Contine un modelo de regresion lineal y otro que combina regresion polinomial y el filtro de kalman.
