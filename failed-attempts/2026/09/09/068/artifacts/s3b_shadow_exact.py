"""Step 3b: exact parent shadow in the ring Z[i], no floating point.
S_v = (1/2^36) sum_w A_w i^w [x^{72-v} y^v](x+y)^{72-w}(x-y)^w.
Compute the bracket exactly (integer), multiply by i^w, divide by 2^36 in Z[i]:
check divisibility. Report exact Gaussian-integer shadow table.
"""
from fractions import Fraction
from math import comb
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]

# c[w][v] = coeff of x^{72-v} y^v in (x+y)^{72-w}(x-y)^w  (integer)
def bracket(w, v):
    s = 0
    for a in range(73):
        b = v - a
        if 0 <= a <= 72 - w and 0 <= b <= w:
            s += comb(72 - w, a) * comb(w, b) * ((-1) ** b)
    return s

# accumulate Gaussian integer numerator N_v = sum_w A_w i^w c(w,v); represent a+bi
print("exact shadow numerators / 2^36:")
shadow = {}
FAIL = []
for v in range(73):
    re, im = 0, 0
    for w in range(73):
        if A[w] == 0:
            continue
        c = bracket(w, v)
        t = A[w] * c
        r = w % 4
        if r == 0:
            re += t
        elif r == 1:
            im += t
        elif r == 2:
            re -= t
        else:
            im -= t
    q_re, m_re = divmod(re, 2 ** 36)
    q_im, m_im = divmod(im, 2 ** 36)
    # divmod floors; require exact divisibility
    exact = (re % 2 ** 36 == 0) and (im % 2 ** 36 == 0)
    if re % 2 ** 36 == 0:
        qre = re // 2 ** 36
    else:
        qre, exact = None, False
    if im % 2 ** 36 == 0:
        qim = im // 2 ** 36
    else:
        qim, exact = None, False
    shadow[v] = (qre, qim, exact)
    if qre or qim:
        print(f"  S[{v}] = ({qre}, {qim}) exact={exact}")
    if not exact and (re != 0 or im != 0):
        FAIL.append(v)
print("inexact weights:", FAIL if FAIL else "NONE — shadow is an exact Gaussian-integer enumerator")
neg = [v for v in range(73) if shadow[v][0] is not None and shadow[v][0] < 0]
print("negative real shadow coeffs:", neg if neg else "none")
nonsupp = [v for v in range(73) if (shadow[v][0] or shadow[v][1]) and v % 4 != 0]
print("shadow support outside 0 mod 4:", nonsupp if nonsupp else "none (all in 0 mod 4)")
# For a Type-II code the shadow theorem (Conway-Sloane) says S=C shadow weights = n/2 mod 4;
# here n/2=36 = 0 mod 4 -> consistent, and shadow==parent enumerator means the putative
# code would have covering-radius-relevant deep-hole structure identical to itself.
same = all((shadow[v][0] or 0) == A[v] and (shadow[v][1] or 0) == 0 for v in range(73))
print("shadow == parent enumerator exactly:", same)
json.dump({str(v): [shadow[v][0], shadow[v][1], shadow[v][2]] for v in range(73)},
          open(os.path.join(HERE, "shadow_exact.json"), "w"), indent=1)
print("wrote shadow_exact.json")
