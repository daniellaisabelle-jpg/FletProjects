import flet as ft

def main(page: ft.Page):
    #muda o título da janela no web e do app no mobile
    page.title = 'HelloApp'
    # cria um componente visual de texto 
    text = ft.Text(
        value='Hello, world',
        text_align=ft.TextAlign.CENTER,
        width=900
        )

    # metodo add adiciona elementeos (controls) dentro da página
    # para ser mostrado na tela
    page.add(text)

if __name__=='__main__':
    # ft.app cria o objeto page = Page()
    # o objeto page é enviado para a função target (main)
    # para ser preenchido.
    ft.app(target=main)
