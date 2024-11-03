import flet as ft

class Agenda(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = ft.colors.BLACK
        self.border_radius = 10
        self.padding = ft.padding.only(top=10, left=10, right= 10)
        self.clip_behavior = ft.ClipBehavior.HARD_EDGE

        self.content = ft.Column(
            controls= [
                ft.Column(
                    controls = [
                        ft.Row(
                            controls = [
                                ft.Text(value="Contatos", size=40, weight="bold"),
                                ft.IconButton(icon=ft.icons.ADD, icon_color="blue")
                            ],
                            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment= "center"
                        ),
                        ft.Row(
                            controls= [
                                ft.TextField(hint_text="Buscar", hint_style=ft.TextStyle(color="#919193"), prefix_icon=ft.icons.SEARCH, border_radius=10, expand=True, bgcolor="#1C1C1E", border_color="#1C1C1E")          
                            ]
                        ),
                        ft.Divider(height=8, color="white24"),
                    ]
                ),
                ft.Column(
                    controls= [
                        FormContainer()
                    ],
                )
            ],
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN
        )
    
    def CreateContact(self):
        

class FormContainer(ft.UserControl):
    def __init__(self):
        #self.func = func
        super().__init__()
    
    def build(self):
        return ft.Container(
            width=400,
            height=50,
            bgcolor=ft.colors.WHITE,
            opacity=0,
            border_radius=ft.BorderRadius(top_left=40, top_right=40, bottom_left=0, bottom_right=0),
            margin= ft.margin.only(left=-10, right=-10),
            animate=ft.animation.Animation(400, ft.AnimationCurve.DECELERATE),
            animate_opacity=200,
            padding= ft.padding.only(top=45, bottom=45)
        )

def main(page: ft.Page):
    page.title = "Agenda Telefônica"
    page.window.width = 400
    page.window.height = 800
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    agenda = Agenda()
    page.add(agenda)

if __name__=="__main__":
    ft.app(target=main)