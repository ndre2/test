from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime
import random

Window.size = (400, 800)

# Pastel color palette
COLORS = {
    'bg': (0.98, 0.97, 0.99),  # Light lavender
    'primary': (0.85, 0.92, 0.98),  # Pastel blue
    'secondary': (0.93, 0.85, 0.95),  # Pastel purple
    'accent_green': (0.85, 0.95, 0.85),  # Pastel green
    'accent_pink': (0.98, 0.88, 0.92),  # Pastel pink
    'text': (0.3, 0.3, 0.35),  # Dark gray
    'text_light': (0.6, 0.6, 0.65),  # Light gray
    'success': (0.70, 0.92, 0.80),  # Pastel green (healthy)
    'warning': (0.98, 0.92, 0.70),  # Pastel yellow
}

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (1, 1, 1, 0)

class PersonCard(Widget):
    def __init__(self, name, room, status, heart_rate, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.room = room
        self.status = status
        self.heart_rate = heart_rate
        self.size_hint_y = None
        self.height = 120

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*COLORS['primary'], 1)
            RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
            Color(*COLORS['text_light'], 0.3)
            Line(rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1]), width=1, rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], 15))

class HelperApp(App):
    def build(self):
        self.title = 'Helper - Home Monitoring'
        
        # Main container
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        main_layout.canvas.before.clear()
        
        with main_layout.canvas.before:
            Color(*COLORS['bg'])
            RoundedRectangle(size=main_layout.size, pos=main_layout.pos)
        
        # Header
        header = BoxLayout(orientation='vertical', size_hint_y=0.12, spacing=5)
        
        title = Label(
            text='Helper',
            size_hint_y=0.5,
            font_size='28sp',
            bold=True,
            color=COLORS['text']
        )
        
        subtitle = Label(
            text='Home Health Monitor',
            size_hint_y=0.5,
            font_size='12sp',
            color=COLORS['text_light']
        )
        
        header.add_widget(title)
        header.add_widget(subtitle)
        main_layout.add_widget(header)
        
        # Status bar
        status_bar = BoxLayout(size_hint_y=0.1, spacing=10)
        
        status_widget = BoxLayout(orientation='vertical', size_hint_x=0.5)
        status_widget.canvas.before.clear()
        with status_widget.canvas.before:
            Color(*COLORS['accent_green'], 1)
            RoundedRectangle(size=status_widget.size, pos=status_widget.pos, radius=[10])
        
        status_title = Label(text='System Status', font_size='11sp', color=COLORS['text'], bold=True)
        status_value = Label(text='✓ All Clear', font_size='12sp', color=COLORS['text'])
        status_widget.add_widget(status_title)
        status_widget.add_widget(status_value)
        
        people_widget = BoxLayout(orientation='vertical', size_hint_x=0.5)
        people_widget.canvas.before.clear()
        with people_widget.canvas.before:
            Color(*COLORS['accent_pink'], 1)
            RoundedRectangle(size=people_widget.size, pos=people_widget.pos, radius=[10])
        
        people_title = Label(text='People Home', font_size='11sp', color=COLORS['text'], bold=True)
        people_value = Label(text='4 Members', font_size='12sp', color=COLORS['text'])
        people_widget.add_widget(people_title)
        people_widget.add_widget(people_value)
        
        status_bar.add_widget(status_widget)
        status_bar.add_widget(people_widget)
        main_layout.add_widget(status_bar)
        
        # Person list title
        list_title = Label(
            text='Household Members',
            size_hint_y=0.08,
            font_size='14sp',
            bold=True,
            color=COLORS['text']
        )
        main_layout.add_widget(list_title)
        
        # Scrollable person list
        scroll_view = ScrollView(size_hint_y=0.55)
        person_grid = GridLayout(cols=1, spacing=12, size_hint_y=None, padding=5)
        person_grid.bind(minimum_height=person_grid.setter('height'))
        
        # Sample data
        people_data = [
            {'name': 'John Doe', 'room': 'Living Room', 'status': 'Active', 'heart_rate': '72 bpm'},
            {'name': 'Jane Doe', 'room': 'Kitchen', 'status': 'Active', 'heart_rate': '68 bpm'},
            {'name': 'Mike (Child)', 'room': 'Bedroom', 'status': 'Sleeping', 'heart_rate': '65 bpm'},
            {'name': 'Sarah (Child)', 'room': 'Study Room', 'status': 'Active', 'heart_rate': '75 bpm'},
        ]
        
        for person in people_data:
            person_container = BoxLayout(orientation='horizontal', size_hint_y=None, height=120, spacing=10)
            
            # Left side - info
            info_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
            info_layout.canvas.before.clear()
            with info_layout.canvas.before:
                Color(*COLORS['primary'], 1)
                RoundedRectangle(size=info_layout.size, pos=info_layout.pos, radius=[12])
            
            name_label = Label(
                text=person['name'],
                size_hint_y=0.35,
                font_size='13sp',
                bold=True,
                color=COLORS['text']
            )
            
            room_label = Label(
                text=f"📍 {person['room']}",
                size_hint_y=0.35,
                font_size='11sp',
                color=COLORS['text_light']
            )
            
            status_label = Label(
                text=f"Status: {person['status']} • {person['heart_rate']}",
                size_hint_y=0.35,
                font_size='10sp',
                color=COLORS['text_light']
            )
            
            info_layout.add_widget(name_label)
            info_layout.add_widget(room_label)
            info_layout.add_widget(status_label)
            
            # Right side - indicator
            indicator = BoxLayout(size_hint_x=0.3)
            indicator.canvas.before.clear()
            with indicator.canvas.before:
                Color(*COLORS['accent_green'], 1)
                RoundedRectangle(size=indicator.size, pos=indicator.pos, radius=[12])
            
            indicator_label = Label(
                text='✓\nHealthy',
                font_size='12sp',
                color=COLORS['text'],
                bold=True
            )
            indicator.add_widget(indicator_label)
            
            person_container.add_widget(info_layout)
            person_container.add_widget(indicator)
            person_grid.add_widget(person_container)
        
        scroll_view.add_widget(person_grid)
        main_layout.add_widget(scroll_view)
        
        # Bottom action buttons
        action_bar = GridLayout(cols=2, spacing=10, size_hint_y=0.1)
        
        view_details_btn = Button(
            text='View Details',
            size_hint_y=None,
            height=50,
            background_normal='',
            background_color=COLORS['primary'] + (1,),
            color=COLORS['text']
        )
        
        settings_btn = Button(
            text='Settings',
            size_hint_y=None,
            height=50,
            background_normal='',
            background_color=COLORS['secondary'] + (1,),
            color=COLORS['text']
        )
        
        action_bar.add_widget(view_details_btn)
        action_bar.add_widget(settings_btn)
        main_layout.add_widget(action_bar)
        
        return main_layout


if __name__ == '__main__':
    HelperApp().run()

