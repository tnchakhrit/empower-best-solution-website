#!/usr/bin/env python3
"""Builds the 6 static HTML pages for empowerbestsolution.com from shared
header/footer templates + per-page content blocks. Run: python3 build.py
"""
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_DARK = '<img src="assets/logo-icon-dark.png" alt="Empower Best Solution" style="height:40px; width:auto; display:block;">'

LOGO_CREAM = '<img src="assets/logo-icon-cream.png" alt="Empower Best Solution" style="height:32px; width:auto; display:block;">'

NAV = [
    ("หน้าแรก", "index.html"),
    ("เกี่ยวกับเรา", "about.html"),
    ("โปรแกรมเตือนตรวจสอบอาคาร", "reminder-program.html"),
    ("บริการของเรา", "services.html"),
    ("ความรู้ตามกฎหมาย", "legal-knowledge.html"),
    ("ติดต่อเรา", "contact.html"),
]


def header(active_href):
    links = []
    for label, href in NAV:
        if href == active_href:
            style = "font-size:14px; font-weight:700; color:#BE7C3E;"
        else:
            style = "font-size:14px; font-weight:500;"
        links.append('      <a class="navlink" href="%s" style="%s">%s</a>' % (href, style, label))
    nav_html = "\n".join(links)
    return '''  <!-- HEADER -->
  <div class="site-header" style="display:flex; align-items:center; justify-content:space-between; padding:22px 64px; background:#F7F2E3; border-bottom:1px solid #E4DCC8; position:relative;">
    <a href="index.html" class="brand" style="display:flex; align-items:center; gap:14px;">
      ''' + LOGO_DARK + '''
      <div style="display:flex; flex-direction:column; line-height:1.3;">
        <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:19px; color:#1E3A28;">Empower Best Solution</span>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:2.5px; color:#BE7C3E; text-transform:uppercase;">Building Inspection · Thailand</span>
      </div>
    </a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle-input">
    <label for="nav-toggle" class="nav-toggle-label" aria-label="เปิดเมนู"><span></span><span></span><span></span></label>
    <nav class="site-nav" style="display:flex; gap:28px; align-items:center;">
''' + nav_html + '''
    </nav>
    <a href="contact.html" class="btn-amber header-cta" style="background:#BE7C3E; color:#FFFFFF; padding:12px 22px; border-radius:4px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; cursor:pointer; white-space:nowrap; display:inline-block;">ปรึกษาเราฟรี</a>
  </div>
'''


FOOTER = '''  <!-- FOOTER -->
  <div style="display:flex; flex-direction:column; background:#1E3A28; padding:64px 64px 28px 64px;">
    <div class="footer-cols" style="display:flex; gap:80px;">
      <div style="display:flex; flex-direction:column; gap:16px; width:320px;">
        <a href="index.html" style="display:flex; align-items:center; gap:12px;">
          ''' + LOGO_CREAM + '''
          <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:17px; color:#F7F2E3;">Empower Best Solution</span>
        </a>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#BE7C3E;">Co., Ltd. · Bangkok, Thailand</span>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:13px; line-height:1.8; color:rgba(247,242,227,0.72);">บริการตรวจสอบอาคารตาม พ.ร.บ. ควบคุมอาคาร โดยทีมวิศวกร ที่ผ่านประสบการณ์บริหารงานวิศวกรรมอาคารใหญ่กว่า 100 โครงการ</p>
        <div style="display:flex; gap:10px; margin-top:8px;">
          <div style="width:34px; height:34px; border:1px solid rgba(247,242,227,0.3); border-radius:50%; display:flex; align-items:center; justify-content:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M12 3C6.5 3 2 6.6 2 11c0 2.8 1.8 5.3 4.6 6.8L6 21l3.7-1.9c.7.1 1.5.2 2.3.2 5.5 0 10-3.6 10-8s-4.5-8.3-10-8.3Z" stroke="#F7F2E3" stroke-width="1.5" stroke-linejoin="round"/></svg></div>
          <div style="width:34px; height:34px; border:1px solid rgba(247,242,227,0.3); border-radius:50%; display:flex; align-items:center; justify-content:center;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M15 4h-2a4 4 0 0 0-4 4v3H6v4h3v9h4v-9h3l1-4h-4V8a1 1 0 0 1 1-1h3Z" stroke="#F7F2E3" stroke-width="1.5" stroke-linejoin="round"/></svg></div>
          <div style="width:34px; height:34px; border:1px solid rgba(247,242,227,0.3); border-radius:50%; display:flex; align-items:center; justify-content:center;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="2" stroke="#F7F2E3" stroke-width="1.5"/><path d="M7 10v7M7 7v.01M11 17v-4.5a2 2 0 0 1 4 0V17M11 12.5V17" stroke="#F7F2E3" stroke-width="1.4" stroke-linecap="round"/></svg></div>
          <div style="width:34px; height:34px; border:1px solid rgba(247,242,227,0.3); border-radius:50%; display:flex; align-items:center; justify-content:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><rect x="2" y="5" width="20" height="14" rx="3" stroke="#F7F2E3" stroke-width="1.5"/><path d="M10 9.5v5l4.5-2.5Z" fill="#F7F2E3"/></svg></div>
        </div>
      </div>
      <div style="display:flex; flex-direction:column; gap:13px; margin-top:4px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:2px; color:#BE7C3E; text-transform:uppercase; margin-bottom:6px;">บริการ</span>
        <a href="services.html#major-inspection" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">ตรวจสอบใหญ่ทุก 5 ปี</a>
        <a href="services.html#annual-inspection" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">ตรวจสอบประจำปี</a>
        <a href="services.html#problem-analysis" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">วิเคราะห์ปัญหาอาคาร</a>
        <a href="services.html#problem-fix" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">แก้ปัญหาอาคาร</a>
      </div>
      <div style="display:flex; flex-direction:column; gap:13px; margin-top:4px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:2px; color:#BE7C3E; text-transform:uppercase; margin-bottom:6px;">บริษัท</span>
        <a href="about.html" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">เกี่ยวกับเรา</a>
        <a href="reminder-program.html" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">โปรแกรมเตือนตรวจสอบอาคาร</a>
        <a href="legal-knowledge.html" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">ความรู้ตามกฎหมาย</a>
        <a href="contact.html" style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:rgba(247,242,227,0.85);">ติดต่อเรา</a>
      </div>
      <div style="display:flex; flex-direction:column; gap:14px; margin-top:4px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:2px; color:#BE7C3E; text-transform:uppercase; margin-bottom:2px;">ติดต่อเรา</span>
        <div style="display:flex; gap:10px; align-items:flex-start; max-width:280px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" style="margin-top:2px; flex-shrink:0;"><path d="M12 22s7-7.5 7-12.5a7 7 0 0 0-14 0C5 14.5 12 22 12 22Z" stroke="#BE7C3E" stroke-width="1.5" stroke-linejoin="round"/><circle cx="12" cy="9.5" r="2.3" stroke="#BE7C3E" stroke-width="1.4"/></svg>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; line-height:1.7; color:rgba(247,242,227,0.85);">59/109 หมู่บ้านเดอะ วอเตอร์เฮ้าส์ ซอยบางบอน 3 ซอย 12 แขวงหลักสอง เขตบางแค กรุงเทพฯ 10160</span>
        </div>
        <a href="tel:0629565194" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:rgba(247,242,227,0.85);">062-956-5194</a>
        <a href="https://line.me/ti/p/@911hrhms" target="_blank" rel="noopener" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:rgba(247,242,227,0.85);">LINE OA: @911hrhms</a>
        <a href="mailto:empower.bestsolution2024@gmail.com" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:rgba(247,242,227,0.85);">empower.bestsolution2024@gmail.com</a>
      </div>
    </div>
    <div style="display:flex; justify-content:space-between; border-top:1px solid rgba(247,242,227,0.15); margin-top:48px; padding-top:24px; flex-wrap:wrap; gap:8px;">
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:rgba(247,242,227,0.5);">© 2026 Empower Best Solution Co., Ltd. สงวนลิขสิทธิ์</span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:rgba(247,242,227,0.5);">ขึ้นทะเบียนผู้ตรวจสอบอาคารกับ ก.ย.ผ.</span>
    </div>
  </div>
'''


def page(title, description, active_href, main_content, extra_head=""):
    return '''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>''' + title + '''</title>
<meta name="description" content="''' + description + '''">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 48 48%27%3E%3Crect width=%2748%27 height=%2748%27 rx=%278%27 fill=%27%231E3A28%27/%3E%3Cpath d=%27M8 38V20l7-9 5 7v20%27 stroke=%27%23F7F2E3%27 stroke-width=%272.2%27 fill=%27none%27 stroke-linejoin=%27round%27/%3E%3Cpath d=%27M19 38V15l5-7 5 7v23%27 stroke=%27%23F7F2E3%27 stroke-width=%272.2%27 fill=%27none%27 stroke-linejoin=%27round%27/%3E%3Cpath d=%27M29 38V21l5-7 7 9v15%27 stroke=%27%23F7F2E3%27 stroke-width=%272.2%27 fill=%27none%27 stroke-linejoin=%27round%27/%3E%3C/svg%3E">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+Thai:wght@500;600;700&family=Noto+Sans+Thai:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">
<link rel="stylesheet" href="assets/styles.css">
''' + extra_head + '''</head>
<body>
<div class="container">
''' + header(active_href) + main_content + FOOTER + '''</div>
</body>
</html>
'''


# ------------------------------------------------------------------
# PAGE CONTENT
# ------------------------------------------------------------------

INDEX_MAIN = '''
  <!-- HERO -->
  <div class="stack-row" style="display:flex; gap:48px; padding:88px 64px 56px 64px; align-items:flex-start;">
    <div style="display:flex; flex-direction:column; gap:28px; flex:1.3; min-width:0; max-width:640px;">
      <div style="display:flex; align-items:center; gap:14px;">
        <div style="width:28px; height:1px; background:#BE7C3E;"></div>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">ธุรกิจหลักของเรา</span>
      </div>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:17px; font-weight:600; color:#1E3A28;">บริการตรวจสอบอาคาร ตาม พ.ร.บ. ควบคุมอาคาร พ.ศ. 2522</span>
      <h1 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:56px; line-height:1.2; color:#1E3A28;">ยกระดับความปลอดภัยอาคาร</h1>
      <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:17px; line-height:1.8; color:#4A564C; max-width:700px;">ไม่ใช่แค่การติกถูกในแบบฟอร์ม — เราตรวจสอบอาคารด้วยมุมมองของผู้ที่เคยจัดการงานวิศวกรรมอาคารใหญ่กว่า 100 โครงการ พร้อมรายงานที่นำไปวางแผนบำรุงรักษาได้จริง</p>
      <div style="display:flex; gap:16px; margin-top:8px; flex-wrap:wrap;">
        <a href="contact.html" class="btn-amber" style="background:#BE7C3E; color:#FFFFFF; padding:16px 28px; border-radius:4px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:15px; cursor:pointer; display:inline-flex; align-items:center; gap:8px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5 8.4 8.4 0 0 1-3.9-.94L3 20l1.05-5.4A8.5 8.5 0 1 1 21 11.5Z" stroke="#FFFFFF" stroke-width="1.6" stroke-linejoin="round"/></svg>
          ปรึกษาเราฟรี
        </a>
        <a href="services.html" class="btn-outline" style="background:transparent; color:#1E3A28; padding:16px 28px; border-radius:4px; border:1.4px solid #1E3A28; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:15px; cursor:pointer; display:inline-flex; align-items:center; gap:8px;">
          บริการของเรา
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
      </div>
    </div>
    <div style="flex:1; min-width:280px; max-width:380px; display:flex; flex-direction:column; gap:16px; padding:32px; background:#1E3A28; border-radius:10px; margin-top:6px;">
      <div class="badge-shine" style="display:inline-flex; align-items:center; gap:8px; width:fit-content; padding:7px 16px 7px 12px; border-radius:20px; border:1px solid rgba(190,124,62,0.55); background:rgba(190,124,62,0.12);">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M12 3a5 5 0 0 0-5 5v3.4c0 .9-.3 1.8-.9 2.5L4.5 16h15L18 13.9c-.6-.7-.9-1.6-.9-2.5V8a5 5 0 0 0-5-5Z" stroke="#BE7C3E" stroke-width="1.6" stroke-linejoin="round"/><path d="M9.5 19a2.5 2.5 0 0 0 5 0" stroke="#BE7C3E" stroke-width="1.6" stroke-linecap="round"/></svg>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#BE7C3E; text-transform:uppercase; white-space:nowrap;">ฟีเจอร์ใหม่ ·</span>
        <svg class="sparkle-mini" style="animation-delay:0s;" width="12" height="12" viewBox="0 0 24 24" fill="#F7F2E3"><path d="M12 0 14.5 9.5 24 12 14.5 14.5 12 24 9.5 14.5 0 12 9.5 9.5Z"/></svg>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#F7F2E3; text-transform:uppercase; font-weight:700; white-space:nowrap;">ไม่มีค่าใช้จ่าย</span>
        <svg class="sparkle-mini" style="animation-delay:0.9s;" width="10" height="10" viewBox="0 0 24 24" fill="#F7F2E3"><path d="M12 0 14.5 9.5 24 12 14.5 14.5 12 24 9.5 14.5 0 12 9.5 9.5Z"/></svg>
      </div>
      <h2 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:22px; color:#F7F2E3;">โปรแกรมเตือนตรวจสอบอาคาร</h2>
      <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; line-height:1.8; color:rgba(247,242,227,0.8);">ลงทะเบียนอาคารของท่านไว้กับเรา รับแจ้งเตือนล่วงหน้าทาง LINE และอีเมล ก่อนถึงกำหนดตรวจสอบทุกครั้ง ไม่ต้องกังวลว่าจะลืมหรือเลยกำหนดตามกฎหมายอีกต่อไป</p>
      <a href="reminder-program.html" class="btn-amber badge-shine" style="background:#BE7C3E; color:#FFFFFF; padding:13px 22px; border-radius:5px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; cursor:pointer; text-align:center; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px;">
        <span>ลงทะเบียนรับการแจ้งเตือน</span>
        <span style="display:inline-flex; align-items:center; gap:3px; color:#F7F2E3; font-weight:800; font-size:15px;">
          <svg class="sparkle-mini" style="animation-delay:0.4s;" width="12" height="12" viewBox="0 0 24 24" fill="#F7F2E3"><path d="M12 0 14.5 9.5 24 12 14.5 14.5 12 24 9.5 14.5 0 12 9.5 9.5Z"/></svg>
          ฟรี
        </span>
      </a>
    </div>
  </div>

  <!-- STATS -->
  <div class="hero-stats" style="display:flex; gap:64px; padding:36px 64px 72px 64px; border-top:1px solid #E4DCC8; margin:0 64px; width:calc(100% - 128px);">
    <div style="display:flex; flex-direction:column; gap:6px;">
      <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:40px; color:#BE7C3E;">100+</span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#4A564C;">โครงการอาคารใหญ่ที่ทีมเคยบริหาร</span>
    </div>
    <div style="display:flex; flex-direction:column; gap:6px;">
      <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:40px; color:#BE7C3E;">20+</span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#4A564C;">ปีประสบการณ์งานวิศวกรรมอาคาร</span>
    </div>
    <div style="display:flex; flex-direction:column; gap:6px;">
      <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:40px; color:#BE7C3E;">100%</span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#4A564C;">ขึ้นทะเบียนผู้ตรวจสอบกับ ก.ย.ผ.</span>
    </div>
  </div>

  <!-- ICON BAND -->
  <div class="icon-band" style="display:flex; background:#1E3A28; padding:32px 64px;">
    <div style="display:flex; align-items:center; gap:12px; flex:1;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 3 4 7v3c0 5 3.4 8.7 8 10 4.6-1.3 8-5 8-10V7l-8-4Z" stroke="#BE7C3E" stroke-width="1.6" stroke-linejoin="round"/></svg>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">ตรวจสอบตาม พ.ร.บ. ควบคุมอาคาร พ.ศ. 2522</span>
    </div>
    <div style="display:flex; align-items:center; gap:12px; flex:1;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="4" y="10" width="7" height="10" stroke="#BE7C3E" stroke-width="1.6"/><rect x="13" y="4" width="7" height="16" stroke="#BE7C3E" stroke-width="1.6"/></svg>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">เชี่ยวชาญอาคารชุด · คอนโด · อาคารสำนักงาน</span>
    </div>
    <div style="display:flex; align-items:center; gap:12px; flex:1;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M6 3h9l4 4v14H6z" stroke="#BE7C3E" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 12h7M9 16h7" stroke="#BE7C3E" stroke-width="1.4" stroke-linecap="round"/></svg>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">รายงานพร้อมส่งหน่วยงานราชการ</span>
    </div>
    <div style="display:flex; align-items:center; gap:12px; flex:1;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="#BE7C3E" stroke-width="1.6"/><path d="M12 7v5l3.2 2" stroke="#BE7C3E" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">ทีมพร้อมให้คำปรึกษาตลอด 24 ชม.</span>
    </div>
  </div>

  <!-- REMINDER PROGRAM BANNER -->
  <div class="stack-row" style="display:flex; align-items:center; justify-content:space-between; gap:48px; margin:80px 64px; padding:48px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
    <div style="display:flex; flex-direction:column; gap:16px; max-width:600px;">
      <div style="display:flex; align-items:center; gap:12px;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 3a5 5 0 0 0-5 5v3.4c0 .9-.3 1.8-.9 2.5L4.5 16h15L18 13.9c-.6-.7-.9-1.6-.9-2.5V8a5 5 0 0 0-5-5Z" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/><path d="M9.5 19a2.5 2.5 0 0 0 5 0" stroke="#1E3A28" stroke-width="1.6" stroke-linecap="round"/></svg>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:2px; color:#BE7C3E; text-transform:uppercase;">ฟีเจอร์ใหม่ · ไม่มีค่าใช้จ่าย</span>
      </div>
      <h2 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:30px; color:#1E3A28;">โปรแกรมเตือนตรวจสอบอาคาร</h2>
      <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:15px; line-height:1.8; color:#4A564C;">ลงทะเบียนอาคารของท่านไว้กับเรา ระบบจะแจ้งเตือนล่วงหน้าทาง LINE และอีเมล ก่อนถึงกำหนดตรวจสอบทุกครั้ง ไม่ต้องกังวลว่าจะลืมหรือเลยกำหนดตามกฎหมายอีกต่อไป</p>
    </div>
    <a href="reminder-program.html" class="btn-amber" style="background:#BE7C3E; color:#FFFFFF; padding:16px 28px; border-radius:4px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:15px; cursor:pointer; white-space:nowrap; display:inline-block;">ลงทะเบียนรับการแจ้งเตือนฟรี</a>
  </div>

  <!-- SERVICES TEASER -->
  <div style="display:flex; flex-direction:column; gap:40px; padding:40px 64px 96px 64px;">
    <div style="display:flex; flex-direction:column; gap:14px; align-items:center; text-align:center;">
      <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">บริการของเรา</span>
      <h2 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:32px; color:#1E3A28;">ครบทุกขั้นตอน ตั้งแต่ตรวจสอบจนถึงแก้ปัญหาจริง</h2>
    </div>
    <div class="grid-4">
      <a href="services.html#major-inspection" style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <div style="width:48px; height:48px; display:flex; align-items:center; justify-content:center; background:#F7F2E3; border-radius:6px;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 21V9l6-5 6 5v12" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/><path d="M14 21v-8l6 3v5" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/></svg>
        </div>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ตรวจสอบใหญ่อาคาร</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.6;">ตรวจสอบละเอียดทุก 5 ปี</span>
      </a>
      <a href="services.html#annual-inspection" style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <div style="width:48px; height:48px; display:flex; align-items:center; justify-content:center; background:#F7F2E3; border-radius:6px;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="4" y="5" width="16" height="16" rx="1" stroke="#1E3A28" stroke-width="1.6"/><path d="M4 10h16M8 3v4M16 3v4" stroke="#1E3A28" stroke-width="1.6" stroke-linecap="round"/></svg>
        </div>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ตรวจสอบประจำปี</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.6;">ติดตามสภาพอาคารต่อเนื่อง</span>
      </a>
      <a href="services.html#problem-analysis" style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <div style="width:48px; height:48px; display:flex; align-items:center; justify-content:center; background:#F7F2E3; border-radius:6px;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="#1E3A28" stroke-width="1.6"/><path d="M20 20l-4.3-4.3" stroke="#1E3A28" stroke-width="1.6" stroke-linecap="round"/></svg>
        </div>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">วิเคราะห์ปัญหาอาคาร</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.6;">หาสาเหตุที่แท้จริงก่อนลงทุน</span>
      </a>
      <a href="services.html#problem-fix" style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <div style="width:48px; height:48px; display:flex; align-items:center; justify-content:center; background:#F7F2E3; border-radius:6px;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M14.7 3.3 3.3 14.7a1 1 0 0 0 0 1.4l4.6 4.6a1 1 0 0 0 1.4 0L20.7 9.3a1 1 0 0 0 0-1.4l-4.6-4.6a1 1 0 0 0-1.4 0Z" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/><path d="M7 17l-3 3" stroke="#1E3A28" stroke-width="1.6" stroke-linecap="round"/></svg>
        </div>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">แก้ปัญหาอาคาร</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.6;">งานระบบ โครงสร้าง สถาปัตย์</span>
      </a>
    </div>
  </div>
'''

ABOUT_MAIN = '''
  <!-- INTRO -->
  <div style="display:flex; flex-direction:column; padding:80px 64px 48px 64px; gap:24px; max-width:820px;">
    <div style="display:flex; align-items:center; gap:14px;">
      <div style="width:28px; height:1px; background:#BE7C3E;"></div>
      <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">เกี่ยวกับเรา</span>
    </div>
    <h1 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:36px; line-height:1.4; color:#1E3A28;">"รายงานตรวจสอบอาคารที่ใช้งานได้จริง<br>ไม่ใช่แค่เอกสารเก็บเข้าตู้"</h1>
    <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:16px; line-height:1.9; color:#4A564C;">Empower Best Solution ก่อตั้งขึ้นจากมุมมองของทีมผู้บริหารงานวิศวกรรมอาคาร (Building Manager &amp; Chief Engineer) ที่เคยบริหารและดูแลโครงการขนาดใหญ่มาแล้วกว่า 100 โครงการ เราเข้าใจดีว่า "รายงานการตรวจสอบอาคารที่ดี" ต้องไม่ใช่แค่เอกสารหนาๆ ที่ทำส่งตามกฎหมายแล้วเก็บเข้าตู้ แต่ต้องเป็นเครื่องมือชี้เป้าปัญหาและแนวทางแก้ไขที่นำไปปฏิบัติได้จริง เราจึงตั้งใจนำประสบการณ์ตรงทั้งหมดจากสนามจริง มาช่วยนิติบุคคลและเจ้าของอาคารในการวางแผน แก้ไขปัญหาเชิงลึก และยกระดับมาตรฐานความปลอดภัยอย่างคุ้มค่าและยั่งยืน</p>
  </div>

  <!-- WHY CHOOSE US -->
  <div style="display:flex; flex-direction:column; gap:36px; padding:24px 64px 64px 64px;">
    <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">ทำไมต้อง Empower Best Solution</span>
    <div class="grid-2">

      <div style="display:flex; flex-direction:column; gap:16px; padding:32px; background:#1E3A28; border-radius:8px;">
        <div style="width:44px; height:44px; display:flex; align-items:center; justify-content:center; background:rgba(247,242,227,0.1); border-radius:6px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7Z" stroke="#F7F2E3" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="12" r="3" stroke="#F7F2E3" stroke-width="1.6"/></svg>
        </div>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#BE7C3E;">01 — THE MANAGER'S PERSPECTIVE</span>
        <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:19px; color:#F7F2E3;">มุมมองของผู้บริหารอาคาร</span>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:rgba(247,242,227,0.78);">ทีมเรามีประสบการณ์ตรงในตำแหน่ง Building Manager และ Chief Engineer ในอาคารใหญ่กว่า 100 โครงการ เราจึงตรวจสอบโดยมองภาพรวมของการบริหารอาคาร ไม่ใช่แค่ในมุมของผู้รับเหมาที่เข้ามาตรวจตามรายการ ทำให้วิเคราะห์ปัญหาได้ตรงจุดและเข้าใจข้อจำกัดของงานจริง</p>
      </div>

      <div style="display:flex; flex-direction:column; gap:16px; padding:32px; background:#1E3A28; border-radius:8px;">
        <div style="width:44px; height:44px; display:flex; align-items:center; justify-content:center; background:rgba(247,242,227,0.1); border-radius:6px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 3 4 6.5v5c0 5 3.4 8.9 8 10 4.6-1.1 8-5 8-10v-5L12 3Z" stroke="#F7F2E3" stroke-width="1.6" stroke-linejoin="round"/></svg>
        </div>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#BE7C3E;">02 — SAFETY &amp; POLICY DRIVEN</span>
        <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:19px; color:#F7F2E3;">ยกระดับความปลอดภัยสู่ระดับนโยบาย</span>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:rgba(247,242,227,0.78);">เราช่วยแปลผลการตรวจสอบให้กลายเป็นแผนงานและงบประมาณประจำปีที่ชัดเจน เพื่อให้คณะกรรมการนิติบุคคลและผู้บริหารอาคารนำไปกำหนดเป็นนโยบายความปลอดภัยได้อย่างมีทิศทาง ไม่ใช่แค่เอกสารที่ทำตามกฎหมายแล้วเก็บเข้าตู้</p>
      </div>

      <div style="display:flex; flex-direction:column; gap:16px; padding:32px; background:#1E3A28; border-radius:8px;">
        <div style="width:44px; height:44px; display:flex; align-items:center; justify-content:center; background:rgba(247,242,227,0.1); border-radius:6px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M2 9 12 4l10 5-10 5-10-5Z" stroke="#F7F2E3" stroke-width="1.6" stroke-linejoin="round"/><path d="M6 11.5V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-4.5" stroke="#F7F2E3" stroke-width="1.6" stroke-linejoin="round"/></svg>
        </div>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#BE7C3E;">03 — CONSULT &amp; COACHING</span>
        <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:19px; color:#F7F2E3;">ปรึกษาและสอนทีมช่างภายในของท่าน</span>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:rgba(247,242,227,0.78);">เราไม่เพียงแค่ตรวจแล้วจากไป แต่พร้อม Coach ทีมช่างประจำอาคารของท่านให้ดูแลรักษาระบบได้อย่างถูกต้อง เพื่อลดการพึ่งพาผู้รับเหมาภายนอกและประหยัดค่าใช้จ่ายระยะยาว</p>
      </div>

      <div style="display:flex; flex-direction:column; gap:16px; padding:32px; background:#1E3A28; border-radius:8px;">
        <div style="width:44px; height:44px; display:flex; align-items:center; justify-content:center; background:rgba(247,242,227,0.1); border-radius:6px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#F7F2E3" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#BE7C3E;">04 — FIELD-PROVEN ADVICE</span>
        <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:19px; color:#F7F2E3;">คำแนะนำที่ผ่านการพิสูจน์จากสนามจริง</span>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:rgba(247,242,227,0.78);">ทุกคำแนะนำของเรามาจากประสบการณ์จัดการอาคาร 100+ โครงการ เรารู้ว่าอะไรใช้ได้จริง อะไรคือความเสี่ยง เพื่อให้ท่านจัดลำดับความสำคัญและลงทุนได้อย่างคุ้มค่าที่สุด</p>
      </div>

    </div>
  </div>

  <!-- STATS BAND -->
  <div class="grid-4" style="background:#1E3A28; margin:0 64px 64px 64px; border-radius:8px; overflow:hidden; gap:0;">
    <div style="display:flex; flex-direction:column; gap:6px; padding:32px; border-right:1px solid rgba(247,242,227,0.12);">
      <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:34px; color:#F7F2E3;">100<span style="color:#BE7C3E;">+</span></span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:rgba(247,242,227,0.72);">อาคารใหญ่ที่ทีมเคยบริหารโดยตรง</span>
    </div>
    <div style="display:flex; flex-direction:column; gap:6px; padding:32px; border-right:1px solid rgba(247,242,227,0.12);">
      <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:34px; color:#F7F2E3;">20 <span style="color:#BE7C3E; font-size:20px;">ปี</span></span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:rgba(247,242,227,0.72);">ค่าเฉลี่ยประสบการณ์ทีมหลัก</span>
    </div>
    <div style="display:flex; flex-direction:column; gap:6px; padding:32px; border-right:1px solid rgba(247,242,227,0.12);">
      <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:34px; color:#F7F2E3;">9 <span style="color:#BE7C3E; font-size:20px;">ประเภท</span></span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:rgba(247,242,227,0.72);">อาคารตามกฎหมายที่เราตรวจสอบครบ</span>
    </div>
    <div style="display:flex; flex-direction:column; gap:6px; padding:32px;">
      <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:34px; color:#F7F2E3;">100<span style="color:#BE7C3E;">%</span></span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:rgba(247,242,227,0.72);">ผ่านการขึ้นทะเบียน ก.ย.ผ.</span>
    </div>
  </div>

  <!-- TEAM -->
  <div style="display:flex; flex-direction:column; gap:20px; padding:0 64px 96px 64px; max-width:820px;">
    <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">ทีมงานของเรา</span>
    <h2 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:28px; color:#1E3A28;">ทีมวิศวกรที่ผ่านสนามจริง</h2>
    <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:15px; line-height:1.9; color:#4A564C;">ทีมวิศวกรของเราขึ้นทะเบียนผู้ตรวจสอบอาคารกับคณะกรรมการควบคุมอาคาร (ก.ย.ผ.) ครบทุกคน และมีพื้นฐานตรงจากตำแหน่งผู้บริหารงานวิศวกรรมอาคาร ไม่ใช่แค่ผู้รับเหมาที่รับงานตรวจสอบเป็นครั้งคราว ทำให้เข้าใจปัญหาที่นิติบุคคลและเจ้าของอาคารต้องเผชิญในแต่ละวันอย่างแท้จริง</p>
  </div>
'''


REMINDER_MAIN = '''
  <!-- HERO -->
  <div class="stack-row" style="display:flex; align-items:center; gap:56px; padding:80px 64px 56px 64px;">
    <div style="display:flex; flex-direction:column; gap:24px; flex:1.1;">
      <div style="display:flex; align-items:center; gap:14px;">
        <div style="width:28px; height:1px; background:#BE7C3E;"></div>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">โปรแกรมเตือนตรวจสอบอาคาร · ไม่มีค่าใช้จ่าย</span>
      </div>
      <h1 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:44px; line-height:1.25; color:#1E3A28;">ไม่พลาดทุกรอบ<br>ตรวจสอบอาคาร</h1>
      <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:16px; line-height:1.85; color:#4A564C; max-width:520px;">ลงทะเบียนฟรี ระบบจะแจ้งเตือนล่วงหน้าให้ท่านทาง LINE และอีเมล ก่อนถึงกำหนดตรวจสอบทุกครั้ง พร้อมทีมงานพร้อมติดต่อเสนอราคาให้ทันเวลา ไม่ต้องกังวลว่าจะลืมหรือเลยกำหนดตามกฎหมายอีกต่อไป</p>
      <div style="display:flex; gap:28px; margin-top:8px; flex-wrap:wrap;">
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:24px; color:#BE7C3E;">90 / 60 / 45</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:#4A564C;">วันแจ้งเตือนล่วงหน้า</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:24px; color:#BE7C3E;">LINE + Email</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:#4A564C;">ช่องทางแจ้งเตือน</span>
        </div>
      </div>
    </div>
    <div style="flex:0.9; display:flex; align-items:center; justify-content:center;">
      <div style="width:100%; max-width:420px; padding:36px; background:#1E3A28; border-radius:10px; display:flex; flex-direction:column; gap:18px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 3a5 5 0 0 0-5 5v3.4c0 .9-.3 1.8-.9 2.5L4.5 16h15L18 13.9c-.6-.7-.9-1.6-.9-2.5V8a5 5 0 0 0-5-5Z" stroke="#BE7C3E" stroke-width="1.6" stroke-linejoin="round"/></svg>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:15px; color:#F7F2E3;">ตัวอย่างการแจ้งเตือน</span>
        </div>
        <div style="background:#F7F2E3; border-radius:8px; padding:18px; display:flex; flex-direction:column; gap:6px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:13px; color:#1E3A28;">Empower Best Solution</span>
          <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:13px; line-height:1.7; color:#4A564C;">แจ้งเตือน: คอนโด "เดอะ ริเวอร์ไซด์" ใกล้ครบกำหนดตรวจสอบประจำปี (ร.1 หมดอายุ 15 พ.ย. 2569) เหลืออีก 60 วัน — ติดต่อทีมงานเพื่อขอใบเสนอราคาได้แล้ววันนี้</p>
        </div>
        <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1px; color:rgba(247,242,227,0.5);">ตัวอย่างข้อมูลสมมติ · Sample data</span>
      </div>
    </div>
  </div>

  <!-- HOW IT WORKS -->
  <div style="display:flex; flex-direction:column; gap:36px; padding:32px 64px 72px 64px;">
    <div style="display:flex; flex-direction:column; gap:14px; align-items:center; text-align:center;">
      <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">ขั้นตอนการทำงาน</span>
      <h2 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:30px; color:#1E3A28;">ลงทะเบียนครั้งเดียว ไม่ต้องจำวันตรวจสอบอีกเลย</h2>
    </div>
    <div class="grid-4">
      <div style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">STEP / 01</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ลงทะเบียนข้อมูลอาคาร</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.7;">กรอกชื่ออาคาร รอบตรวจสอบ และวันหมดอายุของ อ.6 หรือ ร.1</span>
      </div>
      <div style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">STEP / 02</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ยืนยันตัวตนด้วย LINE</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.7;">เพิ่มเพื่อน LINE OA อัตโนมัติในคลิกเดียว เพื่อรับการแจ้งเตือน</span>
      </div>
      <div style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">STEP / 03</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">รับการแจ้งเตือนล่วงหน้า</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.7;">แจ้งเตือนทาง LINE และอีเมล ล่วงหน้า 90 / 60 / 45 วันก่อนครบกำหนด</span>
      </div>
      <div style="display:flex; flex-direction:column; gap:14px; padding:28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">STEP / 04</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ทีมงานติดต่อกลับ</span>
        <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C; line-height:1.7;">เราติดต่อประเมินขอบเขตงานและจัดทำใบเสนอราคาให้ฟรี</span>
      </div>
    </div>
  </div>

  <!-- CHOOSE PATH -->
  <div style="display:flex; flex-direction:column; gap:28px; padding:0 64px 72px 64px;">
    <div style="display:flex; flex-direction:column; gap:10px; align-items:center; text-align:center;">
      <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">เลือกวิธีลงทะเบียน</span>
      <h2 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:26px; color:#1E3A28;">อยากรับแจ้งเตือนผ่านช่องทางไหน?</h2>
    </div>
    <div class="grid-2">
      <div style="display:flex; flex-direction:column; gap:16px; padding:32px; background:#1E3A28; border-radius:10px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 3a5 5 0 0 0-5 5v3.4c0 .9-.3 1.8-.9 2.5L4.5 16h15L18 13.9c-.6-.7-.9-1.6-.9-2.5V8a5 5 0 0 0-5-5Z" stroke="#BE7C3E" stroke-width="1.6" stroke-linejoin="round"/></svg>
          <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:2px; color:#BE7C3E; text-transform:uppercase;">แนะนำ · รับแจ้งเตือนทาง LINE ด้วย</span>
        </div>
        <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:20px; color:#F7F2E3;">ลงทะเบียนผ่าน LINE</h3>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; line-height:1.8; color:rgba(247,242,227,0.8);">ขั้นตอนที่ 1 เพิ่มเพื่อน LINE OA ก่อน จากนั้นกดปุ่ม "ลงทะเบียนอาคาร" ในแชท LINE เพื่อกรอกข้อมูล รับแจ้งเตือนทั้งทาง LINE และอีเมล</p>

        <div id="line-step1-mobile" style="display:none; flex-direction:column; gap:8px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:#BE7C3E; font-weight:600;">ขั้นตอนที่ 1</span>
          <a href="https://line.me/R/ti/p/%40911hrhms" target="_blank" rel="noopener" style="display:flex; align-items:center; justify-content:center; gap:8px; background:#06C755; color:#FFFFFF; padding:14px 24px; border-radius:5px; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; text-decoration:none;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M12 3a5 5 0 0 0-5 5v3.4c0 .9-.3 1.8-.9 2.5L4.5 16h15L18 13.9c-.6-.7-.9-1.6-.9-2.5V8a5 5 0 0 0-5-5Z" stroke="#FFFFFF" stroke-width="1.6" stroke-linejoin="round"/></svg>
            เพิ่มเพื่อน LINE OA @911hrhms
          </a>
        </div>
        <div id="line-step1-desktop" style="display:none; flex-direction:column; align-items:center; gap:10px; background:#F7F2E3; border-radius:8px; padding:20px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:#BE7C3E; font-weight:600; align-self:flex-start;">ขั้นตอนที่ 1</span>
          <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAAE2CAIAAABk3in+AAAF60lEQVR4nO3dMW5bORRA0fEg+5h61pD1Zw2pZyV/2qShEDD0u1TOaQ1blvQv2Dw8fjzP8xdQ9ff0PwCsSBTSJAppEoU0iUKaRCFNopAmUUiTKKR9Wf/4n6//fs7/8Wn++/Z98dP1+13/7o5zr7vzDZ77rM797o3W79cpCmkShTSJQppEIU2ikCZRSJMopEkU0iQKaS+mi9bOTdvsmJqnOWfqHZ17v+eenPd7Jp2ikCZRSJMopEkU0iQKaRKFNIlCmkQhTaKQtjVdtHbjbMrUTp1z24mmvoWpT2PtxmfSKQppEoU0iUKaRCFNopAmUUiTKKRJFNIkCmkHp4tu1Lw3bceNt6rxI6copEkU0iQKaRKFNIlCmkQhTaKQJlFIkyikmS66wM4szrmJqJ2/3JzEanKKQppEIU2ikCZRSJMopEkU0iQKaRKFNIlC2sHpohsnSKbmeKZmgNbO7R+a2gJ14zPpFIU0iUKaRCFNopAmUUiTKKRJFNIkCmkShbSt6aI/7X6r5m1fzammKe/3TDpFIU2ikCZRSJMopEkU0iQKaRKFNIlCmkQh7eN5nun/gS3n5mmmpqlunGo6xykKaRKFNIlCmkQhTaKQJlFIkyikSRTSJAppL3YX3bgX59xdYDuv+363mzVfd+pbONeCUxTSJAppEoU0iUKaRCFNopAmUUiTKKRJFNK2dhc1Z1Oa95dNMcX1Oc59Gk5RSJMopEkU0iQKaRKFNIlCmkQhTaKQJlFIO7i7aEpz5mnnL++Y2rjTvDftxmfDKQppEoU0iUKaRCFNopAmUUiTKKRJFNIkCmkvpotunCBpTp/smJrxmvoW1qbuiZv6NJyikCZRSJMopEkU0iQKaRKFNIlCmkQhTaKQ9mK6aK05qzG1Q+hPu5FtaivSOc0NUk5RSJMopEkU0iQKaRKFNIlCmkQhTaKQJlFIe8Ob0aamfJqbb9bO/c/vN021du79OkUhTaKQJlFIkyikSRTSJAppEoU0iUKaRCFt62a0Hec236zduFNn6ga65oRQ838+9185RSFNopAmUUiTKKRJFNIkCmkShTSJQppEIe3jeZ6RF566V+vG+aH3+zSm5sN2/vIUpyikSRTSJAppEoU0iUKaRCFNopAmUUiTKKRt3Yw2pTkxs6O5j2dtao7nxvmhnWfSKQppEoU0iUKaRCFNopAmUUiTKKRJFNIkCmlbu4tunPNYm7qDbK05XXROczvR1LPhFIU0iUKaRCFNopAmUUiTKKRJFNIkCmkShbSDu4tu3BMzdQfZWnMmZse5Z+P9vgWnKKRJFNIkCmkShTSJQppEIU2ikCZRSJMopG3tLlo7N4tzbjalOT/UvOttam7p3JRPc5+WUxTSJAppEoU0iUKaRCFNopAmUUiTKKRJFNJeTBfdODEz9ZfXbtyp09zkNGXqeXaKQppEIU2ikCZRSJMopEkU0iQKaRKFNIlC2oub0aZusJr6y82pl/d7R2tTu6l2fvfc7JFTFNIkCmkShTSJQppEIU2ikCZRSJMopEkU0l5MF904m7J24z1iU99C89s/tyXIzWjAL5MopEkU0iQKaRKFNIlCmkQhTaKQJlFIezFdtNacxmjeMuZ1f5fmU3eOUxTSJAppEoU0iUKaRCFNopAmUUiTKKRJFNK2povWzk2f3Lh/6MY5nh3vt6tp5+6zHU5RSJMopEkU0iQKaRKFNIlCmkQhTaKQJlFIOzhdxI92JlfOzbVM3TJ27nXXpj6rndd1ikKaRCFNopAmUUiTKKRJFNIkCmkShTSJQprpop80twQ1d/lM/e652aPmfimnKKRJFNIkCmkShTSJQppEIU2ikCZRSJMopH08z7P48dScx47mXpxzu3ya73ft3KafcxNCU0+7UxTSJAppEoU0iUKaRCFNopAmUUiTKKRJFNK2dhc1N/3saG7NOfc5n7uv7dzr3mjn/TpFIU2ikCZRSJMopEkU0iQKaRKFNIlCmkQh7cXuImCWUxTSJAppEoU0iUKaRCFNopAmUUiTKKRJFNL+B/uQIaUGkzgRAAAAAElFTkSuQmCC" width="150" height="150" alt="QR code เพิ่มเพื่อน LINE OA @911hrhms" style="border-radius:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12.5px; color:#1E3A28; text-align:center;">สแกนด้วยมือถือเพื่อเพิ่มเพื่อน LINE OA @911hrhms</span>
        </div>

        <div style="display:flex; flex-direction:column; gap:8px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:#BE7C3E; font-weight:600;">ขั้นตอนที่ 2</span>
          <div style="display:flex; align-items:center; justify-content:center; gap:8px; background:rgba(247,242,227,0.08); border:1.4px dashed rgba(247,242,227,0.35); padding:13px 20px; border-radius:5px; text-align:center;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M8 12h8M8 8h8M8 16h5" stroke="#F7F2E3" stroke-width="1.6" stroke-linecap="round"/><rect x="3" y="4" width="18" height="16" rx="2" stroke="#F7F2E3" stroke-width="1.6"/></svg>
            <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:13.5px; color:#F7F2E3;">เปิดแชท Empower Best Solution ใน LINE แล้วกด "ลงทะเบียนอาคาร"</span>
          </div>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:11.5px; color:rgba(247,242,227,0.55); text-align:center;">เพิ่มเพื่อนแล้ว ระบบจะส่งข้อความต้อนรับพร้อมปุ่มลงทะเบียนให้อัตโนมัติ</span>
        </div>
      </div>
      <div style="display:flex; flex-direction:column; gap:16px; padding:32px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:10px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2" stroke="#1E3A28" stroke-width="1.6"/><path d="M3 7l9 6 9-6" stroke="#1E3A28" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:2px; color:#BE7C3E; text-transform:uppercase;">ทางเลือก · อีเมลเท่านั้น</span>
        </div>
        <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:20px; color:#1E3A28;">ลงทะเบียนผ่านเว็บไซต์</h3>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; line-height:1.8; color:#4A564C;">กรอกฟอร์มด้านล่าง เหมาะสำหรับคนที่ไม่สะดวกใช้ LINE รับแจ้งเตือนทางอีเมลเท่านั้น</p>
        <a href="#reminder-form" style="margin-top:6px; display:flex; align-items:center; justify-content:center; gap:8px; background:transparent; color:#1E3A28; border:1.4px solid #1E3A28; padding:14px 24px; border-radius:5px; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; text-decoration:none;">
          กรอกฟอร์มด้านล่าง
        </a>
      </div>
    </div>
  </div>
  <script>
  (function () {
    var isMobile = /Android|iPhone|iPad|iPod|Mobi/i.test(navigator.userAgent);
    var mobileEl = document.getElementById('line-step1-mobile');
    var desktopEl = document.getElementById('line-step1-desktop');
    if (isMobile) {
      if (mobileEl) mobileEl.style.display = 'flex';
    } else {
      if (desktopEl) desktopEl.style.display = 'flex';
    }
  })();
  </script>

  <!-- FORM -->
  <div class="stack-row" style="display:flex; gap:56px; padding:0 64px 72px 64px;">
    <form id="reminder-form" name="reminder-registration" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thank-you-reminder.html" style="flex:1; display:flex; flex-direction:column; gap:20px; padding:44px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:10px;">
      <input type="hidden" name="form-name" value="reminder-registration">
      <p class="hidden-field"><label>อย่ากรอกช่องนี้ถ้าท่านเป็นมนุษย์: <input name="bot-field"></label></p>
      <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:22px; color:#1E3A28;">ลงทะเบียนรับการแจ้งเตือนฟรี</h3>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12.5px; color:#4A564C; line-height:1.7;">ฟอร์มนี้รับแจ้งเตือนทางอีเมลเท่านั้น หากต้องการรับแจ้งเตือนผ่าน LINE ด้วย แนะนำให้เลือก "ลงทะเบียนผ่าน LINE" ด้านบนแทน</span>
      <div class="form-grid" style="display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:16px;">
        <div style="display:flex; flex-direction:column; gap:6px;">
          <label for="r-name" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">ชื่อ-นามสกุล</label>
          <input id="r-name" name="name" type="text" required placeholder="ชื่อ-นามสกุลของท่าน" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <label for="r-phone" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">เบอร์โทรศัพท์</label>
          <input id="r-phone" name="phone" type="tel" required placeholder="08X-XXX-XXXX" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; grid-column:span 2;">
          <label for="r-email" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">อีเมล</label>
          <input id="r-email" name="email" type="email" required placeholder="name@example.com" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; grid-column:span 2;">
          <label for="r-building" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">ชื่ออาคาร</label>
          <input id="r-building" name="building_name" type="text" required placeholder="เช่น คอนโด เดอะ ริเวอร์ไซด์" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <label for="r-type" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">ประเภทอาคาร</label>
          <select id="r-type" name="building_type" required style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
            <option value="" selected disabled>เลือกประเภทอาคาร (ตามมาตรา 32 ทวิ)</option>
            <option value="อาคารสูง (≥ 23 เมตร)">อาคารสูง (≥ 23 เมตร)</option>
            <option value="อาคารขนาดใหญ่พิเศษ (≥ 10,000 ตร.ม.)">อาคารขนาดใหญ่พิเศษ (≥ 10,000 ตร.ม.)</option>
            <option value="อาคารชุมนุมคน (≥ 1,000 ตร.ม. หรือ ≥ 500 คน)">อาคารชุมนุมคน (≥ 1,000 ตร.ม. หรือ ≥ 500 คน)</option>
            <option value="โรงมหรสพ">โรงมหรสพ</option>
            <option value="โรงแรม ตั้งแต่ 80 ห้องขึ้นไป">โรงแรม ตั้งแต่ 80 ห้องขึ้นไป</option>
            <option value="อาคารชุด / อยู่อาศัยรวม ≥ 2,000 ตร.ม.">อาคารชุด / อยู่อาศัยรวม ≥ 2,000 ตร.ม.</option>
            <option value="โรงงาน ≥ 5,000 ตร.ม.">โรงงาน ≥ 5,000 ตร.ม.</option>
            <option value="ป้าย สูงหรือกว้าง ≥ 15 เมตร">ป้าย สูงหรือกว้าง ≥ 15 เมตร</option>
            <option value="สถานบริการ ≥ 200 ตร.ม.">สถานบริการ ≥ 200 ตร.ม.</option>
            <option value="อื่นๆ">อื่นๆ</option>
          </select>
        </div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <label for="r-expiry" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">วันหมดอายุ อ.6 / ร.1</label>
          <input id="r-expiry" name="expiry_date" type="date" required style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
      </div>
      <button type="submit" class="btn-amber" style="margin-top:6px; background:#BE7C3E; color:#FFFFFF; padding:15px 24px; border-radius:5px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:15px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 3C6.5 3 2 6.6 2 11c0 2.8 1.8 5.3 4.6 6.8L6 21l3.7-1.9c.7.1 1.5.2 2.3.2 5.5 0 10-3.6 10-8s-4.5-8.3-10-8.3Z" stroke="#FFFFFF" stroke-width="1.6" stroke-linejoin="round"/></svg>
        ลงทะเบียนรับการแจ้งเตือน
      </button>
      <span id="reminder-status" role="status" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; text-align:center;"></span>
    </form>
    <script>
    (function () {
      var form = document.getElementById('reminder-form');
      if (!form) return;
      var statusEl = document.getElementById('reminder-status');
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var btn = form.querySelector('button[type="submit"]');
        var data = {
          name: form.querySelector('#r-name').value,
          phone: form.querySelector('#r-phone').value,
          email: form.querySelector('#r-email').value,
          building_name: form.querySelector('#r-building').value,
          building_type: form.querySelector('#r-type').value,
          expiry_date: form.querySelector('#r-expiry').value
        };
        if (btn) btn.disabled = true;
        if (statusEl) {
          statusEl.style.color = '#4A564C';
          statusEl.textContent = 'กำลังส่งข้อมูล...';
        }
        fetch('/.netlify/functions/register-building', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        })
          .then(function (res) {
            return res.json().then(function (body) {
              return { ok: res.ok, body: body };
            });
          })
          .then(function (result) {
            if (result.ok) {
              window.location.href = '/thank-you-reminder.html?email=' + encodeURIComponent(data.email);
            } else {
              if (btn) btn.disabled = false;
              if (statusEl) {
                statusEl.style.color = '#B3423A';
                statusEl.textContent =
                  (result.body && result.body.error) || 'เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง';
              }
            }
          })
          .catch(function () {
            if (btn) btn.disabled = false;
            if (statusEl) {
              statusEl.style.color = '#B3423A';
              statusEl.textContent = 'เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง';
            }
          });
      });
    })();
    </script>

    <div style="flex:0.6; display:flex; flex-direction:column; gap:20px;">
      <div style="display:flex; gap:14px; align-items:flex-start; padding:22px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M4 4h16v13H8l-4 4Z" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">ไม่มีค่าใช้จ่าย</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ลงทะเบียนและรับแจ้งเตือนได้ฟรีตลอด</span>
        </div>
      </div>
      <div style="display:flex; gap:14px; align-items:flex-start; padding:22px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M4 13.5 9 18l11-12" stroke="#1E3A28" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">แก้ไขข้อมูลได้ทุกเมื่อ</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ติดต่อทีมงานทาง LINE เพื่ออัปเดตรอบตรวจปีถัดไป</span>
        </div>
      </div>
      <div style="display:flex; gap:14px; align-items:flex-start; padding:22px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><circle cx="12" cy="12" r="9" stroke="#1E3A28" stroke-width="1.6"/><path d="M9 9l6 6M15 9l-6 6" stroke="#1E3A28" stroke-width="1.6" stroke-linecap="round"/></svg>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">ยกเลิกได้ทุกเมื่อ</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ยกเลิกรับแจ้งเตือนได้จากลิงก์ท้ายอีเมล/LINE</span>
        </div>
      </div>
      <div style="display:flex; gap:14px; align-items:flex-start; padding:22px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M12 3 4 6v5c0 5 3.4 8.7 8 10 4.6-1.3 8-5 8-10V6l-8-3Z" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">ข้อมูลปลอดภัยตาม PDPA</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ใช้เพื่อแจ้งเตือนและติดต่อเสนอราคาเท่านั้น</span>
        </div>
      </div>
    </div>
  </div>
'''


SERVICES_MAIN = '''
  <!-- HERO -->
  <div style="display:flex; flex-direction:column; gap:18px; padding:72px 64px 48px 64px; max-width:760px;">
    <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">บริการของเรา</span>
    <h1 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:34px; line-height:1.4; color:#1E3A28;">บริการตรวจสอบอาคารตามข้อกำหนดของ พ.ร.บ. ควบคุมอาคาร</h1>
    <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:15px; line-height:1.8; color:#4A564C;">เราให้บริการตรวจสอบอาคารตามที่กฎหมายกำหนด ทั้งการตรวจสอบใหญ่ทุก 5 ปีและตรวจสอบประจำปี พร้อมรายงานส่งหน่วยงานราชการได้ทันที และต่อยอดไปถึงการวิเคราะห์และแก้ปัญหาอาคารเชิงลึกสำหรับผู้ที่ต้องการมากกว่ารายงาน</p>
  </div>

  <!-- ZONE 1: LEGAL SERVICES -->
  <div style="display:flex; flex-direction:column; gap:28px; padding:16px 64px 56px 64px;">
    <div style="display:flex; align-items:center; gap:12px;">
      <div style="width:8px; height:8px; border-radius:50%; background:#1E3A28;"></div>
      <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:2px; color:#1E3A28; text-transform:uppercase;">บริการตามกฎหมาย</span>
    </div>
    <div class="grid-2">

      <div id="major-inspection" style="display:flex; flex-direction:column; gap:18px; padding:36px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px; scroll-margin-top:24px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">/ 01</span>
        <div style="width:52px; height:52px; display:flex; align-items:center; justify-content:center; background:#F7F2E3; border-radius:6px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M4 21V9l6-5 6 5v12" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/><path d="M14 21v-8l6 3v5" stroke="#1E3A28" stroke-width="1.6" stroke-linejoin="round"/></svg>
        </div>
        <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:21px; color:#1E3A28;">ตรวจสอบใหญ่อาคาร</h3>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:#4A564C;">การตรวจสอบสภาพอาคารโดยละเอียดทุก 5 ปี ครอบคลุมโครงสร้าง ระบบประกอบอาคาร และระบบความปลอดภัย พร้อมรายงานฉบับสมบูรณ์ส่งกรมโยธาธิการฯ</p>
        <div style="display:flex; flex-direction:column; gap:10px; border-top:1px solid #E4DCC8; padding-top:18px;">
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ตรวจโครงสร้าง ระบบไฟฟ้า ระบบสุขาภิบาล</span></div>
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ตรวจระบบป้องกันและระงับอัคคีภัย</span></div>
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ตรวจระบบบริหารจัดการเพื่อความปลอดภัย</span></div>
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">รายงานพร้อมยื่นต่อเจ้าพนักงานท้องถิ่น</span></div>
        </div>
        <a href="contact.html" style="display:flex; align-items:center; gap:6px; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; color:#1E3A28; margin-top:6px;">ขอใบเสนอราคา <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>

      <div id="annual-inspection" style="display:flex; flex-direction:column; gap:18px; padding:36px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px; scroll-margin-top:24px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">/ 02</span>
        <div style="width:52px; height:52px; display:flex; align-items:center; justify-content:center; background:#F7F2E3; border-radius:6px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><rect x="4" y="5" width="16" height="16" rx="1" stroke="#1E3A28" stroke-width="1.6"/><path d="M4 10h16M8 3v4M16 3v4" stroke="#1E3A28" stroke-width="1.6" stroke-linecap="round"/></svg>
        </div>
        <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:21px; color:#1E3A28;">ตรวจสอบประจำปี</h3>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:#4A564C;">การตรวจสอบประจำปีในปีที่ 1, 2, 3, 4 หลังจากตรวจใหญ่ เน้นการติดตามสภาพอาคารและระบบที่มีความเสี่ยงสูง ให้เป็นไปตามมาตรฐานต่อเนื่อง</p>
        <div style="display:flex; flex-direction:column; gap:10px; border-top:1px solid #E4DCC8; padding-top:18px;">
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ตรวจตามรายการที่กฎกระทรวงกำหนด</span></div>
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">เปรียบเทียบสภาพกับการตรวจครั้งก่อน</span></div>
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">ข้อเสนอแนะการบำรุงรักษาเชิงป้องกัน</span></div>
          <div style="display:flex; gap:10px; align-items:center;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="#BE7C3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#4A564C;">รายงานสรุปพร้อม Action Plan</span></div>
        </div>
        <a href="contact.html" style="display:flex; align-items:center; gap:6px; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; color:#1E3A28; margin-top:6px;">ขอใบเสนอราคา <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>

    </div>
  </div>

  <!-- ZONE 2: VALUE-ADDED SERVICES -->
  <div style="display:flex; flex-direction:column; gap:28px; padding:16px 64px 96px 64px;">
    <div style="display:flex; align-items:center; gap:12px;">
      <div style="width:8px; height:8px; border-radius:50%; background:#BE7C3E;"></div>
      <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:2px; color:#BE7C3E; text-transform:uppercase;">บริการเสริม · แก้ปัญหาเชิงลึก</span>
    </div>
    <div class="grid-2">

      <div id="problem-analysis" style="display:flex; flex-direction:column; gap:18px; padding:36px; background:#1E3A28; border-radius:8px; scroll-margin-top:24px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">/ 03</span>
        <div style="width:52px; height:52px; display:flex; align-items:center; justify-content:center; background:rgba(247,242,227,0.1); border-radius:6px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="#F7F2E3" stroke-width="1.6"/><path d="M20 20l-4.3-4.3" stroke="#F7F2E3" stroke-width="1.6" stroke-linecap="round"/></svg>
        </div>
        <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:21px; color:#F7F2E3;">รับวิเคราะห์ปัญหาอาคาร</h3>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:rgba(247,242,227,0.78);">ให้คำปรึกษาเจาะลึกปัญหาที่พบระหว่างหรือหลังการตรวจสอบ ไม่ว่าจะเป็นรอยร้าวโครงสร้าง การทรุดตัว ระบบไฟฟ้า-ดับเพลิงทำงานผิดปกติ หรือปัญหาน้ำรั่วซึม เพื่อหาสาเหตุที่แท้จริงก่อนตัดสินใจลงทุนแก้ไข</p>
        <div style="display:flex; align-items:center; gap:14px; background:rgba(247,242,227,0.08); border-radius:6px; padding:16px; margin-top:4px;">
          <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:26px; color:#BE7C3E;">-70%</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12.5px; line-height:1.6; color:rgba(247,242,227,0.75);">Downtime ลิฟต์ลดลง ภายใน 6 เดือนแรก จากการเปลี่ยนมาใช้ Predictive Maintenance*</span>
        </div>
        <a href="contact.html" style="display:flex; align-items:center; gap:6px; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; color:#F7F2E3; margin-top:6px;">ขอคำปรึกษา <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>

      <div id="problem-fix" style="display:flex; flex-direction:column; gap:18px; padding:36px; background:#1E3A28; border-radius:8px; scroll-margin-top:24px;">
        <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#BE7C3E;">/ 04</span>
        <div style="width:52px; height:52px; display:flex; align-items:center; justify-content:center; background:rgba(247,242,227,0.1); border-radius:6px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M14.7 3.3 3.3 14.7a1 1 0 0 0 0 1.4l4.6 4.6a1 1 0 0 0 1.4 0L20.7 9.3a1 1 0 0 0 0-1.4l-4.6-4.6a1 1 0 0 0-1.4 0Z" stroke="#F7F2E3" stroke-width="1.6" stroke-linejoin="round"/><path d="M7 17l-3 3" stroke="#F7F2E3" stroke-width="1.6" stroke-linecap="round"/></svg>
        </div>
        <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:21px; color:#F7F2E3;">รับแก้ปัญหาอาคาร</h3>
        <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:rgba(247,242,227,0.78);">ดำเนินการแก้ไขปัญหาที่วิเคราะห์แล้วครบทั้ง 3 ด้าน งานระบบ (ไฟฟ้า ประปา ดับเพลิง ลิฟต์) งานโครงสร้าง และงานสถาปัตยกรรม โดยทีมที่เข้าใจทั้งการบริหารและการซ่อมบำรุงอาคารจริง</p>
        <div style="display:flex; align-items:center; gap:14px; background:rgba(247,242,227,0.08); border-radius:6px; padding:16px; margin-top:4px;">
          <span style="font-family:'Noto Serif Thai',serif; font-weight:700; font-size:26px; color:#BE7C3E;">-22%</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12.5px; line-height:1.6; color:rgba(247,242,227,0.75);">ค่าไฟส่วนกลาง จากการติดตั้ง VFD และจัดตารางเดินปั๊มตาม Peak/Off-peak คืนทุนใน 14 เดือน*</span>
        </div>
        <a href="contact.html" style="display:flex; align-items:center; gap:6px; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; color:#F7F2E3; margin-top:6px;">ขอใบเสนอราคา <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>

    </div>
    <span style="font-family:'Noto Sans Thai',sans-serif; font-size:12px; color:#4A564C;">*ข้อมูลจากโครงการจริงที่ทีมงานเคยให้คำปรึกษา รายละเอียดเฉพาะของลูกค้าได้รับการปิดบังเพื่อรักษาความลับ</span>
  </div>
'''


LEGAL_MAIN = '''
  <!-- HERO -->
  <div style="display:flex; flex-direction:column; gap:18px; padding:72px 64px 48px 64px; max-width:760px;">
    <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">ความรู้ตามกฎหมาย</span>
    <h1 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:34px; line-height:1.4; color:#1E3A28;">ทำความเข้าใจ พ.ร.บ. ควบคุมอาคาร ก่อนถูกปรับ</h1>
    <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:15px; line-height:1.8; color:#4A564C;">รวมความรู้ที่เจ้าของอาคารและนิติบุคคลควรรู้ เกี่ยวกับข้อกำหนดการตรวจสอบอาคารตามกฎหมาย เพื่อให้วางแผนได้ทันก่อนถึงกำหนด</p>
  </div>

  <!-- 9 BUILDING TYPES -->
  <div style="margin:16px 64px 56px 64px; padding:44px; background:#1E3A28; border-radius:10px;">
    <div style="display:inline-block; padding:6px 14px; border:1px solid rgba(190,124,62,0.5); border-radius:4px; margin-bottom:20px;">
      <span style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:1.5px; color:#BE7C3E;">พ.ร.บ. ควบคุมอาคาร พ.ศ. 2522</span>
    </div>
    <h2 style="margin:0 0 10px 0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:26px; color:#F7F2E3;">9 ประเภทอาคาร ที่กฎหมายกำหนดให้ตรวจสอบ</h2>
    <p style="margin:0 0 28px 0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:rgba(247,242,227,0.75); max-width:700px;">หากอาคารของท่านเข้าข่ายต่อไปนี้ จะต้องจัดให้มีการตรวจสอบและรายงานต่อเจ้าพนักงานท้องถิ่น</p>
    <div class="grid-3" style="gap:1px; background:rgba(247,242,227,0.12); border-radius:6px; overflow:hidden;">
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">อาคารสูง (ตั้งแต่ 23 เมตรขึ้นไป)</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">อาคารขนาดใหญ่พิเศษ (≥ 10,000 ตร.ม.)</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">อาคารชุมนุมคน (≥ 1,000 ตร.ม. หรือ ≥ 500 คน)</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">โรงมหรสพ</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">โรงแรม ตั้งแต่ 80 ห้องขึ้นไป</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">อาคารชุด / อยู่อาศัยรวม ≥ 2,000 ตร.ม.</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">โรงงาน ≥ 5,000 ตร.ม.</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">ป้าย สูงหรือกว้าง ≥ 15 เมตร</span></div>
      <div style="display:flex; align-items:center; gap:10px; padding:18px 20px; background:#1E3A28;"><div style="width:5px; height:5px; border-radius:50%; background:#BE7C3E; flex-shrink:0;"></div><span style="font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#F7F2E3;">สถานบริการ ≥ 200 ตร.ม.</span></div>
    </div>
  </div>

  <!-- FAQ -->
  <div style="display:flex; flex-direction:column; gap:24px; padding:16px 64px 64px 64px;">
    <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">คำถามที่พบบ่อย</span>
    <div style="display:flex; flex-direction:column; gap:16px; max-width:880px;">

      <details style="padding:26px 28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <summary style="cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">อาคารชุด / คอนโดของผม ต้องตรวจสอบไหม?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="flex-shrink:0; margin-left:12px;"><path d="M6 9l6 6 6-6" stroke="#BE7C3E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <p style="margin:14px 0 0 0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:#4A564C;">อาคารชุดหรืออาคารที่ใช้เป็นที่อยู่อาศัยรวม ที่มีพื้นที่รวมกันตั้งแต่ 2,000 ตารางเมตรขึ้นไป เข้าข่ายต้องตรวจสอบตามกฎหมาย ท่านสามารถส่งข้อมูลอาคารมาให้เราประเมินเบื้องต้นได้ฟรี</p>
      </details>

      <details style="padding:26px 28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <summary style="cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ต้องตรวจสอบบ่อยแค่ไหน?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="flex-shrink:0; margin-left:12px;"><path d="M6 9l6 6 6-6" stroke="#BE7C3E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <p style="margin:14px 0 0 0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:#4A564C;">อาคารควบคุมต้องได้รับการตรวจสอบใหญ่ทุก 5 ปี และตรวจสอบประจำปีในปีที่ไม่ตรงกับรอบตรวจใหญ่ เพื่อติดตามสภาพอาคารอย่างต่อเนื่อง</p>
      </details>

      <details style="padding:26px 28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <summary style="cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ถ้าไม่ตรวจสอบ มีบทลงโทษอย่างไร?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="flex-shrink:0; margin-left:12px;"><path d="M6 9l6 6 6-6" stroke="#BE7C3E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <p style="margin:14px 0 0 0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:#4A564C;">อาคารที่ไม่ยื่นรายงานการตรวจสอบตามกำหนด อาจมีความผิดตาม พ.ร.บ. ควบคุมอาคาร ทั้งโทษปรับและอาจกระทบต่อการต่ออายุใบอนุญาตใช้อาคาร [ระบุอัตราโทษที่แน่นอนตามกฎหมายฉบับล่าสุด]</p>
      </details>

      <details style="padding:26px 28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <summary style="cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ขั้นตอนการทำงานของ Empower Best Solution เป็นอย่างไร?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="flex-shrink:0; margin-left:12px;"><path d="M6 9l6 6 6-6" stroke="#BE7C3E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <p style="margin:14px 0 0 0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:#4A564C;">เริ่มจากประเมินอาคารเบื้องต้นและเสนอราคา ตรวจสอบหน้างานโดยทีมวิศวกรที่ขึ้นทะเบียน จัดทำรายงานพร้อมข้อเสนอแนะเชิงปฏิบัติ และยื่นรายงานต่อหน่วยงานราชการแทนท่านได้</p>
      </details>

      <details style="padding:26px 28px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <summary style="cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:16px; color:#1E3A28;">ค่าใช้จ่ายในการตรวจสอบประมาณเท่าไหร่?
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="flex-shrink:0; margin-left:12px;"><path d="M6 9l6 6 6-6" stroke="#BE7C3E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <p style="margin:14px 0 0 0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; line-height:1.8; color:#4A564C;">ค่าใช้จ่ายขึ้นอยู่กับขนาด ประเภท และความซับซ้อนของอาคาร ส่งข้อมูลอาคารเบื้องต้นมาให้เราประเมินและจัดทำใบเสนอราคาให้ฟรี</p>
      </details>

    </div>
  </div>

  <!-- CTA BAND -->
  <div class="stack-row" style="display:flex; align-items:center; justify-content:space-between; gap:48px; margin:0 64px 96px 64px; padding:48px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
    <div style="display:flex; flex-direction:column; gap:10px;">
      <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:24px; color:#1E3A28;">ไม่แน่ใจว่าอาคารของท่านเข้าข่ายหรือไม่?</h3>
      <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:14px; color:#4A564C;">ส่งข้อมูลอาคารมาให้ทีมวิศวกรของเราประเมินให้ฟรี</p>
    </div>
    <a href="contact.html" class="btn-amber" style="background:#BE7C3E; color:#FFFFFF; padding:16px 28px; border-radius:4px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:15px; cursor:pointer; white-space:nowrap; display:inline-block;">ปรึกษาเราฟรี</a>
  </div>
'''


CONTACT_MAIN = '''
  <!-- HERO -->
  <div style="display:flex; flex-direction:column; gap:18px; padding:72px 64px 40px 64px; max-width:760px;">
    <span style="font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:3px; color:#BE7C3E; text-transform:uppercase;">ปรึกษาฟรี · ไม่มีค่าใช้จ่าย</span>
    <h1 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:34px; line-height:1.4; color:#1E3A28;">พร้อมประเมินอาคารของท่านวันนี้</h1>
    <p style="margin:0; font-family:'Noto Sans Thai',sans-serif; font-size:15px; line-height:1.8; color:#4A564C;">ส่งรายละเอียดอาคารของท่าน เราจะติดต่อกลับภายใน 24 ชั่วโมง พร้อมประเมินขอบเขตงานและจัดทำใบเสนอราคาให้ฟรี</p>
  </div>

  <!-- CONTACT INFO + FORM -->
  <div class="stack-row" style="display:flex; gap:56px; padding:16px 64px 56px 64px;">

    <div style="flex:0.8; display:flex; flex-direction:column; gap:18px;">
      <div style="display:flex; gap:14px; align-items:flex-start; padding:24px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M12 22s7-7.5 7-12.5a7 7 0 0 0-14 0C5 14.5 12 22 12 22Z" stroke="#BE7C3E" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="9.5" r="2.6" stroke="#BE7C3E" stroke-width="1.4"/></svg>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">ที่อยู่</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; line-height:1.7; color:#4A564C;">59/109 หมู่บ้านเดอะ วอเตอร์เฮ้าส์ ซอยบางบอน 3 ซอย 12 แขวงหลักสอง เขตบางแค กรุงเทพฯ 10160</span>
        </div>
      </div>
      <a href="tel:0629565194" style="display:flex; gap:14px; align-items:center; padding:24px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M5 4h3l2 5-2.5 1.5a11 11 0 0 0 5 5L14 13l5 2v3a2 2 0 0 1-2 2C10.5 20 4 13.5 4 6a2 2 0 0 1 1-2Z" stroke="#BE7C3E" stroke-width="1.4" stroke-linejoin="round"/></svg>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">โทรศัพท์</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; color:#4A564C;">062-956-5194</span>
        </div>
      </a>
      <div style="display:flex; gap:14px; align-items:center; justify-content:space-between; padding:24px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px; flex-wrap:wrap;">
        <a href="https://line.me/ti/p/@911hrhms" target="_blank" rel="noopener" style="display:flex; gap:14px; align-items:center;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><path d="M12 3C6.5 3 2 6.6 2 11c0 2.8 1.8 5.3 4.6 6.8L6 21l3.7-1.9c.7.1 1.5.2 2.3.2 5.5 0 10-3.6 10-8s-4.5-8.3-10-8.3Z" stroke="#BE7C3E" stroke-width="1.4" stroke-linejoin="round"/></svg>
          <div style="display:flex; flex-direction:column; gap:4px;">
            <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">LINE Official Account</span>
            <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; color:#4A564C;">@911hrhms</span>
          </div>
        </a>
        <a href="https://line.me/ti/p/@911hrhms" target="_blank" rel="noopener" style="display:flex; flex-direction:column; align-items:center; gap:6px; flex-shrink:0;">
          <svg width="60" height="60" viewBox="0 0 29 29" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="QR Code สำหรับเพิ่มเพื่อน LINE Official Account Empower Best Solution"><path d="M0,0H1V1H0zM1,0H2V1H1zM2,0H3V1H2zM3,0H4V1H3zM4,0H5V1H4zM5,0H6V1H5zM6,0H7V1H6zM8,0H9V1H8zM9,0H10V1H9zM10,0H11V1H10zM11,0H12V1H11zM12,0H13V1H12zM17,0H18V1H17zM20,0H21V1H20zM22,0H23V1H22zM23,0H24V1H23zM24,0H25V1H24zM25,0H26V1H25zM26,0H27V1H26zM27,0H28V1H27zM28,0H29V1H28zM0,1H1V2H0zM6,1H7V2H6zM9,1H10V2H9zM12,1H13V2H12zM16,1H17V2H16zM18,1H19V2H18zM19,1H20V2H19zM20,1H21V2H20zM22,1H23V2H22zM28,1H29V2H28zM0,2H1V3H0zM2,2H3V3H2zM3,2H4V3H3zM4,2H5V3H4zM6,2H7V3H6zM10,2H11V3H10zM11,2H12V3H11zM13,2H14V3H13zM15,2H16V3H15zM16,2H17V3H16zM17,2H18V3H17zM18,2H19V3H18zM22,2H23V3H22zM24,2H25V3H24zM25,2H26V3H25zM26,2H27V3H26zM28,2H29V3H28zM0,3H1V4H0zM2,3H3V4H2zM3,3H4V4H3zM4,3H5V4H4zM6,3H7V4H6zM8,3H9V4H8zM10,3H11V4H10zM11,3H12V4H11zM12,3H13V4H12zM14,3H15V4H14zM15,3H16V4H15zM16,3H17V4H16zM22,3H23V4H22zM24,3H25V4H24zM25,3H26V4H25zM26,3H27V4H26zM28,3H29V4H28zM0,4H1V5H0zM2,4H3V5H2zM3,4H4V5H3zM4,4H5V5H4zM6,4H7V5H6zM8,4H9V5H8zM10,4H11V5H10zM11,4H12V5H11zM13,4H14V5H13zM14,4H15V5H14zM16,4H17V5H16zM19,4H20V5H19zM22,4H23V5H22zM24,4H25V5H24zM25,4H26V5H25zM26,4H27V5H26zM28,4H29V5H28zM0,5H1V6H0zM6,5H7V6H6zM8,5H9V6H8zM9,5H10V6H9zM11,5H12V6H11zM13,5H14V6H13zM14,5H15V6H14zM15,5H16V6H15zM18,5H19V6H18zM19,5H20V6H19zM22,5H23V6H22zM28,5H29V6H28zM0,6H1V7H0zM1,6H2V7H1zM2,6H3V7H2zM3,6H4V7H3zM4,6H5V7H4zM5,6H6V7H5zM6,6H7V7H6zM8,6H9V7H8zM10,6H11V7H10zM12,6H13V7H12zM14,6H15V7H14zM16,6H17V7H16zM18,6H19V7H18zM20,6H21V7H20zM22,6H23V7H22zM23,6H24V7H23zM24,6H25V7H24zM25,6H26V7H25zM26,6H27V7H26zM27,6H28V7H27zM28,6H29V7H28zM8,7H9V8H8zM14,7H15V8H14zM17,7H18V8H17zM18,7H19V8H18zM19,7H20V8H19zM20,7H21V8H20zM0,8H1V9H0zM4,8H5V9H4zM6,8H7V9H6zM7,8H8V9H7zM8,8H9V9H8zM9,8H10V9H9zM11,8H12V9H11zM13,8H14V9H13zM14,8H15V9H14zM15,8H16V9H15zM16,8H17V9H16zM17,8H18V9H17zM18,8H19V9H18zM20,8H21V9H20zM21,8H22V9H21zM22,8H23V9H22zM23,8H24V9H23zM24,8H25V9H24zM25,8H26V9H25zM28,8H29V9H28zM0,9H1V10H0zM2,9H3V10H2zM3,9H4V10H3zM4,9H5V10H4zM10,9H11V10H10zM12,9H13V10H12zM20,9H21V10H20zM22,9H23V10H22zM24,9H25V10H24zM25,9H26V10H25zM26,9H27V10H26zM27,9H28V10H27zM28,9H29V10H28zM0,10H1V11H0zM1,10H2V11H1zM2,10H3V11H2zM3,10H4V11H3zM4,10H5V11H4zM5,10H6V11H5zM6,10H7V11H6zM7,10H8V11H7zM8,10H9V11H8zM10,10H11V11H10zM13,10H14V11H13zM14,10H15V11H14zM15,10H16V11H15zM17,10H18V11H17zM28,10H29V11H28zM9,11H10V12H9zM10,11H11V12H10zM11,11H12V12H11zM12,11H13V12H12zM13,11H14V12H13zM15,11H16V12H15zM16,11H17V12H16zM17,11H18V12H17zM18,11H19V12H18zM21,11H22V12H21zM25,11H26V12H25zM27,11H28V12H27zM28,11H29V12H28zM0,12H1V13H0zM3,12H4V13H3zM6,12H7V13H6zM10,12H11V13H10zM11,12H12V13H11zM13,12H14V13H13zM17,12H18V13H17zM19,12H20V13H19zM21,12H22V13H21zM27,12H28V13H27zM2,13H3V14H2zM3,13H4V14H3zM7,13H8V14H7zM8,13H9V14H8zM11,13H12V14H11zM12,13H13V14H12zM13,13H14V14H13zM14,13H15V14H14zM16,13H17V14H16zM17,13H18V14H17zM18,13H19V14H18zM22,13H23V14H22zM23,13H24V14H23zM24,13H25V14H24zM25,13H26V14H25zM26,13H27V14H26zM27,13H28V14H27zM28,13H29V14H28zM0,14H1V15H0zM1,14H2V15H1zM2,14H3V15H2zM3,14H4V15H3zM5,14H6V15H5zM6,14H7V15H6zM9,14H10V15H9zM12,14H13V15H12zM16,14H17V15H16zM17,14H18V15H17zM20,14H21V15H20zM23,14H24V15H23zM24,14H25V15H24zM25,14H26V15H25zM26,14H27V15H26zM28,14H29V15H28zM4,15H5V16H4zM5,15H6V16H5zM7,15H8V16H7zM8,15H9V16H8zM9,15H10V16H9zM10,15H11V16H10zM11,15H12V16H11zM14,15H15V16H14zM17,15H18V16H17zM19,15H20V16H19zM20,15H21V16H20zM22,15H23V16H22zM24,15H25V16H24zM27,15H28V16H27zM28,15H29V16H28zM1,16H2V17H1zM2,16H3V17H2zM4,16H5V17H4zM5,16H6V17H5zM6,16H7V17H6zM8,16H9V17H8zM9,16H10V17H9zM10,16H11V17H10zM11,16H12V17H11zM13,16H14V17H13zM14,16H15V17H14zM15,16H16V17H15zM16,16H17V17H16zM17,16H18V17H17zM20,16H21V17H20zM21,16H22V17H21zM27,16H28V17H27zM0,17H1V18H0zM1,17H2V18H1zM3,17H4V18H3zM8,17H9V18H8zM9,17H10V18H9zM11,17H12V18H11zM12,17H13V18H12zM20,17H21V18H20zM22,17H23V18H22zM23,17H24V18H23zM24,17H25V18H24zM25,17H26V18H25zM27,17H28V18H27zM28,17H29V18H28zM4,18H5V19H4zM6,18H7V19H6zM8,18H9V19H8zM9,18H10V19H9zM10,18H11V19H10zM13,18H14V19H13zM14,18H15V19H14zM15,18H16V19H15zM20,18H21V19H20zM22,18H23V19H22zM26,18H27V19H26zM28,18H29V19H28zM3,19H4V20H3zM4,19H5V20H4zM5,19H6V20H5zM7,19H8V20H7zM10,19H11V20H10zM12,19H13V20H12zM13,19H14V20H13zM15,19H16V20H15zM16,19H17V20H16zM17,19H18V20H17zM22,19H23V20H22zM23,19H24V20H23zM24,19H25V20H24zM27,19H28V20H27zM28,19H29V20H28zM0,20H1V21H0zM1,20H2V21H1zM2,20H3V21H2zM5,20H6V21H5zM6,20H7V21H6zM8,20H9V21H8zM9,20H10V21H9zM13,20H14V21H13zM17,20H18V21H17zM20,20H21V21H20zM21,20H22V21H21zM22,20H23V21H22zM23,20H24V21H23zM24,20H25V21H24zM25,20H26V21H25zM28,20H29V21H28zM8,21H9V22H8zM10,21H11V22H10zM11,21H12V22H11zM13,21H14V22H13zM14,21H15V22H14zM16,21H17V22H16zM17,21H18V22H17zM18,21H19V22H18zM19,21H20V22H19zM20,21H21V22H20zM24,21H25V22H24zM28,21H29V22H28zM0,22H1V23H0zM1,22H2V23H1zM2,22H3V23H2zM3,22H4V23H3zM4,22H5V23H4zM5,22H6V23H5zM6,22H7V23H6zM8,22H9V23H8zM9,22H10V23H9zM10,22H11V23H10zM11,22H12V23H11zM16,22H17V23H16zM17,22H18V23H17zM19,22H20V23H19zM20,22H21V23H20zM22,22H23V23H22zM24,22H25V23H24zM25,22H26V23H25zM26,22H27V23H26zM28,22H29V23H28zM0,23H1V24H0zM6,23H7V24H6zM9,23H10V24H9zM10,23H11V24H10zM12,23H13V24H12zM14,23H15V24H14zM17,23H18V24H17zM19,23H20V24H19zM20,23H21V24H20zM24,23H25V24H24zM27,23H28V24H27zM0,24H1V25H0zM2,24H3V25H2zM3,24H4V25H3zM4,24H5V25H4zM6,24H7V25H6zM8,24H9V25H8zM9,24H10V25H9zM11,24H12V25H11zM12,24H13V25H12zM13,24H14V25H13zM14,24H15V25H14zM15,24H16V25H15zM17,24H18V25H17zM19,24H20V25H19zM20,24H21V25H20zM21,24H22V25H21zM22,24H23V25H22zM23,24H24V25H23zM24,24H25V25H24zM25,24H26V25H25zM27,24H28V25H27zM28,24H29V25H28zM0,25H1V26H0zM2,25H3V26H2zM3,25H4V26H3zM4,25H5V26H4zM6,25H7V26H6zM9,25H10V26H9zM12,25H13V26H12zM13,25H14V26H13zM17,25H18V26H17zM18,25H19V26H18zM19,25H20V26H19zM20,25H21V26H20zM27,25H28V26H27zM0,26H1V27H0zM2,26H3V27H2zM3,26H4V27H3zM4,26H5V27H4zM6,26H7V27H6zM9,26H10V27H9zM12,26H13V27H12zM13,26H14V27H13zM14,26H15V27H14zM15,26H16V27H15zM17,26H18V27H17zM18,26H19V27H18zM19,26H20V27H19zM21,26H22V27H21zM25,26H26V27H25zM26,26H27V27H26zM27,26H28V27H27zM28,26H29V27H28zM0,27H1V28H0zM6,27H7V28H6zM9,27H10V28H9zM10,27H11V28H10zM11,27H12V28H11zM12,27H13V28H12zM16,27H17V28H16zM17,27H18V28H17zM18,27H19V28H18zM19,27H20V28H19zM20,27H21V28H20zM23,27H24V28H23zM25,27H26V28H25zM27,27H28V28H27zM28,27H29V28H28zM0,28H1V29H0zM1,28H2V29H1zM2,28H3V29H2zM3,28H4V29H3zM4,28H5V29H4zM5,28H6V29H5zM6,28H7V29H6zM8,28H9V29H8zM11,28H12V29H11zM12,28H13V29H12zM13,28H14V29H13zM16,28H17V29H16zM17,28H18V29H17zM20,28H21V29H20zM21,28H22V29H21zM22,28H23V29H22zM23,28H24V29H23zM25,28H26V29H25zM27,28H28V29H27z" fill="#1E3A28"/></svg>
          <span style="font-family:'IBM Plex Mono',monospace; font-size:9.5px; letter-spacing:0.02em; color:#4A564C; white-space:nowrap;">สแกนเพิ่มเพื่อน</span>
        </a>
      </div>
      <a href="mailto:empower.bestsolution2024@gmail.com" style="display:flex; gap:14px; align-items:center; padding:24px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:8px;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;"><rect x="3" y="5" width="18" height="14" rx="2" stroke="#BE7C3E" stroke-width="1.4"/><path d="m3 7 9 6 9-6" stroke="#BE7C3E" stroke-width="1.4" stroke-linejoin="round"/></svg>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:14px; color:#1E3A28;">อีเมล</span>
          <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; color:#4A564C;">empower.bestsolution2024@gmail.com</span>
        </div>
      </a>
    </div>

    <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thank-you.html" style="flex:1.1; display:flex; flex-direction:column; gap:20px; padding:44px; background:#FFFFFF; border:1px solid #E4DCC8; border-radius:10px;">
      <input type="hidden" name="form-name" value="contact">
      <p class="hidden-field"><label>อย่ากรอกช่องนี้ถ้าท่านเป็นมนุษย์: <input name="bot-field"></label></p>
      <h3 style="margin:0; font-family:'Noto Serif Thai',serif; font-weight:700; font-size:22px; color:#1E3A28;">ส่งข้อความถึงเรา</h3>
      <div class="form-grid" style="display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:16px;">
        <div style="display:flex; flex-direction:column; gap:6px;">
          <label for="c-name" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">ชื่อ-นามสกุล</label>
          <input id="c-name" name="name" type="text" required placeholder="ชื่อ-นามสกุลของท่าน" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <label for="c-phone" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">เบอร์โทรศัพท์</label>
          <input id="c-phone" name="phone" type="tel" required placeholder="08X-XXX-XXXX" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; grid-column:span 2;">
          <label for="c-email" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">อีเมล</label>
          <input id="c-email" name="email" type="email" required placeholder="name@example.com" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; grid-column:span 2;">
          <label for="c-building" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">ชื่ออาคาร (ถ้ามี)</label>
          <input id="c-building" name="building_name" type="text" placeholder="เช่น คอนโด เดอะ ริเวอร์ไซด์" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3;">
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; grid-column:span 2;">
          <label for="c-message" style="font-family:'Noto Sans Thai',sans-serif; font-size:13px; color:#1E3A28; font-weight:600;">รายละเอียดที่ต้องการปรึกษา</label>
          <textarea id="c-message" name="message" placeholder="เช่น ต้องการขอใบเสนอราคาตรวจสอบอาคารประจำปี หรือขอคำปรึกษาปัญหางานระบบอาคาร" rows="4" style="padding:12px 14px; border:1px solid #E4DCC8; border-radius:5px; font-size:14px; color:#4A564C; background:#F7F2E3; resize:none;"></textarea>
        </div>
      </div>
      <button type="submit" class="btn-amber" style="margin-top:6px; background:#BE7C3E; color:#FFFFFF; padding:15px 24px; border-radius:5px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:15px; cursor:pointer;">ส่งข้อความ</button>
    </form>

  </div>

  <!-- REMINDER CTA -->
  <div class="stack-row" style="display:flex; align-items:center; justify-content:space-between; gap:48px; margin:0 64px 96px 64px; padding:40px 48px; background:#1E3A28; border-radius:8px;">
    <div style="display:flex; flex-direction:column; gap:6px;">
      <span style="font-family:'Noto Sans Thai',sans-serif; font-weight:700; font-size:18px; color:#F7F2E3;">อยากให้เราแจ้งเตือนก่อนถึงรอบตรวจสอบอาคาร?</span>
      <span style="font-family:'Noto Sans Thai',sans-serif; font-size:13.5px; color:rgba(247,242,227,0.75);">ลงทะเบียนโปรแกรมเตือนตรวจสอบอาคารได้ฟรี ไม่ต้องรอกรอกฟอร์มด้านบน</span>
    </div>
    <a href="reminder-program.html" class="btn-amber" style="background:#BE7C3E; color:#FFFFFF; padding:15px 26px; border-radius:4px; border:none; font-family:'Noto Sans Thai',sans-serif; font-weight:600; font-size:14px; cursor:pointer; white-space:nowrap; display:inline-block;">ไปที่โปรแกรมเตือนตรวจสอบอาคาร</a>
  </div>
'''


if __name__ == "__main__":
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(
            "Empower Best Solution | ตรวจสอบอาคารตาม พ.ร.บ. ควบคุมอาคาร",
            "บริการตรวจสอบอาคารตาม พ.ร.บ. ควบคุมอาคาร พ.ศ. 2522 โดยทีมวิศวกรที่มีประสบการณ์บริหารอาคารใหญ่กว่า 100 โครงการ ตรวจสอบใหญ่ทุก 5 ปี ตรวจสอบประจำปี พร้อมโปรแกรมเตือนตรวจสอบอาคารฟรี",
            "index.html",
            INDEX_MAIN,
        ))
    print("wrote index.html")

    with open(os.path.join(OUT_DIR, "about.html"), "w", encoding="utf-8") as f:
        f.write(page(
            "เกี่ยวกับเรา | Empower Best Solution",
            "Empower Best Solution ก่อตั้งจากมุมมองผู้บริหารงานวิศวกรรมอาคาร บริหารโครงการใหญ่กว่า 100 โครงการ ทีมวิศวกรขึ้นทะเบียน ก.ย.ผ. ครบทุกคน",
            "about.html",
            ABOUT_MAIN,
        ))
    print("wrote about.html")

    with open(os.path.join(OUT_DIR, "reminder-program.html"), "w", encoding="utf-8") as f:
        f.write(page(
            "โปรแกรมเตือนตรวจสอบอาคาร | Empower Best Solution",
            "ลงทะเบียนฟรี รับการแจ้งเตือนล่วงหน้า 90/60/45 วันก่อนครบกำหนดตรวจสอบอาคาร ทาง LINE และอีเมล ไม่ต้องกังวลว่าจะลืมหรือเลยกำหนดตามกฎหมายอีกต่อไป",
            "reminder-program.html",
            REMINDER_MAIN,
        ))
    print("wrote reminder-program.html")

    with open(os.path.join(OUT_DIR, "services.html"), "w", encoding="utf-8") as f:
        f.write(page(
            "บริการของเรา | Empower Best Solution",
            "บริการตรวจสอบใหญ่อาคารทุก 5 ปี ตรวจสอบประจำปี วิเคราะห์ปัญหาอาคาร และรับแก้ปัญหาอาคารทั้งงานระบบ โครงสร้าง และสถาปัตยกรรม โดยทีมวิศวกรที่ขึ้นทะเบียน ก.ย.ผ.",
            "services.html",
            SERVICES_MAIN,
        ))
    print("wrote services.html")

    with open(os.path.join(OUT_DIR, "legal-knowledge.html"), "w", encoding="utf-8") as f:
        f.write(page(
            "ความรู้ตามกฎหมาย | Empower Best Solution",
            "รวมความรู้ พ.ร.บ. ควบคุมอาคาร พ.ศ. 2522 9 ประเภทอาคารที่ต้องตรวจสอบ และคำถามที่พบบ่อยเกี่ยวกับการตรวจสอบอาคารตามกฎหมาย",
            "legal-knowledge.html",
            LEGAL_MAIN,
        ))
    print("wrote legal-knowledge.html")

    with open(os.path.join(OUT_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(page(
            "ติดต่อเรา | Empower Best Solution",
            "ติดต่อ Empower Best Solution เพื่อขอใบเสนอราคาตรวจสอบอาคาร หรือปรึกษาปัญหางานระบบอาคาร โทร 062-956-5194 หรือ LINE OA @911hrhms",
            "contact.html",
            CONTACT_MAIN,
        ))
    print("wrote contact.html")
