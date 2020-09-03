import re
def word_count(s):       
    ignore = '":;,.-+=/\\|[]{}()*^&'
  
    d = {}
    for i in ignore:
        s = s.replace(i, "") 
    s = s.split() 
    for word in s:
        word = word.lower()
        if word not in d:
            d[word] = 0
        d[word] += 1 
    return d




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))