from selenium import webdriver
import win10toast_click as win10toast
import PySimpleGUI as sg
import webbrowser

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
    icono_si="C:/Selenium/yes.ico"
    icono_no="C:/Selenium/no.ico"
    if disponible:
        Toaster.show_toast(title="¡Disponible!",msg="Los Motorola Pulse 120 ya están en stock en Carrefour!!!!!",duration=120,icon_path=icono_si,callback_on_click=abrirUrl)
    else:
        Toaster.show_toast(title="Los auriculares aún no están en stock.",msg="Los Motorola Pulse 120 aún no están en stock en Carrefour.",icon_path=icono_no,callback_on_click=abrirUrl)

def abrirUrl():
    webbrowser.open("https://www.carrefour.com.ar/elegi-el-regalo-ideal/auriculares-motorola-over-ear-pulse-120-negro.html")

def __main__():
    url="https://www.carrefour.com.ar/elegi-el-regalo-ideal/auriculares-motorola-over-ear-pulse-120-negro.html"
    disponible=obtenerBotonDisponible(url)
    mostrarCartel(disponible)

if __name__=="__main__":
    __main__()