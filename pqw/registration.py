import flet as ft
import sqlite3
from main import *
def show_registration_form(page: ft.Page):
    page.title = "IT PROGER"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 400
    page.window_resizable = False

    def register(e):
        db = sqlite3.connect('it.proger')
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    password TEXT
        )""")
        cur.execute("INSERT INTO users (login, password) VALUES (?, ?)", (user_login.value, user_password.value))       
        db.commit()
        db.close()

        user_login.value = ""
        user_password.value = ""
        btn_reg.text = 'Добавлено'
        page.update()

    def validate(e):
        if all([user_login.value, user_password.value]):
            btn_reg.disabled = False
            btn_auth.disabled = False
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True

        page.update()
     
    def auth_user(e):
        db = sqlite3.connect('it.proger')
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE login = ? AND password = ?", (user_login.value, user_password.value))
        if cur.fetchone() is not None:
            user_login.value = ""
            user_password.value = ""
            btn_auth.text = 'Авторизованно'

            # Очистить страницу и запустить основное приложение
            page.clean()
            main_app(page)  # Вызов основного приложения

        else:
            page.snack_bar = ft.SnackBar(ft.Text("Пользователь не найден"))
            page.snack_bar.open = True
            page.update()

        db.commit()
        db.close()

    user_login = ft.TextField(label="Логин", width=200, on_change=validate)
    user_password = ft.TextField(label="Пароль", password=True, width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text="Регистрация", width=200, on_click=register, disabled=True)
    btn_auth = ft.OutlinedButton(text="Авторизовать", width=200, on_click=auth_user, disabled=True)

    panel_register = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Добавить"),
                    user_login,
                    user_password,
                    btn_reg
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    panel_auth = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Авторизация"),
                    user_login,
                    user_password,
                    btn_auth
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.VERIFIED_USER, label="Регистрация"),
            ft.NavigationBarDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Авторизация"),
        ],
        on_change=lambda e: page.clean() or page.add(panel_register if e.control.selected_index == 0 else panel_auth)
    )
    page.add(panel_register)



    page.add(main)
    page.update()
