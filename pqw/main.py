import flet as ft
from exemples import create_panel_exempless
from ui import create_app_bar, create_panel_plans, show_page 

def main(page: ft.Page):
    page.title = 'APP'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
    page.window_width = 350
    page.window_height = 600
    page.window_resizable = False
    
    app_bar = create_app_bar()
    page.add(app_bar)

    panel_exemples = create_panel_exempless()
    
    selected_plan = ft.Text(size=24, weight=ft.FontWeight.BOLD)
    content_area = ft.Column()

    panel_plans = create_panel_plans(content_area, selected_plan)

    # Журнал
    panel_journal = ft.Row([ft.Text("Журнал")])
    
    # Профиль
    panel_profile = ft.Row([ft.Text("Профиль")])

    def navigate(e):
        index = e.control.selected_index
        page.clean()

        if index == 0:
            app_bar.title = ft.Text("Упражнения", size=20)
            page.add(panel_exemples)
        elif index == 1:
            app_bar.title = ft.Text("Планы", size=20)
            page.add(panel_plans)
            show_page(0, content_area)  # Показать первую страницу по умолчанию
        elif index == 2:
            app_bar.title = ft.Text("Журнал", size=20)
            page.add(panel_journal)
        elif index == 3:
            app_bar.title = ft.Text("Профиль", size=20)
            page.add(panel_profile)

        page.add(app_bar)
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.FITNESS_CENTER, label="Упражнения"),
            ft.NavigationDestination(icon=ft.icons.EVENT, label="Планы"),
            ft.NavigationDestination(icon=ft.icons.SCHEDULE, label="Журнал"),
            ft.NavigationDestination(icon=ft.icons.PERSON, label="Профиль"),
        ],
        on_change=navigate,
        bgcolor=ft.colors.DEEP_ORANGE_300,
        selected_index=0,
    )
    
    page.add(panel_exemples)


    

ft.app(target=main)
