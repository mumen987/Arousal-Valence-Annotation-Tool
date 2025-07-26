# Plot utilities module: handles Matplotlib initialization, label addition, and line drawing
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import config  # Import config module to access constants

def init_figure():
    """Initialize Matplotlib figure: set axes, circle, and coordinate lines"""
    fig, ax = plt.subplots()
    ax.set_xlim(-config.AXIS_LIMIT, config.AXIS_LIMIT)
    ax.set_ylim(-config.AXIS_LIMIT, config.AXIS_LIMIT)
    ax.set_aspect('equal')
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("")

    # Draw reference circle
    circle = patches.Circle((0, 0), radius=config.CIRCLE_RADIUS, fill=False, linestyle='-', color='black', alpha=config.CIRCLE_ALPHA)
    ax.add_patch(circle)

    # Draw coordinate axes
    ax.axhline(y=0, color='black', linewidth=1)
    ax.axvline(x=0, color='black', linewidth=1)

    return fig, ax

def add_labels(ax, labels):
    """Add text labels to the axes and return list of label dictionaries"""
    text_labels = []
    for lbl in labels:
        t = ax.text(lbl["x"], lbl["y"], lbl["text"], fontsize=lbl["fontsize"], ha=lbl["ha"], va=lbl["va"])
        text_labels.append({"artist": t, "text": lbl["text"], "x": lbl["x"], "y": lbl["y"]})
    return text_labels

def draw_label_lines(ax, text_labels, label_lines):
    """Draw reference lines from (0,0) to each label"""
    # Remove old lines
    for line in list(label_lines.values()):
        line.remove()
    label_lines.clear()

    # Add new lines
    for lbl in text_labels:
        x, y = lbl["artist"].get_position()
        line = ax.plot([0, x], [0, y], color='gray', linestyle='--', linewidth=0.5)[0]
        label_lines[lbl["text"]] = line