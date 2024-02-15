import os
import uuid

secrete1 = os.urandom(12)

secrete2 = uuid.uuid4().hex

print(f"SECRETE KEY FROM os:\n {secrete1}")
print("")
print(f"SECRETE KEY FROM uuid:\n {secrete2}")

