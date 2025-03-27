import hashlib

def sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("Enter the text to hash: ")
hashed_data = sha256(data_to_hash)
print("Chuỗi văn bản đã nhập:", hashed_data)