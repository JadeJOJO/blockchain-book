from hashlib import sha256

file = open("chapters/chapter_2/hashing_files/images/cape-town-original.jpg", "rb")
file = open("chapters/chapter_2/hashing_files/images/cape-town-modified.jpg", "rb")
hash = sha256(file.read()).hexdigest()
file.close()

print(f"The hash of my file is: {hash}")
