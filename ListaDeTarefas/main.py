import flet as ft 

def main(page: ft.Page):

    def add_task(e):
            task_text = input_txt.value
            if task_text.strip() == '':
                 return
            
            task_label = ft.Text(task_text)

            def task_completa(e):
                if e.control.value:
                      task_label.opacity = 0.3
                else:
                     task_label.opacity = 1
                page.update()
            checkbox = ft.Checkbox(
                on_change=task_completa
            )

            task = ft.Row(
                controls=[
                    checkbox,
                    task_label,
                ]
            )

            output_col.controls.append(task)
            input_txt.value = ''
            page.update()

    input_txt= ft.TextField(
        expand=True,
        hint_text = 'Descreva a tarefa...'
    )
    input_btn = ft.IconButton(
        icon= ft.Icons.SEND,
        on_click= add_task
    )

    input_row = ft.Row(
         controls=[input_txt,input_btn]
        )

    output_col = ft.Column (
        expand=True,
        horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
        scroll = ft.ScrollMode.AUTO,
        controls=[]
    )
    main_col = ft.Column(
        expand = True,
        controls = [input_row, output_col]
    )

    page.title = 'Lista de tarefas'
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)
