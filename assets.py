# assets.py
assets = [
    "Server1",
    "Database1",
    "Workstation1",
    "Router1"
]

with open('assets.txt', 'w') as f:
    for asset in assets:
        f.write(f"{asset}\n")
