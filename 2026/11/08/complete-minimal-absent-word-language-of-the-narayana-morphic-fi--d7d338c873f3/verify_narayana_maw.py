#!/usr/bin/env python3
"""Direct finite cross-check of the exact minimal absent word classification.

No external libraries. Finite tests complement, but do not substitute for,
the mathematical proof for the infinite morphic word.
"""
from collections import defaultdict

M = {'0': '01', '1': '2', '2': '0'}
ALPHABET = '012'

def morph(s):
    return ''.join(M[c] for c in s)

def finite_iterate(k):
    w = '0'
    for _ in range(k):
        w = morph(w)
    return w

def predicted(max_length):
    result = {2: {'02', '11', '21', '22'}}
    u = '0'
    edges = {('0', '1'), ('1', '1'), ('2', '0'), ('2', '1')}
    j = 1
    while len(u) + 2 <= max_length:
        rights = '01' if j % 2 else '02'
        result[len(u) + 2] = {a + u + b for a in ALPHABET for b in rights
                              if (a, b) not in edges}
        assert len(result[len(u) + 2]) == 2
        assert len(edges) == 4
        if j % 2:
            edges = {(str((int(a) + 1) % 3), {'0': '0', '1': '2'}[b])
                     for a, b in edges}
            u = morph(u)
        else:
            edges = {(str((int(a) + 1) % 3), {'0': '1', '2': '0'}[b])
                     for a, b in edges}
            u = morph(u) + '0'
        j += 1
    return result

def factors(w, n):
    return {w[i:i+n] for i in range(len(w)-n+1)}

def main():
    a, b = finite_iterate(25), finite_iterate(26)
    assert len(a) < len(b)
    limit = 40
    factors_a = {n: factors(a,n) for n in range(1,limit+1)}
    factors_b = {n: factors(b,n) for n in range(1,limit+1)}
    assert factors_a == factors_b, 'Finite prefixes not stabilized for the tested lengths'
    pred = predicted(limit)
    total = 0
    for n in range(2, limit+1):
        observed = {x + mid + z for mid in factors_b[n-2] for x in ALPHABET for z in ALPHABET
                    if x + mid in factors_b[n-1] and mid + z in factors_b[n-1]
                    and x + mid + z not in factors_b[n]} if n>=3 else (
                    {x + z for x in ALPHABET for z in ALPHABET if x+z not in factors_b[2]})
        expected = pred.get(n,set())
        assert observed == expected, (n,sorted(observed),sorted(expected))
        total += len(observed)
    print('PASS: fixed-point language stabilized between morphism iterates 25 and 26')
    print('PASS: exact minimal absent word sets and missing-pair recursions for lengths 2..40')
    print('PASS: %d minimal absent words checked; length counts: %s' %
          (total, [(n,len(pred[n])) for n in sorted(pred)]))
    assert factors_b[3] == {'001','010','012','101','120','200','201'}
    print('PASS: seven 3-letter factors and base extension graph')
    # Directly check all two-sided extension edges, far beyond length 40.
    u, edges = '0', {('0','1'), ('1','1'), ('2','0'), ('2','1')}
    for j in range(1, 14):
        observed_edges = {(b[i-1], b[i+len(u)])
                          for i in range(1, len(b)-len(u))
                          if b.startswith(u, i)}
        assert observed_edges == edges, (j, len(u), observed_edges, edges)
        if j % 2:
            edges = {(str((int(x)+1)%3), {'0':'0','1':'2'}[y]) for x,y in edges}
            u = morph(u)
        else:
            edges = {(str((int(x)+1)%3), {'0':'1','2':'0'}[y]) for x,y in edges}
            u = morph(u) + '0'
    print('PASS: 13 successive full two-sided extension graphs through core length 240')

if __name__ == '__main__':
    main()
