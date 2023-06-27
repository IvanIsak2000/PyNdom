from textual.app import App, ComposeResult
from textual.widgets import Input, Label, RadioButton, RadioSet, Button
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
        with VerticalScroll():

            with RadioSet():
                yield (RadioButton('Warrior'))
                yield (RadioButton('Vampire'))
                yield (RadioButton('Witch'))
                yield (RadioButton('Elf '))
                yield (RadioButton('Druid'))
                yield (RadioButton('Rogue'))

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self.exit(str(event.pressed.label))
        
username  = InputName()
username = username.run()

character = CharacterSelection()
selection = character.run()
print(selection)





