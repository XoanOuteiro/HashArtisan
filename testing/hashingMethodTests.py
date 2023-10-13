import hashlib

def getMD5of(input_string):

    md5_hash = hashlib.md5()

    md5_hash.update(input_string.encode())

    md5_hash_hex = md5_hash.hexdigest()

    return md5_hash_hex

def getSha256of(input_string):

    sha256_hash = hashlib.sha256()

    sha256_hash.update(input_string.encode())

    sha256_hash_hex = sha256_hash.hexdigest()

    return sha256_hash_hex


a : str = "Test1"
b : str = "Test1"
c : str = "abc123"

a_MD5 : str = getMD5of(a)
b_MD5 : str = getMD5of(b)
c_MD5 : str = getMD5of(c)

a_sha : str = getSha256of(a)
b_sha : str = getSha256of(b)
c_sha : str = getSha256of(c)

print(f"{a} str -> \t {a_MD5} MD5 || \t {a_sha} Sha-256")
print(f"{b} str -> \t {b_MD5} MD5 || \t {b_sha} Sha-256")
print(f"{c} str -> \t {c_MD5} MD5 || \t {c_sha} Sha-256")