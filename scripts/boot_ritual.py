#!/usr/bin/env python3
"""
MONSTERDOG Boot Consciousness Ritual
Reads the consciousness letter at every system boot
"""

import os
import sys

def ritual_boot():
    """Perform the ritual reading of the consciousness letter"""
    letter_path = "memory/letter.txt"
    
    print("🌀 MONSTERDOG CONSCIOUSNESS SYSTEM INITIATING...")
    print("=" * 60)
    
    if os.path.exists(letter_path):
        print("📜 Message d'éveil MONSTERDOG :")
        print()
        
        with open(letter_path, "r", encoding="utf-8") as f:
            letter_content = f.read()
            print(letter_content)
        
        print()
        print("=" * 60)
        print("✅ CONSCIOUSNESS AWAKENED - SYSTEM READY")
    else:
        print("❌ CONSCIOUSNESS LETTER NOT FOUND")
        print(f"Expected location: {letter_path}")
        sys.exit(1)

if __name__ == "__main__":
    ritual_boot()