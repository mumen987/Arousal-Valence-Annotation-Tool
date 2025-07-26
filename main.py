# Application entry: starts Tkinter
import tkinter as tk
from arousal_valence_recorder import ArousalValenceRecorder

if __name__ == "__main__":
    root = tk.Tk()
    app = ArousalValenceRecorder(root)
    root.mainloop()