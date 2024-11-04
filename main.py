import flet as ft

class Contatos(ft.Row):
    def __init__(self, name, surname, number, EditarContato, DeleteContato):
        self.EditarContato = EditarContato
        self.DeleteContato = DeleteContato
        super().__init__()
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.complete_name = self.name + " " + self.surname
        self.number = number
        self.alignment = ft.MainAxisAlignment.START
        self.controls = [
            ft.Container(
                content = ft.Row(
                    controls = [
                        ft.Container(
                            content = ft.Text(value=self.complete_name, color="white", weight="bold", size=16),
                        ),
                        ft.Container(
                            content = ft.Row(
                                controls = [
                                    ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e: self.EditarContato(self)),
                                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: self.DeleteContato(self)),
                                ]
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                alignment=ft.alignment.center_left,
                width=365,
                height= 35,
                margin=ft.margin.only(top=-11, bottom=-11),
                ink= True,
                ink_color="#2C2C2C",
                on_click=lambda e: self.EditarContato(self)
            )
        ]

class FormContainer(ft.UserControl):
    def __init__(self, CriarContato, name, surname, number, AddContato):
        self.CriarContato = CriarContato
        self.name = name
        self.surname = surname
        self.number = number
        self.AddContato = AddContato
        self.editando_contato = False
        super().__init__()

    def build(self):
        return ft.Container(
            width=400,
            height=100,
            bgcolor="#1C1C1E",
            border_radius=20,
            opacity=0,
            margin=ft.margin.only(left=-10, right=-10),
            animate=ft.animation.Animation(400, "decelerate"),
            animate_opacity=200,
            padding=ft.padding.only(top=45, bottom=45),
            content = ft.Column(
                controls = [
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(ft.TextButton(text="Cancelar", on_click=self.CriarContato), width=130, alignment=ft.alignment.center_left),
                            ft.Container(ft.Text(value="Novo Contato", color="white"), width=130, alignment=ft.alignment.center),
                            ft.Container(ft.TextButton(text="OK", on_click=lambda e: self.AddContato(e)), width=125, alignment=ft.alignment.center_right),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls= [
                            ft.Image(src="C:/Users/sopena/Documents/GitHub/contact-iphone/assets/contact.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(text="Adicionar Foto", color="white", bgcolor="#2C2C2C")
                        ]
                    ),
                    ft.Container(
                        content= ft.Column(
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.name
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.surname
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        self.number
                                    ],
                                )
                            ]
                        ),
                        padding=ft.padding.only(top=10)
                    ),
                    
                ]
            )
        )


def main(page: ft.Page):
    page.title = "Agenda Telefônica"
    page.window.width = 400
    page.window.height = 800
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    name = ft.TextField(hint_text="Nome", hint_style=ft.TextStyle(color="#919193"), width=360, bgcolor="#3A3A3A", border_color="transparent")
    surname = ft.TextField(hint_text="Sobrenome", hint_style=ft.TextStyle(color="#919193"), width=360, bgcolor="#3A3A3A", border_color="transparent")
    number = ft.TextField(hint_text="Número", hint_style=ft.TextStyle(color="#919193"), width=360, bgcolor="#3A3A3A", border_color="transparent")

    

    def CriarContato(e):
        name.value = ""
        surname.value = ""
        number.value = ""
        if form.height != 650:
            form.height, form.opacity = 650, 1
            form.update()
        else:
            form.height, form.opacity = 100, 0
            form.update()

    def EditarContato(e):
        formcontainer.editando_contato = True
        contato = e
        name.value = e.name
        surname.value = e.surname
        number.value = e.number
        ok_button.on_click = lambda e: ConfirmarEdit(e, contato)
        ok_button.text = "Confirmar"
        new_contact.value = "Editar Contato"
        if form.height != 650:
            form.height, form.opacity = 650, 1
            form.update()
        else:
            form.height, form.opacity = 100, 0
            form.update()
    
    def ConfirmarEdit(e, contato):
        contato.name = name.value.capitalize()
        contato.surname = surname.value.capitalize()
        contato.complete_name = contato.name + " " + contato.surname
        contato.controls[0].content.controls[0].content.value = contato.complete_name
        if form.height == 650:
            form.height, form.opacity = 100, 0
            form.update()
        ok_button.on_click = lambda e: AddContato(e)
        ok_button.text = "Ok"
        new_contact.value = "Novo Contato"
        _main_column_.update()
    
    def DeleteContato(e):
        print("funcionou")
        i = _main_column_.controls.index(e)
        print(i)
        _main_column_.controls.pop(i)
        _main_column_.controls.pop(i)
        _main_column_.update()

    def AddContato(e):
        _main_column_.controls.append(Contatos(name.value, surname.value, number.value, EditarContato, DeleteContato))
        _main_column_.controls.append(ft.Divider(height=3, color="white24"))
        if form.height == 650:
            form.height, form.opacity = 100, 0
            form.update()
        name.value = ""
        surname.value = ""
        _main_column_.update()

    _main_column_ = ft.Column(
        scroll="hidden",
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(value="Contatos", size=40, weight="bold"),
                    ft.IconButton(icon=ft.icons.ADD, on_click=lambda e: CriarContato(e))
                ],
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.TextField(hint_text="Buscar", hint_style=ft.TextStyle(color="#919193"), prefix_icon=ft.icons.SEARCH, border_radius=10, expand=True, bgcolor="#1C1C1E", border_color="transparent"),
                ]
            ),
            ft.Divider(height=3, color="white24"),
        ]
    )

    formcontainer = FormContainer(CriarContato, name, surname, number, AddContato)

    page.add(
        ft.Container(
            width= 400,
            height= 800,
            bgcolor= "black",
            padding= ft.padding.only(left=10, right=10, top=10),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            margin= ft.margin.only(left=-10, right=-10, top=-10, bottom=-10),
            content= ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                controls=[
                        _main_column_,
                        formcontainer
                    ],
                )
            )
        )
    page.update()
    form = page.controls[0].content.controls[1].controls[0]
    ok_button = page.controls[0].content.controls[1].controls[0].content.controls[0].controls[2].content
    new_contact = page.controls[0].content.controls[1].controls[0].content.controls[0].controls[1].content
    column = page.controls[0].content.controls[0]

if __name__=="__main__":
    ft.app(target=main)