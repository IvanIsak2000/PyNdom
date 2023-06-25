from textual.app import App, ComposeResult
from textual.widgets import Input, Label, Button
from textual.containers import Center

class InputName(App):
    def compose(self) -> ComposeResult:

        # first_message = []
        # first_message +='Hey Ya! First? '
        # first_message += "Before starting the game, "
        # first_message +=  "let's decide on the settings!)

        yield Center(Label('Please write your name, stranger:'))
        yield Input(placeholder=" ", id='name')
        yield Center(Button('Save!' ))

    def on_mount(self) -> None:
        self.screen.styles.background = "black"

app = InputName()
print(app.run())



