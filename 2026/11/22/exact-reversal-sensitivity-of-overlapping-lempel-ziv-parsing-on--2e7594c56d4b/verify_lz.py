"""Independent direct Lempel-Ziv parsing test for four-run binary words.

A phrase either has the longest nonempty matching substring starting strictly
before the phrase, allowing a source to overlap the copied phrase, or is a
single novel letter. The test does not use the proof's run-block parsing.
"""

def greedy_count(word):
    pos = 0
    phrases = 0
    while pos < len(word):
        match = 0
        for source in range(pos):
            length = 0
            while pos + length < len(word) and word[source+length] == word[pos+length]:
                length += 1
            if length > match:
                match = length
        pos += max(1, match)
        phrases += 1
    return phrases


def closed_count(a, b, c, d):
    return (3 + (a>1) + (b>1) + (c>a) + (c>2*a) + (d>b))

checked = 0
for a in range(1,14):
    for b in range(1,14):
        for c in range(1,14):
            for d in range(1,14):
                word = '0'*a+'1'*b+'0'*c+'1'*d
                direct = greedy_count(word)
                reverse_direct = greedy_count(word[::-1])
                assert direct == closed_count(a,b,c,d), (a,b,c,d,direct)
                assert reverse_direct == closed_count(d,c,b,a), (a,b,c,d,reverse_direct)
                checked += 1
print(f'PASS: {checked} parameter quadruples; both orientations independently parsed')
print('Example (a,b,c,d)=(2,2,5,3):', greedy_count('00'+'11'+'00000'+'111'), greedy_count(('00'+'11'+'00000'+'111')[::-1]))
