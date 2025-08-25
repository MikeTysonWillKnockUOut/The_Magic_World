# c1
def c1(string):
  return len(string)
# c2
def c2(string):
    frequency = {i: string.count(i) for i in string}
    return frequency
# c3
def c3(string):
    try:
      new_string = string[0]+string[1]+string[-2]+string[-1]
      return new_string
    except:
      return "Empty String"
# 4
def c4(string):
  first = string[0]
  new_string = first
  for i in string[1::]:
    if i == first:
      i = "$"
    new_string += i
  return new_string
# c5
def c5(string_1,string_2):
  return string_2 + " " + string_1
# c6
def c6(string):
  if len(string) < 3:
    return string
  elif string[-3:] == "ing":
    return string + "ly"
  return string + "ing"
#c7
def c7(string):
  try:
    if string.index('not') < string.index('poor'):
      return string[:string.index('not')] + 'good' + string[string.index('poor')+4:]
  except:
    return string
# c8
def c8(list):
  longest_word = list[0]
  for i in list[1::]:
    if len(i) > len(longest_word):
      longest_word = i
  return 'longest_word: ' + longest_word + ' length: ' + str(len(longest_word))
# c9
def  c9(string,n):
  return string.replace(string[n],'')
# c10
def c10(string):
  return string[-1] + string[1:-1] + string[0]
# c11
def c11(string):
  new_string = ''
  for i in range(len(string)):
    if i % 2 == 0:
      new_string += string[i]
  return new_string
# c12
def c12(string):
    frequency = {i: string.count(i) for i in string}
    return frequency
# c13
def c13(string):
  return 'Upper: ' + string.upper() + ' Lower: ' + string.lower()
# c14
def c14(string):
  list = string.split(',')
  list.sort()
  return list
# c15
def c15(a,b):
  return f'<{a}>{b}</{a}>'
# 16
def c16(a,b):
  return a[:len(a)//2] + b + a[len(a)//2:]
# 17
def c17(string):
  return string[-2:] + string[-2:] +string[-2:] +string[-2:]
# 18
def c18(string):
  try:
    return string[:3]
  except:
    return string
# 19
def c19(string,k):
  return string[:string.index(k)]
# 20
def c20(string):
  if len(string) % 4 == 0:
    return string[::-1]
  return string
# 21
def c21(string):
  count = sum(1 if i.isupper() else 0 for i in string[:4])
  if count >= 2:
    return string.upper()
  return string
# 22
def c22(string):
  if len(string)<=1:
    return string
  p = string[0]
  l = ''.join([i for i in string[1:] if i.lower() <= p.lower()])
  r = ''.join([i for i in string[1:] if i.lower() > p.lower()])
  return c22(l) + p + c22(r)
# 23
def c23(text):
    return text.replace("\n", " ")
# 24
def c24(string,list_characters):
  if string[0] in list_characters:
    return True
  return False
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
# 27
def c27(text):
  lines = text.splitlines()
  lst = [i.lstrip() for i in lines]
  return '\n'.join(lst)
# 28
def c28(text, prefix_text):
  lines = text.splitlines()
  lst = [prefix_text + i for i in lines]
  return '\n'.join(lst)
# 29
def c29(text, indent):
    lines = text.splitlines()
    if lines:
        lines[0] = ' ' * indent + lines[0].lstrip()
    return '\n'.join(lines)
# 30
def c30(numbers):
  return [f'{n:.2f}' for n in numbers]
# 31
def c31(numbers):
  return [f'{n:+.2f}' for n in numbers]
# 32
def c32(numbers):
  return [f'{int(n): d}' for n in numbers]
# 33
def c33(number, width):
    return f"{number:0{width}d}"
# 34
def c34(number, width):
    return f"{number:*<{width}}"
# 35
def c35(number):
    return f"{number:,}"
# 36
def c36(number):
    return f"{number:.2%}"
# 37
def c37(number):
    print(f"{number:<10}")
    print(f"{number:>10}")
    print(f"{number:^10}")
# 38
def c38(string, sub):
    return string.count(sub)
# 39
def c39(string):
    return string[::-1]
# 40
def c40(string):
    return ' '.join(reversed(string.split()))
# 41
def c41(string, chars):
    return ''.join(c for c in string if c not in chars)
# 42
def c42(string):
    freq = {}
    for c in string:
        freq[c] = freq.get(c, 0) + 1
    repeated = {k: v for k, v in freq.items() if v > 1}
    return repeated
# 43
def c43(area, volume):
    print(f"The area of the rectangle is {area}cm\u00b2")
    print(f"The volume of the cylinder is {volume}cm\u00b3")
# 44
def c44(string):
    for i, c in enumerate(string):
        print(f"Current character {c} position at {i}")
# 45
def c45(string):
    return set(string.lower()) >= set('abcdefghijklmnopqrstuvwxyz')
# 46
def c46(string):
    return string.split()
# 47
def c47(string, n):
    return string[:n].lower() + string[n:]
# 48
def c48(string):
    string = string.replace(',', '@').replace('.', ',').replace('@', '.')
    return string
# 49
def c49(text):
    vowels = 'aeiouAEIOU'
    count = sum(1 for c in text if c in vowels)
    print(count)
    for v in vowels:
        if text.count(v) > 0:
            print(v, text.count(v))
# 50
def c50(string, delim):
    return string.rsplit(delim, 1)
# 51
def c51(string):
    seen = {}
    for c in string:
        seen[c] = seen.get(c, 0) + 1
    for c in string:
        if seen[c] == 1:
            return c
    return None
# 52
def c52(string, rep):
    from itertools import product
    return [''.join(p) for p in product(string, repeat=rep)]
# 53
def c53(string):
    seen = set()
    for c in string:
        if c in seen:
            return c
        seen.add(c)
    return None
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
# 55
def c55(string):
    words = string.split()
    seen = set()
    for w in words:
        if w in seen:
            return w
        seen.add(w)
    return None
# 56
def c56(string):
    words = string.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[1][0] if len(sorted_freq) > 1 else None
# 57
def c57(string):
    return string.replace(' ', '')
# 58
def c58(string):
    spaces = ' ' * string.count(' ')
    return spaces + string.replace(' ', '')
# 59
def c59(string):
    freq = {}
    for c in string:
        freq[c] = freq.get(c, 0) + 1
    max_count = max(freq.values())
    return max_count
# 60
def c60(string):
    words = string.split()
    return ' '.join(w[0].upper() + w[1:-1].lower() + w[-1].upper() if len(w) > 1 else w.upper() for w in words)
# 61
def c61(string):
    seen = set()
    return ''.join(c for c in string if not (c in seen or seen.add(c)))
# 62
def c62(string):
    return sum(int(c) for c in string if c.isdigit())
# 63
def c63(ip):
    return '.'.join(str(int(o)) for o in ip.split('.'))
# 64
def c64(binary):
    return max(len(s) for s in binary.split('1'))
# 65
def c65(s1, s2):
    common = sorted(set(s1) & set(s2))
    return common if common else "No common characters"
# 66
def c66(s1, s2):
    from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    common = c1 & c2
    extra1 = c1 - common
    extra2 = c2 - common
    return ''.join(sorted(common.elements())) + ''.join(sorted(extra1.elements())) + ''.join(sorted(extra2.elements()))
# 67
def c67(string):
    result = ''
    for c in string:
        if not result or c != result[-1]:
            result += c
    return result
# 68
def c68(string):
    from collections import Counter
    cnt = Counter(string)
    unique = ''.join(k for k, v in cnt.items() if v == 1)
    multiple = ''.join(k for k, v in cnt.items() if v > 1)
    return unique, multiple
# 69
def c69(s1, s2):
    m, n = len(s1), len(s2)
    dp = [['' for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + s1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
    return dp[m][n]
# 70
def c70(s1, s2):
    return ''.join(sorted(set(s1) ^ set(s2)))
# 71
def c71(string):
    spaces = ' ' * string.count(' ')
    return spaces + string.replace(' ', '')
# 72
def c72(string, char):
    return ''.join(c for c in string if c == char)
# 73
def c73(string):
    upper = sum(1 for c in string if c.isupper())
    lower = sum(1 for c in string if c.islower())
    digit = sum(1 for c in string if c.isdigit())
    special = len(string) - upper - lower - digit
    return upper, lower, special, digit
# 74
def c74(s1, s2):
    start, end = 0, len(s1)
    while start < len(s1):
        if all(c in s1[start:end] for c in s2):
            return s1[start:end]
        if len(s1[start:end]) == len(s2):
            start += 1
        end += 1
    return ''
# 75
def c75(string):
    from collections import Counter
    unique = set(string)
    cnt = Counter(string)
    start = end = 0
    min_len = len(string)
    min_window = string
    while end < len(string):
        if all(cnt[c] > 0 for c in unique):
            min_window = string[start:end] if end - start < min_len else min_window
            min_len = min(min_len, end - start)
            cnt[string[start]] -= 1
            start += 1
        else:
            cnt[string[end]] -= 1 if cnt[string[end]] > 0 else 0
            end += 1
    return min_window
# 76
def c76(string, k):
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if len(set(string[i:j])) == k:
                count += 1
    return count
# 77
def c77(string):
    n = len(string)
    return n * (n + 1) // 2
# 78
def c78(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i, c in enumerate(string.lower()):
        if i < 26 and c == alphabet[i]:
            count += 1
    return count
# 79
def c79(string):
    words = string.split()
    smallest = min(words, key=len)
    largest = max(words, key=len)
    return smallest, largest
# 80
def c80(string):
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if string[i:j] and string[i] == string[j-1]:
                count += 1
    return count
# 81
def c81(string, sub):
    return string.find(sub) if sub in string else 'Not found'
# 82
def c82(string, width):
    lines = []
    while string:
        cut = min(width, len(string))
        lines.append(string[:cut])
        string = string[cut:]
    return '\n'.join(lines)
# 83
def c83(num):
    print(f"{num} {oct(num)[2:]} {hex(num)[2:].upper()} {bin(num)[2:]}")
# 84
def c84(string):
    return string.swapcase()
# 85
def c85(bytearr):
    return ''.join(f"{b:02x}" for b in bytearr)
# 86
def c86(string, char):
    return string.replace(char, '')
# 87
def c87(s1, s2):
    return ''.join(set(s1) & set(s2))
# 88
def c88(string, min_len=8):
    has_upper = any(c.isupper() for c in string)
    has_lower = any(c.islower() for c in string)
    has_digit = any(c.isdigit() for c in string)
    has_len = len(string) >= min_len
    return all([has_upper, has_lower, has_digit, has_len])
# 89
def c89(string, unwanted):
    return ''.join(c for c in string if c not in unwanted)
# 90
def c90(string):
    words = string.split()
    seen = set()
    return ' '.join(w for w in words if not (w in seen or seen.add(w)))
# 91
def c91(lst):
    return ','.join(map(str, lst))
# 92
def c92(s1, s2):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, s1, s2).ratio()
# 93
def c93(string):
    return [int(word) for word in string.split() if word.isdigit()]
# 94
def c94(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
# 95
def c95(r, g, b):
    return f"{r:02X}{g:02X}{b:02X}"
# 96
def c96(string):
    words = string.split('_')
    return words[0] + ''.join(w.capitalize() for w in words[1:])
# 97
def c97(string):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
# 98
def c98(string):
    return string[0].lower() + string[1:]
# 99
def c99(string):
    return string.splitlines()
# 100
def c100(string):
    words = string.split()
    for w in words:
        if len(set(w)) != len(w):
            return True
    return False
# 101
def c101(s1, s2):
    if not (s1.isdigit() and s2.isdigit()):
        return "Error in input!"
    return str(int(s1) + int(s2))
# 102
def c102(string):
    import string as s
    return ''.join(c for c in string if c not in s.punctuation)
# 103
def c103(string):
    words = string.split()
    return ' '.join('#' * len(w) if len(w) >= 5 else w for w in words)
# 104
def c104(string):
    words = string.split()
    return ' '.join(w.capitalize() for w in words)
# 105
def c105(email):
    return email.split('@')[0].replace('.', '')
# 106
def c106(string):
    result = ''
    for c in string:
        if not result or c != result[-1]:
            result += c
    return result
# 107
def c107(s1, s2):
    count = 0
    min_len = min(len(s1), len(s2))
    for i in range(min_len - 2):
        if s1[i:i+3] == s2[i:i+3]:
            count += 1
    return count
# 108
def c108(string):
    vowels = 'aeiouAEIOU'
    return ''.join(c if c in vowels else f"-{c}-" for c in string)
# 109
def c109(year_range):
    start, end = map(int, year_range.split('-'))
    count = 0
    for y in range(start, end + 1):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            count += 1
    return count
# 110
def c110(string):
    import re
    return re.sub(r'([A-Z])', r' \1', string).strip()
# 111
def c111(string):
    return ' '.join(str(ord(c) - ord('A') + 1) if c.isupper() else str(ord(c) - ord('a') + 1) for c in string if c.isalpha())
# 112
def c112(s1, s2):
    if not (s1 and s2):
        return False
    return str(int(s1) + int(s2))
# 113
def c113(string):
    words = string.split()
    words.sort(key=lambda w: w.lower()[0])
    return ' '.join(words)

if __name__ == "__main__":
    print(c1("google.com"))
    print(c2("google.com"))
    print(c3("w3resource"), c3("w3"), c3(" w"))
    print(c4("restart"))
    print(c5("abc", "xyz"))
    print(c6("abc"), c6("string"))
    print(c7("The lyrics is not that poor!"), c7("The lyrics is poor!"))
    print(c8(["Exercises", "Python", "Code"]))
    print(c9("w3resource", 2))
    print(c10("w3resource"))
    print(c11("w3resource"))
    print(c12("the quick brown"))
    print(c13("Python"))
    print(c14("red,white,black,red,green,black"))
    print(c15("i", "Python"), c15("b", "Python Tutorial"))
    print(c16("[[]]<<>>", "Python"), c16("{{}}", "PHP"))
    print(c17("Python"), c17("Exercises"))
    print(c18("ipy"), c18("python"))
    print(c19("https://www.w3resource.com/python", "/"))
    print(c20("abcd"), c20("abc"))
    print(c21("PYthOn"))
    print(c22("w3resource"))
    print(c23("Hello\nWorld"))
    print(c24("Python", ['P', 'J']))
    print(c25("Python", 3))
    print(c26("The quick brown fox jumps over the lazy dog"))
    print(c27("    Hello\n        World"))
    print(c28("Hello\nWorld", ">> "))
    print(c29("Hello\nWorld", 4))
    print(c30([3.14159, 2.71828]))
    print(c31([3.14159, -2.71828]))
    print(c32([3.14159, -2.71828]))
    print(c33(42, 5))
    print(c34(42, 5))
    print(c35(1234567))
    print(c36(0.75))
    print(c37(42))
    print(c38("hello hello", "hello"))
    print(c39("Python"))
    print(c40("The quick brown"))
    print(c41("Python", "yt"))
    print(c42("thequickbrownfoxjumpsoverthelazydog"))
    print(c43(1256.66, 1254.725))
    print(c44("w3resource"))
    print(c45("abcdefghijklmnopqrstuvwxyz"))
    print(c46("The quick brown fox"))
    print(c47("Python", 2))
    print(c48("32.054,23"))
    print(c49("hello"))
    print(c50("a,b,c", ","))
    print(c51("abcba"))
    print(c52("ab", 2))
    print(c53("abcba"))
    print(c54("abcba"))
    print(c55("the quick the"))
    print(c56("the quick the quick brown"))
    print(c57("the quick brown"))
    print(c58("the quick brown"))
    print(c59("thequickbrownfox"))
    print(c60("the quick brown"))
    print(c61("abcabc"))
    print(c62("abc123"))
    print(c63("192.168.001.001"))
    print(c64("1100011000"))
    print(c65("python", "typhon"))
    print(c66("listen", "silent"))
    print(c67("aabbcc"))
    print(c68("aabbcc"))
    print(c69("python", "typhon"))
    print(c70("python", "typhon"))
    print(c71("the quick brown"))
    print(c72("Python Exercises", "P"))
    print(c73("Python3!"))
    print(c74("PRWSOERIUSFK", "OSU"))
    print(c75("aabbcc"))
    print(c76("abcde", 3))
    print(c77("abc"))
    print(c78("abcdef"))
    print(c79("the quick brown fox"))
    print(c80("abba"))
    print(c81("the quick brown", "quick"))
    print(c82("The quick brown fox.", 10))
    print(c83(25))
    print(c84("pYTHON"))
    print(c85([111, 12, 45, 67, 109]))
    print(c86("hello", "l"))
    print(c87("Python3", "Python2.7"))
    print(c88("W3resource"))
    print(c89("Pyth*^on Exercis^es", "*^"))
    print(c90("Python Exercises Practice Solution Exercises"))
    print(c91(['Red', 100, -50, 'green', 'w,3,r', 12.12, False]))
    print(c92("Python Exercises", "Python Exercise"))
    print(c93("red 12 black 45 green"))
    print(c94("#FFA501"))
    print(c95(255, 165, 1))
    print(c96("java_script"))
    print(c97("JavaScript"))
    print(c98("Java Script"))
    print(c99("This\nis a\nmultiline\nstring."))
    print(c100("The wait is over."))
    print(c101("23", "19"))
    print(c102("String! With. Punctuation?"))
    print(c103("Count the lowercase letters"))
    print(c104("Red Green WHITE"))
    print(c105("john.smith@example.com"))
    print(c106("Red Green White"))
    print(c107("Red RedGreen", "Red Green"))
    print(c108("Green"))
    print(c109("1981-1991"))
    print(c110("PythonExercises"))
    print(c111("Python"))
    print(c112("234242342341", "2432342342"))
    print(c113("Red Green Black White Pink"))