#!/usr/bin/env python3
"""Exact finite-field certificate for consecutive cubic-coset words.

No external packages or network; enumerate all extension fields below the
proved analytic cutoff, verify each defining polynomial is irreducible,
and cross-check pow-character colors against independently listed cube cosets.
"""
import itertools
import json
from collections import Counter

# Coefficients are in increasing-degree order, including the leading 1.
POLYS = {
    (5, 2): [1, 1, 1],
    (7, 2): [1, 0, 1],
    (11, 2): [1, 0, 1],
    (13, 2): [1, 3, 1],
    (17, 2): [1, 1, 1],
    (7, 3): [1, 0, 1, 1],
    (19, 2): [1, 0, 1],
    (23, 2): [1, 0, 1],
    (5, 4): [1, 0, 1, 1, 1],
}


def is_prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, int(n ** .5) + 1))


def trim(a):
    a = a[:]
    while a and a[-1] == 0: a.pop()
    return a


def poly_remainder(a, b, p):
    a = trim([x % p for x in a]); b = trim([x % p for x in b])
    inv = pow(b[-1], -1, p)
    while a and len(a) >= len(b):
        c = a[-1] * inv % p
        offset = len(a) - len(b)
        for j, z in enumerate(b):
            a[offset+j] = (a[offset+j] - c*z) % p
        a = trim(a)
    return a


def irreducible(f, p):
    d = len(f) - 1
    for k in range(1, d // 2 + 1):
        for a in itertools.product(range(p), repeat=k):
            if not poly_remainder(f, list(a) + [1], p): return False
    return True


def field(p, f):
    d = len(f)-1
    q = p**d
    digits = []
    for x in range(q):
        ds = []; y = x
        for _ in range(d): ds.append(y % p); y //= p
        digits.append(ds)
    def mul(x, y):
        a = digits[x]; b = digits[y]; c = [0] * (2*d-1)
        for i in range(d):
            for j in range(d): c[i+j] += a[i]*b[j]
        for i in range(2*d-2, d-1, -1):
            k = c[i] % p
            for j in range(d): c[i-d+j] -= k*f[j]
        return sum((c[i] % p) * p**i for i in range(d))
    def power(x, e):
        y = 1
        while e:
            if e & 1: y = mul(y, x)
            x = mul(x, x)
            e >>= 1
        return y
    def add_const(x, c):
        return x - x%p + (x%p + c)%p
    return q, mul, power, add_const


def extension_cases(bound=841):
    out=[]
    for p in range(3, int(bound**.5)+1, 2):
        if not is_prime(p): continue
        q=p*p; d=2
        while q < bound:
            if q % 3 == 1: out.append((p,d))
            d+=1; q*=p
    return sorted(out,key=lambda pd: pd[0]**pd[1])


def certify(p,d):
    f = POLYS[p,d]
    assert f[-1] == 1 and len(f) == d+1 and irreducible(f,p), (p,d,f)
    q,mul,power,add_const=field(p,f)
    assert q % 3 == 1
    for x in range(1,q):
        assert power(x,q-1)==1
    cube={power(x,3) for x in range(1,q)}
    assert len(cube) == (q-1)//3
    g=next(x for x in range(2,q) if x not in cube)
    omega=power(g,(q-1)//3)
    assert omega != 1 and power(omega,3)==1
    color_by_pow={1:0,omega:1,mul(omega,omega):2}
    assert len(color_by_pow)==3
    labels=[None]*q
    for x in range(1,q):
        labels[x]=color_by_pow[power(x,(q-1)//3)]
    labels_from_cosets={}
    for t in range(3):
        h=power(g,t)
        for c in cube:
            z=mul(h,c)
            assert z not in labels_from_cosets
            labels_from_cosets[z]=t
    assert len(labels_from_cosets)==q-1
    assert all(labels[x] == labels_from_cosets[x] for x in range(1,q))
    H=Counter(); W={}
    for x in range(q):
        w=(labels[x],labels[add_const(x,1)],labels[add_const(x,2)])
        if None in w: continue
        H[w]+=1
        W.setdefault(w,x)
    words=list(itertools.product(range(3),repeat=3))
    missing=[list(w) for w in words if H[w]==0]
    assert sum(H.values())==q-3
    result={"q":q,"p":p,"e":d,"defining_polynomial_ascending":f,
            "least_noncube_encoded":g,"third_root_encoded":omega,
            "realized_words":27-len(missing),"missing_words":missing,
            "min_positive_count":min(H.values()),"max_count":max(H.values()),
            "witness_by_word":{"".join(map(str,w)):W[w] for w in words if w in W}}
    return result


def main():
    assert extension_cases()==list(POLYS), (extension_cases(),list(POLYS))
    results=[certify(p,d) for p,d in extension_cases()]
    assert [(r['q'],len(r['missing_words'])) for r in results] == [
        (25,10),(49,8),(121,0),(169,0),(289,0),(343,0),(361,0),(529,0),(625,0)]
    print(json.dumps({"analytic_cutoff":841,"finite_records":results},
                     separators=(',',':'),sort_keys=True))
    print('VERIFY_OK 9 extension fields checked, 7 complete; 9 irreducible polynomials; '
          'cubic-coset cross-check; 27 candidate words per field')

if __name__=='__main__': main()
