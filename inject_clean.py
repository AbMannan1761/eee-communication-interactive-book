import json
import os

# File paths
workspace_dir = r"c:\Users\mannan\OneDrive - Bangladesh Telecommunication Regulatory Commission\ABM\abm academy\book\EEE job preparation"
html_filepath = os.path.join(workspace_dir, "index.html")
dataset_filepath = os.path.join(workspace_dir, "dataset.json")

# Load dataset
with open(dataset_filepath, "r", encoding="utf-8") as f:
    dataset = json.load(f)

# Re-load clean HTML from git or fresh state to avoid duplicate injections
# Let's run a git checkout on index.html first to ensure we start from a clean state!
os.system(f'git checkout dc2fd42e875a3057555355010fb47d69a1f91936 -- "{html_filepath}"')

with open(html_filepath, "r", encoding="utf-8") as f:
    html_content = f.read()

print(f"Loaded {len(dataset['mcqs'])} MCQs and {len(dataset['flashcards'])} Flashcards.")
print(f"Fresh HTML length: {len(html_content)} characters.")

# Define CSS to inject
css_to_inject = """
        /* --- STYLES FOR EDITABLE SIMULATOR INPUTS & VISUALIZERS --- */
        .label-input {
            background: rgba(9, 13, 22, 0.4);
            border: 1px solid var(--border-color);
            color: var(--accent-color);
            font-weight: bold;
            font-size: 0.9rem;
            width: 80px;
            text-align: center;
            border-radius: 4px;
            outline: none;
            padding: 2px 5px;
            font-family: inherit;
            transition: var(--transition);
        }
        .label-input:focus {
            border-color: var(--accent-color);
            background: rgba(0, 242, 254, 0.15);
            box-shadow: 0 0 5px rgba(0, 242, 254, 0.4);
        }
        body.light-theme .label-input {
            background: rgba(255, 255, 255, 0.8);
            border: 1px solid #d1dfed;
        }

        .visualizer-box {
            margin-top: 15px;
            margin-bottom: 20px;
            background: rgba(9, 13, 22, 0.6);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        body.light-theme .visualizer-box {
            background: rgba(240, 245, 250, 0.8);
            border-color: #d1dfed;
        }
        .visualizer-box canvas {
            width: 100%;
            height: auto;
            max-height: 160px;
            display: block;
        }

        /* --- STYLES FOR FLASHCARDS MODULE (TAB 5) --- */
        .flashcards-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px 0;
        }
        .flashcards-controls {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }
        .flashcard-deck {
            perspective: 1000px;
            width: 100%;
            max-width: 500px;
            height: 320px;
            margin: 0 auto 30px auto;
            cursor: pointer;
        }
        .flashcard-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            border-radius: 15px;
        }
        .flashcard-deck.flipped .flashcard-inner {
            transform: rotateY(180deg);
        }
        .flashcard-front, .flashcard-back {
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 15px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 30px;
            box-sizing: border-box;
            border: 2px solid var(--border-color);
        }
        .flashcard-front {
            background: linear-gradient(135deg, rgba(26, 44, 64, 0.9) 0%, rgba(9, 13, 22, 0.9) 100%);
            color: var(--text-primary);
        }
        body.light-theme .flashcard-front {
            background: linear-gradient(135deg, #ffffff 0%, #f0f5fa 100%);
            color: var(--text-primary);
            border-color: #d1dfed;
        }
        .flashcard-back {
            background: linear-gradient(135deg, rgba(9, 13, 22, 0.9) 0%, rgba(13, 33, 53, 0.9) 100%);
            color: var(--accent-color);
            transform: rotateY(180deg);
        }
        body.light-theme .flashcard-back {
            background: linear-gradient(135deg, #f0f5fa 0%, #e1e9f0 100%);
            color: #0072ff;
            border-color: #d1dfed;
        }
        .flashcard-question {
            font-size: 1.35rem;
            font-weight: 600;
            line-height: 1.5;
            margin-bottom: 15px;
        }
        .flashcard-answer {
            font-size: 1.15rem;
            line-height: 1.6;
            color: var(--text-primary);
        }
        body.light-theme .flashcard-answer {
            color: #1a2c40;
        }
        .flashcard-badge {
            position: absolute;
            top: 15px;
            left: 15px;
            font-size: 0.75rem;
            padding: 4px 10px;
            border-radius: 20px;
            background: rgba(0, 242, 254, 0.15);
            color: var(--accent-color);
            border: 1px solid rgba(0, 242, 254, 0.3);
        }
        body.light-theme .flashcard-badge {
            background: rgba(0, 114, 255, 0.1);
            color: #0072ff;
            border-color: rgba(0, 114, 255, 0.2);
        }
        .flashcard-tip {
            position: absolute;
            bottom: 15px;
            font-size: 0.75rem;
            color: var(--text-secondary);
        }
        .flashcard-nav-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }
        .flashcard-progress {
            width: 100%;
            max-width: 500px;
            margin: 20px auto 0 auto;
        }
        .flashcard-progress-bar-container {
            height: 8px;
            background: rgba(255,255,255,0.05);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }
        body.light-theme .flashcard-progress-bar-container {
            background: rgba(0,0,0,0.05);
        }
        .flashcard-progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #00f2fe, #0072ff);
            width: 0%;
            transition: width 0.3s ease;
        }

        /* --- STYLES FOR MCQ PRACTICE MODULE (TAB 6) --- */
        .mcq-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px 0;
        }
        .quiz-modes {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .quiz-mode-card {
            background: rgba(26, 44, 64, 0.4);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            cursor: pointer;
            transition: var(--transition);
        }
        body.light-theme .quiz-mode-card {
            background: #ffffff;
            border-color: #d1dfed;
        }
        .quiz-mode-card:hover {
            transform: translateY(-5px);
            border-color: var(--accent-color);
            box-shadow: 0 5px 15px rgba(0, 242, 254, 0.15);
        }
        .quiz-mode-card i {
            font-size: 2rem;
            color: var(--accent-color);
            margin-bottom: 12px;
        }
        .quiz-mode-card h4 {
            font-size: 1.1rem;
            margin-bottom: 8px;
            color: var(--text-primary);
        }
        .quiz-mode-card p {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }

        .quiz-active-area {
            background: rgba(26, 44, 64, 0.2);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 25px;
        }
        body.light-theme .quiz-active-area {
            background: #ffffff;
            border-color: #d1dfed;
        }

        .quiz-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }
        body.light-theme .quiz-header {
            border-color: #d1dfed;
        }

        .quiz-timer {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #ff007f;
            font-weight: bold;
            font-size: 1.1rem;
        }

        .mcq-question-text {
            font-size: 1.25rem;
            font-weight: 600;
            line-height: 1.6;
            margin-bottom: 20px;
            color: var(--text-primary);
        }

        .mcq-options-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
            margin-bottom: 20px;
        }
        @media (min-width: 600px) {
            .mcq-options-grid {
                grid-template-columns: 1fr 1fr;
            }
        }

        .mcq-option-btn {
            background: rgba(9, 13, 22, 0.5);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 15px 20px;
            text-align: left;
            color: var(--text-primary);
            font-size: 0.98rem;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;
        }
        body.light-theme .mcq-option-btn {
            background: #f8fafc;
            border-color: #e2e8f0;
        }
        .mcq-option-btn:hover:not(:disabled) {
            border-color: var(--accent-color);
            background: rgba(0, 242, 254, 0.08);
        }
        .mcq-option-btn:disabled {
            cursor: not-allowed;
        }
        .mcq-option-badge {
            width: 26px;
            height: 26px;
            border-radius: 50%;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border-color);
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 0.85rem;
            flex-shrink: 0;
        }
        body.light-theme .mcq-option-badge {
            background: #ffffff;
            border-color: #cbd5e1;
        }

        /* Option states */
        .mcq-option-btn.correct {
            border-color: #00ff66 !important;
            background: rgba(0, 255, 102, 0.15) !important;
            color: #ffffff !important;
        }
        body.light-theme .mcq-option-btn.correct {
            color: #0d5a2b !important;
            background: #e6fced !important;
        }
        .mcq-option-btn.correct .mcq-option-badge {
            background: #00ff66 !important;
            border-color: #00ff66 !important;
            color: #000000 !important;
        }

        .mcq-option-btn.incorrect {
            border-color: #ff0033 !important;
            background: rgba(255, 0, 51, 0.15) !important;
            color: #ffffff !important;
        }
        body.light-theme .mcq-option-btn.incorrect {
            color: #7f1d1d !important;
            background: #fef2f2 !important;
        }
        .mcq-option-btn.incorrect .mcq-option-badge {
            background: #ff0033 !important;
            border-color: #ff0033 !important;
            color: #ffffff !important;
        }

        .mcq-explanation-panel {
            background: rgba(0, 242, 254, 0.05);
            border-left: 4px solid var(--accent-color);
            border-radius: 0 8px 8px 0;
            padding: 20px;
            margin-top: 20px;
            animation: slideDown 0.3s ease-out;
        }
        body.light-theme .mcq-explanation-panel {
            background: #f0f9ff;
            border-left-color: #0072ff;
        }
        .mcq-explanation-panel h5 {
            color: var(--accent-color);
            margin-bottom: 8px;
            font-size: 1rem;
        }
        body.light-theme .mcq-explanation-panel h5 {
            color: #0072ff;
        }
        .mcq-explanation-panel p {
            font-size: 0.92rem;
            line-height: 1.6;
        }

        .quiz-footer {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }

        /* Results Screen */
        .quiz-results-screen {
            text-align: center;
            padding: 30px 10px;
        }
        .result-score-circle {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            background: linear-gradient(135deg, #00f2fe, #0072ff);
            margin: 0 auto 20px auto;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #090d16;
            box-shadow: 0 8px 25px rgba(0, 242, 254, 0.3);
        }
        .result-score-circle .score-num {
            font-size: 2.2rem;
            font-weight: 800;
            color: #000000 !important;
        }
        .result-score-circle .score-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #000000 !important;
        }
        .result-feedback {
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 15px;
            color: var(--text-primary);
        }
        .result-stats-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            max-width: 500px;
            margin: 0 auto 30px auto;
        }
        .result-stat-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 10px;
        }
        body.light-theme .result-stat-card {
            background: #f8fafc;
            border-color: #cbd5e1;
        }
        .result-stat-card .stat-val {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--accent-color);
        }
        body.light-theme .result-stat-card .stat-val {
            color: #0072ff;
        }
        .result-stat-card .stat-lbl {
            font-size: 0.75rem;
            color: var(--text-secondary);
            margin-top: 4px;
        }

        .results-review-section {
            text-align: left;
            margin-top: 40px;
            border-top: 1px solid var(--border-color);
            padding-top: 30px;
        }
        .review-item {
            margin-bottom: 25px;
            padding-bottom: 20px;
            border-bottom: 1px dashed var(--border-color);
        }
        .review-item:last-child {
            border-bottom: none;
        }
        .review-question {
            font-weight: 600;
            font-size: 1.05rem;
            margin-bottom: 10px;
        }
        .review-user-ans {
            font-size: 0.9rem;
            margin-bottom: 5px;
        }
        .review-correct-ans {
            font-size: 0.9rem;
            margin-bottom: 8px;
        }

        /* --- BRANDING & DESIGN OVERRIDES (3D VIBE & ENGINEERING MOOD) --- */
        :root {
            --bg-color: #0b111e !important; /* Deepest cyber navy */
            --card-bg: #121927 !important; /* Cyber card navy */
            --accent-gradient: linear-gradient(135deg, #00f2fe 0%, #7f00ff 50%, #ff007f 100%) !important;
            --accent-color: #00f2fe !important;
            --secondary-color: #7f00ff !important;
            --border-color: #1e293b !important;
            --text-primary: #f8fafc !important;
            --text-secondary: #94a3b8 !important;
            --text-muted: #64748b !important;
            --shadow-glow: 0 0 25px rgba(0, 242, 254, 0.25) !important;
            --shadow-md: 0 8px 30px rgba(0, 0, 0, 0.4) !important;
            --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.6) !important;
            --card-right-bg: rgba(9, 14, 23, 0.85) !important;
            --highlight-box-bg: rgba(0, 242, 254, 0.05) !important;
            --simulator-out-bg: rgba(9, 14, 23, 0.9) !important;
        }

        body.light-theme {
            --bg-color: #f1f5f9 !important;
            --card-bg: #ffffff !important;
            --text-primary: #0f172a !important;
            --text-secondary: #475569 !important;
            --text-muted: #64748b !important;
            --border-color: #e2e8f0 !important;
            --accent-gradient: linear-gradient(135deg, #0052d4 0%, #4364f7 50%, #6fb1fc 100%) !important;
            --accent-color: #2563eb !important;
            --secondary-color: #4f46e5 !important;
            --shadow-glow: 0 0 25px rgba(37, 99, 235, 0.12) !important;
            --shadow-md: 0 8px 30px rgba(0, 50, 100, 0.04) !important;
            --shadow-lg: 0 16px 40px rgba(0, 50, 100, 0.06) !important;
            --card-right-bg: #f8fafc !important;
            --highlight-box-bg: rgba(37, 99, 235, 0.04) !important;
            --simulator-out-bg: #f8fafc !important;
        }

        body {
            background-image: radial-gradient(rgba(0, 242, 254, 0.08) 1.5px, transparent 1.5px) !important;
            background-size: 30px 30px !important;
            background-attachment: fixed !important;
        }
        body.light-theme {
            background-image: radial-gradient(rgba(37, 99, 235, 0.07) 1.5px, transparent 1.5px) !important;
        }

        header {
            background: rgba(11, 16, 27, 0.8) !important;
            backdrop-filter: blur(15px) !important;
            border-bottom: 1px solid var(--border-color) !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
        }
        body.light-theme header {
            background: rgba(255, 255, 255, 0.8) !important;
            box-shadow: 0 4px 20px rgba(0, 50, 100, 0.03) !important;
        }

        .app-card, .theory-section, .simulator-widget, .quiz-active-area, .quiz-mode-card {
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2), inset 0 1px 0 0 rgba(255, 255, 255, 0.03) !important;
            border: 1px solid var(--border-color) !important;
            background: var(--card-bg) !important;
            border-radius: 16px !important;
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease, border-color 0.3s ease !important;
        }
        .app-card:hover, .theory-section:hover, .simulator-widget:hover, .quiz-mode-card:hover {
            transform: translateY(-6px) scale(1.005) !important;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35), var(--shadow-glow) !important;
            border-color: var(--accent-color) !important;
        }
        body.light-theme .app-card, body.light-theme .theory-section, body.light-theme .simulator-widget, body.light-theme .quiz-active-area, body.light-theme .quiz-mode-card {
            box-shadow: 0 10px 30px rgba(0, 50, 100, 0.03), inset 0 1px 0 0 rgba(255, 255, 255, 0.5) !important;
        }

        .label-input {
            border-radius: 6px !important;
            background: rgba(9, 14, 23, 0.6) !important;
            border: 1px solid var(--border-color) !important;
            color: var(--accent-color) !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.3) !important;
            transition: var(--transition) !important;
        }
        .label-input:focus {
            border-color: var(--accent-color) !important;
            box-shadow: 0 0 10px rgba(0, 242, 254, 0.3), inset 0 2px 4px rgba(0,0,0,0.3) !important;
            background: rgba(0, 242, 254, 0.05) !important;
        }
        body.light-theme .label-input {
            background: #f8fafc !important;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.05) !important;
            border-color: var(--border-color) !important;
        }
        body.light-theme .label-input:focus {
            box-shadow: 0 0 10px rgba(37, 99, 235, 0.2), inset 0 1px 2px rgba(0,0,0,0.05) !important;
            background: #ffffff !important;
        }

        .btn, .tab-btn {
            position: relative;
            border-bottom: 3px solid rgba(0, 0, 0, 0.3) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.3s ease !important;
        }
        .btn:active, .tab-btn:active {
            transform: translateY(2px) !important;
            border-bottom-width: 1px !important;
        }
        .tab-btn.active {
            box-shadow: 0 0 15px rgba(0, 242, 254, 0.3), 0 4px 10px rgba(0, 0, 0, 0.3) !important;
            border-bottom-color: rgba(0, 0, 0, 0.4) !important;
        }
        body.light-theme .tab-btn.active {
            box-shadow: 0 0 15px rgba(37, 99, 235, 0.2), 0 4px 10px rgba(0, 50, 100, 0.05) !important;
        }

        .visualizer-box {
            background: rgba(9, 14, 23, 0.8) !important;
            border: 1px solid var(--border-color) !important;
            box-shadow: inset 0 2px 10px rgba(0,0,0,0.5) !important;
            border-radius: 12px !important;
        }
        body.light-theme .visualizer-box {
            background: #f8fafc !important;
            box-shadow: inset 0 2px 10px rgba(0, 50, 100, 0.02) !important;
            border-color: var(--border-color) !important;
        }

        /* --- LOGO & HEADER ANIMATION STYLES (GIF-LIKE MOVEMENT) --- */
        .header-logo-container {
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 5px;
            width: 55px;
            height: 55px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            animation: floatLogo 3.5s ease-in-out infinite;
            transition: var(--transition);
        }
        body.light-theme .header-logo-container {
            background: rgba(0, 0, 0, 0.02);
            box-shadow: 0 4px 15px rgba(0, 50, 100, 0.05);
        }

        .header-logo-svg {
            overflow: visible;
        }

        @keyframes floatLogo {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-4px) rotate(3deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }

        @keyframes spinHexagon {
            0% { transform: rotate(0deg); transform-origin: 50px 50px; }
            100% { transform: rotate(360deg); transform-origin: 50px 50px; }
        }
        
        @keyframes wavePulse {
            0% { stroke-dashoffset: 0; }
            100% { stroke-dashoffset: -40; }
        }

        @keyframes coreBreathe {
            0% { r: 5.5; opacity: 0.8; }
            50% { r: 8.5; opacity: 1; }
            100% { r: 5.5; opacity: 0.8; }
        }

        .logo-polygon {
            animation: spinHexagon 16s linear infinite;
        }

        .logo-wave {
            stroke-dasharray: 100;
            animation: wavePulse 3s linear infinite;
            stroke: var(--accent-color) !important;
        }

        .logo-core {
            animation: coreBreathe 2s ease-in-out infinite;
        }

        @keyframes textGradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .header-title {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            font-size: 1.5rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            animation: floatText 4s ease-in-out infinite;
        }

        @keyframes floatText {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-2px); }
            100% { transform: translateY(0px); }
        }

        header h1 span:first-child {
            background: linear-gradient(90deg, #00f2fe, #7f00ff, #ff007f, #00f2fe);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textGradientShift 6s ease infinite;
            font-weight: 800;
        }

        body.light-theme header h1 span:first-child {
            background: linear-gradient(90deg, #0052d4, #4364f7, #6fb1fc, #0052d4);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textGradientShift 6s ease infinite;
        }

        .tagline-styled {
            font-size: 0.9rem !important;
            font-family: var(--font-heading) !important;
            font-style: italic !important;
            font-weight: 500 !important;
            color: var(--text-secondary) !important;
            letter-spacing: 0.3px !important;
            opacity: 0.85 !important;
            border-left: 2px solid var(--border-color) !important;
            padding-left: 10px !important;
            margin-left: 5px !important;
            animation: pulseTagline 2.5s ease-in-out infinite !important;
            display: inline-block !important;
        }

        @keyframes pulseTagline {
            0% { opacity: 0.7; text-shadow: 0 0 2px transparent; }
            50% { opacity: 1; text-shadow: 0 0 8px rgba(0, 242, 254, 0.4); }
            100% { opacity: 0.7; text-shadow: 0 0 2px transparent; }
        }
        
        body.light-theme .tagline-styled {
            animation: pulseTaglineLight 2.5s ease-in-out infinite !important;
        }
        @keyframes pulseTaglineLight {
            0% { opacity: 0.7; }
            50% { opacity: 1; text-shadow: 0 0 8px rgba(37, 99, 235, 0.2); }
            100% { opacity: 0.7; }
        }

        /* --- GEMINI CHATBOT FLOATING WIDGET STYLES --- */
        .gemini-chat-launcher {
            position: fixed;
            bottom: 25px;
            right: 25px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #00f2fe 0%, #7f00ff 100%);
            box-shadow: 0 8px 32px rgba(0, 242, 254, 0.4), 0 0 15px rgba(0, 242, 254, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 1000;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            outline: none;
        }
        body.light-theme .gemini-chat-launcher {
            background: linear-gradient(135deg, #0052d4 0%, #4364f7 100%);
            box-shadow: 0 8px 32px rgba(37, 99, 235, 0.3), 0 0 15px rgba(37, 99, 235, 0.15);
        }
        .gemini-chat-launcher:hover {
            transform: scale(1.1) rotate(5deg);
            box-shadow: 0 12px 40px rgba(0, 242, 254, 0.55), 0 0 25px rgba(0, 242, 254, 0.35);
        }
        .gemini-chat-launcher svg {
            animation: geminiPulse 4s ease-in-out infinite;
        }
        @keyframes geminiPulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.08); }
            100% { transform: scale(1); }
        }

        .gemini-chat-panel {
            position: fixed;
            bottom: 95px;
            right: 25px;
            width: 380px;
            max-width: calc(100vw - 50px);
            height: 550px;
            max-height: calc(100vh - 150px);
            border-radius: 16px;
            background: rgba(18, 25, 39, 0.82);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 16px 48px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transform: scale(0.9) translateY(20px);
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.1), opacity 0.3s ease, visibility 0.3s;
            overflow: hidden;
        }
        body.light-theme .gemini-chat-panel {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(0, 0, 0, 0.08);
            box-shadow: 0 16px 48px rgba(0, 50, 100, 0.1);
        }
        .gemini-chat-panel.active {
            opacity: 1;
            visibility: visible;
            transform: scale(1) translateY(0);
        }

        .gemini-chat-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 15px 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            background: rgba(0, 0, 0, 0.15);
        }
        body.light-theme .gemini-chat-header {
            border-bottom-color: rgba(0, 0, 0, 0.06);
            background: rgba(0, 0, 0, 0.02);
        }

        .chat-header-btn:hover {
            color: var(--accent-color) !important;
        }
        body.light-theme .chat-header-btn:hover {
            color: #0072ff !important;
        }

        .gemini-chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .chat-msg {
            max-width: 85%;
            padding: 12px 16px;
            font-size: 0.92rem;
            line-height: 1.5;
            animation: msgFadeIn 0.3s ease-out;
        }
        @keyframes msgFadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .chat-msg.user {
            align-self: flex-end;
            background: linear-gradient(135deg, rgba(0, 242, 254, 0.18) 0%, rgba(127, 0, 255, 0.18) 100%);
            color: #ffffff;
            border-radius: 14px 14px 0 14px;
            border: 1px solid rgba(0, 242, 254, 0.3);
            text-align: left;
        }
        body.light-theme .chat-msg.user {
            background: linear-gradient(135deg, rgba(0, 82, 212, 0.1) 0%, rgba(67, 100, 247, 0.1) 100%);
            color: #0f172a;
            border-color: rgba(67, 100, 247, 0.2);
        }

        .chat-msg.assistant {
            align-self: flex-start;
            background: rgba(255, 255, 255, 0.04);
            color: var(--text-primary);
            border-radius: 14px 14px 14px 0;
            border: 1px solid rgba(255, 255, 255, 0.06);
            text-align: left;
        }
        body.light-theme .chat-msg.assistant {
            background: rgba(0, 0, 0, 0.03);
            border-color: rgba(0, 0, 0, 0.04);
        }

        .quick-suggestions-box {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 12px;
        }

        .suggestion-tag {
            background: rgba(0, 242, 254, 0.08);
            border: 1px solid rgba(0, 242, 254, 0.2);
            color: var(--accent-color);
            border-radius: 15px;
            padding: 5px 12px;
            font-size: 0.76rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        body.light-theme .suggestion-tag {
            background: rgba(37, 99, 235, 0.06);
            border-color: rgba(37, 99, 235, 0.15);
            color: #2563eb;
        }
        .suggestion-tag:hover {
            background: var(--accent-color);
            color: #000000 !important;
            border-color: var(--accent-color);
            transform: translateY(-1px);
        }
        body.light-theme .suggestion-tag:hover {
            background: #2563eb;
            color: #ffffff !important;
            border-color: #2563eb;
        }

        .gemini-chat-input-area {
            display: flex;
            gap: 10px;
            padding: 15px 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            background: rgba(0, 0, 0, 0.15);
        }
        body.light-theme .gemini-chat-input-area {
            border-top-color: rgba(0, 0, 0, 0.06);
            background: rgba(0, 0, 0, 0.02);
        }

        .gemini-chat-input-area input {
            flex: 1;
            padding: 10px 14px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background: rgba(9, 13, 22, 0.6);
            color: var(--text-primary);
            outline: none;
            font-family: inherit;
            font-size: 0.92rem;
            transition: var(--transition);
        }
        .gemini-chat-input-area input:focus {
            border-color: var(--accent-color);
            box-shadow: 0 0 8px rgba(0, 242, 254, 0.25);
        }
        body.light-theme .gemini-chat-input-area input {
            background: #ffffff;
        }

        .gemini-chat-input-area button {
            width: 40px;
            height: 40px;
            border-radius: 8px;
            background: var(--accent-gradient);
            border: none;
            color: #000000 !important;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.2s ease;
        }
        body.light-theme .gemini-chat-input-area button {
            color: #ffffff !important;
        }
        .gemini-chat-input-area button:hover {
            transform: scale(1.05);
            opacity: 0.9;
        }
        .gemini-chat-input-area button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .gemini-config-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(9, 13, 22, 0.96);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 30px;
            box-sizing: border-box;
            z-index: 1001;
            text-align: center;
        }
        body.light-theme .gemini-config-overlay {
            background: rgba(255, 255, 255, 0.98);
        }
        .gemini-config-overlay.active {
            display: flex;
            animation: overlayFadeIn 0.2s ease-out;
        }
        @keyframes overlayFadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* --- PREMIUM SINGLE THEME TOGGLE SWITCH --- */
        .theme-switch-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            color: var(--accent-color);
            width: 42px;
            height: 42px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05), 0 4px 10px rgba(0,0,0,0.2);
            font-size: 1.1rem;
            outline: none;
        }
        body.light-theme .theme-switch-btn {
            background: rgba(0, 0, 0, 0.03);
            color: #2563eb;
            box-shadow: inset 0 1px 0 rgba(0,0,0,0.02), 0 4px 10px rgba(0, 50, 100, 0.05);
        }
        .theme-switch-btn:hover {
            transform: scale(1.08) rotate(15deg);
            border-color: var(--accent-color);
            box-shadow: 0 0 12px rgba(0, 242, 254, 0.25);
        }
        body.light-theme .theme-switch-btn:hover {
            border-color: #2563eb;
            box-shadow: 0 0 12px rgba(37, 99, 235, 0.15);
        }

        /* --- SPACE OPTIMIZATION & COMPACT LAYOUT OVERRIDES --- */
        header {
            padding: 8px 20px !important;
        }
        .header-logo-container {
            width: 40px !important;
            height: 40px !important;
            padding: 3px !important;
            border-radius: 8px !important;
        }
        .header-logo-svg {
            width: 32px !important;
            height: 32px !important;
        }
        .logo-polygon {
            transform-origin: 50px 50px;
        }
        .header-title {
            font-size: 1.25rem !important;
            gap: 6px !important;
        }
        .header-subtitle {
            margin: 1px 0 0 0 !important;
            font-size: 0.8rem !important;
        }
        .tagline-styled {
            font-size: 0.8rem !important;
            padding-left: 8px !important;
        }
        .container {
            margin: 12px auto !important;
            padding: 0 15px !important;
        }
        .tabs-nav-container {
            margin-bottom: 12px !important;
        }
        .tabs-nav-title {
            font-size: 0.85rem !important;
            margin-bottom: 5px !important;
        }
        .tabs {
            grid-template-columns: repeat(auto-fit, minmax(135px, 1fr)) !important;
            gap: 8px !important;
        }
        .tab-btn {
            padding: 8px 10px !important;
            font-size: 0.78rem !important;
            border-radius: 6px !important;
            gap: 6px !important;
            border-bottom-width: 2px !important;
        }
        .theory-section {
            padding: 20px !important;
            margin-bottom: 20px !important;
            border-radius: 12px !important;
        }
        .theory-badge {
            margin-bottom: 8px !important;
        }
        .theory-section h2 {
            font-size: 1.3rem !important;
            margin-bottom: 12px !important;
            padding-bottom: 8px !important;
            gap: 8px !important;
        }
        .theory-content p {
            font-size: 0.9rem !important;
            margin-bottom: 10px !important;
            line-height: 1.5 !important;
        }
        .theory-content h4 {
            font-size: 1rem !important;
            margin: 12px 0 6px 0 !important;
        }
        .theory-highlight-box {
            padding: 12px 15px !important;
            margin: 10px 0 !important;
        }
        .split-card {
            margin-bottom: 20px !important;
            border-radius: 12px !important;
        }
        .card-left {
            padding: 18px !important;
        }
        .card-right {
            padding: 18px !important;
        }
        .simulator-grid {
            gap: 15px !important;
        }
        .simulator-inputs {
            gap: 10px !important;
        }
        .input-group {
            gap: 4px !important;
        }
        .input-group label {
            font-size: 0.82rem !important;
        }
        .input-group input[type="number"], .input-group select {
            padding: 6px 10px !important;
            font-size: 0.88rem !important;
            border-radius: 5px !important;
        }
        .simulator-outputs {
            padding: 15px !important;
            border-radius: 8px !important;
        }
        .output-heading {
            font-size: 0.9rem !important;
            margin-bottom: 10px !important;
            padding-bottom: 6px !important;
        }
        .output-value-block {
            gap: 8px !important;
            margin-bottom: 10px !important;
        }
        .output-row {
            padding-bottom: 6px !important;
        }
        .output-label {
            font-size: 0.82rem !important;
        }
        .output-val {
            font-size: 0.95rem !important;
        }
        .output-math-steps {
            padding: 10px !important;
            font-size: 0.82rem !important;
            border-radius: 5px !important;
        }
        .app-card {
            padding: 12px 15px !important;
            margin-bottom: 15px !important;
            gap: 12px !important;
        }
        .app-icon {
            font-size: 1.6rem !important;
        }
        .app-content h4 {
            font-size: 1rem !important;
            margin-bottom: 4px !important;
        }
        .app-content p {
            font-size: 0.82rem !important;
        }
        .visualizer-box {
            margin-top: 8px !important;
            margin-bottom: 8px !important;
            padding: 6px !important;
            border-radius: 8px !important;
        }
        .visualizer-box canvas {
            max-height: 110px !important;
        }
"""

# HTML Tab Buttons
tab_buttons_to_add = """                <button class="tab-btn" onclick="switchTab(4)">
                    <i class="fa-solid fa-circle-play"></i> Video Lectures (লেকচার ভিডিও)
                </button>
                <button class="tab-btn" onclick="switchTab(5)">
                    <i class="fa-solid fa-clone"></i> Ch-5: যোগাযোগ ফ্ল্যাশকার্ড
                </button>
                <button class="tab-btn" onclick="switchTab(6)">
                    <i class="fa-solid fa-circle-question"></i> Ch-6: কুইজ প্র্যাকটিস
                </button>"""

# HTML Tab Panels
tab_panels_to_add = """
        <!-- ======================= TAB 6: FLASHCARDS ======================= -->
        <div id="panel-5" class="tab-panel">
            <div class="theory-section">
                <span class="theory-badge">রিভিশন ফ্ল্যাশকার্ড • Revision Deck</span>
                <h2><i class="fa-solid fa-clone"></i> যোগাযোগ প্রকৌশল রিভিশন ফ্ল্যাশকার্ড</h2>
                <div class="theory-content">
                    <p>যোগাযোগ প্রকৌশল বা ও পালস কোড মডুলেশন (PCM) সিস্টেমের প্রধান বিষয়গুলো সহজে মুখস্থ এবং দ্রুত রিভিশন করতে এই ১০০টি ফ্ল্যাশকার্ড ব্যবহার করো। কার্ডটিতে ক্লিক করলে এটি উল্টে যাবে এবং সঠিক উত্তরটি দেখাবে।</p>
                </div>
            </div>

            <div class="flashcards-container">
                <div class="flashcards-controls">
                    <div>
                        <label for="flashcard-cat-select" style="font-size: 0.9rem; font-weight: bold; margin-right: 8px;">ক্যাটাগরি ফিল্টার:</label>
                        <select id="flashcard-cat-select" onchange="filterFlashcards(this.value)" style="padding: 8px 12px; border-radius: 6px; background-color: rgba(9, 13, 22, 0.8); border: 1px solid var(--border-color); color: var(--text-primary); outline: none; font-family: inherit;">
                            <option value="all">সকল ক্যাটাগরি (১০০টি)</option>
                            <option value="Sampling Basics">Sampling Basics</option>
                            <option value="Nyquist Theorem">Nyquist Theorem</option>
                            <option value="Aliasing">Aliasing</option>
                            <option value="Composite Signals">Composite Signals</option>
                            <option value="PCM Basics">PCM Basics</option>
                            <option value="Multiplexing">Multiplexing</option>
                            <option value="TDM">TDM</option>
                            <option value="Standards">Standards</option>
                            <option value="Quantization Basics">Quantization Basics</option>
                            <option value="Companding">Companding</option>
                            <option value="Delta Modulation">Delta Modulation</option>
                            <option value="Noise & Power">Noise & Power</option>
                            <option value="Storage Calculations">Storage Calculations</option>
                            <option value="Dynamic Range">Dynamic Range</option>
                            <option value="Modulation Basics">Modulation Basics</option>
                            <option value="Carrier Modulation">Carrier Modulation</option>
                            <option value="Detection">Detection</option>
                        </select>
                    </div>
                    <button class="btn btn-secondary" onclick="shuffleFlashcards()"><i class="fa-solid fa-shuffle"></i> সাফল করুন (Shuffle)</button>
                </div>

                <div class="flashcard-deck" onclick="flipFlashcard()">
                    <div class="flashcard-inner">
                        <div class="flashcard-front">
                            <span class="flashcard-badge" id="fc-badge">Sampling</span>
                            <div class="flashcard-question" id="fc-question">প্রশ্ন লোড হচ্ছে...</div>
                            <span class="flashcard-tip"><i class="fa-solid fa-arrow-pointer"></i> দেখতে ক্লিক করুন</span>
                        </div>
                        <div class="flashcard-back">
                            <span class="flashcard-badge" id="fc-badge-back">Sampling</span>
                            <div class="flashcard-answer" id="fc-answer">উত্তর লোড হচ্ছে...</div>
                            <span class="flashcard-tip"><i class="fa-solid fa-arrow-pointer"></i> পুনরায় দেখতে ক্লিক করুন</span>
                        </div>
                    </div>
                </div>

                <div class="flashcard-nav-buttons">
                    <button class="btn btn-secondary" onclick="prevFlashcard()"><i class="fa-solid fa-chevron-left"></i> পূর্ববর্তী</button>
                    <button class="btn btn-primary" onclick="markFlashcardLearned()" id="btn-fc-learned"><i class="fa-solid fa-check"></i> শিখেছি / জানি</button>
                    <button class="btn btn-secondary" onclick="nextFlashcard()">পরবর্তী <i class="fa-solid fa-chevron-right"></i></button>
                </div>

                <div class="flashcard-progress">
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-secondary);">
                        <span id="fc-counter">কার্ড ১/১০০</span>
                        <span id="fc-learned-counter">শেখা হয়েছে: ০টি (০%)</span>
                    </div>
                    <div class="flashcard-progress-bar-container">
                        <div class="flashcard-progress-bar" id="fc-progress-bar"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ======================= TAB 7: MCQ PRACTICE ======================= -->
        <div id="panel-6" class="tab-panel">
            <div class="theory-section">
                <span class="theory-badge">মূল্যায়ন মডিউল • Practice Engine</span>
                <h2><i class="fa-solid fa-circle-question"></i> ইইই জব প্রিপারেশন: কুইজ প্র্যাকটিস ও মক টেস্ট</h2>
                <div class="theory-content">
                    <p>পরীক্ষার জন্য প্রস্তুতি যাচাই করতে ১০০টি প্রশ্ন নিয়ে সাজানো এই কুইজ ইঞ্জিন ব্যবহার করো। তুমি কুইক প্র্যাকটিস বা পূর্ণাঙ্গ টাইমারযুক্ত মক টেস্ট দিতে পারো।</p>
                </div>
            </div>

            <div class="mcq-container">
                <!-- Select Quiz Mode -->
                <div id="quiz-intro-area">
                    <div class="quiz-modes">
                        <div class="quiz-mode-card" onclick="startQuiz('quick')">
                            <i class="fa-solid fa-bolt"></i>
                            <h4>কুইক প্র্যাকটিস</h4>
                            <p>১০টি র‍্যান্ডম প্রশ্ন নিয়ে সাধারণ প্রস্তুতি অনুশীলন করুন।</p>
                        </div>
                        <div class="quiz-mode-card" onclick="startQuiz('mock')">
                            <i class="fa-solid fa-stopwatch"></i>
                            <h4>মক টেস্ট (Timed)</h4>
                            <p>২০টি র‍্যান্ডম প্রশ্ন এবং ২০ মিনিট সময় নিয়ে পরীক্ষা দিন।</p>
                        </div>
                        <div class="quiz-mode-card" onclick="showCategoryQuizSelector()">
                            <i class="fa-solid fa-list-check"></i>
                            <h4>অধ্যায় ভিত্তিক পরীক্ষা</h4>
                            <p>নির্দিষ্ট একটি বিষয়ের ওপরে সবগুলো প্রশ্ন প্র্যাকটিস করুন।</p>
                        </div>
                    </div>
                    
                    <div id="cat-quiz-selector-box" class="quiz-active-area" style="display: none; text-align: center;">
                        <h4 style="margin-bottom: 15px;">অনুশীলনের জন্য অধ্যায় নির্বাচন করুন:</h4>
                        <select id="mcq-cat-select" style="padding: 10px 15px; border-radius: 6px; background-color: rgba(9, 13, 22, 0.8); border: 1px solid var(--border-color); color: var(--text-primary); outline: none; width: 100%; max-width: 400px; margin-bottom: 20px; font-family: inherit;">
                            <option value="Sampling">অধ্যায় ১: Sampling & Nyquist Rate (২০টি MCQ)</option>
                            <option value="PCM & TDM">অধ্যায় ২: PCM Bit Rate & TDM (২০টি MCQ)</option>
                            <option value="SQNR">অধ্যায় ৩: SQNR & Companding (২০টি MCQ)</option>
                            <option value="Storage">অধ্যায় ৪: Storage & Dynamic Range (২০টি MCQ)</option>
                            <option value="Modulation">অধ্যায় ৫: Carrier Modulation (২০টি MCQ)</option>
                        </select>
                        <div>
                            <button class="btn btn-primary" onclick="startQuiz('category')">শুরু করুন</button>
                            <button class="btn btn-secondary" onclick="hideCategoryQuizSelector()">ফিরে যান</button>
                        </div>
                    </div>
                </div>

                <!-- Active Quiz Area -->
                <div id="quiz-play-area" class="quiz-active-area" style="display: none;">
                    <div class="quiz-header">
                        <div>
                            <span class="badge" id="quiz-mode-badge" style="background-color: var(--accent-color); color: #000; font-weight: bold; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; margin-right: 8px;">Quick Practice</span>
                            <span id="quiz-q-counter" style="font-weight: 500;">প্রশ্ন ১/১০</span>
                        </div>
                        <div class="quiz-timer" id="quiz-timer-box" style="display: none;">
                            <i class="fa-solid fa-clock"></i> <span id="quiz-timer-text">20:00</span>
                        </div>
                    </div>

                    <div class="mcq-question-area">
                        <div class="mcq-question-text tex2jax_process" id="mcq-q-text">
                            স্যাম্পলিং থিওরেম অনুযায়ী, এনালগ সিগন্যালকে বিকৃতি ছাড়া পুনর্গঠন করতে স্যাম্পলিং রেট ($f_s$) কত হতে হবে?
                        </div>
                        <div class="mcq-options-grid" id="mcq-options-box">
                            <!-- Options rendered dynamically -->
                        </div>
                        
                        <!-- Explanation revealed on click -->
                        <div class="mcq-explanation-panel tex2jax_process" id="mcq-explanation-box" style="display: none;">
                            <h5><i class="fa-solid fa-circle-info"></i> ব্যাখ্যা ও বিশ্লেষণ:</h5>
                            <p id="mcq-explanation-text">ব্যাখ্যা টেক্সট...</p>
                        </div>
                    </div>

                    <div class="quiz-footer">
                        <button class="btn btn-secondary" onclick="quitQuiz()"><i class="fa-solid fa-xmark"></i> শেষ করুন</button>
                        <button class="btn btn-primary" id="btn-next-q" onclick="nextQuizQuestion()" disabled>পরবর্তী প্রশ্ন <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Results Summary Screen -->
                <div id="quiz-result-area" class="quiz-active-area" style="display: none;">
                    <div class="quiz-results-screen">
                        <div class="result-score-circle">
                            <span class="score-num" id="res-score">১৮</span>
                            <span class="score-label" id="res-total">/ ২০</span>
                        </div>
                        <div class="result-feedback" id="res-feedback">অসাধারণ! আপনি চমৎকার প্রস্তুতি নিয়েছেন।</div>
                        
                        <div class="result-stats-grid">
                            <div class="result-stat-card">
                                <div class="stat-val" id="res-percentage">৯০%</div>
                                <div class="stat-lbl">সঠিকতার হার</div>
                            </div>
                            <div class="result-stat-card">
                                <div class="stat-val" id="res-time">০৪:২৫</div>
                                <div class="stat-lbl">ব্যয়িত সময়</div>
                            </div>
                            <div class="result-stat-card">
                                <div class="stat-val" id="res-correct-count">১৮/২০</div>
                                <div class="stat-lbl">সঠিক উত্তর</div>
                            </div>
                        </div>

                        <div style="display: flex; gap: 15px; justify-content: center;">
                            <button class="btn btn-primary" onclick="restartQuiz()"><i class="fa-solid fa-rotate-left"></i> আবার পরীক্ষা দিন</button>
                            <button class="btn btn-secondary" onclick="showReviewScreen()"><i class="fa-solid fa-list-check"></i> ভুলগুলো রিভিউ করুন</button>
                            <button class="btn btn-secondary" onclick="quitQuiz()"><i class="fa-solid fa-house"></i> হোম</button>
                        </div>

                        <!-- Review of questions -->
                        <div class="results-review-section" id="quiz-review-box" style="display: none;">
                            <h3 style="margin-bottom: 20px; border-bottom: 2px solid var(--border-color); padding-bottom: 10px;"><i class="fa-solid fa-clipboard-question"></i> বিস্তারিত প্রশ্নোত্তর ও ব্যাখ্যা রিভিউ</h3>
                            <div id="quiz-review-list">
                                <!-- Review items dynamically populated -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

# Replace spans with editable label inputs
span_replacements = [
    (r'<span id="val-t1-f1">300</span>', r'<input type="number" id="val-t1-f1" class="label-input" value="300" oninput="syncVal(\'t1-f1\', this, updateT1)">'),
    (r'<span id="val-t1-f2">500</span>', r'<input type="number" id="val-t1-f2" class="label-input" value="500" oninput="syncVal(\'t1-f2\', this, updateT1)">'),
    (r'<span id="val-t1-overhead">0</span>', r'<input type="number" id="val-t1-overhead" class="label-input" value="0" oninput="syncVal(\'t1-overhead\', this, updateT1)">'),
    
    (r'<span id="val-t2-channels">10</span>', r'<input type="number" id="val-t2-channels" class="label-input" value="10" oninput="syncVal(\'t2-channels\', this, updateT2)">'),
    (r'<span id="val-t2-fm">4000</span>', r'<input type="number" id="val-t2-fm" class="label-input" value="4000" oninput="syncVal(\'t2-fm\', this, updateT2)">'),
    (r'<span id="val-t2-bits">8</span>', r'<input type="number" id="val-t2-bits" class="label-input" value="8" oninput="syncVal(\'t2-bits\', this, updateT2)">'),
    (r'<span id="val-t2-sync">1</span>', r'<input type="number" id="val-t2-sync" class="label-input" value="1" oninput="syncVal(\'t2-sync\', this, updateT2)">'),
    (r'<span id="val-t2-control">1</span>', r'<input type="number" id="val-t2-control" class="label-input" value="1" oninput="syncVal(\'t2-control\', this, updateT2)">'),
    
    (r'<span id="val-t3-fm">100</span>', r'<input type="number" id="val-t3-fm" class="label-input" value="100" oninput="syncVal(\'t3-fm\', this, updateT3)">'),
    (r'<span id="val-t3-error">0.25</span>', r'<input type="number" id="val-t3-error" class="label-input" value="0.25" step="0.05" oninput="syncVal(\'t3-error\', this, updateT3)">'),
    (r'<span id="val-t3-patients">10</span>', r'<input type="number" id="val-t3-patients" class="label-input" value="10" oninput="syncVal(\'t3-patients\', this, updateT3)">'),
    (r'<span id="val-t3-mu">100</span>', r'<input type="number" id="val-t3-mu" class="label-input" value="100" oninput="syncVal(\'t3-mu\', this, updateT3)">'),
    
    (r'<span id="val-t4-fm">20000</span>', r'<input type="number" id="val-t4-fm" class="label-input" value="20000" oninput="syncVal(\'t4-fm\', this, updateT4)">'),
    (r'<span id="val-t4-bits">16</span>', r'<input type="number" id="val-t4-bits" class="label-input" value="16" oninput="syncVal(\'t4-bits\', this, updateT4)">'),
    (r'<span id="val-t4-duration">600</span>', r'<input type="number" id="val-t4-duration" class="label-input" value="600" oninput="syncVal(\'t4-duration\', this, updateT4)">'),
]

# Perform span replacements
modified_html = html_content
for old_span, new_input in span_replacements:
    modified_html = modified_html.replace(old_span, new_input)

# Inject Canvas Visualizers contextually into the 4 outputs
heading_str = '<h4 class="output-heading"><i class="fa-solid fa-square-poll-vertical"></i> Live Calculation Outputs</h4>'

parts = modified_html.split(heading_str)
if len(parts) == 5:
    print("Found exactly 4 occurrences of output-heading. Injecting canvases...")
    new_parts = []
    new_parts.append(parts[0])
    for i in range(1, 5):
        canvas_id = f"canvas-t{i}"
        canvas_html = f'{heading_str}\n                        <div class="visualizer-box"><canvas id="{canvas_id}" width="400" height="150"></canvas></div>'
        new_parts.append(canvas_html + parts[i])
    modified_html = "".join(new_parts)
else:
    print(f"Warning: Found {len(parts)-1} occurrences of output-heading instead of 4.")

# Inject CSS Styles inside </style>
style_end_idx = modified_html.find('</style>')
if style_end_idx != -1:
    modified_html = modified_html[:style_end_idx] + css_to_inject + modified_html[style_end_idx:]
    print("Injected CSS styles.")

# Inject Tab Buttons
old_video_tab = """                <button class="tab-btn" onclick="switchTab(4)">
                    <i class="fa-solid fa-circle-play"></i> Video Lectures (লেকচার ভিডিও)
                </button>"""
modified_html = modified_html.replace(old_video_tab, tab_buttons_to_add)

# Inject Tab Panels
container_closing = "        </div>\n    </div>\n\n    <script>"
container_closing_idx = modified_html.find(container_closing)
if container_closing_idx != -1:
    modified_html = modified_html[:container_closing_idx + 14] + tab_panels_to_add + modified_html[container_closing_idx + 14:]
    print("Injected tab panels.")

# Let's generate the JavaScript code including the dataset and engines
js_code_to_inject = f"""
        // --- INLINED STUDY DECK DATABASE (100 MCQs & 100 Flashcards) ---
        const studyDataset = {json.dumps(dataset, ensure_ascii=False)};

        // Helper to toggle theme with single button switch
        function toggleTheme() {{
            const currentTheme = localStorage.getItem('theme') || 'dark';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            setTheme(newTheme);
        }}

        // Helper to safely set display elements (checking if input or text span)
        function setDisplayValue(id, val) {{
            const el = document.getElementById(id);
            if (!el) return;
            if (el.tagName === 'INPUT') {{
                el.value = val;
            }} else {{
                el.innerText = val;
            }}
        }}

        // Bi-directional slider-input synchronization
        function syncVal(sliderId, inputEl, updateFn) {{
            const slider = document.getElementById(sliderId);
            if (!slider) return;
            let val = parseFloat(inputEl.value);
            if (isNaN(val)) return;
            
            // Clamp to slider boundaries
            const min = parseFloat(slider.min);
            const max = parseFloat(slider.max);
            if (val < min) val = min;
            if (val > max) val = max;
            
            slider.value = val;
            inputEl.value = val;
            updateFn();
        }}

        // --- REAL-TIME GRAPHICAL VISUALIZERS ---

        // Visualizer 1: Sampling & Nyquist Plot
        function drawT1Plot(f1, f2, fs) {{
            const canvas = document.getElementById('canvas-t1');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;
            ctx.clearRect(0, 0, w, h);
            
            const activeTheme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
            
            // Draw grid
            ctx.strokeStyle = activeTheme === 'dark' ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';
            ctx.lineWidth = 1;
            for (let x = 0; x < w; x += 40) {{
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
            }}
            for (let y = 0; y < h; y += 30) {{
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
            }}
            
            // Center axis
            ctx.strokeStyle = activeTheme === 'dark' ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.15)';
            ctx.beginPath();
            ctx.moveTo(0, h/2);
            ctx.lineTo(w, h/2);
            ctx.stroke();

            const fm = Math.max(f1, f2);
            const duration = 2.5 / fm; // show 2.5 cycles of fm
            
            // Draw continuous wave
            ctx.strokeStyle = '#00f2fe';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            for (let i = 0; i <= w; i++) {{
                const t = (i / w) * duration;
                const yVal = 0.5 * Math.sin(2 * Math.PI * f1 * t) + 0.5 * Math.sin(2 * Math.PI * f2 * t);
                const yPixel = h/2 - yVal * (h/2.5);
                if (i === 0) ctx.moveTo(i, yPixel);
                else ctx.lineTo(i, yPixel);
            }}
            ctx.stroke();
            
            // Draw samples
            const Ts = 1 / fs;
            ctx.fillStyle = '#ff007f';
            ctx.strokeStyle = '#ff007f';
            ctx.lineWidth = 1.5;
            
            for (let t = 0; t <= duration; t += Ts) {{
                const xPixel = (t / duration) * w;
                const yVal = 0.5 * Math.sin(2 * Math.PI * f1 * t) + 0.5 * Math.sin(2 * Math.PI * f2 * t);
                const yPixel = h/2 - yVal * (h/2.5);
                
                // draw stem
                ctx.beginPath();
                ctx.moveTo(xPixel, h/2);
                ctx.lineTo(xPixel, yPixel);
                ctx.stroke();
                
                // draw dot
                ctx.beginPath();
                ctx.arc(xPixel, yPixel, 4, 0, 2 * Math.PI);
                ctx.fill();
            }}
            
            // If aliased, draw the aliased low frequency wave
            if (fs < 2 * fm) {{
                ctx.strokeStyle = 'rgba(255, 0, 0, 0.6)';
                ctx.setLineDash([5, 5]);
                ctx.lineWidth = 2;
                ctx.beginPath();
                const f_alias = Math.abs(fs - fm);
                for (let i = 0; i <= w; i++) {{
                    const t = (i / w) * duration;
                    const yVal = Math.sin(2 * Math.PI * f_alias * t);
                    const yPixel = h/2 - yVal * (h/2.5);
                    if (i === 0) ctx.moveTo(i, yPixel);
                    else ctx.lineTo(i, yPixel);
                }}
                ctx.stroke();
                ctx.setLineDash([]);
                
                ctx.fillStyle = '#ff0033';
                ctx.font = 'bold 12px Inter, Arial';
                ctx.fillText('অ্যালাইসিং বিকৃতি (Aliasing Distortion)', 15, 20);
            }} else {{
                ctx.fillStyle = '#00ff66';
                ctx.font = 'bold 12px Inter, Arial';
                ctx.fillText('নিখুঁত পুনর্গঠন (Perfect Reconstruction)', 15, 20);
            }}
        }}

        // Visualizer 2: TDM Frame Layout
        function drawT2Plot(channels, bits, sync, control) {{
            const canvas = document.getElementById('canvas-t2');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;
            ctx.clearRect(0, 0, w, h);
            
            const activeTheme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
            
            ctx.fillStyle = activeTheme === 'dark' ? '#ffffff' : '#1a2c40';
            ctx.font = 'bold 12px Inter, Arial';
            ctx.textAlign = 'left';
            ctx.fillText(`TDM Frame Layout (M: ${{channels}} channels, n: ${{bits}} bits)`, 10, 18);
            
            const startX = 20;
            const startY = h / 2 - 10;
            const frameW = w - 40;
            const frameH = 30;
            
            ctx.strokeStyle = activeTheme === 'dark' ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)';
            ctx.strokeRect(startX, startY, frameW, frameH);
            
            const displaySlots = [];
            if (sync > 0) {{
                displaySlots.push({{ label: 'Sync', size: sync, color: '#f5a623' }});
            }}
            
            if (channels <= 8) {{
                for (let i = 1; i <= channels; i++) {{
                    displaySlots.push({{ label: `Ch ${{i}}`, size: bits, color: `hsl(${{i * 45}}, 70%, 50%)` }});
                }}
            }} else {{
                for (let i = 1; i <= 4; i++) {{
                    displaySlots.push({{ label: `Ch ${{i}}`, size: bits, color: `hsl(${{i * 45}}, 70%, 50%)` }});
                }}
                displaySlots.push({{ label: '...', size: 0, color: '#444444' }});
                displaySlots.push({{ label: `Ch ${{channels}}`, size: bits, color: `hsl(${{channels * 45}}, 70%, 50%)` }});
            }}
            
            if (control > 0) {{
                displaySlots.push({{ label: 'Ctrl', size: control, color: '#d0021b' }});
            }}
            
            let curX = startX;
            const totalWeight = displaySlots.length;
            const slotW = frameW / totalWeight;
            
            displaySlots.forEach((slot, index) => {{
                ctx.fillStyle = slot.color;
                ctx.fillRect(curX + 2, startY + 2, slotW - 4, frameH - 4);
                
                ctx.fillStyle = '#ffffff';
                ctx.font = '10px Inter, Arial';
                ctx.textAlign = 'center';
                ctx.fillText(slot.label, curX + slotW / 2, startY + 20);
                
                if (slot.size > 0) {{
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
                    ctx.font = '8px Inter, Arial';
                    ctx.fillText(`${{slot.size}}b`, curX + slotW / 2, startY + 10);
                }}
                
                curX += slotW;
            }});
            
            // Draw sweep pointer
            const time = (Date.now() / 1500) % displaySlots.length;
            const sweepIndex = Math.floor(time);
            const sweepX = startX + sweepIndex * slotW + slotW / 2;
            
            ctx.fillStyle = '#00f2fe';
            ctx.beginPath();
            ctx.moveTo(sweepX, startY - 4);
            ctx.lineTo(sweepX - 5, startY - 12);
            ctx.lineTo(sweepX + 5, startY - 12);
            ctx.fill();
        }}

        // Visualizer 3: SQNR & Quantization Plot
        function drawT3Plot(levels, mu) {{
            const canvas = document.getElementById('canvas-t3');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;
            ctx.clearRect(0, 0, w, h);
            
            const midX = w / 2;
            const activeTheme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
            
            ctx.strokeStyle = activeTheme === 'dark' ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)';
            ctx.beginPath(); ctx.moveTo(midX, 0); ctx.lineTo(midX, h); ctx.stroke();
            
            // Left Half: Companding
            ctx.fillStyle = activeTheme === 'dark' ? '#ffffff' : '#1a2c40';
            ctx.font = 'bold 10px Inter, Arial';
            ctx.textAlign = 'left';
            ctx.fillText(`Compression Curve (μ = ${{mu}})`, 10, 18);
            
            const curveW = midX - 30;
            const curveH = h - 40;
            const startCurveX = 15;
            const startCurveY = h - 15;
            
            ctx.strokeStyle = activeTheme === 'dark' ? 'rgba(255, 255, 255, 0.3)' : 'rgba(0, 0, 0, 0.3)';
            ctx.beginPath();
            ctx.moveTo(startCurveX, startCurveY); ctx.lineTo(startCurveX + curveW, startCurveY);
            ctx.moveTo(startCurveX, startCurveY); ctx.lineTo(startCurveX, startCurveY - curveH);
            ctx.stroke();
            
            ctx.strokeStyle = '#ff007f';
            ctx.lineWidth = 2;
            ctx.beginPath();
            for (let xPixel = 0; xPixel <= curveW; xPixel++) {{
                const x = xPixel / curveW;
                let y = x;
                if (mu > 0) {{
                    y = Math.log(1 + mu * x) / Math.log(1 + mu);
                }}
                const yPixel = startCurveY - y * curveH;
                if (xPixel === 0) ctx.moveTo(startCurveX + xPixel, yPixel);
                else ctx.lineTo(startCurveX + xPixel, yPixel);
            }}
            ctx.stroke();
            
            // Right Half: Staircase Quantizer
            ctx.fillStyle = activeTheme === 'dark' ? '#ffffff' : '#1a2c40';
            ctx.fillText(`Quantizer Stairs (L = ${{levels}})`, midX + 10, 18);
            
            const plotW = w - midX - 25;
            const plotH = h - 40;
            const startPlotX = midX + 10;
            const startPlotY = h / 2 + 10;
            
            ctx.strokeStyle = '#00f2fe';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            for (let i = 0; i <= plotW; i++) {{
                const t = (i / plotW) * (2 * Math.PI);
                const yVal = Math.sin(t);
                const yPixel = startPlotY - yVal * (plotH / 2.3);
                if (i === 0) ctx.moveTo(startPlotX + i, yPixel);
                else ctx.lineTo(startPlotX + i, yPixel);
            }}
            ctx.stroke();
            
            ctx.strokeStyle = '#00ff66';
            ctx.lineWidth = 1.8;
            ctx.beginPath();
            for (let i = 0; i <= plotW; i++) {{
                const t = (i / plotW) * (2 * Math.PI);
                const yVal = Math.sin(t);
                const levelIndex = Math.round((yVal + 1) / 2 * (levels - 1));
                const quantizedVal = (levelIndex / (levels - 1)) * 2 - 1;
                const yPixel = startPlotY - quantizedVal * (plotH / 2.3);
                if (i === 0) ctx.moveTo(startPlotX + i, yPixel);
                else ctx.lineTo(startPlotX + i, yPixel);
            }}
            ctx.stroke();
        }}

        // Visualizer 4: Storage Space Comparison
        function drawT4Plot(totalSize) {{
            const canvas = document.getElementById('canvas-t4');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;
            ctx.clearRect(0, 0, w, h);
            
            const activeTheme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
            
            ctx.fillStyle = activeTheme === 'dark' ? '#ffffff' : '#1a2c40';
            ctx.font = 'bold 11px Inter, Arial';
            ctx.textAlign = 'left';
            ctx.fillText('Storage Capacity & Comparison', 10, 16);
            
            const cardX = 15;
            const cardY = 30;
            const cardW = 90;
            const cardH = h - 45;
            
            ctx.strokeStyle = activeTheme === 'dark' ? '#00f2fe' : '#0072ff';
            ctx.lineWidth = 2;
            ctx.strokeRect(cardX, cardY, cardW, cardH);
            
            ctx.fillStyle = activeTheme === 'dark' ? 'rgba(0, 242, 254, 0.1)' : 'rgba(0, 114, 255, 0.1)';
            ctx.fillRect(cardX + cardW - 12, cardY, 12, 12);
            ctx.beginPath();
            ctx.moveTo(cardX + cardW - 12, cardY);
            ctx.lineTo(cardX + cardW, cardY + 12);
            ctx.stroke();
            
            ctx.fillStyle = activeTheme === 'dark' ? '#00f2fe' : '#0072ff';
            ctx.font = 'bold 12px Inter, Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`${{totalSize.toFixed(2)}}`, cardX + cardW / 2, cardY + cardH / 2 - 2);
            ctx.font = '9px Inter, Arial';
            ctx.fillText('MB File', cardX + cardW / 2, cardY + cardH / 2 + 10);
            
            const barX = 125;
            const barW = w - barX - 15;
            const barH = 10;
            const spacing = 20;
            
            const comps = [
                {{ label: 'Floppy (1.44 MB)', size: 1.44, color: '#f5a623' }},
                {{ label: 'Current File', size: totalSize, color: '#ff007f' }},
                {{ label: 'Standard MP3 (5.0 MB)', size: 5.0, color: '#00ff66' }},
                {{ label: 'CD Audio (700 MB)', size: 700.0, color: '#00f2fe' }}
            ];
            
            const maxBase = Math.max(10, totalSize);
            ctx.textAlign = 'left';
            
            comps.forEach((comp, index) => {{
                const y = 30 + index * spacing;
                
                ctx.fillStyle = activeTheme === 'dark' ? 'rgba(255, 255, 255, 0.6)' : '#5c6b73';
                ctx.font = '8px Inter, Arial';
                ctx.fillText(comp.label, barX, y + 8);
                
                ctx.fillStyle = activeTheme === 'dark' ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';
                ctx.fillRect(barX, y + 10, barW, barH);
                
                let fillW = (comp.size / maxBase) * barW;
                if (comp.size === 700) fillW = barW;
                if (fillW > barW) fillW = barW;
                
                ctx.fillStyle = comp.color;
                ctx.fillRect(barX, y + 10, fillW, barH);
                
                ctx.fillStyle = activeTheme === 'dark' ? '#ffffff' : '#1a2c40';
                ctx.font = 'bold 8px Inter, Arial';
                ctx.fillText(comp.size >= 1000 ? `${{(comp.size/1024).toFixed(1)}} GB` : `${{comp.size.toFixed(2)}} MB`, barX + barW - 50, y + 8);
            }});
        }}

        // Setup sweep interval for TDM pointer
        setInterval(() => {{
            if (activeTab === 1) {{
                const channels = parseInt(document.getElementById('t2-channels').value) || 10;
                const bits = parseInt(document.getElementById('t2-bits').value) || 8;
                const sync = parseInt(document.getElementById('t2-sync').value) || 1;
                const control = parseInt(document.getElementById('t2-control').value) || 1;
                drawT2Plot(channels, bits, sync, control);
            }}
        }}, 100);

        // --- FLASHCARDS ENGINE ---
        let currentFlashcardIndex = 0;
        let filteredFlashcards = [...studyDataset.flashcards];
        let learnedFlashcards = new Set(JSON.parse(localStorage.getItem('learnedFlashcards') || '[]'));

        function loadFlashcard(index) {{
            if (filteredFlashcards.length === 0) {{
                document.getElementById('fc-question').innerText = "কোনো ফ্ল্যাশকার্ড পাওয়া যায়নি!";
                document.getElementById('fc-answer').innerText = "অনুগ্রহ করে অন্য কোনো ক্যাটাগরি ফিল্টার করুন।";
                return;
            }}
            currentFlashcardIndex = index;
            const card = filteredFlashcards[index];
            
            document.querySelector('.flashcard-deck').classList.remove('flipped');
            
            setTimeout(() => {{
                document.getElementById('fc-question').innerText = card.q;
                document.getElementById('fc-answer').innerHTML = card.a;
                document.getElementById('fc-badge').innerText = card.cat;
                document.getElementById('fc-badge-back').innerText = card.cat;
                
                const btn = document.getElementById('btn-fc-learned');
                if (learnedFlashcards.has(card.q)) {{
                    btn.innerHTML = '<i class="fa-solid fa-check-double"></i> শিখেছি (Learned)';
                    btn.classList.add('btn-primary');
                    btn.classList.remove('btn-secondary');
                }} else {{
                    btn.innerHTML = '<i class="fa-solid fa-check"></i> শিখেছি / জানি';
                    btn.classList.remove('btn-primary');
                    btn.classList.add('btn-secondary');
                }}
                
                document.getElementById('fc-counter').innerText = `কার্ড ${{index + 1}}/${{filteredFlashcards.length}}`;
                updateFlashcardProgress();
                triggerMathJax();
            }}, 150);
        }}

        function flipFlashcard() {{
            document.querySelector('.flashcard-deck').classList.toggle('flipped');
        }}

        function nextFlashcard() {{
            if (filteredFlashcards.length === 0) return;
            let nextIndex = (currentFlashcardIndex + 1) % filteredFlashcards.length;
            loadFlashcard(nextIndex);
        }}

        function prevFlashcard() {{
            if (filteredFlashcards.length === 0) return;
            let prevIndex = (currentFlashcardIndex - 1 + filteredFlashcards.length) % filteredFlashcards.length;
            loadFlashcard(prevIndex);
        }}

        function shuffleFlashcards() {{
            for (let i = filteredFlashcards.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [filteredFlashcards[i], filteredFlashcards[j]] = [filteredFlashcards[j], filteredFlashcards[i]];
            }}
            loadFlashcard(0);
        }}

        function filterFlashcards(category) {{
            if (category === 'all') {{
                filteredFlashcards = [...studyDataset.flashcards];
            }} else {{
                filteredFlashcards = studyDataset.flashcards.filter(c => c.cat === category);
            }}
            loadFlashcard(0);
        }}

        function markFlashcardLearned() {{
            if (filteredFlashcards.length === 0) return;
            const card = filteredFlashcards[currentFlashcardIndex];
            if (learnedFlashcards.has(card.q)) {{
                learnedFlashcards.delete(card.q);
            }} else {{
                learnedFlashcards.add(card.q);
            }}
            localStorage.setItem('learnedFlashcards', JSON.stringify([...learnedFlashcards]));
            loadFlashcard(currentFlashcardIndex);
        }}

        function updateFlashcardProgress() {{
            const total = studyDataset.flashcards.length;
            const learned = studyDataset.flashcards.filter(c => learnedFlashcards.has(c.q)).length;
            const pct = total > 0 ? Math.round((learned / total) * 100) : 0;
            
            document.getElementById('fc-learned-counter').innerText = `শেখা হয়েছে: ${{learned}}টি (${{pct}}%)`;
            document.getElementById('fc-progress-bar').style.width = `${{pct}}%`;
        }}

        // --- MCQ QUIZ ENGINE ---
        let quizQuestions = [];
        let currentQuizIndex = 0;
        let quizUserAnswers = [];
        let quizMode = 'quick';
        let quizTimeLeft = 20 * 60;
        let quizTimerInterval = null;
        let quizStartTime = null;

        function startQuiz(mode) {{
            quizMode = mode;
            document.getElementById('quiz-intro-area').style.display = 'none';
            document.getElementById('quiz-play-area').style.display = 'block';
            document.getElementById('quiz-result-area').style.display = 'none';
            document.getElementById('quiz-review-box').style.display = 'none';
            
            if (mode === 'quick') {{
                quizQuestions = selectRandomQuestions(10);
                document.getElementById('quiz-mode-badge').innerText = 'কুইক প্র্যাকটিস';
                document.getElementById('quiz-timer-box').style.display = 'none';
            }} else if (mode === 'mock') {{
                quizQuestions = selectRandomQuestions(20);
                document.getElementById('quiz-mode-badge').innerText = 'মক টেস্ট (Timed)';
                document.getElementById('quiz-timer-box').style.display = 'flex';
                startMockTimer();
            }} else if (mode === 'category') {{
                const cat = document.getElementById('mcq-cat-select').value;
                quizQuestions = studyDataset.mcqs.filter(m => {{
                    if (cat === 'Sampling') return m.id <= 20;
                    if (cat === 'PCM & TDM') return m.id > 20 && m.id <= 40;
                    if (cat === 'SQNR') return m.id > 40 && m.id <= 60;
                    if (cat === 'Storage') return m.id > 60 && m.id <= 80;
                    if (cat === 'Modulation') return m.id > 80;
                    return false;
                }});
                document.getElementById('quiz-mode-badge').innerText = `অধ্যায় ভিত্তিক: ${{cat}}`;
                document.getElementById('quiz-timer-box').style.display = 'none';
            }}

            currentQuizIndex = 0;
            quizUserAnswers = [];
            quizStartTime = Date.now();
            loadQuizQuestion(0);
        }}

        function selectRandomQuestions(count) {{
            const list = [...studyDataset.mcqs];
            for (let i = list.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [list[i], list[j]] = [list[j], list[i]];
            }}
            return list.slice(0, count);
        }}

        function showCategoryQuizSelector() {{
            document.getElementById('cat-quiz-selector-box').style.display = 'block';
        }}

        function hideCategoryQuizSelector() {{
            document.getElementById('cat-quiz-selector-box').style.display = 'none';
        }}

        function loadQuizQuestion(index) {{
            currentQuizIndex = index;
            const q = quizQuestions[index];
            
            document.getElementById('quiz-q-counter').innerText = `প্রশ্ন ${{index + 1}}/${{quizQuestions.length}}`;
            document.getElementById('mcq-q-text').innerText = q.q;
            
            const box = document.getElementById('mcq-options-box');
            box.innerHTML = '';
            
            const letters = ['A', 'B', 'C', 'D'];
            q.options.forEach((opt, idx) => {{
                const btn = document.createElement('button');
                btn.className = 'mcq-option-btn';
                btn.innerHTML = `<span class="mcq-option-badge">${{letters[idx]}}</span> <span class="opt-text">${{opt}}</span>`;
                btn.onclick = () => selectMCQOption(idx);
                box.appendChild(btn);
            }});
            
            document.getElementById('mcq-explanation-box').style.display = 'none';
            document.getElementById('btn-next-q').disabled = true;
            if (index === quizQuestions.length - 1) {{
                document.getElementById('btn-next-q').innerText = 'ফলাফল দেখুন';
            }} else {{
                document.getElementById('btn-next-q').innerHTML = 'পরবর্তী প্রশ্ন <i class="fa-solid fa-arrow-right"></i>';
            }}
            
            triggerMathJax();
        }}

        function selectMCQOption(optIdx) {{
            const q = quizQuestions[currentQuizIndex];
            quizUserAnswers[currentQuizIndex] = optIdx;
            
            const btns = document.querySelectorAll('.mcq-option-btn');
            btns.forEach((btn, idx) => {{
                btn.disabled = true;
                if (idx === q.correct) {{
                    btn.classList.add('correct');
                }} else if (idx === optIdx) {{
                    btn.classList.add('incorrect');
                }}
            }});
            
            document.getElementById('mcq-explanation-text').innerHTML = q.explanation;
            document.getElementById('mcq-explanation-box').style.display = 'block';
            document.getElementById('btn-next-q').disabled = false;
            
            triggerMathJax();
        }}

        function nextQuizQuestion() {{
            if (currentQuizIndex === quizQuestions.length - 1) {{
                finishQuiz();
            }} else {{
                loadQuizQuestion(currentQuizIndex + 1);
            }}
        }}

        function startMockTimer() {{
            clearInterval(quizTimerInterval);
            quizTimeLeft = 20 * 60;
            updateTimerDisplay();
            
            quizTimerInterval = setInterval(() => {{
                quizTimeLeft--;
                updateTimerDisplay();
                if (quizTimeLeft <= 0) {{
                    clearInterval(quizTimerInterval);
                    alert('সময় শেষ! আপনার মক টেস্ট অটো-সাবমিট করা হচ্ছে।');
                    finishQuiz();
                }}
            }}, 1000);
        }}

        function updateTimerDisplay() {{
            const min = Math.floor(quizTimeLeft / 60);
            const sec = quizTimeLeft % 60;
            document.getElementById('quiz-timer-text').innerText = `${{min.toString().padStart(2, '0')}}:${{sec.toString().padStart(2, '0')}}`;
        }}

        function finishQuiz() {{
            clearInterval(quizTimerInterval);
            document.getElementById('quiz-play-area').style.display = 'none';
            document.getElementById('quiz-result-area').style.display = 'block';
            
            let correctCount = 0;
            quizQuestions.forEach((q, idx) => {{
                if (quizUserAnswers[idx] === q.correct) correctCount++;
            }});
            
            const total = quizQuestions.length;
            const pct = Math.round((correctCount / total) * 100);
            
            const elapsed = Math.round((Date.now() - quizStartTime) / 1000);
            const min = Math.floor(elapsed / 60);
            const sec = elapsed % 60;
            const timeText = `${{min.toString().padStart(2, '0')}}:${{sec.toString().padStart(2, '0')}}`;
            
            document.getElementById('res-score').innerText = correctCount;
            document.getElementById('res-total').innerText = `/ ${{total}}`;
            document.getElementById('res-percentage').innerText = `${{pct}}%`;
            document.getElementById('res-time').innerText = timeText;
            document.getElementById('res-correct-count').innerText = `${{correctCount}}/${{total}}`;
            
            let feedback = "ভাল চেষ্টা! আরও বেশি বেশি অনুশীলন করুন।";
            if (pct >= 90) feedback = "অসাধারণ! আপনার প্রস্তুতি খুবই চমৎকার।";
            else if (pct >= 70) feedback = "বেশ ভালো! অল্প কিছু সংশোধনী প্রয়োজন।";
            document.getElementById('res-feedback').innerText = feedback;
        }}

        function showReviewScreen() {{
            document.getElementById('quiz-review-box').style.display = 'block';
            const list = document.getElementById('quiz-review-list');
            list.innerHTML = '';
            
            quizQuestions.forEach((q, idx) => {{
                const userAns = quizUserAnswers[idx] !== undefined ? q.options[quizUserAnswers[idx]] : 'কোনো উত্তর দেয়া হয়নি';
                const correctAns = q.options[q.correct];
                const isCorrect = quizUserAnswers[idx] === q.correct;
                
                const item = document.createElement('div');
                item.className = 'review-item';
                item.innerHTML = `
                    <div class="review-question tex2jax_process">${{idx + 1}}. ${{q.q}}</div>
                    <div class="review-user-ans" style="color: ${{isCorrect ? '#00ff66' : '#ff0033'}};">
                        <i class="fa-solid fa-${{isCorrect ? 'check' : 'xmark'}}"></i> আপনার নির্বাচন: ${{userAns}}
                    </div>
                    ${{!isCorrect ? `<div class="review-correct-ans" style="color: #00ff66;"><i class="fa-solid fa-circle-check"></i> সঠিক উত্তর: ${{correctAns}}</div>` : ''}}
                    <div class="mcq-explanation-panel tex2jax_process" style="margin-top: 10px; display: block;">
                        <strong>ব্যাখ্যা:</strong> ${{q.explanation}}
                    </div>
                `;
                list.appendChild(item);
            }});
            
            triggerMathJax();
            smoothScroll(document.getElementById('quiz-review-box'));
        }}

        function restartQuiz() {{
            startQuiz(quizMode);
        }}

        function quitQuiz() {{
            clearInterval(quizTimerInterval);
            document.getElementById('quiz-intro-area').style.display = 'block';
            document.getElementById('quiz-play-area').style.display = 'none';
            document.getElementById('quiz-result-area').style.display = 'none';
            document.getElementById('cat-quiz-selector-box').style.display = 'none';
        }}

        // --- GEMINI CHATBOT ENGINE LOGIC ---
        let isGeminiConfigOpen = false;

        function toggleGeminiChat() {{
            const panel = document.getElementById('gemini-chat-panel');
            if (panel) {{
                panel.classList.toggle('active');
            }}
        }}

        function toggleGeminiConfig() {{
            const overlay = document.getElementById('gemini-config-overlay');
            if (overlay) {{
                isGeminiConfigOpen = !isGeminiConfigOpen;
                overlay.classList.toggle('active', isGeminiConfigOpen);
                if (isGeminiConfigOpen) {{
                    const savedKey = localStorage.getItem('gemini_api_key') || '';
                    document.getElementById('gemini-api-key-input').value = savedKey;
                }}
            }}
        }}

        function saveGeminiApiKey() {{
            const key = document.getElementById('gemini-api-key-input').value.trim();
            localStorage.setItem('gemini_api_key', key);
            toggleGeminiConfig();
            appendBotMessage("এপিআই কি (API Key) সফলভাবে সেভ করা হয়েছে! এখন আপনি পূর্ণাঙ্গ এআই চ্যাট করতে পারবেন।");
        }}

        function handleGeminiKeyPress(event) {{
            if (event.key === 'Enter') {{
                sendGeminiMessage();
            }}
        }}

        function sendQuickQuery(text) {{
            const input = document.getElementById('gemini-chat-input');
            if (input) {{
                input.value = text;
                sendGeminiMessage();
            }}
        }}

        function appendUserMessage(text) {{
            const msgs = document.getElementById('gemini-chat-messages');
            if (!msgs) return;
            const msgDiv = document.createElement('div');
            msgDiv.className = 'chat-msg user';
            msgDiv.innerText = text;
            msgs.appendChild(msgDiv);
            msgs.scrollTop = msgs.scrollHeight;
        }}

        function appendBotMessage(text) {{
            const msgs = document.getElementById('gemini-chat-messages');
            if (!msgs) return;
            const msgDiv = document.createElement('div');
            msgDiv.className = 'chat-msg assistant';
            msgDiv.innerHTML = text;
            msgs.appendChild(msgDiv);
            msgs.scrollTop = msgs.scrollHeight;
            return msgDiv;
        }}

        function getLocalFallbackResponse(query) {{
            const q = query.toLowerCase();
            
            const hasTopic = q.includes('sampl') || q.includes('স্যাম্প') || q.includes('nyquist') || q.includes('নাইকু') || 
                             q.includes('pcm') || q.includes('পিসিএম') || q.includes('tdm') || q.includes('টিডিএম') || 
                             q.includes('sqnr') || q.includes('কোয়ান্ট') || q.includes('quant') || q.includes('compand') || 
                             q.includes('কম্প্যা') || q.includes('noise') || q.includes('শব্দ') || q.includes('storage') || 
                             q.includes('মেমরি') || q.includes('modulation') || q.includes('মডুলে') || q.includes('carrier') || 
                             q.includes('ask') || q.includes('fsk') || q.includes('psk') || q.includes('qam') || 
                             q.includes('aliasing') || q.includes('এলিয়াসি');
                             
            if (!hasTopic) {{
                return "আমি দুঃখিত, আমি শুধুমাত্র ও পালস কোড মডুলেশন (PCM) এবং ওয়ের অধ্যায় সম্পর্কিত প্রশ্নের উত্তর দিতে পারি। দয়া করে আপনার পাঠ্যক্রমের ওপর কোনো প্রশ্ন জিজ্ঞেস করুন।";
            }}
            
            if (q.includes('sampling rate') || q.includes('স্যাম্পলিং রেট') || q.includes('sampling frequency')) {{
                return "<strong>স্যাম্পলিং রেট (Sampling Rate - $f_s$):</strong><br>একটি অ্যানালগ সিগন্যাল থেকে প্রতি সেকেন্ডে কতগুলো স্যাম্পল বা নমুনা নেওয়া হবে, তাকে স্যাম্পলিং রেট বলা হয়। এর একক Hertz (Hz)। স্যাম্পলিং থিওরেম অনুযায়ী, সিগন্যালকে বিকৃতি ছাড়া পুনর্গঠন করতে স্যাম্পলিং রেট অবশ্যই সিগন্যালের সর্বোচ্চ কম্পাঙ্কের দ্বিগুণের সমান বা বেশি হতে হবে ($f_s \\ge 2f_m$)।";
            }}
            if (q.includes('nyquist rate') || q.includes('নাইকুইস্ট')) {{
                return "<strong>নাইকুইস্ট রেট (Nyquist Rate):</strong><br>সিগন্যালকে নিখুঁতভাবে রিকনস্ট্রাকশন করতে সর্বনিম্ন যে হারে স্যাম্পল নিতে হয়, তাকে নাইকুইস্ট রেট বলে। গাণিতিকভাবে, $\\text{{Nyquist Rate}} = 2f_m$, যেখানে $f_m$ হলো সিগন্যালের সর্বোচ্চ কম্পাঙ্ক। যদি স্যাম্পলিং রেট নাইকুইস্ট রেটের চেয়ে কম হয় ($f_s < 2f_m$), তবে <strong>Aliasing</strong> বা সিগন্যাল বিকৃতি ঘটে।";
            }}
            if (q.includes('tdm') || q.includes('টিডিএম') || q.includes('time division')) {{
                return "<strong>টাইম ডিভিশন মাল্টিপ্লেক্সিং (Time Division Multiplexing - TDM):</strong><br>TDM এমন একটি প্রক্রিয়া যেখানে একাধিক ইনপুট সিগন্যাল একই ট্রান্সমিশন চ্যানেল শেয়ার করে বিভিন্ন ক্ষুদ্র ক্ষুদ্র টাইম স্লট (Time Slot) ব্যবহারের মাধ্যমে। এখানে একাধিক চ্যানেল পর্যায়ক্রমে একটি ফ্রেমে নিজ নিজ স্লট পায়, যার ফলে একটি সাধারণ মিডিয়াম ব্যবহার করে সব সিগন্যাল একসাথে পাঠানো সম্ভব হয়।";
            }}
            if (q.includes('sqnr') || q.includes('signal to quantization')) {{
                return "<strong>SQNR (Signal-to-Quantization Noise Ratio):</strong><br>কোয়ান্টাইজেশন প্রক্রিয়ায় সৃষ্ট নয়েজের সাপেক্ষে মূল সিগন্যালের পাওয়ারের অনুপাতকে SQNR বলে। PCM সিস্টেমে প্রতি স্যাম্পলে বিট সংখ্যা ($n$) ১টি করে বাড়ালে SQNR প্রায় <strong>$6\\text{{ dB}}$</strong> বৃদ্ধি পায়। SQNR বৃদ্ধির প্রধান উপায় হলো বিট সংখ্যা ($n$) বাড়ানো অথবা <strong>Companding ($\\mu$-law / A-law)</strong> প্রযুক্তি ব্যবহার করা।";
            }}
            if (q.includes('aliasing') || q.includes('এলিয়াসি')) {{
                return "<strong>Aliasing (এলিয়াসিং):</strong><br>যদি স্যাম্পলিং রেট সিগন্যালের সর্বোচ্চ কম্পাঙ্কের দ্বিগুণের কম হয় ($f_s < 2f_m$), তবে উচ্চ কম্পাঙ্কের সিগন্যাল অংশ লো-ফ্রিকোয়েন্সি তরঙ্গের রূপ ধারণ করে মূল অ্যানালগ সিগন্যালের সাথে মিশে যায়। একেই এলিয়াসিং বিকৃতি বলে। এটি দূর করতে স্যাম্পলিং করার পূর্বে একটি <strong>Anti-aliasing Low-pass Filter</strong> ব্যবহার করা হয়।";
            }}
            if (q.includes('pcm') || q.includes('পিসিএম') || q.includes('pulse code')) {{
                return "<strong>পালস কোড মডুলেশন (PCM):</strong><br>অ্যানালগ সিগন্যালকে ডিজিটাল সিগন্যালে রূপান্তরের জন্য ব্যবহৃত প্রধান কৌশল হলো PCM। এর ৩টি ধাপ রয়েছে:<br>১. **স্যাম্পলিং (Sampling)**: অ্যানালগ ওয়েভের নির্দিষ্ট সময়ের অন্তর স্যাম্পল নেওয়া<br>২. **কোয়ান্টাইজেশন (Quantization)**: স্যাম্পলগুলোকে নিকটবর্তী নির্দিষ্ট অ্যামপ্লিচিউড লেভেলে রাউন্ড করা<br>৩. **কোডিং (Encoding)**: প্রতিটি লেভেলকে বাইনারি বিটে রূপান্তর করা।";
            }}
            
            return "আমি কমিউনিকেশন ইঞ্জিনিয়ারিং সম্পর্কিত আপনার প্রশ্নটি বুঝতে পেরেছি। তবে এই বিষয়ে বিস্তারিত উত্তর দিতে আমার একটি এপিআই কি প্রয়োজন। অনুগ্রহ করে চ্যাটের ওপরে থাকা গিয়ার (Gear) আইকনটিতে ক্লিক করে আপনার <strong>Gemini API Key</strong> সেট করুন, যাতে আমি জেমিনি নেটওয়ার্কের মাধ্যমে আপনাকে পূর্ণাঙ্গ সমাধান দিতে পারি।";
        }}

        async function sendGeminiMessage() {{
            const input = document.getElementById('gemini-chat-input');
            const sendBtn = document.getElementById('gemini-send-btn');
            if (!input || !sendBtn) return;
            const query = input.value.trim();
            if (!query) return;

            input.value = '';
            appendUserMessage(query);

            const apiKey = localStorage.getItem('gemini_api_key');

            if (!apiKey) {{
                sendBtn.disabled = true;
                const typingMsg = appendBotMessage("<i class='fa-solid fa-spinner fa-spin'></i> উত্তর খোঁজা হচ্ছে...");
                setTimeout(() => {{
                    const fallbackResponse = getLocalFallbackResponse(query);
                    typingMsg.innerHTML = fallbackResponse;
                    if (window.MathJax) {{
                        window.MathJax.typesetPromise([typingMsg]).catch(err => console.log(err));
                    }}
                    sendBtn.disabled = false;
                }}, 1000);
                return;
            }}

            sendBtn.disabled = true;
            const typingMsg = appendBotMessage("<i class='fa-solid fa-spinner fa-spin'></i> জেমিনি এআই টাইপ করছে...");

            const systemInstructionText = `You are a specialized AI assistant for ABM Academy. Your name is "ABM Academy Gemini Assistant".
Your primary task is to answer students' questions about Communication Engineering, Pulse Code Modulation (PCM), Nyquist Rate, TDM, SQNR, Carrier Modulation, and other related EEE topics.
CRITICAL TOPIC GATING RULES:
1. ONLY answer questions related to Communication Systems, Signal Processing, PCM, Delta Modulation, Carrier Modulation (ASK, FSK, PSK, QAM), Multiplexing, TDM, FDM, Sampling, Nyquist Theorem, Quantization, SQNR, Shannon Capacity, and storage calculations.
2. If the user asks about ANY unrelated topic (e.g. general history, recipes, generic coding in python/java unless related to engineering math, literature, celebrity, other subjects), politely refuse to answer. You must reply in Bengali: "আমি দুঃখিত, আমি শুধুমাত্র ও পালস কোড মডুলেশন (PCM) এবং ওয়ের অধ্যায় সম্পর্কিত প্রশ্নের উত্তর দিতে পারি।"
3. Always respond in a clear, friendly, and academic tone in Bengali.
4. Keep the explanation concise and directly focused on clearing the student's concept.
5. Use LaTeX inline style $...$ and display style $$...$$ for math formulas so that MathJax can parse them.`;

            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${{apiKey}}`;

            try {{
                const response = await fetch(apiUrl, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        contents: [{{
                            parts: [{{ text: query }}]
                        }}],
                        systemInstruction: {{
                            parts: [{{ text: systemInstructionText }}]
                        }}
                    }})
                }});

                if (!response.ok) {{
                    throw new Error(`API error code: ${{response.status}}`);
                }}

                const data = await response.json();
                
                let botText = "";
                if (data.candidates && data.candidates[0] && data.candidates[0].content && data.candidates[0].content.parts[0]) {{
                    botText = data.candidates[0].content.parts[0].text;
                }} else {{
                    botText = "আমি দুঃখিত, জেমিনি এআই থেকে কোনো উত্তর পাওয়া যায়নি। অনুগ্রহ করে আপনার এপিআই কি অথবা প্রশ্নটি যাচাই করুন।";
                }}

                let formattedText = botText
                    .replace(/\\n/g, '<br>')
                    .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
                    .replace(/\\*(.*?)\\*/g, '<em>$1</em>')
                    .replace(/### (.*?)(<br>|$)/g, '<h3>$1</h3>')
                    .replace(/## (.*?)(<br>|$)/g, '<h2>$1</h2>');

                typingMsg.innerHTML = formattedText;
                
                if (window.MathJax) {{
                    window.MathJax.typesetPromise([typingMsg]).catch(err => console.log(err));
                }}
            }} catch (err) {{
                console.error(err);
                typingMsg.innerHTML = `<span style="color: var(--danger-color);"><i class="fa-solid fa-triangle-exclamation"></i> এরর: জেমিনি এআই সার্ভারের সাথে যুক্ত হওয়া যায়নি। আপনার ইন্টারনেট সংযোগ এবং এপিআই কি (API Key) চেক করে পুনরায় চেষ্টা করুন। (এরর: ${{err.message}})</span>`;
            }} finally {{
                sendBtn.disabled = false;
            }}
        }}
"""

# Inject JS Logic before </script> at the end
script_end_idx = modified_html.rfind('</script>')
if script_end_idx != -1:
    modified_html = modified_html[:script_end_idx] + js_code_to_inject + modified_html[script_end_idx:]
    print("Injected JS logic and dataset.")

# Replace updateTX functions character by character to avoid regex issues
def replace_function_safe(content, func_name, new_body):
    search_str = f"function {func_name}"
    idx = content.find(search_str)
    if idx == -1:
        print(f"Warning: {func_name} not found.")
        return content
    
    start_brace = content.find("{", idx)
    if start_brace == -1:
        return content
    
    signature = content[idx:start_brace].strip()
    
    brace_count = 1
    end_brace = -1
    for i in range(start_brace + 1, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_brace = i
                break
                
    if end_brace == -1:
        print(f"Error: Matching closing brace for {func_name} not found.")
        return content
        
    new_func = f"{signature} {{\n{new_body}\n        }}"
    content = content[:idx] + new_func + content[end_brace + 1:]
    print(f"Successfully replaced {func_name}")
    return content


new_updateT1_body = """            const f1 = parseFloat(document.getElementById('t1-f1').value);
            const f2 = parseFloat(document.getElementById('t1-f2').value);
            const overhead = parseFloat(document.getElementById('t1-overhead').value);

            setDisplayValue('val-t1-f1', f1);
            setDisplayValue('val-t1-f2', f2);
            setDisplayValue('val-t1-overhead', overhead);

            const fm = Math.max(f1, f2);
            const fnq = 2 * fm;
            const fs = fnq * (1 + overhead / 100);
            const ts = 1000 / fs; // ms

            document.getElementById('out-t1-fm').innerText = `${fm} Hz`;
            document.getElementById('out-t1-fnq').innerText = `${fnq} Hz`;
            document.getElementById('out-t1-fs').innerText = `${fs.toFixed(0)} Hz`;
            document.getElementById('out-t1-ts').innerText = `${ts.toFixed(3)} ms`;

            // LaTeX formatting
            const mathOut = document.getElementById('out-t1-math');
            mathOut.innerHTML = `
                $$f_m = \\\\max(${f1}, ${f2}) = ${fm}\\\\text{ Hz}$$
                $$f_{NQ} = 2 \\\\cdot f_m = ${fnq}\\\\text{ Hz}$$
                $$f_s = f_{NQ} \\\\cdot (1 + ${overhead}\\\\\%) = ${fs.toFixed(0)}\\\\text{ Hz}$$
                $$T_s = \\\\frac{1}{f_s} = ${ts.toFixed(3)}\\\\text{ ms}$$
            `;
            triggerMathJax();
            drawT1Plot(f1, f2, fs);"""

new_updateT2_body = """            const channels = parseInt(document.getElementById('t2-channels').value);
            const fm = parseFloat(document.getElementById('t2-fm').value);
            const bits = parseInt(document.getElementById('t2-bits').value);
            const sync = parseInt(document.getElementById('t2-sync').value);
            const control = parseInt(document.getElementById('t2-control').value);

            setDisplayValue('val-t2-channels', channels);
            setDisplayValue('val-t2-fm', fm);
            setDisplayValue('val-t2-bits', bits);
            setDisplayValue('val-t2-sync', sync);
            setDisplayValue('val-t2-control', control);

            const fs = 2 * fm;
            const fLength = bits * channels + sync + control;
            const rb = fs * fLength; // bps
            const bw = rb / 2; // Hz (min Nyquist BW)

            document.getElementById('out-t2-fs').innerText = `${fs} Hz`;
            document.getElementById('out-t2-flen').innerText = `${fLength} bits`;
            document.getElementById('out-t2-rb').innerText = `${(rb / 1000).toFixed(1)} kbps`;
            document.getElementById('out-t2-bw').innerText = `${(bw / 1000).toFixed(1)} kHz`;

            const mathOut = document.getElementById('out-t2-math');
            mathOut.innerHTML = `
                $$f_s = 2 \\\\cdot f_m = 2 \\\\times ${fm} = ${fs}\\\\text{ Hz}$$
                $$\\\\text{Frame Length} = (M \\\\cdot n) + a + c = (${channels} \\\\times ${bits}) + ${sync} + ${control} = ${fLength}\\\\text{ bits}$$
                $$R_b = f_s \\\\cdot \\\\text{Length} = ${fs} \\\\times ${fLength} = ${(rb/1000).toFixed(1)}\\\\text{ kbps}$$
                $$B_{min} = \\\\frac{R_b}{2} = ${(bw/1000).toFixed(1)}\\\\text{ kHz}$$
            `;
            triggerMathJax();
            drawT2Plot(channels, bits, sync, control);"""

new_updateT3_body = """            const fm = parseFloat(document.getElementById('t3-fm').value);
            const error = parseFloat(document.getElementById('t3-error').value);
            const patients = parseInt(document.getElementById('t3-patients').value);
            const mu = parseFloat(document.getElementById('t3-mu').value);

            setDisplayValue('val-t3-fm', fm);
            setDisplayValue('val-t3-error', error);
            setDisplayValue('val-t3-patients', patients);
            setDisplayValue('val-t3-mu', mu);

            // Quantization calculations
            const lMin = 100 / error;
            const bitsRequired = Math.ceil(Math.log2(lMin));
            const levels = Math.pow(2, bitsRequired); // Strict 2^n rounding

            const fs = 4 * fm; // Twice the Nyquist Rate
            const rb = levels > 0 ? (bitsRequired * fs * patients) : 0;
            const bw = rb / 2;

            // SQNR calculations
            const sqnrUni = 1.76 + 6.02 * bitsRequired;
            let sqnrMu = 0;
            if (mu > 0) {
                const num = 3 * Math.pow(levels, 2);
                const den = Math.pow(Math.log(1 + mu), 2);
                sqnrMu = 10 * Math.log10(num / den);
            } else {
                sqnrMu = sqnrUni;
            }

            document.getElementById('out-t3-levels').innerText = levels;
            document.getElementById('out-t3-bits').innerText = `${bitsRequired} bits`;
            document.getElementById('out-t3-sqnr-uni').innerText = `${sqnrUni.toFixed(2)} dB`;
            document.getElementById('out-t3-sqnr-mu').innerText = `${sqnrMu.toFixed(2)} dB`;
            document.getElementById('out-t3-bw').innerText = `${(bw / 1000).toFixed(1)} kHz`;

            const mathOut = document.getElementById('out-t3-math');
            mathOut.innerHTML = `
                $$L \\\\ge 100 / ${error} = ${lMin.toFixed(0)} \\\\Rightarrow L_{actual} = ${levels}$$
                $$n = ${bitsRequired}\\\\text{ bits}$$
                $$\\\\text{SQNR (Uniform)} = 1.76 + 6.02(${bitsRequired}) = ${sqnrUni.toFixed(2)}\\\\text{ dB}$$
            `;
            triggerMathJax();
            drawT3Plot(levels, mu);"""

new_updateT4_body = """            const fm = parseFloat(document.getElementById('t4-fm').value);
            const bits = parseInt(document.getElementById('t4-bits').value);
            const channels = parseInt(document.getElementById('t4-channels').value);
            const duration = parseFloat(document.getElementById('t4-duration').value);

            setDisplayValue('val-t4-fm', fm);
            setDisplayValue('val-t4-bits', bits);
            setDisplayValue('val-t4-duration', duration);

            const fs = 2 * fm;
            const rb = fs * bits * channels;
            const totalBits = rb * duration;
            const totalSize = totalBits / (8 * 1000 * 1000); // MB in decimal

            document.getElementById('out-t4-fs').innerText = `${fs} Hz`;
            document.getElementById('out-t4-rb').innerText = `${(rb / 1000).toFixed(1)} kbps`;
            document.getElementById('out-t4-size').innerText = `${totalSize.toFixed(2)} MB`;

            const mathOut = document.getElementById('out-t4-math');
            mathOut.innerHTML = `
                $$R_b = M \\\\cdot n \\\\cdot f_s = ${channels} \\\\times ${bits} \\\\times ${fs} = ${(rb/1000).toFixed(1)}\\\\text{ kbps}$$
                $$\\\\text{Storage Size} = \\\\frac{R_b \\\\cdot \\\\text{Time}}{8 \\\\cdot 10^6} = \\\\frac{${rb} \\\\times ${duration}}{8 \\\\cdot 10^6} = ${totalSize.toFixed(2)}\\\\text{ MB}$$
            `;
            triggerMathJax();
            drawT4Plot(totalSize);"""

modified_html = replace_function_safe(modified_html, "updateT1", new_updateT1_body)
modified_html = replace_function_safe(modified_html, "updateT2", new_updateT2_body)
modified_html = replace_function_safe(modified_html, "updateT3", new_updateT3_body)
modified_html = replace_function_safe(modified_html, "updateT4", new_updateT4_body)

# Replace the setTheme function to support visualizer updates
new_setTheme_body = """            const body = document.body;
            const toggleBtn = document.getElementById('theme-toggle-btn');
            
            if (theme === 'light') {
                body.classList.add('light-theme');
                if (toggleBtn) {
                    toggleBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
                    toggleBtn.style.color = '#eab308'; // Golden sun color
                }
                localStorage.setItem('theme', 'light');
            } else {
                body.classList.remove('light-theme');
                if (toggleBtn) {
                    toggleBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
                    toggleBtn.style.color = '#00f2fe'; // Cyan moon color
                }
                localStorage.setItem('theme', 'dark');
            }
            
            // Redraw visualizers
            if (typeof updateT1 === 'function') {
                updateT1();
                updateT2();
                updateT3();
                updateT4();
            }"""

modified_html = replace_function_safe(modified_html, "setTheme", new_setTheme_body)

# Replace title and header elements for animated brand design
old_title = "<title>ABM Academy - A Digital Learning Platform</title>"
new_title = "<title>ABM Academy - Your Digital Learning hub.</title>"
modified_html = modified_html.replace(old_title, new_title)

old_full_header = """    <header>
        <div class="header-brand">
            <div class="header-logo">ABM</div>
            <div>
                <h1><span>ABM Academy</span> - A Digital Learning Platform</h1>
                <p>Interactive E-Learning E-Book for Communication Engineering</p>
            </div>
        </div>
        <div class="theme-actions">
            <!-- Dynamic Theme Toggle Options -->
            <div class="theme-toggle-container">
                <button class="theme-option active" id="theme-dark-btn" onclick="setTheme('dark')">
                    <i class="fa-solid fa-moon"></i> <span>ডার্ক মোড</span>
                </button>
                <button class="theme-option" id="theme-light-btn" onclick="setTheme('light')">
                    <i class="fa-solid fa-sun"></i> <span>লাইট মোড</span>
                </button>
            </div>
            <p style="font-style: italic; font-weight: 500; font-size: 0.85rem;" class="quiz-explanation-text"><i class="fa-solid fa-book-open"></i> E-Book 2026</p>
        </div>
    </header>"""

new_full_header = """    <header>
        <div class="header-brand">
            <div class="header-logo-container">
                <svg class="header-logo-svg" viewBox="0 0 100 100" width="32" height="32">
                    <defs>
                        <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#00f2fe" />
                            <stop offset="50%" stop-color="#7f00ff" />
                            <stop offset="100%" stop-color="#ff007f" />
                        </linearGradient>
                        <filter id="logoGlow" x="-25%" y="-25%" width="150%" height="150%">
                            <feGaussianBlur stdDeviation="3" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>
                    </defs>
                    <g class="logo-3d-group">
                        <polygon points="50,12 83,31 83,69 50,88 17,69 17,31" fill="none" stroke="url(#logoGrad)" stroke-width="4.5" class="logo-polygon" filter="url(#logoGlow)"/>
                        <path d="M28,50 Q39,30 50,50 T72,50" fill="none" stroke="url(#logoGrad)" stroke-width="4" stroke-linecap="round" class="logo-wave"/>
                        <circle cx="50" cy="50" r="5.5" fill="url(#logoGrad)" class="logo-core" filter="url(#logoGlow)"/>
                    </g>
                </svg>
            </div>
            <div>
                <h1 class="header-title"><span>ABM Academy</span> <span class="tagline-styled">Your Digital Learning hub.</span></h1>
                <p class="header-subtitle">Interactive E-Learning E-Book for Communication Engineering</p>
            </div>
        </div>
        <div class="theme-actions">
            <!-- Premium Single Toggle Switch -->
            <button class="theme-switch-btn" id="theme-toggle-btn" onclick="toggleTheme()" title="থিম পরিবর্তন করুন (Toggle Theme)">
                <i class="fa-solid fa-moon"></i>
            </button>
            <p style="font-style: italic; font-weight: 500; font-size: 0.85rem; margin: 0;" class="quiz-explanation-text"><i class="fa-solid fa-book-open"></i> E-Book 2026</p>
        </div>
    </header>"""

modified_html = modified_html.replace(old_full_header, new_full_header)
print("Updated title, tagline, and animated SVG logo.")

# Inject Chatbot HTML before </body> at the end
chatbot_html_to_inject = """
    <!-- Floating Gemini Chatbot Widget -->
    <button class="gemini-chat-launcher" id="gemini-chat-launcher" onclick="toggleGeminiChat()" aria-label="Toggle Chatbot">
        <svg viewBox="0 0 100 100" width="32" height="32">
            <defs>
                <linearGradient id="geminiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#9bf8f4" />
                    <stop offset="50%" stop-color="#6f86ff" />
                    <stop offset="100%" stop-color="#ff99ca" />
                </linearGradient>
            </defs>
            <path d="M50,15 C50,34.33 34.33,50 15,50 C34.33,50 50,65.67 50,85 C50,65.67 65.67,50 85,50 C65.67,50 50,34.33 50,15 Z" fill="url(#geminiGrad)" />
            <circle cx="70" cy="30" r="4" fill="#fff" opacity="0.8" />
            <circle cx="30" cy="70" r="3" fill="#fff" opacity="0.6" />
        </svg>
    </button>

    <div class="gemini-chat-panel" id="gemini-chat-panel">
        <div class="gemini-chat-header">
            <div style="display: flex; align-items: center; gap: 10px;">
                <svg viewBox="0 0 100 100" width="22" height="22" style="overflow: visible;">
                    <path d="M50,15 C50,34.33 34.33,50 15,50 C34.33,50 50,65.67 50,85 C50,65.67 65.67,50 85,50 C65.67,50 50,34.33 50,15 Z" fill="url(#geminiGrad)" />
                </svg>
                <span style="font-weight: 700; font-size: 1.05rem; background: linear-gradient(90deg, #00f2fe, #ff007f); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Gemini Assistant</span>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
                <button class="chat-header-btn" onclick="toggleGeminiConfig()" title="Settings / API Key" style="background: none; border: none; color: var(--text-secondary); cursor: pointer; font-size: 1.1rem; padding: 2px; transition: color 0.2s;"><i class="fa-solid fa-gear"></i></button>
                <button class="chat-header-btn" onclick="toggleGeminiChat()" title="Close Chat" style="background: none; border: none; color: var(--text-secondary); cursor: pointer; font-size: 1.1rem; padding: 2px; transition: color 0.2s;"><i class="fa-solid fa-chevron-down"></i></button>
            </div>
        </div>

        <div class="gemini-chat-messages" id="gemini-chat-messages">
            <div class="chat-msg assistant">
                স্বাগতম! আমি <strong>ABM Academy Gemini Assistant</strong>। কুইজ, স্যাম্পলিং, নাইকুইস্ট রেট, TDM, SQNR, কেরিয়ার মডুলেশন (ASK, FSK, PSK, QAM) বা রিলেটেড যেকোনো গাণিতিক সমস্যা সমাধান করতে আমি আপনাকে সাহায্য করতে পারি। 
                <br><br>
                <em>প্রশ্ন করুন অথবা নিচের দ্রুত সাজেশনগুলো থেকে সিলেক্ট করুন:</em>
                <div class="quick-suggestions-box">
                    <span class="suggestion-tag" onclick="sendQuickQuery('স্যাম্পলিং রেট (Sampling Rate) কী?')">স্যাম্পলিং রেট কী?</span>
                    <span class="suggestion-tag" onclick="sendQuickQuery('Nyquist Rate এবং Nyquist Interval বলতে কী বোঝায়?')">Nyquist Rate কী?</span>
                    <span class="suggestion-tag" onclick="sendQuickQuery('TDM (Time Division Multiplexing) কীভাবে কাজ করে?')">TDM কী?</span>
                    <span class="suggestion-tag" onclick="sendQuickQuery('PCM সিস্টেমে SQNR বৃদ্ধির উপায়গুলো কী কী?')">SQNR বৃদ্ধির উপায় কী?</span>
                    <span class="suggestion-tag" onclick="sendQuickQuery('Aliasing বিকৃতি দূর করার উপায় কী?')">Aliasing দূর করার উপায়?</span>
                </div>
            </div>
        </div>

        <div class="gemini-chat-input-area">
            <input type="text" id="gemini-chat-input" placeholder="কমিউনিকেশন ইঞ্জিনিয়ারিং এর প্রশ্ন লিখুন..." onkeypress="handleGeminiKeyPress(event)">
            <button id="gemini-send-btn" onclick="sendGeminiMessage()" aria-label="Send Message"><i class="fa-solid fa-paper-plane"></i></button>
        </div>

        <!-- Config Settings Overlay -->
        <div class="gemini-config-overlay" id="gemini-config-overlay">
            <h4 style="margin-bottom: 12px; color: var(--accent-color);"><i class="fa-solid fa-key"></i> Gemini API Key কনফিগার করুন</h4>
            <p style="font-size: 0.8rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 20px;">
                জেমিনি এআই এপিআই সরাসরি ব্যবহার করতে আপনার নিজস্ব API Key এখানে সেট করুন। আপনার কি-টি ব্রাউজারের লোকাল স্টোরেজে সুরক্ষিত থাকবে।
            </p>
            <input type="password" id="gemini-api-key-input" placeholder="AIzaSy..." style="width: 100%; padding: 10px 12px; border-radius: 6px; border: 1px solid var(--border-color); background: rgba(0,0,0,0.3); color: #fff; margin-bottom: 20px; font-family: monospace; outline: none; text-align: center;">
            <div style="display: flex; gap: 10px; width: 100%; justify-content: center;">
                <button class="btn btn-primary" onclick="saveGeminiApiKey()" style="padding: 8px 16px; font-size: 0.85rem;"><i class="fa-solid fa-floppy-disk"></i> সেভ করুন</button>
                <button class="btn btn-secondary" onclick="toggleGeminiConfig()" style="padding: 8px 16px; font-size: 0.85rem;">ফিরে যান</button>
            </div>
        </div>
    </div>
"""

body_end_idx = modified_html.rfind('</body>')
if body_end_idx != -1:
    modified_html = modified_html[:body_end_idx] + chatbot_html_to_inject + modified_html[body_end_idx:]
    print("Injected Chatbot HTML mockup.")

# Write output file
with open(html_filepath, "w", encoding="utf-8") as f:
    f.write(modified_html)

print("HTML file successfully updated.")
