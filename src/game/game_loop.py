from textual.app import App, ComposeResult
from textual.widgets import  Label, Button 
from textual.containers import Center, VerticalScroll, HorizontalScroll

from game.events import get_random_event
import sys

class Event(App):
    def compose(self) -> ComposeResult:
        event = get_random_event()
        yield Center(Label(f"\n\n\n\n{event['text']}\n\n\n\n"))


        if event['result'].split()[0] == 'damage':
            with HorizontalScroll():
                yield Center(Button.success('Pass'))
                yield Center(Button.error('Attack'))

            with VerticalScroll():
                yield Center(Button.error('Exit'))

        else:
            with VerticalScroll():
                yield Center(Button.success('Next'))
                yield Center(Button.error('Exit'))

    def on_mount(self) -> None:
        self.screen.styles.background = "black"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button.label))




while 1:
    currency_event = Event()
    move = currency_event.run()

    if move == 'Attack':
        pass

    if move == 'Exit':
        sys.exit()
