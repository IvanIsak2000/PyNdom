import secrets
import toml 
import string

def get_random_event() -> dict:
    all_events = toml.load('game/events.toml')

    nature_of_event = ['bad_events', 'good_events', 'neutral_events']
    nature_of_event = secrets.choice(nature_of_event)
    
    event_number =  secrets.choice([1,2,3])

    return (all_events[nature_of_event][str(event_number)])


