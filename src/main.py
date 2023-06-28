from textual.app import App, ComposeResult
from textual.widgets import Label, Button
from textual.containers import Center

import webbrowser
import sys

logo ='''

8888888b.           888b    888      888                        
888   Y88b          8888b   888      888                        
888    888          88888b  888      888                        
888   d88P 888  888 888Y88b 888  .d88888  .d88b.  88888b.d88b.  
8888888P"  888  888 888 Y88b888 d88" 888 d88""88b 888 "888 "88b 
888        888  888 888  Y88888 888  888 888  888 888  888  888 
888        Y88b 888 888   Y8888 Y88b 888 Y88..88P 888  888  888 
888         "Y88888 888    Y888  "Y88888  "Y88P"  888  888  888 
                888                                             
           Y8b d88P                                             
            "Y88P"                                              

'''

class MainMenu(App):
    def compose(self):
        yield Center(Label(logo))
        yield Center(Button('Start', id='start'))
        yield Center(Button('Settings', id='settings'))
        yield Center(Button('GitHub', id='github'))
        yield Center(Button('Exit', id='exit'))
    
    def on_mount(self) -> None:
        self.screen.styles.background = "black"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button.id))


if __name__ == "__main__":
    user_choose_mode = MainMenu()
    mode = user_choose_mode.run()
    
    if mode == 'start':
        import start

    elif mode == 'github':
        webbrowser.open('https://github.com/IvanIsak2000/PyNdom')
        
    elif mode == 'exit':
        sys.exit()