# Main application class: integrates UI, variables, and modules
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import config
import plot_utils
import data_utils
import event_handlers

class ArousalValenceRecorder:
    def __init__(self, master):
        # Debug: Confirm event_handlers module loaded
        print("Debug: Event handlers attributes:", dir(event_handlers))
        self.master = master
        self.master.title("Arousal-Valence Annotation Tool")

        # Variable initialization
        self.username_var = tk.StringVar(value=config.DEFAULT_USERNAME)
        self.stimulus_valence = tk.DoubleVar(value=config.DEFAULT_STIMULUS_VALENCE)
        self.stimulus_intensity = tk.DoubleVar(value=config.DEFAULT_STIMULUS_INTENSITY)
        self.emotion_type = tk.StringVar(value=config.DEFAULT_EMOTION_TYPE)

        # Data storage
        self.data = []  # Point data
        self.segments = []  # Optional segment data
        self.text_labels = []  # Labels
        self.points_artists = []  # Point artists
        self.lines_artists = []  # Line artists
        self.label_lines = {}  # Label lines

        # Drag variables
        self.dragging_label = None
        self.drag_offset_x = 0
        self.drag_offset_y = 0

        # Time tracking
        self.current_time = 0.0
        self.last_time = None
        self.last_arousal = None
        self.last_valence = None

        # UI frames
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.ui_frame = tk.Frame(self.master)
        self.ui_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        # Buttons
        self.save_record_button = tk.Button(
            self.bottom_frame, text="Save & Clear", command=self.save_and_clear
        )
        self.save_record_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_layout_button = tk.Button(
            self.bottom_frame, text="Save Layout", command=self.save_layout
        )
        self.save_layout_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Username input
        tk.Label(self.ui_frame, text="Username:").pack(side=tk.LEFT, padx=5)
        self.username_entry = tk.Entry(self.ui_frame, textvariable=self.username_var, width=10)
        self.username_entry.pack(side=tk.LEFT)

        # Emotion type menu
        tk.Label(self.ui_frame, text="Emotion Type:").pack(side=tk.LEFT, padx=5)
        self.emotion_menu = tk.OptionMenu(
            self.ui_frame,
            self.emotion_type,
            "Anger", "Disgust", "Fear", "Joy", "Sadness", "Surprise"
        )
        self.emotion_menu.pack(side=tk.LEFT)

        # Stimulus valence slider
        tk.Label(self.ui_frame, text="Stimulus Valence (-1 ~ 1):").pack(side=tk.LEFT, padx=5)
        self.valence_slider = tk.Scale(
            self.ui_frame,
            from_=-1.0, to=1.0,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            variable=self.stimulus_valence,
            length=150
        )
        self.valence_slider.pack(side=tk.LEFT)

        # Stimulus intensity slider
        tk.Label(self.ui_frame, text="Stimulus Intensity (-1 ~ 1):").pack(side=tk.LEFT, padx=5)
        self.intensity_slider = tk.Scale(
            self.ui_frame,
            from_=-1.0, to=1.0,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            variable=self.stimulus_intensity,
            length=150
        )
        self.intensity_slider.pack(side=tk.LEFT)

        # Initialize plot
        self.fig, self.ax = plot_utils.init_figure()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Add labels
        self.text_labels = plot_utils.add_labels(self.ax, config.LABELS)

        # Draw label lines
        plot_utils.draw_label_lines(self.ax, self.text_labels, self.label_lines)

        # Connect events
        self.cid_click = self.fig.canvas.mpl_connect('button_press_event', lambda e: event_handlers.on_click(e, self))
        self.cid_release = self.fig.canvas.mpl_connect('button_release_event', lambda e: event_handlers.on_release(e, self))
        self.cid_motion = self.fig.canvas.mpl_connect('motion_notify_event', lambda e: event_handlers.on_motion(e, self))

        # Auto-load layout
        self.load_layout()

    def save_and_clear(self):
        """Save records and clear data"""
        data_utils.save_records(self.data)
        self.data.clear()
        self.segments.clear()
        self.last_time = None
        self.last_arousal = None
        self.last_valence = None
        self.current_time = 0.0

        # Remove points and lines
        for pt in self.points_artists:
            pt.remove()
        self.points_artists.clear()

        for ln in self.lines_artists:
            ln.remove()
        self.lines_artists.clear()

        self.canvas.draw()

    def save_layout(self):
        """Save layout"""
        data_utils.save_layout(self.text_labels)

    def load_layout(self):
        """Load layout and redraw lines"""
        data_utils.load_layout(self.text_labels)
        plot_utils.draw_label_lines(self.ax, self.text_labels, self.label_lines)
        self.canvas.draw()