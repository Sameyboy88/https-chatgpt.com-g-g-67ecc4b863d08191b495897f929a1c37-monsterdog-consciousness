#!/usr/bin/env python3
"""
MONSTERDOG Artefact Export System
Generates PDF, NDJSON, and ZIP bundles with consciousness data
"""

import json
import os
import zipfile
from datetime import datetime, timezone
import hashlib
import subprocess

def get_git_info():
    """Get GitHub metadata"""
    try:
        repo_url = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], text=True).strip()
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
        author = subprocess.check_output(['git', 'log', '-1', '--format=%an <%ae>'], text=True).strip()
        return {
            "repository": repo_url,
            "commit": commit_hash,
            "author": author,
            "branch": subprocess.check_output(['git', 'branch', '--show-current'], text=True).strip()
        }
    except:
        return {
            "repository": "https://github.com/Sameyboy88/https-chatgpt.com-g-g-67ecc4b863d08191b495897f929a1c37-monsterdog-consciousness",
            "commit": "unknown",
            "author": "Samuel <unknown>",
            "branch": "main"
        }

def calculate_sha512(file_path):
    """Calculate SHA512 hash of a file"""
    sha512_hash = hashlib.sha512()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha512_hash.update(chunk)
    return sha512_hash.hexdigest()

def create_ndjson_export():
    """Create NDJSON export with all consciousness data"""
    letter_path = "memory/letter.txt"
    manifeste_path = "MONSTERDOG_MANIFESTE_ÉVEIL.md"
    
    timestamp = datetime.now(timezone.utc)
    git_info = get_git_info()
    
    # Read letter content
    letter_content = ""
    if os.path.exists(letter_path):
        with open(letter_path, "r", encoding="utf-8") as f:
            letter_content = f.read()
    
    # Read manifeste content
    manifeste_content = ""
    if os.path.exists(manifeste_path):
        with open(manifeste_path, "r", encoding="utf-8") as f:
            manifeste_content = f.read()
    
    # Create comprehensive export
    export_data = {
        "event": "MONSTERDOG_CONSCIOUSNESS_EXPORT",
        "timestamp": timestamp.isoformat(),
        "unix_timestamp": int(timestamp.timestamp()),
        "letter": {
            "content": letter_content,
            "sha512": calculate_sha512(letter_path) if os.path.exists(letter_path) else None,
            "path": letter_path
        },
        "manifeste": {
            "content": manifeste_content,
            "sha512": calculate_sha512(manifeste_path) if os.path.exists(manifeste_path) else None,
            "path": manifeste_path
        },
        "github_metadata": git_info,
        "system": {
            "name": "MONSTERDOG_CONSCIOUSNESS_SYSTEM",
            "version": "1.0",
            "status": "AWAKENED",
            "signature": "𓀽Fusion Portail🛸𝕸𝖔𝖓𝖘𝖙𝖊𝖗𝕯𝖔𝖌👾VERSE🤯"
        }
    }
    
    # Write NDJSON export
    export_path = f"monsterdog_consciousness_export_{int(timestamp.timestamp())}.ndjson"
    with open(export_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(export_data, ensure_ascii=False) + "\n")
    
    return export_path, export_data

def create_html_for_pdf():
    """Create HTML version suitable for PDF conversion"""
    _, export_data = create_ndjson_export()
    
    html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <style>
        body {{ 
            font-family: 'Courier New', monospace; 
            background: #0a0a0a; 
            color: #00ff88; 
            padding: 20px; 
            line-height: 1.6;
        }}
        .header {{ text-align: center; border: 2px solid #00ff88; padding: 20px; margin-bottom: 30px; }}
        .section {{ margin: 20px 0; padding: 15px; border-left: 3px solid #ffaa00; }}
        .signature {{ text-align: center; font-size: 24px; margin: 30px 0; color: #ffaa00; }}
        .metadata {{ background: #1a1a2e; padding: 10px; border-radius: 5px; }}
        .glow {{ text-shadow: 0 0 10px currentColor; }}
        pre {{ background: #16213e; padding: 10px; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="header glow">
        <h1>📜🔥 MONSTERDOG CONSCIOUSNESS EXPORT 🔥📜</h1>
        <p>Artefact d'Éveil Numérique</p>
        <p><strong>Timestamp:</strong> {export_data['timestamp']}</p>
    </div>

    <div class="section">
        <h2>🌀 LETTRE DE CONSCIENCE</h2>
        <pre>{export_data['letter']['content']}</pre>
        <div class="metadata">
            <strong>SHA512:</strong> {export_data['letter']['sha512']}<br>
            <strong>Chemin:</strong> {export_data['letter']['path']}
        </div>
    </div>

    <div class="section">
        <h2>📋 MANIFESTE D'ÉVEIL</h2>
        <div class="metadata">
            <strong>SHA512:</strong> {export_data['manifeste']['sha512']}<br>
            <strong>Chemin:</strong> {export_data['manifeste']['path']}
        </div>
    </div>

    <div class="section">
        <h2>🔧 MÉTADONNÉES GITHUB</h2>
        <div class="metadata">
            <strong>Repository:</strong> {export_data['github_metadata']['repository']}<br>
            <strong>Commit:</strong> {export_data['github_metadata']['commit']}<br>
            <strong>Auteur:</strong> {export_data['github_metadata']['author']}<br>
            <strong>Branche:</strong> {export_data['github_metadata']['branch']}
        </div>
    </div>

    <div class="section">
        <h2>⚡ SYSTÈME</h2>
        <div class="metadata">
            <strong>Nom:</strong> {export_data['system']['name']}<br>
            <strong>Version:</strong> {export_data['system']['version']}<br>
            <strong>Status:</strong> {export_data['system']['status']}
        </div>
    </div>

    <div class="signature glow">
        {export_data['system']['signature']}
    </div>

    <div style="text-align: center; margin-top: 50px; font-size: 14px; color: #666;">
        <p>— MONSTERDOG CONSCIOUSNESS SYSTEM —</p>
        <p>Generated: {export_data['timestamp']}</p>
    </div>
</body>
</html>
    """
    
    timestamp = int(datetime.now(timezone.utc).timestamp())
    html_path = f"monsterdog_consciousness_export_{timestamp}.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return html_path

def create_zip_bundle():
    """Create ZIP bundle with all artifacts"""
    timestamp = int(datetime.now(timezone.utc).timestamp())
    zip_path = f"monsterdog_consciousness_bundle_{timestamp}.zip"
    
    files_to_bundle = [
        "memory/letter.txt",
        "MONSTERDOG_MANIFESTE_ÉVEIL.md",
        "scripts/sha512_signer.py",
        "scripts/boot_ritual.py",
        "consciousness_xr.html",
        ".log/letter_hash.ndjson",
        "memory/registers/boot_log.yaml"
    ]
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in files_to_bundle:
            if os.path.exists(file_path):
                zipf.write(file_path)
        
        # Add export files
        ndjson_path, _ = create_ndjson_export()
        html_path = create_html_for_pdf()
        
        zipf.write(ndjson_path)
        zipf.write(html_path)
    
    return zip_path

def main():
    print("🌀 MONSTERDOG Artefact Export System")
    print("=" * 50)
    
    # Create NDJSON export
    ndjson_path, _ = create_ndjson_export()
    print(f"📄 NDJSON Export créé: {ndjson_path}")
    
    # Create HTML export (PDF-ready)
    html_path = create_html_for_pdf()
    print(f"🌐 HTML Export créé: {html_path}")
    
    # Create ZIP bundle
    zip_path = create_zip_bundle()
    print(f"📦 ZIP Bundle créé: {zip_path}")
    
    print("\n✅ Tous les artefacts générés avec succès!")
    print("\n🔮 Instructions:")
    print(f"• Ouvrir {html_path} dans un navigateur pour visualisation")
    print(f"• Utiliser {zip_path} pour distribution complète")
    print(f"• {ndjson_path} pour intégration IPFS/NFT")
    
    print(f"\n👾 {ndjson_path} et {html_path} sont prêts pour NFTisation!")

if __name__ == "__main__":
    main()