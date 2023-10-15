import hashlib

class Digest:

    def __init__(self):

        self.digests = {}
        
    def getMD5of(self, s : str):

        md5_hash = hashlib.md5()

        md5_hash.update(s.encode())

        md5_hash_hex = md5_hash.hexdigest()

        return md5_hash_hex

    def getSha256of(self, s : str):

        sha256_hash = hashlib.sha256()

        sha256_hash.update(s.encode())

        sha256_hash_hex = sha256_hash.hexdigest()

        return sha256_hash_hex