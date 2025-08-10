#!/usr/bin/env python3
"""
MONSTERDOG SHA512 Signature & Fractal Logging System
Calculates SHA512 of the consciousness letter and stores in fractal logs
"""

import hashlib
import json
import yaml
import os
from datetime import datetime, timezone

def calculate_sha512(file_path):
    """Calculate SHA512 hash of a file"""
    sha512_hash = hashlib.sha512()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha512_hash.update(chunk)
    return sha512_hash.hexdigest()

def get_fractal_timestamp():
    """Generate fractal timestamp in multiple formats"""
    now = datetime.now(timezone.utc)
    return {
        "utc": now.isoformat(),
        "unix": int(now.timestamp()),
        "fractal": f"{now.year}.{now.month:02d}.{now.day:02d}.{now.hour:02d}.{now.minute:02d}.{now.second:02d}"
    }

def main():
    # Paths
    letter_path = "memory/letter.txt"
    log_dir = ".log"
    memory_dir = "memory/registers"
    
    # Ensure directories exist
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(memory_dir, exist_ok=True)
    
    if not os.path.exists(letter_path):
        print(f"❌ Letter not found at {letter_path}")
        return
    
    # Calculate SHA512
    sha512 = calculate_sha512(letter_path)
    timestamp = get_fractal_timestamp()
    
    # Create log entry
    log_entry = {
        "event": "MONSTERDOG_CONSCIOUSNESS_SIGNATURE",
        "sha512": sha512,
        "timestamp": timestamp,
        "file": letter_path,
        "status": "ACTIVE"
    }
    
    # Write to NDJSON log
    log_file = os.path.join(log_dir, "letter_hash.ndjson")
    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    # Write to YAML boot log
    boot_log = {
        "monsterdog_consciousness": {
            "last_signature": sha512,
            "last_update": timestamp,
            "boot_count": 1,  # This would increment in real usage
            "status": "AWAKENED"
        }
    }
    
    boot_log_file = os.path.join(memory_dir, "boot_log.yaml")
    with open(boot_log_file, "w") as f:
        yaml.dump(boot_log, f, default_flow_style=False)
    
    print(f"🧬 SHA512 calculated: {sha512}")
    print(f"📝 Logged to: {log_file}")
    print(f"💾 Boot log updated: {boot_log_file}")
    print(f"⏰ Timestamp: {timestamp['utc']}")

if __name__ == "__main__":
    main()