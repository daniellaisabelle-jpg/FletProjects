import flet as ft

EMOJIS = ['😀', '😅', '🤩', '🥵', '👾']
# IDX controla o indice da lista de emojis e smp estará atualizado com o índice do emoji que está sendo exibido
IDX = 0
# a função main recebe o objeto página que carrega todos os elementos gráficos. Page é criado pelo framework flet durante a execução
def main(page: ft.Page):
    # configurações da página
    
    page.title = 'EmojiApp'
    # alinha verticalmente os elementos no centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # parametro value deste objeto contém o valor mostrado na tela
    input = ft.Text(value=EMOJIS[0], size=90)

    #função que é executada ao clicar em btn

    def refresh_click(e):
        global IDX
        # se idx > tamanho de emojis:
        # idx volta para 0
        IDX = (IDX + 1) % len(EMOJIS)
        # altera o elemento textual p emoji na posição idx
        input.value = EMOJIS[IDX]
    #elemento botão com icon de atualizar
    btn = ft.IconButton(ft.Icons.REFRESH, on_click=refresh_click)
    # elemento de layout; cada linha item inserido em controls irá ser posicionado em coluna desta linha. "INPUT" e "BTN" ficarão lado a lado.
    row = ft.Row(
        alignment= ft.MainAxisAlignment.CENTER,
        controls=[
            input,
            btn
        ]
    )

    # add elementos na página
    page.add(row)

if __name__ == '__main__':
    # dá início a execução do app
    # target: aponta para a função que irá manipular a página do app
    ft.run(main)    
