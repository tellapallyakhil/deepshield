import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_slide_layout = prs.slide_layouts[6] # Blank slide

    # Color Palette - Modern Cyber Dark Theme
    BG_COLOR = RGBColor(11, 15, 25)         # #0B0F19 (Deep Charcoal Slate)
    CARD_BG = RGBColor(21, 28, 44)          # #151C2C (Elevated Surface)
    CARD_BORDER = RGBColor(37, 47, 74)      # #252F4A (Subtle border)
    ACCENT_BLUE = RGBColor(59, 130, 246)    # #3B82F6 (Electric Blue)
    ACCENT_CYAN = RGBColor(6, 182, 212)     # #06B6D4 (Cyan Tech)
    ACCENT_GREEN = RGBColor(16, 185, 129)   # #10B981 (Emerald Shield)
    ACCENT_AMBER = RGBColor(245, 158, 11)   # #F59E0B (Warning Amber)
    ACCENT_RED = RGBColor(239, 68, 68)      # #EF4444 (Critical Red)
    TEXT_WHITE = RGBColor(255, 255, 255)    # #FFFFFF
    TEXT_MUTED = RGBColor(148, 163, 184)    # #94A3B8 (Cool Slate Gray)
    TEXT_LIGHT = RGBColor(226, 232, 240)    # #E2E8F0 (Off White)

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text=""):
        # Top Accent Line
        accent_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.45), Inches(0.6), Inches(0.06))
        accent_line.fill.solid()
        accent_line.fill.fore_color.rgb = ACCENT_CYAN
        accent_line.line.fill.background()

        # Category / Section Pill Text
        if category_text:
            cat_box = slide.shapes.add_textbox(Inches(1.5), Inches(0.35), Inches(10), Inches(0.35))
            tf_cat = cat_box.text_frame
            tf_cat.word_wrap = True
            p_cat = tf_cat.paragraphs[0]
            p_cat.text = category_text.upper()
            p_cat.font.size = Pt(10)
            p_cat.font.bold = True
            p_cat.font.color.rgb = ACCENT_CYAN

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.75))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s1)

    # Decorative background card
    add_card(s1, 0.8, 0.8, 11.733, 5.9, CARD_BG, CARD_BORDER)

    # Top Tag
    tag_box = s1.shapes.add_textbox(Inches(1.4), Inches(1.3), Inches(8), Inches(0.4))
    p = tag_box.text_frame.paragraphs[0]
    p.text = "ENTERPRISE SOC SECURITY • MULTI-MODAL ARTIFICIAL INTELLIGENCE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    # Main Project Title
    main_title = s1.shapes.add_textbox(Inches(1.4), Inches(1.7), Inches(10.5), Inches(1.3))
    tf = main_title.text_frame
    p = tf.paragraphs[0]
    p.text = "deepSheild (HTCS)"
    p.font.size = Pt(46)
    p.font.bold = True
    p.font.color.rgb = RGBColor(96, 165, 250)

    # Subtitle
    sub_title = s1.shapes.add_textbox(Inches(1.4), Inches(2.85), Inches(10.5), Inches(0.9))
    tf_sub = sub_title.text_frame
    p = tf_sub.paragraphs[0]
    p.text = "Holistic Threat Command System — Multi-Modal AI Security & Deepfake Detection Platform"
    p.font.size = Pt(18)
    p.font.color.rgb = TEXT_LIGHT

    # Divider
    div = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.4), Inches(3.9), Inches(10.5), Inches(0.02))
    div.fill.solid()
    div.fill.fore_color.rgb = CARD_BORDER
    div.line.fill.background()

    # Meta cards: Candidate & Guide
    meta_box1 = s1.shapes.add_textbox(Inches(1.4), Inches(4.2), Inches(4.8), Inches(1.8))
    tf1 = meta_box1.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "PRESENTED BY:"
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_CYAN

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "[Student Name / Candidate]"
    p1_sub.font.size = Pt(18)
    p1_sub.font.bold = True
    p1_sub.font.color.rgb = TEXT_WHITE

    p1_det = tf1.add_paragraph()
    p1_det.text = "Department of Computer Science & Engineering\nRoll No / Register ID: [Your Roll No]"
    p1_det.font.size = Pt(12)
    p1_det.font.color.rgb = TEXT_MUTED

    meta_box2 = s1.shapes.add_textbox(Inches(6.8), Inches(4.2), Inches(5.0), Inches(1.8))
    tf2 = meta_box2.text_frame
    p2 = tf2.paragraphs[0]
    p2.text = "PROJECT SUPERVISOR & GUIDE:"
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_GREEN

    p2_sub = tf2.add_paragraph()
    p2_sub.text = "[Guide Name / Faculty Mentor]"
    p2_sub.font.size = Pt(18)
    p2_sub.font.bold = True
    p2_sub.font.color.rgb = TEXT_WHITE

    p2_det = tf2.add_paragraph()
    p2_det.text = "Designation & Department\nInstitution / University Name (2025–2026)"
    p2_det.font.size = Pt(12)
    p2_det.font.color.rgb = TEXT_MUTED

    s1.notes_slide.notes_text_frame.text = (
        "Good morning respected evaluators, guide, and faculty members. Today I am presenting 'deepSheild (HTCS)' "
        "— a next-generation Holistic Threat Command System designed to tackle modern cyber threats using multi-modal AI."
    )

    # ==========================================
    # SLIDE 2: GROWING MODERN THREATS
    # ==========================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s2)
    add_header(s2, "The Next-Gen Cyber Threat Landscape", "Threat Environment Analysis")

    cols2 = [
        ("🎭 Generative AI Weaponization", 
         "Synthetic Media & Voice Clones", 
         ACCENT_RED,
         [
             "Hyper-realistic Deepfake video synthesis bypassing biometrics and KYC authentication.",
             "Few-shot voice cloning enabling high-profile CEO fraud and audio phishing ('vishing').",
             "AI-generated impersonation capable of convincing multi-million dollar unauthorized transactions."
         ]),
        ("⚡ Multi-Vector Coordinated Attacks", 
         "Blended Threat Campaigns", 
         ACCENT_AMBER,
         [
             "Attackers no longer deploy isolated exploits; modern campaigns blend multiple vectors.",
             "A phishing email embeds a zero-day malicious URL backed by an executive deepfake video.",
             "Simultaneous lateral network intrusion distracts analysts from exfiltration channels."
         ]),
        ("📉 Enterprise Defense Breakdown", 
         "Alert Fatigue & Blind Spots", 
         ACCENT_BLUE,
         [
             "SOC teams face over 10,000+ un-correlated security telemetry alerts daily.",
             "Traditional SIEM & EDR tools lack native capability to inspect audio/video tampering.",
             "Delayed response times (MTTR > 4.5 hours) allow attackers to cause critical damage."
         ])
    ]

    for i, (title, sub, color, points) in enumerate(cols2):
        left = 0.8 + i * 3.95
        add_card(s2, left, 1.6, 3.8, 5.2)
        
        # Indicator bar
        bar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(1.6), Inches(3.8), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()

        tb = s2.shapes.add_textbox(Inches(left + 0.25), Inches(1.85), Inches(3.3), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        p_sub = tf.add_paragraph()
        p_sub.text = sub.upper()
        p_sub.font.size = Pt(9.5)
        p_sub.font.bold = True
        p_sub.font.color.rgb = color
        p_sub.space_after = Pt(14)

        for pt in points:
            p_pt = tf.add_paragraph()
            p_pt.text = f"•  {pt}"
            p_pt.font.size = Pt(11.5)
            p_pt.font.color.rgb = TEXT_LIGHT
            p_pt.space_after = Pt(10)

    s2.notes_slide.notes_text_frame.text = (
        "In Slide 2, we explore why this project is critically needed today. Cyber threats have evolved from simple "
        "malware scripts to sophisticated, coordinated attacks leveraging generative AI—such as deepfake executive videos "
        "and voice clones that bypass standard enterprise defenses."
    )

    # ==========================================
    # SLIDE 3: PROBLEM STATEMENT
    # ==========================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s3)
    add_header(s3, "Problem Statement: The Failure of Siloed Security", "Vulnerability & Gap Analysis")

    grid3 = [
        ("01", "Fragmented Tooling & Blind Spots", 
         "Current organizations rely on disjointed point solutions for email, network logs, and endpoints. There is zero native integration for deepfake video or synthetic audio forensics."),
        ("02", "Lack of Cross-Modal Threat Fusion", 
         "When an incident spans an email, a malicious URL, and a deepfake video, security engines fail to link these events together into a singular unified attack narrative."),
        ("03", "Exorbitant Latency & Manual Triage", 
         "Analysts manually inspect media files using isolated offline utilities, causing response times to lag behind automated, fast-moving adversary campaigns."),
        ("04", "Unverifiable Forensic Chain of Custody", 
         "Evidence gathered during rapid incident response often lacks cryptographic SHA-256 validation and immutable audit logging, leading to inadmissible evidence in legal hearings.")
    ]

    for i, (num, title, desc) in enumerate(grid3):
        row = i // 2
        col = i % 2
        left = 0.8 + col * 5.95
        top = 1.6 + row * 2.65
        add_card(s3, left, top, 5.75, 2.45)

        tb = s3.shapes.add_textbox(Inches(left + 0.3), Inches(top + 0.25), Inches(5.15), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p_num = tf.paragraphs[0]
        p_num.text = f"GAP {num}  •  CRITICAL LIMITATION"
        p_num.font.size = Pt(9.5)
        p_num.font.bold = True
        p_num.font.color.rgb = ACCENT_RED

        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.size = Pt(16)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.space_after = Pt(6)

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(11.5)
        p_desc.font.color.rgb = TEXT_MUTED

    s3.notes_slide.notes_text_frame.text = (
        "Here we articulate the core problem statement: The enterprise security paradigm is broken because tools operate in silos. "
        "When an attacker launches a multi-modal attack, disconnected monitors cannot see the big picture."
    )

    # ==========================================
    # SLIDE 4: CORE PROJECT OBJECTIVES
    # ==========================================
    s4 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s4)
    add_header(s4, "Core Project Objectives & Design Goals", "System Mission & Scope")

    objs = [
        ("🎯", "Multi-Modal AI Threat Detection", 
         "Build specialized high-accuracy neural networks and machine learning models for Video Deepfakes, Voice Clones, Phishing Emails, Malicious URLs, and Network Intrusions."),
        ("⚡", "Holistic Threat Fusion (HTCS)", 
         "Formulate an adaptive probabilistic Bayesian fusion algorithm that synthesizes disjointed cross-modal signals into an actionable 0–100% Risk Score with 4 triage tiers."),
        ("🖥️", "Unified SOC Analyst Workbench", 
         "Engineer an intuitive, modern reactive web console offering centralized case management, sub-second telemetry metrics, and visual Explainable AI (XAI) heatmaps."),
        ("⚖️", "Cryptographic Forensics & Compliance", 
         "Implement tamper-proof SHA-256 digital fingerprinting, user-authenticated audit trails, and automated chain of custody generation for legal and regulatory compliance.")
    ]

    for i, (icon, title, desc) in enumerate(objs):
        left = 0.8 + i * 2.95
        add_card(s4, left, 1.6, 2.85, 5.2)

        tb = s4.shapes.add_textbox(Inches(left + 0.25), Inches(1.85), Inches(2.35), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p_ic = tf.paragraphs[0]
        p_ic.text = icon
        p_ic.font.size = Pt(28)
        p_ic.space_after = Pt(8)

        p_t = tf.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = ACCENT_CYAN
        p_t.space_after = Pt(10)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = TEXT_LIGHT

    s4.notes_slide.notes_text_frame.text = (
        "The project has 4 central objectives: Multi-modal AI detection, Bayesian threat fusion, "
        "a unified SOC workbench, and cryptographic digital forensics."
    )

    # ==========================================
    # SLIDE 5: MEDIA SECURITY MODULES
    # ==========================================
    s5 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s5)
    add_header(s5, "Media Security Modules: Video & Voice Defense", "AI Engine Specifications")

    # Left: Video Deepfake
    add_card(s5, 0.8, 1.6, 5.75, 5.2)
    tb_vid = s5.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.25), Inches(4.7))
    tf_v = tb_vid.text_frame
    tf_v.word_wrap = True

    p = tf_v.paragraphs[0]
    p.text = "🎭 Deepfake Video Detection Engine"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(96, 165, 250)

    p_sub = tf_v.add_paragraph()
    p_sub.text = "VISION TRANSFORMER (ViT-B/16) + EFFICIENTNET-B4 ENSEMBLE"
    p_sub.font.size = Pt(9.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_CYAN
    p_sub.space_after = Pt(12)

    v_points = [
        "Dataset Baseline: Trained on 400 FaceForensics++ benchmark videos (200 pristine, 200 manipulated) + 140,000 face image corpus.",
        "Facial Extraction & Preprocessing: MTCNN face localization and temporal frame extraction at critical keyframe timestamps.",
        "Micro-Artifact Inspection: Analyzes Laplacian variance (skin blur artifacts), boundary mask blending gradients, and eye-blink dynamics.",
        "Temporal Voting Filter: Applies median-filtered scoring across frame sequences to resist compression noise and motion blur."
    ]
    for pt in v_points:
        p_pt = tf_v.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = TEXT_LIGHT
        p_pt.space_after = Pt(7)

    # Right: Voice Clone
    add_card(s5, 6.75, 1.6, 5.75, 5.2)
    tb_aud = s5.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.25), Inches(4.7))
    tf_a = tb_aud.text_frame
    tf_a.word_wrap = True

    p = tf_a.paragraphs[0]
    p.text = "🎙️ Synthetic Voice Clone Analyzer"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(52, 211, 153)

    p_sub = tf_a.add_paragraph()
    p_sub.text = "BIOMETRIC ACOUSTIC PITCH & VOCODER PHASE ANALYZER"
    p_sub.font.size = Pt(9.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_GREEN
    p_sub.space_after = Pt(12)

    a_points = [
        "Fundamental Frequency (F0) Tracking: Measures pitch jitter & shimmer to identify unnatural robotic phase continuity in neural vocoders.",
        "Spectral Flatness & Roll-off: Quantifies synthetic high-frequency artifacts left behind by generative speech synthesis models (TTS).",
        "MFCC Delta Transitions: Extracts 20 Mel-Frequency Cepstral Coefficients and their first/second derivatives for vocal tract signature verification.",
        "Sub-Second Latency: Processes audio clips in under 450 milliseconds, enabling live call verification."
    ]
    for pt in a_points:
        p_pt = tf_a.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = TEXT_LIGHT
        p_pt.space_after = Pt(7)

    s5.notes_slide.notes_text_frame.text = (
        "In Slide 5, we present our two core media security modules: ViT + EfficientNet-B4 for deepfake video detection, "
        "and biometric acoustic pitch/shimmer analysis for voice cloning."
    )

    # ==========================================
    # SLIDE 6: CYBER THREAT MODULES
    # ==========================================
    s6 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s6)
    add_header(s6, "Cyber Threat Modules: URL, Email & Network IDS", "AI Engine Specifications")

    cols6 = [
        ("📧 Phishing Email Analysis",
         "DistilBERT NLP Engine",
         ACCENT_CYAN,
         [
             "Pretexting Intent Detection: NLP classification of urgency cues, fear triggers, and financial extortion.",
             "Header Forensic Validation: Inspects RFC 5322 metadata, detecting SPF/DKIM spoofing and mismatching return-paths.",
             "Credential Theft Traps: Highlights deceptive links hiding behind innocent anchor texts."
         ]),
        ("🌐 Malicious URL Scanner",
         "Random Forest Classifier",
         ACCENT_BLUE,
         [
             "Trained on 100,000 URLs: Rigorously benchmarked across PhishTank and Alexa Top 1 Million datasets.",
             "99.66% Accuracy: Sub-15 millisecond evaluation on feature extraction alone.",
             "Feature Extraction: Shannon entropy, lexical character ratios, suspicious TLDs, IP-based URLs, and redirection chains."
         ]),
        ("🛡️ Network Intrusion (IDS)",
         "Deep PyTorch Autoencoder",
         ACCENT_AMBER,
         [
             "Trained on 500,000 Flows: Utilizes CIC-IDS2017 flow statistics as normal baseline behavior.",
             "Unsupervised Anomaly Scoring: Identifies novel zero-day attacks by computing flow reconstruction error loss.",
             "Detects Volumetric Threats: DDoS, Port scans, Brute-force SSH, and lateral exfiltration traffic."
         ])
    ]

    for i, (title, sub, color, points) in enumerate(cols6):
        left = 0.8 + i * 3.95
        add_card(s6, left, 1.6, 3.8, 5.2)

        bar = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(1.6), Inches(3.8), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()

        tb = s6.shapes.add_textbox(Inches(left + 0.25), Inches(1.85), Inches(3.3), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        p_sub = tf.add_paragraph()
        p_sub.text = sub.upper()
        p_sub.font.size = Pt(9.5)
        p_sub.font.bold = True
        p_sub.font.color.rgb = color
        p_sub.space_after = Pt(14)

        for pt in points:
            p_pt = tf.add_paragraph()
            p_pt.text = f"• {pt}"
            p_pt.font.size = Pt(11)
            p_pt.font.color.rgb = TEXT_LIGHT
            p_pt.space_after = Pt(9)

    s6.notes_slide.notes_text_frame.text = (
        "Slide 6 covers the traditional yet modernized cyber threat modules: DistilBERT for emails, a 99.66% accurate Random Forest "
        "for malicious URLs, and a PyTorch Autoencoder for network intrusion detection."
    )

    # ==========================================
    # SLIDE 7: HTCS THREAT FUSION ENGINE
    # ==========================================
    s7 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s7)
    add_header(s7, "HTCS Threat Fusion Engine: Cross-Modal Risk Aggregation", "Core Algorithmic Innovation")

    # Left: Formula & Mechanics Card
    add_card(s7, 0.8, 1.6, 5.75, 5.2)
    tb_f = s7.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.25), Inches(4.7))
    tf_f = tb_f.text_frame
    tf_f.word_wrap = True

    p = tf_f.paragraphs[0]
    p.text = "⚡ Probabilistic Risk Fusion Formula"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(96, 165, 250)

    p_sub = tf_f.add_paragraph()
    p_sub.text = "ADAPTIVE BAYESIAN-WEIGHTED CORRELATION"
    p_sub.font.size = Pt(9.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_CYAN
    p_sub.space_after = Pt(14)

    p_eq = tf_f.add_paragraph()
    p_eq.text = "Score = [ ∑ (Risk_i × Weight_i) / ∑ Weight_i ] × 100"
    p_eq.font.size = Pt(13)
    p_eq.font.bold = True
    p_eq.font.color.rgb = RGBColor(253, 224, 71)
    p_eq.space_after = Pt(12)

    f_points = [
        "Dynamic Vector Weighting: Network Intrusion (0.35), Deepfake Video (0.20), Voice Clone (0.15), Malicious URL (0.15), Phishing Email (0.15).",
        "Confidence Scaling: Malicious predictions contribute directly through their confidence probability; safe predictions reduce risk exposure.",
        "Critical Alert Synthesis: Flags any individual module with >75% malicious confidence as an immediate high-priority indicator.",
        "Explainable AI Output: Delivers actionable human-readable explanations alongside the numerical score."
    ]
    for pt in f_points:
        p_pt = tf_f.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = TEXT_LIGHT
        p_pt.space_after = Pt(8)

    # Right: Threat Triage Levels
    add_card(s7, 6.75, 1.6, 5.75, 5.2)
    tb_t = s7.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.25), Inches(4.7))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True

    p = tf_t.paragraphs[0]
    p.text = "🚦 Four-Tier Incident Severity Matrix"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    p_sub = tf_t.add_paragraph()
    p_sub.text = "AUTOMATED SOC INCIDENT TRIAGE WORKFLOW"
    p_sub.font.size = Pt(9.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_GREEN
    p_sub.space_after = Pt(14)

    tiers = [
        ("CRITICAL SEVERITY (Score > 75%)", ACCENT_RED, "Immediate automated isolation; revoke active sessions; dispatch emergency alert to CISO & Tier-3 SOC team."),
        ("HIGH SEVERITY (Score 51% – 75%)", ACCENT_AMBER, "Urgent forensic investigation required; quarantine suspicious emails & block domains at gateway firewall."),
        ("MEDIUM SEVERITY (Score 26% – 50%)", ACCENT_BLUE, "Enriched background telemetry gathering; trigger user re-authentication challenge (MFA)."),
        ("LOW / SAFE SEVERITY (Score 0% – 25%)", ACCENT_GREEN, "Normal operational event; logged to PostgreSQL audit table for periodic compliance archiving.")
    ]
    for tier_title, t_col, t_desc in tiers:
        p_t1 = tf_t.add_paragraph()
        p_t1.text = tier_title
        p_t1.font.size = Pt(12)
        p_t1.font.bold = True
        p_t1.font.color.rgb = t_col

        p_t2 = tf_t.add_paragraph()
        p_t2.text = t_desc
        p_t2.font.size = Pt(10.5)
        p_t2.font.color.rgb = TEXT_MUTED
        p_t2.space_after = Pt(8)

    s7.notes_slide.notes_text_frame.text = (
        "Slide 7 explains the HTCS Threat Fusion Engine — our core innovation that turns isolated data into a single unified risk score "
        "ranging from 0 to 100%, categorized into 4 automated action tiers."
    )

    # ==========================================
    # SLIDE 8: TECHNOLOGY STACK
    # ==========================================
    s8 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s8)
    add_header(s8, "Enterprise Technology Stack", "System Architecture & Engineering")

    stack_cards = [
        ("Frontend Application", ACCENT_BLUE, [
            "Framework: Next.js 16 (Turbopack)",
            "Language: TypeScript (React 19)",
            "Styling: Tailwind CSS Glassmorphism",
            "Icons & UI: Lucide React",
            "State & HTTP: Axios client + Server Rewrites"
        ]),
        ("Backend & API Layer", ACCENT_CYAN, [
            "Framework: FastAPI (Python 3.11)",
            "ASGI Server: Uvicorn Async Server",
            "Data Validation: Pydantic v2 schemas",
            "Security: OAuth2 + JWT Bearer Tokens",
            "ORM: SQLAlchemy ORM & Alembic"
        ]),
        ("AI & Deep Learning Core", ACCENT_GREEN, [
            "PyTorch 2.x & Torchvision (ViT & Autoencoder)",
            "Hugging Face Transformers (DistilBERT)",
            "Scikit-learn (Random Forest URL Scanner)",
            "OpenCV & PIL (Video frame manipulation)",
            "Librosa & Soundfile (Acoustic audio signal)"
        ]),
        ("Data & Infrastructure", ACCENT_AMBER, [
            "Database: PostgreSQL 15 (ACID compliance)",
            "Cache & Broker: Redis 7 In-Memory Store",
            "Task Queue: Celery Distributed Workers",
            "Orchestration: Docker & Docker Compose",
            "Forensics: Cryptographic SHA-256 Hashing"
        ])
    ]

    for i, (cat, col, items) in enumerate(stack_cards):
        left = 0.8 + i * 2.95
        add_card(s8, left, 1.6, 2.85, 5.2)

        bar = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(1.6), Inches(2.85), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()

        tb = s8.shapes.add_textbox(Inches(left + 0.2), Inches(1.85), Inches(2.45), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = cat
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(14)

        for item in items:
            p_item = tf.add_paragraph()
            p_item.text = f"• {item}"
            p_item.font.size = Pt(10.5)
            p_item.font.color.rgb = TEXT_LIGHT
            p_item.space_after = Pt(8)

    s8.notes_slide.notes_text_frame.text = (
        "In Slide 8, we review the technology stack. The platform uses Next.js 16 with Turbopack on the frontend, "
        "FastAPI with Python 3.11 for high-concurrency API handling, PyTorch and Hugging Face for machine learning, "
        "and PostgreSQL, Redis, and Celery orchestrated via Docker Compose."
    )

    # ==========================================
    # SLIDE 9: SYSTEM ARCHITECTURE & PIPELINE
    # ==========================================
    s9 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s9)
    add_header(s9, "End-to-End System Architecture & Data Flow", "Data Pipeline & Flow Design")

    # Workflow Steps across horizontal pipeline
    flow_steps = [
        ("Step 1", "Evidence Ingestion", "Web, Email, Video, Voice & PCAP files ingested via Next.js reverse proxy."),
        ("Step 2", "API Gateway & Auth", "FastAPI validates JWT credentials, enforces rate limits, logs audit entry."),
        ("Step 3", "SHA-256 Hashing", "Cryptographic fingerprint generated and locked into PostgreSQL audit record."),
        ("Step 4", "Parallel ML Pipeline", "Celery / Workers run ViT, DistilBERT, RF, and Autoencoders concurrently."),
        ("Step 5", "HTCS Threat Fusion", "Bayesian correlation calculates case risk score and flags high-risk indicators."),
        ("Step 6", "Analyst Workbench", "Live telemetry, XAI explainability heatmaps, and mitigation actions displayed.")
    ]

    for i, (st, title, desc) in enumerate(flow_steps):
        col = i % 3
        row = i // 3
        left = 0.8 + col * 3.95
        top = 1.6 + row * 2.65
        add_card(s9, left, top, 3.8, 2.45)

        tb = s9.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.2), Inches(3.3), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p_st = tf.paragraphs[0]
        p_st.text = f"{st.upper()}  •  PIPELINE STAGE"
        p_st.font.size = Pt(9.5)
        p_st.font.bold = True
        p_st.font.color.rgb = ACCENT_CYAN

        p_t = tf.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.space_after = Pt(6)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = TEXT_MUTED

    s9.notes_slide.notes_text_frame.text = (
        "Slide 9 outlines the end-to-end data flow. Ingestion begins at the Next.js reverse proxy, passes into FastAPI with JWT security, "
        "undergoes SHA-256 hashing, fans out to parallel ML workers, feeds into the HTCS fusion engine, and renders live on the SOC workbench."
    )

    # ==========================================
    # SLIDE 10: KEY FEATURES & SOC WORKBENCH
    # ==========================================
    s10 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s10)
    add_header(s10, "Key Features & Analyst SOC Workbench", "Product & User Experience Capabilities")

    feats = [
        ("🗂️ Unified Investigation Cases", 
         "Consolidates dozens of multimedia and cyber evidence files under a single master case record with chronological timelines."),
        ("📊 Live Threat Telemetry", 
         "Real-time database-driven SOC overview tracking active investigations, threat distribution, and mean processing latencies."),
        ("🔍 Explainable AI (XAI) Deep-Dive", 
         "Transparent confidence metrics, Laplacian texture metrics, acoustic spectrogram readouts, and token-level attention highlights."),
        ("🛡️ Multi-Tenant RBAC Security", 
         "Role-Based Access Control ensuring only verified investigators and admins can review sensitive forensic records."),
        ("⚡ High-Performance Concurrency", 
         "Non-blocking asynchronous execution allowing massive uploads without freezing the analyst's interactive UI."),
        ("📄 Exportable Audit Reports", 
         "Automated generation of compliance-ready forensic summaries detailing model versioning, SHA-256 hashes, and analyst actions.")
    ]

    for i, (title, desc) in enumerate(feats):
        col = i % 3
        row = i // 3
        left = 0.8 + col * 3.95
        top = 1.6 + row * 2.65
        add_card(s10, left, top, 3.8, 2.45)

        tb = s10.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.2), Inches(3.3), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = RGBColor(96, 165, 250)
        p_t.space_after = Pt(6)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = TEXT_LIGHT

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 showcases the key user-facing features of the SOC workbench: unified case workspaces, live telemetry, "
        "explainable AI inspection, role-based access control, high concurrency, and exportable forensic reports."
    )

    # ==========================================
    # SLIDE 11: DIGITAL FORENSICS & CHAIN OF CUSTODY
    # ==========================================
    s11 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s11)
    add_header(s11, "Digital Forensics & Cryptographic Chain of Custody", "Legal Admissibility & Evidence Integrity")

    cols11 = [
        ("🔒 SHA-256 Digital Fingerprinting",
         "Cryptographic Integrity",
         ACCENT_CYAN,
         [
             "Upon file reception, the binary stream is immediately hashed via SHA-256 before disk writing.",
             "Any post-ingestion tampering, frame alteration, or audio truncation invalidates the checksum immediately.",
             "Guarantees bit-level identical matching between ingested evidence and court-presented material."
         ]),
        ("📜 Immutable Audit Logging",
         "Chronological Accountability",
         ACCENT_GREEN,
         [
             "Every action (case creation, file upload, scan execution, score aggregation) is logged to the database.",
             "Logs record User ID, timestamp, target entity, and exact system operations performed.",
             "Complies with NIST SP 800-86 and ISO/IEC 27037 standards for digital evidence handling."
         ]),
        ("⚖️ Courtroom Admissibility",
         "Enterprise Legal Readiness",
         ACCENT_AMBER,
         [
             "Ensures strict chain of custody required for criminal prosecution and cyber insurance recovery.",
             "Tracks model versions (e.g. ViT v1.0, FF++ 140k dataset) to provide reproducible algorithmic proof.",
             "Prevents defense claims of evidence spoliation or unauthorized evidence manipulation."
         ])
    ]

    for i, (title, sub, color, points) in enumerate(cols11):
        left = 0.8 + i * 3.95
        add_card(s11, left, 1.6, 3.8, 5.2)

        bar = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(1.6), Inches(3.8), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()

        tb = s11.shapes.add_textbox(Inches(left + 0.25), Inches(1.85), Inches(3.3), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        p_sub = tf.add_paragraph()
        p_sub.text = sub.upper()
        p_sub.font.size = Pt(9.5)
        p_sub.font.bold = True
        p_sub.font.color.rgb = color
        p_sub.space_after = Pt(14)

        for pt in points:
            p_pt = tf.add_paragraph()
            p_pt.text = f"• {pt}"
            p_pt.font.size = Pt(11)
            p_pt.font.color.rgb = TEXT_LIGHT
            p_pt.space_after = Pt(9)

    s11.notes_slide.notes_text_frame.text = (
        "In Slide 11, we emphasize forensic integrity. Without tamper-evident chain of custody and cryptographic SHA-256 hashes, "
        "even the most accurate AI detection cannot hold up in court. deepSheild builds this directly into the database architecture."
    )

    # ==========================================
    # SLIDE 12: EXPERIMENTAL RESULTS & BENCHMARKS
    # ==========================================
    s12 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s12)
    add_header(s12, "Model Evaluation & Benchmark Performance", "Empirical Experimental Results")

    # Table Card
    add_card(s12, 0.8, 1.55, 11.733, 5.3)

    # Add Table
    table_shape = s12.shapes.add_table(6, 6, Inches(1.0), Inches(1.75), Inches(11.333), Inches(3.8))
    table = table_shape.table

    # Column Widths
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(2.3)
    table.columns[2].width = Inches(1.7)
    table.columns[3].width = Inches(1.7)
    table.columns[4].width = Inches(1.7)
    table.columns[5].width = Inches(1.733)

    headers = ["SECURITY MODULE", "MODEL BACKBONE", "TRAINING DATASET", "ACCURACY", "F1-SCORE", "AVG LATENCY"]
    data = [
        ["Malicious URL Scanner", "Random Forest (lexical + entropy)", "PhishTank + Alexa Top 1M", "99.66%", "99.65%", "12 ms"],
        ["Phishing Email Engine", "Fine-Tuned DistilBERT NLP", "Enron + Phishing Corpus", "96.20%", "96.10%", "85 ms"],
        ["Network IDS Anomaly", "PyTorch Deep Autoencoder", "CIC-IDS2017 (500k flows)", "97.10%", "96.80%", "18 ms"],
        ["Deepfake Video ViT", "Google ViT-B/16 + EfficientNet-B4", "FaceForensics++ (400 vids)", "94.80%", "94.35%", "8.9 s / vid"],
        ["Synthetic Voice Clones", "Biometric Acoustic F0 & MFCC", "Custom TTS & Real Speech", "92.40%", "92.10%", "420 ms"]
    ]

    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(30, 41, 59)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(data):
        for col_idx, val in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(21, 28, 44) if row_idx % 2 == 0 else RGBColor(15, 23, 42)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.color.rgb = TEXT_WHITE if col_idx < 3 else (RGBColor(52, 211, 153) if "99" in val or "97" in val or "96" in val or "94" in val or "92" in val else TEXT_LIGHT)
            p.alignment = PP_ALIGN.LEFT if col_idx < 3 else PP_ALIGN.CENTER

    # Summary footnote
    tb_fn = s12.shapes.add_textbox(Inches(1.0), Inches(5.85), Inches(11.333), Inches(0.8))
    tf_fn = tb_fn.text_frame
    p_fn = tf_fn.paragraphs[0]
    p_fn.text = "Key Benchmark Takeaway: The Random Forest URL classifier achieves industry-leading 99.66% accuracy in 12ms, while the ViT ensemble achieves 94.80% deepfake detection with resilient temporal frame voting."
    p_fn.font.size = Pt(11)
    p_fn.font.bold = True
    p_fn.font.color.rgb = ACCENT_GREEN

    s12.notes_slide.notes_text_frame.text = (
        "Slide 12 provides empirical validation of our models. Our URL classifier achieves 99.66% accuracy in just 12 milliseconds, "
        "while our Deepfake ViT model achieves 94.80% accuracy over rigorous FaceForensics++ video testing."
    )

    # ==========================================
    # SLIDE 13: LIVE DEMO & CASE WALKTHROUGH
    # ==========================================
    s13 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s13)
    add_header(s13, "Incident Lifecycle Walkthrough: Attack to Containment", "Operational Demonstration")

    steps13 = [
        ("Phase 1: Infiltration", ACCENT_RED, [
            "Adversary targets CFO with a spear-phishing email containing an urgent wire transfer pretext.",
            "Email contains a link to an obfuscated credential harvesting portal and attaches an MP4 video message from the 'CEO'."
        ]),
        ("Phase 2: Automated Ingestion", ACCENT_AMBER, [
            "Evidence is loaded into deepSheild Case #6. SHA-256 fingerprints are generated instantly upon upload.",
            "FastAPI parallelizes evaluation: DistilBERT scans email text, Random Forest evaluates URL, ViT processes video frames."
        ]),
        ("Phase 3: HTCS Threat Fusion", ACCENT_CYAN, [
            "URL classified as Malicious (99.6% conf); Email flagged as Phishing (96.2% conf); Video flagged as Deepfake (70% conf).",
            "HTCS Bayesian Engine aggregates the evidence into an overall risk score of 88.5% -> Categorized as CRITICAL."
        ]),
        ("Phase 4: Triage & Containment", ACCENT_GREEN, [
            "Real-time SOC dashboard highlights the active attack with an emergency banner.",
            "Immutable audit record generated; verified forensic report exported for incident response team."
        ])
    ]

    for i, (title, col, points) in enumerate(steps13):
        left = 0.8 + i * 2.95
        add_card(s13, left, 1.6, 2.85, 5.2)

        bar = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(1.6), Inches(2.85), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()

        tb = s13.shapes.add_textbox(Inches(left + 0.2), Inches(1.85), Inches(2.45), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(12)

        for pt in points:
            p_pt = tf.add_paragraph()
            p_pt.text = f"• {pt}"
            p_pt.font.size = Pt(10.5)
            p_pt.font.color.rgb = TEXT_LIGHT
            p_pt.space_after = Pt(8)

    s13.notes_slide.notes_text_frame.text = (
        "In Slide 13, we walk through a realistic operational incident: An attacker impersonates a CEO using a deepfake video and phishing email. "
        "We trace the lifecycle through ingestion, parallel ML analysis, Bayesian risk fusion, and final containment."
    )

    # ==========================================
    # SLIDE 14: EXPECTED OUTCOMES & IMPACT
    # ==========================================
    s14 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s14)
    add_header(s14, "Expected Outcomes & Enterprise Impact", "Value Proposition & Measurable Benefits")

    outcomes = [
        ("⚡ 85% Reduction in MTTR", 
         "Mean Time to Respond shrinks from hours to sub-minute automated triaging through cross-modal threat correlation and unified dashboards."),
        ("🛡️ Comprehensive AI Fraud Prevention", 
         "Stops high-value Business Email Compromise (BEC) and voice-cloned wire fraud before financial authorization occurs."),
        ("📉 Elimination of SOC Alert Fatigue", 
         "Replaces unmanageable disjointed telemetry with consolidated Bayesian Risk Scores, allowing tier-1 analysts to focus on genuine threats."),
        ("⚖️ Court-Ready Digital Forensic Assurance", 
         "Automates chain of custody maintenance with cryptographic hashes, meeting insurance audit and regulatory legal standards.")
    ]

    for i, (title, desc) in enumerate(outcomes):
        row = i // 2
        col = i % 2
        left = 0.8 + col * 5.95
        top = 1.6 + row * 2.65
        add_card(s14, left, top, 5.75, 2.45)

        tb = s14.shapes.add_textbox(Inches(left + 0.3), Inches(top + 0.25), Inches(5.15), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(17)
        p_title.font.bold = True
        p_title.font.color.rgb = RGBColor(96, 165, 250)
        p_title.space_after = Pt(8)

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_LIGHT

    s14.notes_slide.notes_text_frame.text = (
        "Slide 14 details the tangible impact: 85% reduction in MTTR, eradication of alert fatigue, comprehensive protection against "
        "AI-driven fraud, and verifiable courtroom admissibility."
    )

    # ==========================================
    # SLIDE 15: FUTURE ENHANCEMENTS & CONCLUSION
    # ==========================================
    s15 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s15)
    add_header(s15, "Future Roadmap & Project Conclusion", "Research Directions & Summary")

    # Left: Roadmap
    add_card(s15, 0.8, 1.6, 5.75, 5.2)
    tb_rd = s15.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.25), Inches(4.7))
    tf_rd = tb_rd.text_frame
    tf_rd.word_wrap = True

    p = tf_rd.paragraphs[0]
    p.text = "🚀 Future Research Roadmap"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    p_sub = tf_rd.add_paragraph()
    p_sub.text = "NEXT-GENERATION CAPABILITIES"
    p_sub.font.size = Pt(9.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_CYAN
    p_sub.space_after = Pt(14)

    roadmap = [
        "Autonomous SOAR Orchestration: Automatic firewall rule injection and Active Directory credential locking upon Critical threat detection.",
        "Post-Quantum Cryptography (PQC): Integrating CRYSTALS-Dilithium quantum-resistant signatures for chain of custody logs.",
        "Real-Time Video Stream Analysis: Optimizing ViT pipelines with TensorRT for live RTSP/WebRTC meeting inspection.",
        "Multi-Agent AI Defense: Autonomous LLM agents paired with deepfake detectors to conduct automated adversary threat hunting."
    ]
    for pt in roadmap:
        p_pt = tf_rd.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = TEXT_LIGHT
        p_pt.space_after = Pt(8)

    # Right: Conclusion Card
    add_card(s15, 6.75, 1.6, 5.75, 5.2)
    tb_c = s15.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.25), Inches(4.7))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True

    p = tf_c.paragraphs[0]
    p.text = "🎯 Project Conclusion"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    p_sub = tf_c.add_paragraph()
    p_sub.text = "SUMMARY OF ACHIEVEMENTS"
    p_sub.font.size = Pt(9.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_GREEN
    p_sub.space_after = Pt(14)

    p_body = tf_c.add_paragraph()
    p_body.text = (
        "deepSheild (HTCS) successfully bridges the critical gap between traditional cybersecurity systems "
        "and generative AI threat vectors.\n\n"
        "By synthesizing Deepfake Video, Voice Clone, Phishing, URL, and Network anomalies into an unified Bayesian "
        "Risk Fusion Engine, deepSheild empowers enterprise SOC teams to detect, correlate, and contain multi-modal attacks "
        "with sub-second latency and legally admissible cryptographic integrity."
    )
    p_body.font.size = Pt(12)
    p_body.font.color.rgb = TEXT_LIGHT
    p_body.space_after = Pt(16)

    p_ty = tf_c.add_paragraph()
    p_ty.text = "Thank you! Questions & Discussion."
    p_ty.font.size = Pt(16)
    p_ty.font.bold = True
    p_ty.font.color.rgb = RGBColor(96, 165, 250)

    s15.notes_slide.notes_text_frame.text = (
        "In conclusion, deepSheild (HTCS) solves the modern challenge of multi-modal AI-driven cyber threats. "
        "Thank you for your time and attention. I am now open to any questions."
    )

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deepSheild_HTCS_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
