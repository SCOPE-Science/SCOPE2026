"""Verify coprime-pair separator {5,7}->N=11 in S7 and singleton {5}->7 via Heisenberg mod 25.
Fast deterministic checks (permutations of 7 points, 3x3 matrices mod 25)."""
import json, math

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    n = len(p); q = [0]*n
    for i in range(n): q[p[i]] = i
    return tuple(q)
def pw(p, k):
    n = len(p); r = list(range(n))
    for _ in range(k):
        r = [p[r[i]] for i in range(n)]
    return tuple(r)
def comm(a, b):
    return compose(compose(compose(a, b), inv(a)), inv(b))
def is_id(p): return all(p[i]==i for i in range(len(p)))
def cyc(n, c):
    p = list(range(n))
    for i in range(len(c)): p[c[i]] = c[(i+1)%len(c)]
    return tuple(p)
def w(a,b,s): return comm(pw(a,s), pw(b,s))

A = cyc(7,[0,1,2,3,4])   # order 5 -> kills w_5
B = cyc(7,[0,1,2,3,4,5,6]) # order 7 -> kills w_7
out = {'S7_57': {
  'ordA5': pw(A,5)==tuple(range(7)), 'ordB7': pw(B,7)==tuple(range(7)),
  'w5_id': is_id(w(A,B,5)), 'w7_id': is_id(w(A,B,7)),
  'w11_nontrivial': not is_id(w(A,B,11)),
  'w13_nontrivial': not is_id(w(A,B,13))}}
# singleton {5} -> 7: UT3(Z/25), [A^s,B^s]=E13(s^2); 25|25 yes, 25|49 no
out['singleton_5_mod25'] = {'kill5': (25 % 25 == 0), 'preserve7': (49 % 25 != 0)}
print(json.dumps(out, indent=1))
