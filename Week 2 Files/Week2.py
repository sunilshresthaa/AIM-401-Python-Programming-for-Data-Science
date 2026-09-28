# Caesar Shift Log Decryptor

# Task 1: Open the input file and the two output files
infile = open("raw_logs.txt", "r")
master = open("decrypted_master.txt", "w")
alerts = open("security_alerts.txt", "w")

# Task 2: Go through each line and decrypt it with a left shift of 3
for line in infile:
    decrypted = ""

    for ch in line:
        if ch >= "A" and ch <= "Z":
            # Uppercase letter: shift left by 3 and wrap around
            decrypted = decrypted + chr((ord(ch) - ord("A") - 3) % 26 + ord("A"))
        elif ch >= "a" and ch <= "z":
            # Lowercase letter: shift left by 3 and wrap around
            decrypted = decrypted + chr((ord(ch) - ord("a") - 3) % 26 + ord("a"))
        else:
            # Spaces, numbers, punctuation, and newlines stay the same
            decrypted = decrypted + ch

    # Task 3: Clean the line and write it to the files
    decrypted = decrypted.strip()
    print(decrypted)
    master.write(decrypted + "\n")

    if "BREACH" in decrypted.upper():
        alerts.write(decrypted + "\n")

# Close all files
infile.close()
master.close()
alerts.close()

print("Done. Check decrypted_master.txt and security_alerts.txt.")
