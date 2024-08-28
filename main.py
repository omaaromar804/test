from flet import *

def main(page:Page):
    page.title = "flashlight"
    page.scroll="Auto"
    page.window.width="390"
    page.window.height="740"
    page.window.top="1"
    page.window.left="960"
    page.theme_mode=ThemeMode.LIGHT
    page.bgcolor=colors.WHITE
    flashlight=Flashlight()
    page.overlay.append(flashlight)
    ph=PermissionHandler()
    page.overlay.append(ph)
    def open_app(e):
        ph.open_app_settings()
    page.add(
        AppBar(
            leading=Icon(icons.HOME),
            leading_width="40",
            bgcolor="#e1331e",
            color=colors.WHITE,
            title=Text("flashlight app"),
            center_title=True,
            actions=[
                IconButton(icon=icons.SETTINGS,tooltip="settings",on_click=open_app)
            ]
        ),
        Row([Text("\n\nWelcome!",size="30",text_align="center",color=colors.BLACK)],alignment=MainAxisAlignment.CENTER),
        Row([
Image(src="images/logo.png",width="260",tooltip="logo")
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            ElevatedButton("On",width="100",icon=icons.PLAY_ARROW,style=ButtonStyle(bgcolor="#e1331e",color=colors.WHITE,padding=15,shape=ContinuousRectangleBorder(radius=100)),on_click=lambda _:flashlight.turn_on()),
            ElevatedButton("Off",width="100",icon=icons.PLAY_DISABLED,style=ButtonStyle(bgcolor="#e1331e",color=colors.WHITE,padding=15,shape=ContinuousRectangleBorder(radius=100)),on_click=lambda _:flashlight.turn_off())

        ],alignment=MainAxisAlignment.CENTER),
        Row([
Text("\n\n\n\n\n\nOmar Almohaws",size=16,color=colors.BLACK)
        ],alignment=MainAxisAlignment.CENTER)
    )
    page.update()

app(main)
