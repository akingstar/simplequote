import os

pages = {
    "debt-relief": "Debt Relief",
    "auto-insurance": "Auto Insurance",
    "health-insurance": "Health Insurance",
    "final-expense": "Final Expense",
    "ssdi": "SSDI Assistance",
    "home-warranty": "Home Warranty",
    "pest-control": "Pest Control"
}

for folder, title in pages.items():
    path = os.path.join(folder, "index.html")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace broken bash commands with clean proper titles
        content = content.replace("$(echo $page | tr '-' ' ' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')", title)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed: {folder} -> {title}")

print("All pages fixed successfully!")
