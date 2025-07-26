# Configuration module: stores constants, default values, and label definitions for centralized modification
import matplotlib

# Font configuration (supports non-ASCII characters, including Japanese)
matplotlib.rcParams['font.family'] = ['Meiryo']

# Default variable values
DEFAULT_USERNAME = "User01"
DEFAULT_EMOTION_TYPE = "Anger"
DEFAULT_STIMULUS_VALENCE = 0.0
DEFAULT_STIMULUS_INTENSITY = 0.0

# Label list: each is a dictionary with position, text (now in Japanese), and style
LABELS = [
    {"x": -0.05, "y": 1.05, "text": "目覚めた ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": 0.1, "y": 1.00, "text": "● 驚いた", "fontsize": 10, "ha": 'left', "va": 'bottom'},
    {"x": 0.25, "y": 0.95, "text": "● 興奮した", "fontsize": 10, "ha": 'left', "va": 'bottom'},
    {"x": -0.8, "y": 1.0, "text": "警戒した ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": -0.8, "y": 1.0, "text": "怒った ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": -0.9, "y": 0.9, "text": "恐れ ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": -0.9, "y": 0.8, "text": "緊張 ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": -0.9, "y": 0.7, "text": "心配 ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": -0.8, "y": 0.6, "text": "不愉快 ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": -0.7, "y": 0.5, "text": "苛立ち ●", "fontsize": 10, "ha": 'right', "va": 'bottom'},
    {"x": 0.9, "y": 0.5, "text": "● 幸福", "fontsize": 10, "ha": 'left', "va": 'bottom'},
    {"x": 0.8, "y": 0.4, "text": "● 喜び", "fontsize": 10, "ha": 'left', "va": 'bottom'},
    {"x": 0.7, "y": 0.3, "text": "● 嬉しい", "fontsize": 10, "ha": 'left', "va": 'bottom'},
    {"x": 0.7, "y": 0.2, "text": "● 心地よい", "fontsize": 10, "ha": 'left', "va": 'bottom'},
    {"x": -0.9, "y": -0.1, "text": "惨め ●", "fontsize": 10, "ha": 'right', "va": 'top'},
    {"x": -0.8, "y": -0.2, "text": "落ち込んだ ●", "fontsize": 10, "ha": 'right', "va": 'top'},
    {"x": -0.9, "y": -0.3, "text": "悲しみ ●", "fontsize": 10, "ha": 'right', "va": 'top'},
    {"x": -0.9, "y": -0.4, "text": "陰鬱 ●", "fontsize": 10, "ha": 'right', "va": 'top'},
    {"x": -0.8, "y": -0.5, "text": "退屈 ●", "fontsize": 10, "ha": 'right', "va": 'top'},
    {"x": -0.8, "y": -0.6, "text": "だるい ●", "fontsize": 10, "ha": 'right', "va": 'top'},
    {"x": -0.7, "y": -0.7, "text": "疲れた ●", "fontsize": 10, "ha": 'right', "va": 'top'},
    {"x": 0.8, "y": -0.1, "text": "● 満足した", "fontsize": 10, "ha": 'left', "va": 'top'},
    {"x": 0.7, "y": -0.2, "text": "● 満足", "fontsize": 10, "ha": 'left', "va": 'top'},
    {"x": 0.7, "y": -0.3, "text": "● 落ち着いた", "fontsize": 10, "ha": 'left', "va": 'top'},
    {"x": 0.7, "y": -0.4, "text": "● リラックスした", "fontsize": 10, "ha": 'left', "va": 'top'},
    {"x": 0.7, "y": -0.5, "text": "● 快適", "fontsize": 10, "ha": 'left', "va": 'top'},
    {"x": 0.7, "y": -0.6, "text": "● 安堵した", "fontsize": 10, "ha": 'left', "va": 'top'},
    {"x": 0, "y": -0.9, "text": "● 眠気", "fontsize": 10, "ha": 'left', "va": 'top'}
]

# Other constants
CIRCLE_RADIUS = 1.0
CIRCLE_ALPHA = 0.3
AXIS_LIMIT = 1.2
TIME_INCREMENT = 30.0  # Time increment per click (seconds)
LAYOUT_FILE = "layout.csv"
DATA_FILE = "emotion_data.csv"
RIGHT_BUTTON = 3  # Right mouse button (cross-OS compatible)
DRAG_THRESHOLD = 0.1  # Drag detection threshold