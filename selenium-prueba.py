from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import pytest_html 




#Funcion para usar time.sleep

def espera(tiempo):
    time.sleep(tiempo)
    return 

# Inicializar el navegador (en mi caso, Chrome)
browser = webdriver.Chrome()
# Abrir la página web donde se encuentra el formulario
browser.get('https://www.saucedemo.com/')

titulo_de_la_pagina = browser.title
def historia1(browser):
#--Historia 1:

    # Aqui busca los campos de usuario y contrasena 
    usuario = browser.find_element(By.ID, 'user-name')

    contrasena = browser.find_element(By.ID, 'password')


    # Agrega por entrada los datos en los campos de inicio de sesion 
    usuario.send_keys('standard_user')
    espera(2)
    contrasena.send_keys('secret_sauce')
    espera(2)
    browser.save_screenshot("captura_de_pantalla.png")

    # Pulsa el boton de login para pasar a la pagina principal
    boton_enviar = browser.find_element(By.ID, 'login-button')
    boton_enviar.click()

    espera(2)
    assert titulo_de_la_pagina in browser.title
    
historia1(browser)


#---Historia 2 
def historia2(browser):
    #Agrega un objeto al carrito
    boton_agregar_mochila = browser.find_element(By.ID,'add-to-cart-sauce-labs-backpack')
    boton_agregar_mochila.click()
    espera(2)

    #Agrega un objeto al carrito
    boton_agregar_polo = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    boton_agregar_polo.click()
    espera(2)
    browser.save_screenshot("captura_de_pantalla2.png")
    assert titulo_de_la_pagina in browser.title

historia2(browser)


def historia3(browser):
    ###Historia 3 

    #Abre el carrito 
    boton_carrito = browser.find_element(By.LINK_TEXT, "2")
    boton_carrito.click()
    espera(2)
    browser.save_screenshot("captura_de_pantalla3.png")
    assert titulo_de_la_pagina in browser.title
    
historia3(browser)

def historia4(browser):
    ### Historia 4 

    #Abre la caja
    boton_caja = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
    boton_caja.click()
    espera(2)


    #Pulsa el campo de nombre e introduce el nombre
    facturacion_nombre = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]")
    facturacion_nombre.click()
    facturacion_nombre.send_keys("Stanley")
    espera(2)


    #Pulsa el campo de nombre e introduce el nombre
    facturacion_apellido = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]")
    facturacion_apellido.click()
    facturacion_apellido.send_keys("Faria")
    espera(2)


    #Pulsa el campo de nombre e introduce el nombre

    facturacion_codigo_postal = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]")
    facturacion_codigo_postal.click()
    facturacion_codigo_postal.send_keys('10013')
    espera(2)
    browser.save_screenshot("captura_de_pantalla4.png")
    assert titulo_de_la_pagina in browser.title
   
historia4(browser)

def historia5(browser):
#---Historia 5 

    #Pulsa el boton continuar para pasar a la facturacion
    continuar = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]")
    continuar.click()
    espera(2)
    browser.save_screenshot("captura_de_pantalla5.png")
    #Pulsa el boton de finalizar 
    boton_finalizar = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]")
    boton_finalizar.click()

    espera(2)
historia5(browser)

def volver(browser):
    espera(2)
    #Vuelve a la pantalla inicial 
    barra = browser.find_element(By.ID, "react-burger-menu-btn")
    barra.click()
    espera(2)
    volver_inicio = browser.find_element(By.ID, "inventory_sidebar_link")
    volver_inicio.click()

    espera(2)
    ###Cuanto tiene la pagina activa
    espera(15)
    # Cerrar el navegador
    browser.quit()
volver(browser)


