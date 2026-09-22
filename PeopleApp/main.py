import flet as ft 

def main(page: ft.Page):

    def add_task(e):
            nome_text = input_nome.value
            idade_text = input_idade.value
            email_text = input_email.value


            card = ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column([
                        ft.Text(nome_text, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Idade: {idade_text}"),
                        ft.Text(f"E-mail: {email_text}"),
        ])
    )
)


            input_nome.value = ''
            input_idade.value = ''
            input_email.value = ''
            output_col.controls.append(card)
            page.update()

    input_nome= ft.TextField(
        expand=True,
        hint_text = 'Nome...'
    )
    input_idade= ft.TextField(
        expand=True,
        hint_text = 'Idade...'
    )
    input_email= ft.TextField(
        expand=True,
        hint_text = 'Email...'
    )
    input_btn = ft.IconButton(
        icon= ft.Icons.SEND,
        on_click= add_task
    )
    input_col = ft.Column (
        expand=True,
        horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
        scroll = ft.ScrollMode.AUTO,
        controls=[input_nome, input_idade, input_email]
    )
    input_row = ft.Row(
        controls=[input_col, input_btn]
    )
    output_col = ft.Column(
         
    )
    main_col = ft.Column(
        expand = True,
        controls = [input_row, output_col]
    )

    page.title = 'Lista de tarefas'
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)
   