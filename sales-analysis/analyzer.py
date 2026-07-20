import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "../dummy folder/New Text Document (2).txt"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
    # Use 'with' to automatically handle closing the file
    with open(data_path, "r") as data:
        print(data.read()) # Read and print the contents
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")
