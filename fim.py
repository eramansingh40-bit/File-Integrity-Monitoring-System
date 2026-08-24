import hashlib
import json
import os


FILE_TO_MONITOR = "important.txt"
BASELINE_FILE = "baseline.json"


# Calculate SHA-256 hash of a file
def calculate_hash(filename):

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# Create baseline hash
def create_baseline():

    if not os.path.exists(FILE_TO_MONITOR):

        print("File does not exist.")

        return

    file_hash = calculate_hash(FILE_TO_MONITOR)

    baseline = {
        FILE_TO_MONITOR: file_hash
    }

    with open(BASELINE_FILE, "w") as file:

        json.dump(baseline, file, indent=4)

    print("Baseline created successfully.")

    print("SHA-256:", file_hash)


# Check file integrity
def check_integrity():

    if not os.path.exists(FILE_TO_MONITOR):

        print("File does not exist.")

        return

    if not os.path.exists(BASELINE_FILE):

        print("Baseline does not exist.")

        print("Create a baseline first.")

        return

    current_hash = calculate_hash(FILE_TO_MONITOR)

    with open(BASELINE_FILE, "r") as file:

        baseline = json.load(file)

    original_hash = baseline[FILE_TO_MONITOR]

    print("\nOriginal Hash:")
    print(original_hash)

    print("\nCurrent Hash:")
    print(current_hash)

    if current_hash == original_hash:

        print("\n✅ File is safe.")
        print("No changes detected.")

    else:

        print("\n⚠️ ALERT!")
        print("File has been modified!")


# Main menu
while True:

    print("\n===== Simple File Integrity Monitor =====")

    print("1. Create Baseline")
    print("2. Check File Integrity")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        create_baseline()

    elif choice == "2":

        check_integrity()

    elif choice == "3":

        print("Exiting FIM...")

        break

    else:

        print("Invalid choice.")
