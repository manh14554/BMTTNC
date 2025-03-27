import hashlib

def md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()

data = input("Enter the text to hash: ")
md5_hash = md5(data)
print("Mã băm MD5 của chuỗi '{}' là: {}".format(data, md5_hash))