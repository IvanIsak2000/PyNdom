from textual.app import App, ComposeResult
from textual.widgets import Label, RadioButton, RadioSet, Button, Header
from textual.containers import Center, VerticalScroll

from game.character_logos import *
from game.texts import *
from game.name import get_random_name



CSS_for_characters = '''

    #heal{
        background: green;
        }

    #power{
        background: red;
        }

    #energy{
        background: yellow 60%;
        }

    #weapon{
        background: blue; 
        }

'''

class CharacterSelection(App[None]):
    CSS = '''
    VerticalScroll {
    align: center middle;
    }

    Horizontal {
        width: 100;
        height: 100%;
        align: center middle;

    }

    RadioSet {
        width: 100%;
        align: center middle;


    }

    '''

    def compose(self) -> ComposeResult:

        name = get_random_name()
        
       
        with VerticalScroll():
            yield Center(Label(f'Welcome {name}!\n'))
            with RadioSet():
                yield RadioButton('Warrior')
                yield RadioButton('Vampire')
                yield RadioButton('Ork')
                # yield RadioButton('Witch')
                # yield RadioButton('Elf')
                # yield RadioButton('Druid')
                # yield RadioButton('Rogue')
                
    def on_mount(self) -> None:
        self.screen.styles.background = "black"                

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self.exit(str(event.pressed.label))


class Warrior(App):
    # CSS = CSS_for_characters

    def compose (self) -> ComposeResult:
        yield Center(Label(warrior_logo))
        yield Center(Label(warrior_health, id='heal'))
        yield Center(Label(warrior_power, id='power'))
        yield Center(Label(warrior_starting_energy, id='energy'))
        yield Center(Label(warrior_starting_weapon, id='weapon'))
        yield Center(Button.success('Start'))
        yield Center(Button.error('Back'))   

    def on_mount(self) -> None:
        self.screen.styles.background = "black"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button.label))


class Vampire(App):
    # CSS = CSS_for_characters

    def compose (self) -> ComposeResult:
        yield Center(Label(vampire_logo))
        yield Center(Label(vampire_health, id='heal'))
        yield Center(Label(vampire_power, id='power'))
        yield Center(Label(vampire_starting_energy, id='energy'))
        yield Center(Label(vampire_starting_weapon, id='weapon'))
        yield Center(Button.success('Start'))
        yield Center(Button.error('Back'))   

    def on_mount(self) -> None:
        self.screen.styles.background = "black"       

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button.label))    

class Ork(App):
    # CSS = CSS_for_characters

    def compose(self) -> ComposeResult:
        yield Center(Label(ork_logo))
        yield Center(Label(ork_health, id='heal'))
        yield Center(Label(ork_power, id='power'))
        yield Center(Label(ork_starting_energy, id='energy'))
        yield Center(Label(ork_starting_weapon, id='weapon'))
        yield Center(Button.success('Start'))
        yield Center(Button.error('Back')) 

    def on_mount(self) -> None:
        self.screen.styles.background = "black"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button.label))  

# class Witch(App):
#     def compose(self) -> ComposeResult:
#         yield Label(witch_logo)
# class Elf(App):
#     def compose(self) -> ComposeResult:
#         yield Label(ork_logo)
# class StartCharacterInfo(App):
#     def compose(self) -> ComposeResult:
#         yield Label(logo)
#     def on_mount(self) -> None:
#         self.screen.styles.background = "black"



character_list = CharacterSelection()
selection = character_list.run()

match selection:
    case 'Warrior':
        character_mode = Warrior()
        if character_mode.run() == 'Start':
            import game.game_loop 
        else:
            character_list.run()

    case 'Vampire':
        character_mode = Vampire()
        if character_mode.run() == 'Start':
            import game.game_loop  
        else:
            character_list.run()

    case 'Ork':
        character_mode = Ork()
        if character_mode.run() == 'Start':
            import game.game_loop 
        else:
            character_list.run()







