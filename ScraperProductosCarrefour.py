from selenium import webdriver
import win10toast
import PySimpleGUI as sg

def obtenerBotonDisponible(url):
    opciones = webdriver.ChromeOptions()
    opciones.headless = True
    browser=webdriver.Chrome(options=opciones)
    browser.get(url)
    disponible=browser.find_element_by_css_selector("#product_addtocart_form > div.info-y-galleria-wrapper.clearfix > div.informacion-producto > div.add-to-cart-wrapper > div > button").is_enabled()
    browser.close()
    return disponible

def mostrarCartel(disponible):
    Toaster=win10toast.ToastNotifier()
    if disponible:
        Toaster.show_toast(title="¡Disponible!",msg="Los Motorola Pulse 120 ya están en stock en Carrefour!!!!!")
    else:
        Toaster.show_toast(title="Los auriculares aún no están en stock.",msg="Los Motorola Pulse 120 aún no están en stock en Carrefour.")

def __main__():
    url="https://www.carrefour.com.ar/elegi-el-regalo-ideal/auriculares-motorola-over-ear-pulse-120-negro.html"
    disponible=obtenerBotonDisponible(url)
    mostrarCartel(disponible)

if __name__=="__main__":
    __main__()
