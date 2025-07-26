# Event handling module: defines mouse click, release, and motion events
import math
import config

def on_click(event, self):
    """Handle mouse click: left-click adds point, right-click starts label drag"""
    if event.button == 1:  # Left-click: add point
        if event.inaxes != self.ax:
            return
        V = event.xdata
        A = event.ydata

        new_time = self.current_time
        self.current_time += config.TIME_INCREMENT

        point_data = {
            "time_s": new_time,
            "arousal": A,
            "valence": V,
            "emotion_type": self.emotion_type.get(),
            "stimulus_valence": self.stimulus_valence.get(),
            "stimulus_intensity": self.stimulus_intensity.get(),
            "session_id": self.username_var.get()
        }
        self.data.append(point_data)

        # Plot new point
        color = 'red' if len(self.data) == 1 else 'green'
        pt = self.ax.plot(V, A, 'o', color=color, markersize=5)[0]
        self.points_artists.append(pt)

        # Connect to previous point
        if len(self.data) > 1:
            prev_pt = self.data[-2]
            line = self.ax.plot(
                [prev_pt["valence"], V],
                [prev_pt["arousal"], A],
                color='black', linestyle='-', linewidth=1
            )[0]
            self.lines_artists.append(line)

        # Update last point info
        self.last_time = new_time
        self.last_arousal = A
        self.last_valence = V

        self.canvas.draw()

    if event.button == config.RIGHT_BUTTON:  # Right-click: drag label
        label = find_label_near(event.xdata, event.ydata, self.text_labels)
        if label is not None:
            self.dragging_label = label
            self.drag_offset_x = label["x"] - event.xdata
            self.drag_offset_y = label["y"] - event.ydata
            label["artist"].set_color('red')
            self.canvas.draw()

def on_release(event, self):
    """Handle mouse release: end drag, update position and lines"""
    if event.button == config.RIGHT_BUTTON and self.dragging_label is not None:
        self.dragging_label["x"] = self.dragging_label["artist"].get_position()[0]
        self.dragging_label["y"] = self.dragging_label["artist"].get_position()[1]
        self.dragging_label["artist"].set_color('black')

        # Update reference line
        text = self.dragging_label["text"]
        if text in self.label_lines:
            line = self.label_lines[text]
            line.set_xdata([0, self.dragging_label["x"]])
            line.set_ydata([0, self.dragging_label["y"]])

        self.dragging_label = None
        self.canvas.draw()

def on_motion(event, self):
    """Handle mouse motion: drag label"""
    if self.dragging_label is not None and event.inaxes == self.ax:
        new_x = event.xdata + self.drag_offset_x
        new_y = event.ydata + self.drag_offset_y
        self.dragging_label["artist"].set_position((new_x, new_y))
        self.canvas.draw()

def find_label_near(x, y, text_labels, threshold=config.DRAG_THRESHOLD):
    """Find label near mouse position"""
    candidate = None
    min_dist = threshold
    for lbl in text_labels:
        lx, ly = lbl["artist"].get_position()
        dist = math.sqrt((lx - x)**2 + (ly - y)**2)
        if dist < min_dist:
            candidate = lbl
            min_dist = dist
    return candidate