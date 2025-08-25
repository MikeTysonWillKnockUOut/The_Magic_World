# c1
def c1(string):
  return len(string)
print(c1("google.com"))
# c2
def c2(string):
    frequency = {i: string.count(i) for i in string}
    return frequency
print(c2("google.com"))
# c3
def c3(string):
    try:
      new_string = string[0]+string[1]+string[-2]+string[-1]
      return new_string
    except:
      return "Empty String"
print(c3("w3resource"), c3("w3"), c3(" w"))
# 4
def c4(string):
  first = string[0]
  new_string = first
  for i in string[1::]:
    if i == first:
      i = "$"
    new_string += i
  return new_string
print(c4("restart"))
# c5
def c5(string_1,string_2):
  return string_2 + " " + string_1
print(c5("abc", "xyz"))
# c6
def c6(string):
  if len(string) < 3:
    return string
  elif string[-3:] == "ing":
    return string + "ly"
  return string + "ing"
print(c6("abc"), c6("string"))
#c7
def c7(string):
  try:
    if string.index('not') < string.index('poor'):
      return string[:string.index('not')] + 'good' + string[string.index('poor')+4:]
  except:
    return string
print(c7("The lyrics is not that poor!"), c7("The lyrics is poor!"))
# c8
def c8(list):
  longest_word = list[0]
  for i in list[1::]:
    if len(i) > len(longest_word):
      longest_word = i
  return 'longest_word: ' + longest_word + ' length: ' + str(len(longest_word))
print(c8(["Exercises", "Python", "Code"]))
# c9
def  c9(string,n):
  return string.replace(string[n],'')
print(c9("w3resource", 2))
# c10
def c10(string):
  return string[-1] + string[1:-1] + string[0]
print(c10("w3resource"))
# c11
def c11(string):
  new_string = ''
  for i in range(len(string)):
    if i % 2 == 0:
      new_string += string[i]
  return new_string
print(c11("w3resource"))
# c12
def c12(string):
    frequency = {i: string.count(i) for i in string}
    return frequency
print(c12("the quick brown"))
# c13
def c13(string):
  return 'Upper: ' + string.upper() + ' Lower: ' + string.lower()
print(c13("Python"))
# c14
def c14(string):
  list = string.split(',')
  list.sort()
  return list
print(c14("red,white,black,red,green,black"))
# c15
def c15(a,b):
  return f'<{a}>{b}</{a}>'
print(c15("i", "Python"), c15("b", "Python Tutorial"))
# 16
def c16(a,b):
  return a[:len(a)//2] + b + a[len(a)//2:]
print(c16("[[]]<<>>", "Python"), c16("{{}}", "PHP"))
# 17
def c17(string):
  return string[-2:] + string[-2:] +string[-2:] +string[-2:]
print(c17("Python"), c17("Exercises"))
# 18
def c18(string):
  try:
    return string[:3]
  except:
    return string
print(c18("ipy"), c18("python"))
# 19
def c19(string,k):
  return string[:string.index(k)]
print(c19("https://www.w3resource.com/python", "/"))
# 20
def c20(string):
  if len(string) % 4 == 0:
    return string[::-1]
  return string
print(c20("abcd"), c20("abc"))
# 21
def c21(string):
  count = sum(1 if i.isupper() else 0 for i in string[:4])
  if count >= 2:
    return string.upper()
  return string
print(c21("PYthOn"))
# 22
def c22(string):
  if len(string)<=1:
    return string
  p = string[0]
  l = ''.join([i for i in string[1:] if i.lower() <= p.lower()])
  r = ''.join([i for i in string[1:] if i.lower() > p.lower()])
  return c22(l) + p + c22(r)
print(c22("w3resource"))
# 23
def c23(text):
    return text.replace("\n", " ")
print(c23("Hello\nWorld"))
# 24
def c24(string,list_characters):
  if string[0] in list_characters:
    return True
  return False
print(c24("Python", ['P', 'J']))
# 25
def c25(string, k):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in string.lower():
        if i in alphabet_lower:
            new_index = (alphabet_lower.index(i) + k) % 26
            result += alphabet_lower[new_index]
        else:
            result += i
    return result
print(c25("Python", 3))
# 26
def c26(text):
    text = c23(text)
    k = 50
    u = 0
    while u + k < len(text):
        cut = u + k
        while cut > u and text[cut] != ' ':
            cut -= 1
        if cut == u:
            cut = u + k
        print(text[u:cut].strip())
        u = cut + 1
    print(text[u:])
    return
print(c26("The quick brown fox jumps over the lazy dog"))
# 27
def c27(text):
  lines = text.splitlines()
  lst = [i.lstrip() for i in lines]
  return '\n'.join(lst)
print(c27("    Hello\n        World"))
# 28
def c28(text, prefix_text):
  lines = text.splitlines()
  lst = [prefix_text + i for i in lines]
  return '\n'.join(lst)
print(c28("Hello\nWorld", ">> "))
# 29
def c29(text, indent):
    lines = text.splitlines()
    if lines:
        lines[0] = ' ' * indent + lines[0].lstrip()
    return '\n'.join(lines)
print(c29("Hello\nWorld", 4))
# 30
def c30(numbers):
  return [f'{n:.2f}' for n in numbers]
print(c30([3.14159, 2.71828]))
# 31
def c31(numbers):
  return [f'{n:+.2f}' for n in numbers]
print(c31([3.14159, -2.71828]))
# 32
def c32(numbers):
  return [f'{int(n): d}' for n in numbers]
print(c32([3.14159, -2.71828]))
# 33
def c33(number, width):
    return f"{number:0{width}d}"
print(c33(42, 5))
# 34
def c34(number, width):
    return f"{number:*<{width}}"
print(c34(42, 5))
# 35
def c35(number):
    return f"{number:,}"
print(c35(1234567))
# 36
def c36(number):
    return f"{number:.2%}"
print(c36(0.75))
# 37
def c37(number):
    print(f"{number:<10}")
    print(f"{number:>10}")
    print(f"{number:^10}")
print(c37(42))
# 38
def c38(string, sub):
    return string.count(sub)
print(c38("hello hello", "hello"))
# 39
def c39(string):
    return string[::-1]
print(c39("Python"))
# 40
def c40(string):
    return ' '.join(reversed(string.split()))
print(c40("The quick brown"))
# 41
def c41(string, chars):
    return ''.join(c for c in string if c not in chars)
print(c41("Python", "yt"))
# 42
def c42(string):
    freq = {}
    for c in string:
        freq[c] = freq.get(c, 0) + 1
    repeated = {k: v for k, v in freq.items() if v > 1}
    return repeated
print(c42("thequickbrownfoxjumpsoverthelazydog"))
#43
def c43(area, volume):
    print(f"The area of the rectangle is {area}cm\u00b2")
    print(f"The volume of the cylinder is {volume}cm\u00b3")
print(c43(1256.66, 1254.725))
# 44
def c44(string):
    for i, c in enumerate(string):
        print(f"Current character {c} position at {i}")
print(c44("w3resource"))
# 45
def c45(string):
    return set(string.lower()) >= set('abcdefghijklmnopqrstuvwxyz')
print(c45("abcdefghijklmnopqrstuvwxyz"))
# 46
def c46(string):
    return string.split()
print(c46("The quick brown fox"))
# 47
def c47(string, n):
    return string[:n].lower() + string[n:]
print(c47("Python", 2))
#48
def c48(string):
    string = string.replace(',', '@').replace('.', ',').replace('@', '.')
    return string
print(c48("32.054,23"))
#49
def c49(text):
    vowels = 'aeiouAEIOU'
    count = sum(1 for c in text if c in vowels)
    print(count)
    for v in vowels:
        if text.count(v) > 0:
            print(v, text.count(v))
print(c49("hello"))
# 50
def c50(string, delim):
    return string.rsplit(delim, 1)
print(c50("a,b,c", ","))
# 51
def c51(string):
    seen = {}
    for c in string:
        seen[c] = seen.get(c, 0) + 1
    for c in string:
        if seen[c] == 1:
            return c
    return None
print(c51("abcba"))
# 52
def c52(string, rep):
    from itertools import product
    return [''.join(p) for p in product(string, repeat=rep)]
print(c52("ab", 2))
# 53
def c53(string):
    seen = set()
    for c in string:
        if c in seen:
            return c
        seen.add(c)
    return None
print(c53("abcba"))
# 54
def c54(string):
    seen = {}
    min_index = len(string)
    first_repeated = None
    for i, c in enumerate(string):
        if c in seen and seen[c] < min_index:
            min_index = seen[c]
            first_repeated = c
        seen[c] = i
    return first_repeated
print(c54("abcba"))
# 55
def c55(string):
    words = string.split()
    seen = set()
    for w in words:
        if w in seen:
            return w
        seen.add(w)
    return None
print(c55("the quick the"))
# 56
def c56(string):
    words = string.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[1][0] if len(sorted_freq) > 1 else None
print(c56("the quick the quick brown"))
# 57
def c57(string):
    return string.replace(' ', '')
print(c57("the quick brown"))
# 58
def c58(string):
    spaces = ' ' * string.count(' ')
    return spaces + string.replace(' ', '')
print(c58("the quick brown"))
# 59
def c59(string):
    freq = {}
    for c in string:
        freq[c] = freq.get(c, 0) + 1
    max_count = max(freq.values())
    return max_count
print(c59("thequickbrownfox"))
# 60
def c60(string):
    words = string.split()
    return ' '.join(w[0].upper() + w[1:-1].lower() + w[-1].upper() if len(w) > 1 else w.upper() for w in words)
print(c60("the quick brown"))
