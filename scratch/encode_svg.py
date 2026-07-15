import base64

svg_header = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 220" width="100%">
  <defs>
    <!-- Dark Space Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d" />
      <stop offset="50%" stop-color="#070b14" />
      <stop offset="100%" stop-color="#020408" />
    </linearGradient>

    <!-- Text Gradient with Animation -->
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe">
        <animate attributeName="stop-color" values="#00f2fe; #a855f7; #00f2fe" dur="5s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#4facfe">
        <animate attributeName="stop-color" values="#4facfe; #38bdf8; #4facfe" dur="5s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Border Glow Gradient -->
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe">
        <animate attributeName="stop-color" values="#00f2fe; #a855f7; #00f2fe" dur="6s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#38bdf8">
        <animate attributeName="stop-color" values="#38bdf8; #00f2fe; #38bdf8" dur="6s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#a855f7">
        <animate attributeName="stop-color" values="#a855f7; #38bdf8; #a855f7" dur="6s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Node Gradient -->
    <linearGradient id="node-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#a855f7" />
    </linearGradient>
  </defs>

  <style>
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 0.6; }
      50% { transform: scale(1.15); opacity: 1; }
    }
    @keyframes dash {
      to { stroke-dashoffset: -40; }
    }
    .title {
      font-family: 'Righteous', 'Segoe UI', -apple-system, sans-serif;
      font-weight: 800;
      font-size: 46px;
      fill: url(#text-grad);
    }
    .subtitle {
      font-family: 'Inter', 'Segoe UI', -apple-system, sans-serif;
      font-weight: 600;
      font-size: 16px;
      fill: #e2e8f0;
      letter-spacing: 3px;
    }
    .tagline {
      font-family: 'Inter', 'Segoe UI', -apple-system, sans-serif;
      font-weight: 400;
      font-size: 13px;
      fill: #64748b;
      letter-spacing: 0.5px;
    }
    .node-pulse {
      transform-origin: center;
      animation: pulse 3s infinite ease-in-out;
    }
    .connection-active {
      stroke: url(#node-grad);
      stroke-width: 1.5;
      stroke-dasharray: 8 4;
      animation: dash 1.5s linear infinite;
      opacity: 0.8;
    }
    .border-glow {
      stroke: url(#border-grad);
      stroke-width: 2.5;
    }
  </style>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg-grad)" rx="16" />
  
  <!-- Outer Glow Border -->
  <rect x="2" y="2" width="796" height="216" fill="none" class="border-glow" rx="14" />

  <!-- Technical Grid Overlay -->
  <g opacity="0.04">
    <path d="M 0,20 L 800,20 M 0,40 L 800,40 M 0,60 L 800,60 M 0,80 L 800,80 M 0,100 L 800,100 M 0,120 L 800,120 M 0,140 L 800,140 M 0,160 L 800,160 M 0,180 L 800,180 M 0,200 L 800,200" stroke="#ffffff" stroke-width="1" />
    <path d="M 50,0 L 50,220 M 100,0 L 100,220 M 150,0 L 150,220 M 200,0 L 200,220 M 250,0 L 250,220 M 300,0 L 300,220 M 350,0 L 350,220 M 400,0 L 400,220 M 450,0 L 450,220 M 500,0 L 500,220 M 550,0 L 550,220 M 600,0 L 600,220 M 650,0 L 650,220 M 700,0 L 700,220 M 750,0 L 750,220" stroke="#ffffff" stroke-width="1" />
  </g>

  <!-- Left Info Panel -->
  <g transform="translate(60, 65)">
    <!-- Pill Badge -->
    <rect x="0" y="0" width="180" height="24" rx="12" fill="#1e293b" />
    <circle cx="12" cy="12" r="4" fill="#00f2fe">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="100" y="16" text-anchor="middle" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#38bdf8" letter-spacing="1.5">AI &amp; CLOUD ENGINEER</text>

    <!-- Name -->
    <text x="0" y="65" class="title">Polisetti Bharath</text>
    
    <!-- Subtitle -->
    <text x="0" y="98" class="subtitle">Cloud Computing &amp; Machine Learning</text>
    <text x="0" y="118" class="tagline">Designing next-generation intelligent applications &bull; B.Tech CSE Honors '28</text>
  </g>

  <!-- Right Neural Graphic -->
  <g transform="translate(560, 30)">
    <!-- Connection lines -->
    <line x1="40" y1="40" x2="100" y2="30" class="connection-active" />
    <line x1="40" y1="40" x2="60" y2="90" class="connection-active" />
    <line x1="100" y1="30" x2="140" y2="60" class="connection-active" />
    <line x1="60" y1="90" x2="140" y2="60" class="connection-active" />
    <line x1="60" y1="90" x2="100" y2="145" class="connection-active" />
    <line x1="140" y1="60" x2="180" y2="110" class="connection-active" />
    <line x1="100" y1="145" x2="180" y2="110" class="connection-active" />

    <!-- Outer Glow Orbs -->
    <circle cx="40" cy="40" r="14" fill="#00f2fe" opacity="0.2" class="node-pulse" />
    <circle cx="100" cy="30" r="12" fill="#a855f7" opacity="0.2" class="node-pulse" />
    <circle cx="60" cy="90" r="18" fill="#00f2fe" opacity="0.2" class="node-pulse" />
    <circle cx="140" cy="60" r="16" fill="#a855f7" opacity="0.2" class="node-pulse" />
    <circle cx="100" cy="145" r="14" fill="#00f2fe" opacity="0.2" class="node-pulse" />
    <circle cx="180" cy="110" r="20" fill="#a855f7" opacity="0.2" class="node-pulse" />

    <!-- Solid Core Nodes -->
    <circle cx="40" cy="40" r="6" fill="#00f2fe" />
    <circle cx="100" cy="30" r="5" fill="#a855f7" />
    <circle cx="60" cy="90" r="8" fill="#00f2fe" />
    <circle cx="140" cy="60" r="7" fill="#a855f7" />
    <circle cx="100" cy="145" r="6" fill="#00f2fe" />
    <circle cx="180" cy="110" r="9" fill="#a855f7" />

    <!-- Dynamic Orbiting Dots -->
    <circle cx="10" cy="70" r="3.5" fill="#1e293b" />
    <circle cx="20" cy="125" r="3.5" fill="#1e293b" />
    <circle cx="70" cy="175" r="3.5" fill="#1e293b" />
  </g>
</svg>"""

svg_footer = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 80" width="100%">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a0f1d" />
      <stop offset="100%" stop-color="#020408" />
    </linearGradient>
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe">
        <animate attributeName="stop-color" values="#00f2fe; #a855f7; #00f2fe" dur="5s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#a855f7">
        <animate attributeName="stop-color" values="#a855f7; #00f2fe; #a855f7" dur="5s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe">
        <animate attributeName="stop-color" values="#00f2fe; #a855f7; #00f2fe" dur="5s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#a855f7">
        <animate attributeName="stop-color" values="#a855f7; #00f2fe; #a855f7" dur="5s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
  </defs>
  <style>
    .footer-quote {
      font-family: 'Righteous', 'Segoe UI', -apple-system, sans-serif;
      font-size: 15px;
      fill: url(#text-grad);
      font-weight: 600;
      letter-spacing: 0.5px;
    }
    .footer-text {
      font-family: 'Inter', 'Segoe UI', -apple-system, sans-serif;
      font-size: 12px;
      fill: #64748b;
      font-weight: 600;
      letter-spacing: 2px;
    }
    .border-glow {
      stroke: url(#border-grad);
      stroke-width: 2.5;
    }
  </style>
  <rect width="100%" height="100%" fill="url(#bg-grad)" rx="12" />
  <rect x="2" y="2" width="796" height="76" fill="none" class="border-glow" rx="10" />
  <text x="40" y="46" class="footer-quote">Building intelligent systems, one algorithm at a time.</text>
  <text x="760" y="46" class="footer-text" text-anchor="end">EST. 2028</text>
</svg>"""

header_b64 = base64.b64encode(svg_header.encode('utf-8')).decode('utf-8')
footer_b64 = base64.b64encode(svg_footer.encode('utf-8')).decode('utf-8')

with open("scratch/header_b64.txt", "w") as f:
    f.write(f"data:image/svg+xml;base64,{header_b64}")

with open("scratch/footer_b64.txt", "w") as f:
    f.write(f"data:image/svg+xml;base64,{footer_b64}")

print("Encodings written successfully!")
