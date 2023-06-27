from textual.app import App, ComposeResult
from textual.widgets import Input, Label, Button, Checkbox
from textual.containers import Center, VerticalScroll

class InputName(App):
    def compose(self) -> ComposeResult:
        yield Center(Label('Please write your name, stranger:'))
        yield Input(placeholder=" ", id='name')
        yield Center(Button('Save!', id='save'))

    def on_mount(self) -> None:
        self.screen.styles.background = "black"
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
          self.exit(str(event.button.id))

class CharacterSelection(App[None]):
    def compose(self) -> ComposeResult:
            yield Center(Label('Please choose character:'))
            with VerticalScroll():
                yield Center(Checkbox('Warrior'))
                yield Center(Checkbox('Vampire'))
                yield Center(Checkbox('Witch'))
                yield Center(Checkbox('Elf '))
                yield Center(Checkbox('Druid'))
                yield Center(Checkbox('Rogue'))

username  = InputName()
username = username.run()

character = CharacterSelection()
print(character.run())






