user = {"name": "Alice", "age": 25}
print(user["email"])  # KeyError - no email key
# Check if key exists
if "email" in user:
    print(user["email"])

# Use get() with default
email = user.get("email", "no-email@example.com")

# Or handle the error
try:
    print(user["email"])
except KeyError:
    print("Email not found")