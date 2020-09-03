# Your code here

f = open(r"C:\Users\iulia\Desktop\CS_2\cs-module-project-hash-tables\applications\histo\robin.txt")
robin = f.read()

def histo(t):
    cache = {}
    punct = '":;,.-+=/\\|[]{}()*^&?'

    for p in punct:
        t = t.replace(p, '')
    t = t.split()

    for word in t:
        word = word.lower()
        if word not in cache:
            cache[word] = 0
        cache[word] += 1
    cache = {k: v for k, v in sorted(cache.items(), key=lambda item: item[1], reverse = True)}
    for i, b in cache.items():
        print(i, b * "#")
   

print(histo(robin))