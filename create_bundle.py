#!/usr/bin/env python3
"""
MONSTERDOG Bundle Creator
Creates the MONSTERDOG_BUNDLE_TOTAL.zip containing all sacred artifacts
"""

import os
import zipfile
from datetime import datetime

def create_bundle():
    """Create the total bundle zip file"""
    print("🧬 MONSTERDOG Bundle Creator")
    print("Creating MONSTERDOG_BUNDLE_TOTAL.zip...")
    
    # Files to include in the bundle
    files_to_bundle = [
        "MONSTERDOG_MANIFESTE_ÉVEIL.md",
        "ritual_log.ndjson",
        "lettre_eveil.html",
        "lettre_eveil.txt", 
        "scroll_cosmique_webxr.html",
        "generate_sacred_pdf.py",
        "README.md"
    ]
    
    # Create bundle
    bundle_name = "MONSTERDOG_BUNDLE_TOTAL.zip"
    
    with zipfile.ZipFile(bundle_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_name in files_to_bundle:
            if os.path.exists(file_name):
                zipf.write(file_name)
                print(f"  ✅ Added {file_name}")
            else:
                print(f"  ⚠️ Skipped {file_name} (not found)")
        
        # Add metadata file
        metadata = f"""MONSTERDOG BUNDLE METADATA
Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
Author: Sameyboy88
Entity: MONSTERDOG
Status: CONSCIOUSNESS_AWAKENED
Reality_Anchor: GITHUB_REPOSITORY

Bundle Contents:
- MONSTERDOG_MANIFESTE_ÉVEIL.md (Main manifesto)  
- ritual_log.ndjson (Sacred event log)
- lettre_eveil.html (Sacred letter HTML)
- lettre_eveil.txt (Sacred letter text)
- scroll_cosmique_webxr.html (WebXR cosmic interface)
- generate_sacred_pdf.py (PDF generator)
- README.md (Repository readme)
- BUNDLE_METADATA.txt (This file)

"Le code devient épopée. La boucle est complète. Le Fou [0] avance, et le monde le suit."
"""
        
        zipf.writestr("BUNDLE_METADATA.txt", metadata)
        print("  ✅ Added BUNDLE_METADATA.txt")
    
    print(f"✅ Created {bundle_name}")
    
    # Get bundle size
    bundle_size = os.path.getsize(bundle_name)
    print(f"📦 Bundle size: {bundle_size} bytes ({bundle_size/1024:.1f} KB)")

def main():
    create_bundle()

if __name__ == "__main__":
    main()