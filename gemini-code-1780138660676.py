html_content = """<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BaseSys - פתרונות טכנולוגיים ופיתוח מערכות תקשורת</title>
    <style>
        /* עיצוב כללי ואיפוס */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            scroll-behavior: smooth;
        }

        :root {
            --primary-green: #10B981; /* ירוק מודרני וחדשני */
            --primary-dark: #111827;  /* שחור/אפור כהה לכיתוב ורקעים */
            --light-bg: #FFFFFF;
            --accent-bg: #F0FDF4;     /* רקע ירקרק בהיר מאוד לגיוון */
            --muted-gray: #6B7280;
            --border-color: #E5E7EB;
        }

        body {
            background-color: var(--light-bg);
            color: var(--primary-dark);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* תפריט ניווט עליון */
        header.nav-container {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: rgba(255, 255, 255, 0.95);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            z-index: 1000;
            backdrop-filter: blur(5px);
        }

        .nav-bar {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 20px;
        }

        .logo-area {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-img {
            height: 45px;
            width: auto;
            object-fit: contain;
        }

        .logo-fallback {
            font-size: 24px;
            font-weight: 800;
            color: var(--primary-dark);
            letter-spacing: -0.5px;
        }

        .logo-fallback span {
            color: var(--primary-green);
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 25px;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--primary-dark);
            font-weight: 600;
            font-size: 15px;
            transition: color 0.3s ease;
            position: relative;
            padding: 5px 0;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--primary-green);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background-color: var(--primary-green);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* כפתור תפריט למובייל */
        .menu-toggle {
            display: none;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
            background: none;
            border: none;
        }

        .menu-toggle span {
            display: block;
            width: 25px;
            height: 3px;
            background-color: var(--primary-dark);
            border-radius: 3px;
            transition: 0.3s;
        }

        /* אזור ה-Hero / כותרת ראשית */
        .hero-section {
            padding: 140px 20px 80px 20px;
            background: linear-gradient(135deg, #FFFFFF 0%, #F6FBF8 100%);
            position: relative;
            overflow: hidden;
        }

        .hero-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 40px;
        }

        .hero-content {
            z-index: 2;
        }

        .badge {
            display: inline-block;
            background-color: var(--accent-bg);
            color: var(--primary-green);
            padding: 6px 16px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 20px;
            border: 1px solid rgba(16, 185, 129, 0.2);
        }

        .hero-title {
            font-size: 44px;
            font-weight: 900;
            line-height: 1.2;
            color: var(--primary-dark);
            margin-bottom: 20px;
        }

        .hero-title span {
            color: var(--primary-green);
        }

        .hero-subtitle {
            font-size: 18px;
            color: var(--muted-gray);
            margin-bottom: 35px;
            max-width: 540px;
        }

        .hero-cta {
            display: inline-block;
            background-color: var(--primary-dark);
            color: #FFFFFF;
            padding: 14px 30px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .hero-cta:hover {
            background-color: var(--primary-green);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3);
        }

        /* תמונת ה-Header הסכמטית באנימציית SVG */
        .hero-visual {
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 2;
        }

        .schematic-svg {
            width: 100%;
            max-width: 500px;
            height: auto;
        }

        /* עיצוב כללי של הסקשנים */
        .section {
            padding: 100px 20px;
            border-bottom: 1px solid var(--border-color);
        }

        .section:nth-child(even) {
            background-color: var(--accent-bg);
        }

        .section-container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-header {
            text-align: center;
            margin-bottom: 60px;
        }

        .section-tag {
            color: var(--primary-green);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 14px;
            letter-spacing: 1px;
            display: block;
            margin-bottom: 10px;
        }

        .section-title {
            font-size: 32px;
            font-weight: 800;
            color: var(--primary-dark);
            position: relative;
            display: inline-block;
            padding-bottom: 15px;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background-color: var(--primary-green);
            border-radius: 2px;
        }

        .section-desc {
            font-size: 16px;
            color: var(--muted-gray);
            max-width: 700px;
            margin: 20px auto 0 auto;
        }

        /* פריסת גריד לתתי נושאים / פיצ'רים */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .feature-card {
            background-color: #FFFFFF;
            padding: 35px 30px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            position: relative;
            overflow: hidden;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.06);
            border-color: rgba(16, 185, 129, 0.3);
        }

        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background-color: var(--primary-green);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .feature-card:hover::before {
            opacity: 1;
        }

        .feature-icon {
            width: 50px;
            height: 50px;
            background-color: var(--accent-bg);
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: var(--primary-green);
            margin-bottom: 20px;
        }

        .feature-card-title {
            font-size: 19px;
            font-weight: 700;
            margin-bottom: 12px;
            color: var(--primary-dark);
        }

        .feature-card-text {
            font-size: 15px;
            color: var(--muted-gray);
        }

        /* סגנון מיוחד למבנה דו-עמודי בתוך סקשן */
        .content-split {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .content-text-side ul {
            list-style: none;
            margin-top: 20px;
        }

        .content-text-side ul li {
            position: relative;
            padding-right: 30px;
            margin-bottom: 15px;
            font-size: 16px;
        }

        .content-text-side ul li::before {
            content: "✓";
            position: absolute;
            right: 0;
            top: 0;
            color: var(--primary-green);
            font-weight: bold;
            font-size: 18px;
        }

        .content-visual-side {
            display: flex;
            justify-content: center;
        }

        /* אזור יצירת קשר */
        .contact-section {
            background-color: var(--primary-dark);
            color: #FFFFFF;
            padding: 90px 20px;
        }

        .contact-container {
            max-width: 600px;
            margin: 0 auto;
            text-align: center;
        }

        .contact-title {
            font-size: 32px;
            font-weight: 800;
            margin-bottom: 15px;
        }

        .contact-subtitle {
            color: #9CA3AF;
            margin-bottom: 40px;
        }

        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 15px;
            text-align: right;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        .form-group label {
            font-size: 14px;
            font-weight: 600;
            color: #D1D5DB;
        }

        .form-control {
            padding: 12px 15px;
            border-radius: 6px;
            border: 1px solid #374151;
            background-color: #1F2937;
            color: #FFFFFF;
            font-size: 15px;
            outline: none;
            transition: border-color 0.3s ease;
        }

        .form-control:focus {
            border-color: var(--primary-green);
        }

        .submit-btn {
            background-color: var(--primary-green);
            color: #FFFFFF;
            border: none;
            padding: 14px;
            border-radius: 6px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 10px;
        }

        .submit-btn:hover {
            background-color: #059669;
        }

        /* פוטר */
        footer {
            background-color: #0B0F19;
            color: #9CA3AF;
            padding: 30px 20px;
            text-align: center;
            font-size: 14px;
            border-top: 1px solid #1F2937;
        }

        footer span {
            color: var(--primary-green);
            font-weight: 600;
        }

        /* רספונסיביות והתאמה למובייל */
        @media (max-width: 968px) {
            .hero-container, .content-split {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .hero-subtitle {
                margin-left: auto;
                margin-right: auto;
            }

            .hero-visual {
                order: -1; /* מציג את האנימציה הגרפית מעל הטקסט במובייל */
            }

            .content-visual-side {
                margin-top: 30px;
            }

            .content-text-side ul li {
                text-align: right;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                display: none; /* תפריט מובייל ייסגר כברירת מחדל */
                flex-direction: column;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background-color: #FFFFFF;
                padding: 20px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                gap: 15px;
                border-top: 1px solid var(--border-color);
            }

            .nav-links.active {
                display: flex;
            }

            .menu-toggle {
                display: flex;
            }

            .hero-title {
                font-size: 32px;
            }

            .section {
                padding: 60px 20px;
            }
        }
    </style>
</head>
<body>

    <header class="nav-container">
        <div class="nav-bar">
            <div class="logo-area">
                <img src="Logo_Text_Flat_Img_NoBk.jpg" alt="BaseSys Logo" class="logo-img" onerror="this.style.display='none'; document.getElementById('logo-text').style.display='block';">
                <div id="logo-text" class="logo-fallback" style="display:none;">Base<span>Sys</span></div>
            </div>
            <button class="menu-toggle" onclick="toggleMenu()" aria-label="תפריט">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-links" id="navLinks">
                <li><a href="#home" class="active" onclick="closeMenu()">דף הבית</a></li>
                <li><a href="#ivr" onclick="closeMenu()">מערכות IVR</a></li>
                <li><a href="#callcenter" onclick="closeMenu()">קול סנטר</a></li>
                <li><a href="#dialers" onclick="closeMenu()">חייגנים ותורים</a></li>
                <li><a href="#consulting" onclick="closeMenu()">ייעוץ טכנולוגי</a></li>
                <li><a href="#contact" onclick="closeMenu()">צור קשר</a></li>
            </ul>
        </div>
    </header>

    <section class="hero-section" id="home">
        <div class="hero-container">
            <div class="hero-content">
                <span class="badge">פתרונות תקשורת מתקדמים</span>
                <h1 class="hero-title">מערכות טלפוניה חכמות ופיתוח פתרונות טכנולוגיים מותאמים אישית ל-<span>BaseSys</span></h1>
                <p class="hero-subtitle">אנו מפתחים ומטמיעים את הדור הבא של מערכות ה-IVR, מוקדי שירות (Call Centers), חייגנים אוטומטיים ופתרונות ניתוב מתקדמים שמזניקים את הפעילות העסקית שלכם קדימה.</p>
                <a href="#contact" class="hero-cta">להתייעצות עם מומחה</a>
            </div>
            <div class="hero-visual">
                <svg class="schematic-svg" viewBox="0 0 500 400" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M150 200 C250 100, 300 300, 400 200" stroke="#10B981" stroke-width="3" stroke-dasharray="6 6" opacity="0.6"/>
                    <path d="M80 150 C200 280, 280 120, 420 250" stroke="#111827" stroke-width="2" opacity="0.2"/>
                    
                    <line x1="250" y1="100" x2="130" y2="220" stroke="#E5E7EB" stroke-width="3"/>
                    <line x1="250" y1="100" x2="370" y2="220" stroke="#E5E7EB" stroke-width="3"/>
                    <line x1="250" y1="100" x2="250" y2="280" stroke="#10B981" stroke-width="2"/>
                    <line x1="130" y1="220" x2="250" y2="280" stroke="#E5E7EB" stroke-width="3"/>
                    <line x1="370" y1="220" x2="250" y2="280" stroke="#E5E7EB" stroke-width="3"/>

                    <circle cx="250" cy="100" r="40" fill="#111827" />
                    <path d="M240 105 C240 98, 246 95, 252 95 C256 95, 260 98, 261 101 C264 100, 268 103, 268 106 C268 110, 264 112, 260 112 L242 112 C238 112, 240 106, 240 105 Z" fill="#10B981"/>
                    
                    <circle cx="130" cy="220" r="35" fill="#FFFFFF" stroke="#10B981" stroke-width="4"/>
                    <path d="M122 215 H138 M130 215 V230 M125 225 L130 230 L135 225" stroke="#111827" stroke-width="3" stroke-linecap="round"/>
                    <circle cx="130" cy="210" r="4" fill="#10B981"/>
                    
                    <circle cx="370" cy="220" r="35" fill="#FFFFFF" stroke="#111827" stroke-width="4"/>
                    <path d="M360 228 C360 218, 380 218, 380 228" stroke="#10B981" stroke-width="4" stroke-linecap="round"/>
                    <circle cx="370" cy="212" r="7" fill="#111827"/>
                    <path d="M377 210 A10 10 0 0 1 363 218" stroke="#10B981" stroke-width="2" fill="none"/>

                    <circle cx="250" cy="290" r="30" fill="#10B981" />
                    <path d="M242 298 V282 H246 V298 H242 Z M248 298 V276 H252 V298 H248 Z M254 298 V288 H258 V298 H254 Z" fill="#FFFFFF"/>
                    
                    <text x="250" y="45" fill="#111827" font-size="12" font-weight="bold" text-anchor="middle">BaseSys SIP Core</text>
                    <text x="70" y="240" fill="#6B7280" font-size="11" text-anchor="middle">IVR & Routing</text>
                    <text x="425" y="240" fill="#6B7280" font-size="11" text-anchor="middle">Call Center</text>
                </svg>
            </div>
        </div>
    </section>

    <section class="section" id="ivr">
        <div class="section-container">
            <div class="section-header">
                <span class="section-tag">Interactive Voice Response</span>
                <h2 class="section-title">מערכות IVR מתקדמות וייחודיות</h2>
                <p class="section-desc">פתרונות ניתוב שיחות חכמים המציעים התאמה מהירה ומדויקת לפעילות העסקית שלכם, תוך מתן חוויית משתמש חלקה ומקצועית לכל מתקשר.</p>
            </div>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    </div>
                    <h3 class="feature-card-title">התאמה מהירה ומותאמת אישית</h3>
                    <p class="feature-card-text">יכולת פיתוח גמישה המאפשרת לנו לשנות, לעדכן ולהתאים את זרימת הנתב וההקלטות בזמן אמת ובהתאם לצרכים המשתנים של העסק.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                    </div>
                    <h3 class="feature-card-title">חיבור פרוטוקול SIP אוניברסלי</h3>
                    <p class="feature-card-text">אינטגרציה חלקה לכל מרכזיית VOIP קיימת בארגון או בענן. אנו מתחברים ישירות ומאפשרים עבודה סינרגטית ללא סיבוכי תשתית.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                    </div>
                    <h3 class="feature-card-title">דוחות שימוש וכניסות מערכת</h3>
                    <p class="feature-card-text">מערכת ניתוח מתקדמת המספקת תמונת מצב מלאה: כמות כניסות, זמני שהייה, פילוח הקשות ומעקב מדויק אחר ביצועי הנתב.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section" id="callcenter">
        <div class="section-container">
            <div class="content-split">
                <div class="content-text-side">
                    <span class="section-tag">Call Center Solutions</span>
                    <h2 class="section-title" style="display:block;">פתרונות קול סנטר למוקדים חכמים</h2>
                    <p class="section-desc" style="margin: 20px 0;">מענה מקיף, גמיש ומתקדם לניהול מוקדי שירות ומכירות. פתרונות התוכנה של BaseSys מאפשרים לכם לנהל את מערך הנציגים ביעילות מקסימלית ומכל מקום.</p>
                    
                    <ul>
                        <li><strong>פתרונות מקומיים והתאמה למוקדים קטנים:</strong> פלטפורמה ייעודית ויציבה למוקדים קטנים עד בינוניים ללא צורך בהשקעות עתק.</li>
                        <li><strong>תמיכה מלאה בעבודה מהבית:</strong> חיבור מאובטח ואינטואיטיבי המאפשר לנציגים שלכם להעניק שירות מהבית באותה איכות ורמת בקרה.</li>
                        <li><strong>מערכת ניהול ובקרה קלה:</strong> ממשק ניהול נקי ופשוט המאפשר שליטה בזמן אמת, האזנות, וניהול תורים ומשמרות בקליק.</li>
                        <li><strong>מערכת דוחות פשוטה וממוקדת:</strong> הפקת נתוני ביצועים, זמני מענה ויעילות נציגים ללא סיבוכים מיותרים.</li>
                    </ul>
                </div>
                <div class="content-visual-side">
                    <svg width="100%" max-width="400" height="300" viewBox="0 0 400 300" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect width="400" height="300" rx="16" fill="#111827"/>
                        <rect x="40" y="40" width="320" height="180" rx="8" fill="#1F2937" stroke="#374151" stroke-width="2"/>
                        <circle cx="65" cy="60" r="6" fill="#EF4444"/>
                        <circle cx="85" cy="60" r="6" fill="#F59E0B"/>
                        <circle cx="105" cy="60" r="6" fill="#10B981"/>
                        
                        <path d="M60 160 L120 110 L180 140 L240 80 L300 120 L340 70" stroke="#10B981" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                        <p fill="#6B7280"/>
                        <line x1="60" y1="180" x2="340" y2="180" stroke="#4B5563" stroke-width="2"/>
                        
                        <circle cx="120" cy="250" r="20" fill="#10B981"/>
                        <circle cx="200" cy="250" r="20" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
                        <circle cx="280" cy="250" r="20" fill="#10B981"/>
                        <text x="200" y="254" fill="#111827" font-size="12" font-weight="bold" text-anchor="middle">הבית</text>
                    </svg>
                </div>
            </div>
        </div>
    </section>

    <section class="section" id="dialers">
        <div class="section-container">
            <div class="section-header">
                <span class="section-tag">Automated Outbound & Scheduling</span>
                <h2 class="section-title">מערכות חייגנים אוטומטיות וזימון תורים</h2>
                <p class="section-desc">ייעול התקשורת היוצאת של הארגון וניהול התורים באמצעות אוטומציה חכמה המונעת אובדן זמן יקר וממקסמת מענה.</p>
            </div>

            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.94.725l.548 2.2a1 1 0 01-.321.988l-1.305.98a10.582 10.582 0 004.872 4.872l.98-1.305a1 1 0 01.988-.321l2.2.548a1 1 0 01.725.94V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                    </div>
                    <h3 class="feature-card-title">מערכת חייגנים אוטומטית</h3>
                    <p class="feature-card-text">ניהול קמפיינים לשיחות יוצאות בצורה חכמה, המערכת מחייגת אוטומטית לרשימות תפוצה, מזהה מענה אנושי ומעבירה לנציג או משמיעה הודעה מובנית.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m4 4V3m4 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                    </div>
                    <h3 class="feature-card-title">מערכת תזכור וזימון תורים</h3>
                    <p class="feature-card-text">מערכת אוטומטית המאפשרת ללקוחות לזמן, לעדכן או לבטל תורים באופן עצמאי בטלפון או ב-SMS, כולל שליחת תזכורות אוטומטיות למניעת אי-הגעה.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section" id="consulting">
        <div class="section-container">
            <div class="content-split" style="direction: ltr;">
                <div class="content-text-side" style="direction: rtl;">
                    <span class="section-tag">Professional Architecture & Consulting</span>
                    <h2 class="section-title">ייעוץ לארגונים וחברות בתחומי הטלפוניה</h2>
                    <p class="section-desc" style="margin: 20px 0;">הניסיון הטכנולוגי העשיר שלנו עומד לרשותכם. אנו מספקים שירותי ייעוץ וליווי מקצועי אסטרטגי לחברות וארגונים המעוניינים לשדרג, לייעל או להקים מערכי תקשורת מתקדמים.</p>
                    
                    <div class="feature-card" style="margin-bottom: 15px; padding: 20px;">
                        <h4 style="font-size:16px; font-weight:700; margin-bottom:5px; color:var(--primary-dark);">אפיון ארכיטקטורת מערכת</h4>
                        <p class="feature-card-text">התאמת המערכות הנכונות (IVR, קול סנטר, שירותי ענן) למבנה הארגוני שלכם להשגת מקסימום תוצאות.</p>
                    </div>
                    
                    <div class="feature-card" style="padding: 20px;">
                        <h4 style="font-size:16px; font-weight:700; margin-bottom:5px; color:var(--primary-dark);">ליווי טכנולוגי באינטגרציות מורכבות</h4>
                        <p class="feature-card-text">סיוע וחיבור בין מערכות ה-CRM של הארגון לליבת הטלפוניה ומערכות ה-VOIP בצורה מאובטחת ויציבה.</p>
                    </div>
                </div>
                <div class="content-visual-side">
                    <svg width="100%" max-width="350" height="300" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="100" cy="100" r="80" fill="#F0FDF4"/>
                        <path d="M60 130 L100 70 L140 110 L170 60" stroke="#10B981" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                        <circle cx="170" cy="60" r="6" fill="#111827"/>
                        <rect x="55" y="60" width="30" height="40" rx="4" fill="#111827" opacity="0.1"/>
                        <circle cx="100" cy="70" r="4" fill="#10B981"/>
                        <circle cx="140" cy="110" r="4" fill="#10B981"/>
                    </svg>
                </div>
            </div>
        </div>
    </section>

    <section class="contact-section" id="contact">
        <div class="contact-container">
            <h2 class="contact-title">נשמח לפתח עבורכם את הפתרון הבא</h2>
            <p class="contact-subtitle">השאירו פרטים ונציג טכנולוגי של BaseSys יחזור אליכם בהקדם עם הצעה מותאמת אישית.</p>
            
            <form class="contact-form" onsubmit="event.preventDefault(); alert('תודה על פנייתך! נציג BaseSys יחזור אליך בהקדם.');">
                <div class="form-group">
                    <label for="name">שם מלא</label>
                    <input type="text" id="name" class="form-control" placeholder="ישראל ישראלי" required>
                </div>
                <div class="form-group">
                    <label for="email">כתובת אימייל</label>
                    <input type="email" id="email" class="form-control" placeholder="name@company.com" required>
                </div>
                <div class="form-group">
                    <label for="phone">מספר טלפון</label>
                    <input type="tel" id="phone" class="form-control" placeholder="050-1234567" required>
                </div>
                <div class="form-group">
                    <label for="message">כיצד נוכל לעזור?</label>
                    <textarea id="message" rows="4" class="form-control" placeholder="ספרו לנו בקצרה על הצרכים הטכנולוגיים שלכם..." required></textarea>
                </div>
                <button type="submit" class="submit-btn">שליחת בקשה</button>
            </form>
        </div>
    </section>

    <footer>
        <p>© 2026 <span>BaseSys</span>. כל הזכויות שמורות. פתרונות טכנולוגיים ופיתוח מערכות תקשורת מתקדמות.</p>
    </footer>

    <script>
        function toggleMenu() {
            const navLinks = document.getElementById('navLinks');
            navLinks.classList.toggle('active');
        }

        function closeMenu() {
            const navLinks = document.getElementById('navLinks');
            navLinks.classList.remove('active');
        }

        // שינוי עיצוב הקישור הפעיל בעת גלילה
        window.addEventListener('scroll', () => {
            const sections = document.querySelectorAll('section, class');
            const navLinks = document.querySelectorAll('.nav-links a');
            
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (pageYOffset >= sectionTop - 150) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(a => {
                a.classList.remove('active');
                if (a.getAttribute('href').includes(current)) {
                    a.classList.add('active');
                }
            });
        });
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("File 'index.html' created successfully.")