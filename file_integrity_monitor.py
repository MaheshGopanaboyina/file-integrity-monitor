import hashlib
import os
import json
import time

# Configuration
MONITORED_DIR = "./monitored_files"
HASH_DB_FILE = "file_hashes.json"

def calculate_file_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def load_hashes():
    if os.path.exists(HASH_DB_FILE):
        with open(HASH_DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_DB_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def scan_and_compare():
    stored_hashes = load_hashes()
    current_hashes = {}
    changes = []

    # Walk through monitored directory
    for root, dirs, files in os.walk(MONITORED_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            relpath = os.path.relpath(filepath, MONITORED_DIR)
            file_hash = calculate_file_hash(filepath)
            current_hashes[relpath] = file_hash

            if relpath not in stored_hashes:
                changes.append(f"[NEW FILE] {relpath}")
            elif stored_hashes[relpath] != file_hash:
                changes.append(f"[MODIFIED] {relpath}")

    # Detect deleted files
    for old_file in stored_hashes:
        if old_file not in current_hashes:
            changes.append(f"[DELETED] {old_file}")

    if changes:
        print("\n🔍 Detected Changes:")
        for change in changes:
            print("  " + change)
    else:
        print("\n✅ No changes detected.")

    # Save current hashes
    save_hashes(current_hashes)

if __name__ == "__main__":
    print("🔐 File Integrity Monitor Started")
    print(f"Monitoring folder: {MONITORED_DIR}")
    scan_and_compare()
