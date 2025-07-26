# Data utilities module: handles saving/loading layouts and records
import csv
import os
import config  # Import config module to access constants

def save_layout(text_labels):
    """Save label layout to CSV"""
    with open(config.LAYOUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["text", "x", "y"])
        for lbl in text_labels:
            t = lbl["text"]
            x, y = lbl["artist"].get_position()
            writer.writerow([t, x, y])
    print(f"Layout saved to {config.LAYOUT_FILE}")

def load_layout(text_labels):
    """Load label layout from CSV and update positions"""
    if not os.path.exists(config.LAYOUT_FILE):
        print(f"Error: {config.LAYOUT_FILE} does not exist")
        return
    layout_map = {}
    try:
        with open(config.LAYOUT_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            print(f"Debug: CSV header: {header}")
            if header != ["text", "x", "y"]:
                print(f"Error: Invalid header in {config.LAYOUT_FILE}, expected ['text', 'x', 'y']")
                return
            for row in reader:
                if len(row) == 3:
                    text, x_str, y_str = row
                    try:
                        x_pos = float(x_str)
                        y_pos = float(y_str)
                        layout_map[text] = (x_pos, y_pos)
                        print(f"Debug: Loaded position for '{text}': ({x_pos}, {y_pos})")
                    except ValueError as e:
                        print(f"Error: Invalid coordinates for '{text}': {x_str}, {y_str} ({e})")
    except Exception as e:
        print(f"Failed to read {config.LAYOUT_FILE}: {e}")
        return

    # Update label positions
    updated = False
    for lbl in text_labels:
        t = lbl["text"]
        if t in layout_map:
            x_pos, y_pos = layout_map[t]
            lbl["artist"].set_position((x_pos, y_pos))
            lbl["x"] = x_pos
            lbl["y"] = y_pos
            updated = True
            print(f"Debug: Updated '{t}' to position ({x_pos}, {y_pos})")
    if not updated:
        print("Warning: No labels updated from layout.csv")
    else:
        print(f"{config.LAYOUT_FILE} loaded successfully")

def save_records(data):
    """Append data points to CSV (one row per point)"""
    if not data:
        print("Currently no points to save.")
        return

    need_header = not os.path.isfile(config.DATA_FILE) or os.path.getsize(config.DATA_FILE) == 0

    with open(config.DATA_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if need_header:
            writer.writerow([
                "time_s", "arousal", "valence", "emotion_type",
                "stimulus_valence", "stimulus_intensity", "session_id"
            ])
        for p in data:
            writer.writerow([
                p["time_s"], p["arousal"], p["valence"], p["emotion_type"],
                p["stimulus_valence"], p["stimulus_intensity"], p["session_id"]
            ])
    print(f"Records appended to: {config.DATA_FILE}")