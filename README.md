#  Simple File Integrity Monitoring System (FIM)

A beginner-friendly **Python File Integrity Monitoring (FIM)** project that detects unauthorized or unexpected file modifications by comparing **SHA-256 hashes**.

The project creates a trusted **baseline hash** for a file and later compares the file's current hash against the original hash.

If both hashes are the same:

```text
 File is safe.
No changes detected.
```

If the hashes are different:

```text
 ALERT!
File has been modified!
```

---

##  Project Objective

The main objective of this project is to understand how a **File Integrity Monitoring system** can detect changes to important files.

For example, the original file contains:

```text
Hello Amandeep
```

The FIM calculates a SHA-256 hash:

```text
017fa86e6ce0df35c3dfce559ae2360ef1858eb69675251d30de3eb1d55ba8af
```

If the file is later changed to:

```text
Hello Amandeep How are you
```

the SHA-256 hash changes:

```text
a83be2f106f8cd9c8824a03bc4c62f0a1b3521f86c3e922c6fc1e359216c90d4
```

The FIM detects that the hashes are different and generates an alert.

---

#  What is File Integrity Monitoring?

**File Integrity Monitoring (FIM)** is a security technique used to monitor important files and detect unauthorized changes.

A FIM system can detect changes such as:

* File content modification
* File replacement
* File deletion
* Unexpected changes to important files

In this project, we use **SHA-256 hashing** to detect content changes.

---

#  What is SHA-256?

SHA-256 is a cryptographic hash function.

It creates a unique-looking digital fingerprint for a file.

For example:

```text
File:
Hello Amandeep

        ↓
     SHA-256
        ↓

017fa86e6ce0df35c3dfce559ae2360ef1858eb69675251d30de3eb1d55ba8af
```

If even a small part of the file changes:

```text
Hello Amandeep How are you
```

the resulting hash changes:

```text
a83be2f106f8cd9c8824a03bc4c62f0a1b3521f86c3e922c6fc1e359216c90d4
```

Therefore:

```text
Original Hash == Current Hash
        ↓
No modification
```

while:

```text
Original Hash != Current Hash
        ↓
 Modification detected
```

---

#  Project Architecture

```text
                  ┌─────────────────┐
                  │ important.txt   │
                  └────────┬────────┘
                           │
                           ↓
                    ┌─────────────┐
                    │   SHA-256   │
                    │ Hash Engine │
                    └──────┬──────┘
                           │
                  ┌────────┴────────┐
                  │                 │
                  ↓                 ↓
           Create Baseline      Later Check
                  │                 │
                  ↓                 ↓
          Original Hash        Current Hash
                  │                 │
                  ↓                 ↓
           ┌───────────────────────────┐
           │      Hash Comparison      │
           └────────────┬──────────────┘
                        │
              ┌─────────┴─────────┐
              ↓                   ↓
           Same Hash          Different Hash
              ↓                   ↓
         No Changes          ALERT
```

---

#  Project Structure

```text
Simple-FIM/
│
├── fim.py
├── important.txt
├── baseline.json
└── README.md
```

### `fim.py`

The main Python program.

It:

* Calculates SHA-256 hashes
* Creates the baseline
* Reads the saved baseline
* Compares original and current hashes
* Displays a security alert when a change is detected

### `important.txt`

The test file monitored by the FIM.

Example:

```text
Hello Amandeep
```

### `baseline.json`

Stores the trusted/original SHA-256 hash.

Example:

```json
{
    "important.txt": "017fa86e6ce0df35c3dfce559ae2360ef1858eb69675251d30de3eb1d55ba8af"
}
```

---

#  Technologies Used

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python 3   | Programming language     |
| `hashlib`  | SHA-256 hash calculation |
| `json`     | Store baseline hash      |
| `os`       | File existence checking  |
| Kali Linux | Testing environment      |
| Git/GitHub | Project management       |

No external Python package is required for this basic version because `hashlib`, `json`, and `os` are part of Python's standard library.

---

#  Installation

## 1. Create the project

```bash
mkdir ~/Simple-FIM
cd ~/Simple-FIM
```

Create the files:

```bash
touch fim.py
touch important.txt
```

---

## 2. Add test data

Run:

```bash
echo "Hello Amandeep" > important.txt
```

Check the file:

```bash
cat important.txt
```

Output:

```text
Hello Amandeep
```

---

#  Run the FIM

Run:

```bash
python3 fim.py
```

The program displays:

```text
===== Simple File Integrity Monitor =====
1. Create Baseline
2. Check File Integrity
3. Exit

Enter your choice:
```

---

#  Testing the Project

## Test 1 — Create the Baseline

Select:

```text
1
```

Output:

```text
Baseline created successfully.

SHA-256:
017fa86e6ce0df35c3dfce559ae2360ef1858eb69675251d30de3eb1d55ba8af
```

The hash is stored in:

```text
baseline.json
```

---

#  Test 2 — Check an Unmodified File

Select:

```text
2
```

Output:

```text
Original Hash:
017fa86e6ce0df35c3dfce559ae2360ef1858eb69675251d30de3eb1d55ba8af

Current Hash:
017fa86e6ce0df35c3dfce559ae2360ef1858eb69675251d30de3eb1d55ba8af

 File is safe.
No changes detected.
```

Because:

```text
Original Hash == Current Hash
```

the file has not changed.

---

#  Test 3 — Modify the File

Exit the program and modify the file:

```bash
echo "Hello Amandeep How are you" > important.txt
```

Check:

```bash
cat important.txt
```

Output:

```text
Hello Amandeep How are you
```

Now run:

```bash
python3 fim.py
```

Select:

```text
2
```

The result should be similar to:

```text
Original Hash:
017fa86e6ce0df35c3dfce559ae2360ef1858eb69675251d30de3eb1d55ba8af

Current Hash:
a83be2f106f8cd9c8824a03bc4c62f0a1b3521f86c3e922c6fc1e359216c90d4

 ALERT!
File has been modified!
```

This demonstrates successful file integrity detection.

---

#  Important Testing Rule

**Do not create a new baseline after modifying the file.**

The baseline represents the **trusted/original state**.

Correct workflow:

```text
Create Baseline
      ↓
Original Hash Saved
      ↓
Modify File
      ↓
Check Integrity
      ↓
Compare Hashes
      ↓
 Alert
```

Incorrect workflow:

```text
Create Baseline
      ↓
Modify File
      ↓
 Create New Baseline
      ↓
Check Integrity
      ↓
Hashes Match
      ↓
No Alert
```

If you create a new baseline after modifying the file, the modified file becomes the new "trusted" version.

---

#  Complete Workflow

```text
             START
               │
               ↓
       Select File to Monitor
               │
               ↓
        Calculate SHA-256
               │
               ↓
        Create Baseline
               │
               ↓
       Save Original Hash
               │
               ↓
          Wait / Later
               │
               ↓
        Calculate Hash Again
               │
               ↓
       Compare Two Hashes
               │
        ┌──────┴──────┐
        ↓             ↓
      Same         Different
        ↓             ↓
    No Change     ALERT
```

---

#  How the Python Code Works

The project uses:

```python
import hashlib
```

to calculate SHA-256.

The important function is:

```python
def calculate_hash(filename):

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()
```

The file is read in small chunks and passed to SHA-256.

Finally:

```python
sha256.hexdigest()
```

returns the file's hash.

---

#  Security Use Case

FIM can be useful for monitoring sensitive files.

For example:

```text
/etc/passwd
/etc/ssh/sshd_config
Application configuration files
Web server files
Important scripts
Security configuration files
```

A simplified SOC workflow could be:

```text
Important File
      ↓
FIM
      ↓
Hash Changed
      ↓
Security Alert
      ↓
SOC Analyst
      ↓
Investigate
```

A hash change does **not automatically mean an attack**. An authorized administrator or software update can also change a file.

The SOC analyst should investigate the event and determine whether the modification was authorized.

---

#  Future Improvements

This basic project can be expanded into a more realistic FIM tool.

Possible improvements:

* Monitor multiple files
* Monitor entire directories
* Detect file creation
* Detect file deletion
* Detect file modification
* Record timestamps
* Create an alert log
* Send email alerts
* Add a web dashboard
* Integrate with a SIEM
* Integrate with Wazuh
* Add user/process information
* Protect the baseline from unauthorized modification
* Run continuously instead of using manual checks

---

#  Possible SOC Integration

A future version could send FIM alerts to a SIEM such as Wazuh.

Example:

```text
File Modified
      ↓
Python FIM
      ↓
Security Event
      ↓
Wazuh / SIEM
      ↓
SOC Dashboard
      ↓
Analyst Investigation
```

This would make the project more relevant to a **SOC Analyst portfolio**.

---

#  Learning Outcomes

After completing this project, you will understand:

* What File Integrity Monitoring is
* What SHA-256 hashing is
* How file hashes work as digital fingerprints
* How to create a trusted baseline
* How to compare file hashes
* How modifications can be detected
* Basic Python file handling
* JSON data storage
* Basic security alert generation
* How FIM can be used in a SOC environment

---

#  Limitations

This is a **learning/demo FIM tool**, not a production security product.

The current version:

* Monitors only one file
* Requires manual checking
* Stores the baseline locally
* Does not automatically monitor changes in real time
* Does not identify who modified the file
* Does not identify which process modified the file
* Does not send alerts to a SIEM
* Does not protect the baseline from tampering

These limitations can be addressed in future versions.

---

#  Author

**Amandeep Singh**

Cybersecurity / SOC Analyst Learning Project

---

# Disclaimer

This project is developed for **educational and cybersecurity learning purposes**. It is intended to demonstrate the basic concept of File Integrity Monitoring using SHA-256 hashes.
