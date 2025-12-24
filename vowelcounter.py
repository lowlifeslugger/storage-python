def proto_vowel_counter():
    script = input("text : ").lower()
    a = (script.count("a"))
    e = (script.count("e"))
    i = (script.count("i"))
    o = (script.count("o"))
    u = (script.count("u"))
    print(a+e+i+o+u)

def vowel_counter_2():
    total = 0
    script = input("text : ").lower()
    vowels = "aeiou"
    for v in vowels:
        total += script.count(v) 
    print(total)
   