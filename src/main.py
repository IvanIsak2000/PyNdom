from textual.app import App, ComposeResult
from textual.widgets import Label, Button


class MainMenu(App[str]):
    def compose(self):
        yield Label('PyRPG')
        yield Button('Start', id='start')
        yield Button('Settings', id='settings')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        move = self.exit(event.button.id)
        return move 


class StartState(App[str]):
    ...

if __name__ == "__main__":
    app = MainMenu()
    reply = app.run()
    print(reply)
