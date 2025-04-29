import hashlib

# Creating different hashes
message = "Hello, World!"
hash_object = hashlib.sha256(message.encode())
print(hash_object.hexdigest())

# Output: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f

# Even a small change creates a completely different hash
message2 = "Hello, World"  # Removed the !
hash_object2 = hashlib.sha256(message2.encode())
print(hash_object2.hexdigest())
# Output: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f

