import flet as ft 
import os
from view import BookApp

def main(page: ft.Page):
    page.title = 'App de livros'
    book_app = BookApp()
    page.add(BookApp())
    book_app.load_books()

    '''def add_book(e):
            title_text = input_title.value
            autor_text = input_autor.value
            desc_text = input_desc.value
            preco_text = input_preco.value
            
            card = ft.Card(
                content=ft.Container(
                padding=10,
                content=ft.Column([
                    ft.Text(title_text, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Autor: {autor_text}"),
                    ft.Text(f"Descrição: {desc_text}"),
                    ft.Text(f"Preço:{preco_text}")
                    ]
                    ) 
                )
            )

            input_title.value = ''
            input_autor.value = ''
            input_desc.value = ''
            input_preco.value = ''
            output_col.controls.append(card)
            page.update()

    input_title= ft.TextField(
        expand=True,
        hint_text = 'Título...'
    )
    input_autor= ft.TextField(
        expand=True,
        hint_text = 'Autor...'
    )
    input_desc= ft.TextField(
        expand=True,
        hint_text = 'Descrição...'
    )
    input_preco= ft.TextField(
            expand=True,
            hint_text = 'Preço...'
        )
    input_btn = ft.IconButton(
        icon= ft.Icons.SEND,
        on_click= add_book
    )

    input_col = ft.Column (
            expand=True,
            horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
            scroll = ft.ScrollMode.AUTO,
            controls=[input_title, input_autor, input_desc, input_preco]
        )
    
    input_row = ft.Row(
            controls=[input_col, input_btn]
        )
    output_col = ft.Column(
             
        )
    main_col = ft.Column(
            expand = True,
            controls = [input_row, output_col]
        )'''

if __name__ == "__main__":
    ft.run(main)
   