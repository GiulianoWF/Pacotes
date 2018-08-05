#!/usr/bin/env phyton
'''
	Giuliano WF -- Giuka.91@hotmail.com

	Pequeno script para buscar a quantidade de pacotes perdidos em um modem net

	MIT License
'''
import re
import requests

USERNAME = 'admin' #Login do modem.
PASSWORD = 'admin' #Senha para login.
payloadLogin = {'loginUsername':USERNAME,'loginPassword':PASSWORD, 'rememberMe':'rememberMe'} #O nome de cada variável pode ser encontrado no <form> no qual é preenchido o login.

urlLogin= 'http://192.168.1.1/goform/login'    #Este endereço pode ser encontrado analizando o método <form> no qual é preenchido o login.
urlDados = 'http://192.168.1.1/RgConnect.asp'  #Este endereço onde se encontra as informações desejadas.


s = requests.Session()
response = s.post(urlLogin, data=payloadLogin)

dados = s.get(urlDados)
texto = dados.text

print re.findall('<tr bgcolor="#CCCCCC"><td>(.*)</td><td>(.*)</td></tr', texto)  #É usada expressões regulares para obter os dados desejados da página.