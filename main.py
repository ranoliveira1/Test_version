import flet as ft

def main(page: ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor="#2A685A"
    page.padding=0
    
    def update_screen_size(e=None):
        screen_size_text.value = f"Largura da tela: {page.window.width}, Altura da tela: {page.window.height}"
        page.update()

    # Texto para exibir o tamanho da tela
    screen_size_text = ft.Text(height=100, offset=ft.Offset(x=0.3, y=0.3))

    # Atualizar o tamanho da tela ao iniciar o aplicativo
    update_screen_size()

    # Configurar evento de redimensionamento da janela
    page.window.on_resized = update_screen_size
    

    layout1 = ft.Container(
            bgcolor=ft.colors.WHITE,
            opacity=0.2,
            height=200,
            width=500,
            content=ft.Column(
                controls=[ft.Text(value="ok")]
            )
    )

    layout = ft.Container(
            border_radius=ft.border_radius.all(20),
            content=ft.Column(
                    width=700,
                    height=600,
                    scroll=ft.ScrollMode.ALWAYS,
                    controls=[
                        screen_size_text,
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            opacity=0.2,
                            width=700,
                            #height=600,
                            border_radius=ft.border_radius.all(20),
                            content=ft.Text(value="okokokokookokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokokk", color="black", no_wrap=False, size=100),
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER
                        )
                    ]
                )
    )
            






    # all_files = []

    # def on_files_selected(e):
    #     path=e.files[0].path
    #     name=e.files[0].name
    #     print(name)
    #     print(path)
    #     # for file in e.files:
    #     #     all_files.append(file.path)
        
    #     # print(all_files[0])
    #     url = upload_file(name, path)
    #     print(url)
    #     create_Record({'Anexo': [{'url': url}]})


    # file_picker = ft.FilePicker(
    #     on_result=on_files_selected
    # )

    # btn_select_files = ft.ElevatedButton(
    #     text="Upload Files",
    #     on_click=lambda _: file_picker.pick_files(allow_multiple=True)
    # )


    page.add(layout)


ft.app(target=main, assets_dir="assets")

#file = 'https://storage.googleapis.com/attachments_to_airtable/step2'

#create_Record({"Anexo": [{"url": file}]})