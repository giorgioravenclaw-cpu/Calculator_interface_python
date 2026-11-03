import flet as ft
import random
max = None  
min= None 
quant= None   
 
 
def main(page: ft.Page):
    page.title = "dispari compresi tra a e b (esclusi)"
    page.window.width = 320
    page.window.height = 550
 
    result1 = ft.Text(value="0", size=32, color=ft.Colors.WHITE)  # numero in composizione
 
    display_a = ft.Text(value="min = ?", size=18, color=ft.Colors.CYAN)
    display_b = ft.Text(value="max = ?", size=18, color=ft.Colors.CYAN)
    #display_quant = ft.Text(value="quant = ?", size=18, color=ft.Colors.CYAN)
    
    output = ft.Text(value="", size=18, color=ft.Colors.AMBER)
 
    def button_click(e):
        global min,max,quant
        data = e.control.data
        current1 = result1.value
 
        if data == "C":
            result1.value = "0"
 
        elif data == "min":
            try:
                min = int(current1)
                display_a.value = f"min = {min}"
                result1.value = "0"
            except ValueError:
                result1.value = "0"

        #elif data == "quant":
                  #  try:
                  #      quant = int(current1)
                    #    display_a.value = f"quant= {quant}"
                    #    result1.value = "0"
                    #except ValueError:
                    #    result1.value = "0"

        elif data == "max":
                    try:
                        max = int(current1)
                        display_b.value = f"max = {max}"
                        result1.value = "0"
                    except ValueError:
                        result1.value = "0"
 
        
 
        elif data == "=":
            if max is None or min is None: #or quant is None :
                output.value = "Inserisci prima sia a che b"
            else:
                #for n in range (1,quant):
                N1=random.randint(min,max)
                numero_casuale=[]
                numero_casuale.append(N1)
                
                if numero_casuale: # se dispari esiste
                    output.value = "numero casuale: ".join(str(n) for n in numero_casuale)
                else:
                    output.value = "Nessun dispari trovato tra a e b"
 
        else:  # cifre 0-9 e "-"
            if current1 == "0":
                result1.value = data
            else:
                result1.value = current1 + data
 
        page.update()
 
    def btn(label):
        return ft.ElevatedButton(
            label,
            data=label,
            on_click=button_click,
            expand=True, # Dice al bottone di espandersi per occupare tutto lo spazio disponibile nella riga (ft.Row) in cui si trova, 
            #invece di avere una 
            #dimensione fissa piccola — è quello che fa sì che i bottoni nella stessa riga abbiano tutti la stessa larghezza, 
            # riempiendo lo schermo.
        )
 
    page.add(
        ft.Container(
            content=result1,
            alignment=ft.Alignment.CENTER_RIGHT,
            padding=20,
            bgcolor=ft.Colors.BLACK,
        ),
        ft.Row([btn("7"), btn("8"), btn("9")]),
        ft.Row([btn("4"), btn("5"), btn("6")]),
        ft.Row([btn("1"), btn("2"), btn("3")]),
        #ft.Row([btn("C"), btn("0"), btn("quant")]),
        ft.Row([btn("C"), btn("0")]),
        ft.Row([btn("min"),btn("max"), btn("=")]),
        ft.Divider(),
        display_a,
        display_b,
        #display_quant,
        
        output,
    )
 
 
ft.run(main)