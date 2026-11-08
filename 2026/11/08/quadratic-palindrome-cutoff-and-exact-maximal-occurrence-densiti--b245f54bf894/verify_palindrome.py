"""Standalone finite diagnostics for generalized Mephisto-word palindromes.

Mathematical proof and all-parameter bounds are in RESULT.md; this file tests finite prefixes.
"""
from collections import Counter

def word(b, min_length):
    s = '0'
    while len(s) < min_length:
        s = ''.join(c * (b - 1) + str(1-int(c)) for c in s)
    return s

def palindrome_locations(s, n):
    return {i for i in range(len(s) - n + 1) if s[i:i+n] == s[i:i+n][::-1]}

def run_test():
    checked = 0
    for b in range(3, 11):
        s = word(b, 40000)
        L = b*b-1
        a = palindrome_locations(s, L)
        expect = {b*q for q in range((len(s)-L)//b+1)
                  if s[q:q+b] in ('0'*b,'1'*b)}
        assert a == expect, (b, len(a), len(expect), list(a ^ expect)[:12])
        assert not palindrome_locations(s, L+1), ('long_even_odd', b)
        assert not palindrome_locations(s, L+2), ('long_odd_even', b)
        factors = {s[i:i+L] for i in a}
        forms = {(digit*(b-1)+str(1-int(digit)))*(b-1) + digit*(b-1)
                 for digit in '01'}
        assert factors == forms, (b, factors, forms)
        for i in a:
            assert i%b == 0
            q = i//b
            t, r = divmod(q,b)
            assert r==b-1 and s[t] != s[t+1]
        checked += 3*(len(s)-L+1)
    # Necessary residue/optional count arithmetic in the symbolic proof.
    modular = 0
    for b in range(3, 251):
        for N in (b*b-2,b*b-1,b*b):
            for r in range(b):
                c = (2*r+N-1)%b
                if c not in ((b-4)%b,(b-3)%b): continue
                opts = sum(1 for j in range(N) if (r+j)%b == b-1)
                if N>=b*b-1: assert opts == b
                if N==b*b-2 and r>=2: assert opts == b
                modular+=1
    print('VERIFY_OK', 'bases=3..10', 'palindrome_window_tests=',checked,
          'modular_cases=',modular)

if __name__=='__main__': run_test()
