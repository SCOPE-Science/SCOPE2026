"""Pure-python full-2-descent upper bound + point search for E_d: y^2=x(x-9d)(x-729d).
Sound upper bound: enumerate (b1,b2,b3) squarefree triples dividing 3d with product square;
drop only triples provably locally insoluble (real signs / mod p^k brute force).
Point search: naive rational x=p/q scan for lower bound.
"""
import json, math, itertools
from fractions import Fraction

def squarefree_divisors(n):
    n = abs(n)
    if n == 0:
        return [1]
    import sympy as sp
    f = sp.factorint(n)
    primes = list(f.keys())
    divs = [1]
    for p in primes:
        divs = divs + [d*p for d in divs]
    return sorted(divs)

def signed_sf_divisors(d):
    base = squarefree_divisors(3*d)
    out = []
    for b in base:
        out.append(b)
        out.append(-b)
    return sorted(set(out))

def sel2_candidates(d):
    divs = signed_sf_divisors(d)
    s = set(divs)
    trips = []
    for b1 in divs:
        for b2 in divs:
            # b1*b2*b3 = square => b3 = sqf(b1*b2)
            b3 = b1*b2
            # reduce to squarefree kernel
            import sympy as sp
            if b3 == 0:
                continue
            f = sp.factorint(abs(b3))
            k = 1
            for p, e in f.items():
                if e % 2 == 1:
                    k *= p
            b3s = k if b3 > 0 else -k
            if b3s in s:
                trips.append((b1, b2, b3s))
    return sorted(set(trips))

def has_sol_mod(b1, b2, c, p, k=3, cap=2000000):
    """Return True if b1*u^2 - b2*v^2 = c soluble mod p^k (search). False = proven insoluble mod p^k."""
    m = p**k
    # brute u,v mod m; cap effort
    if m*m > cap and p > 7:
        # sample residues: check squares sets instead
        sq = set((t*t) % m for t in range(m)) if m <= 5000 else None
        if sq is None:
            return True  # inconclusive -> keep (sound)
        vals = set()
        for s1 in sq:
            vals.add((b1*s1) % m)
            if len(vals) > 20000:
                break
        return True  # too big: inconclusive
    for u in range(m):
        a = (b1*u*u - c) % m
        for v in range(m):
            if (b2*v*v) % m == a:
                return True
    return False

def real_possible(b1, b2, b3, d):
    # need b1*u^2 = x, b2*v^2 = x-9d, b3*w^2 = x-729d with same x; signs constrain
    # necessary: not (b1<=0 and ...). Simple: there exists real x with sign(x)==sign(b1) etc.
    # brute: test candidate x values of both signs large
    for x in (-10**6, -1.0, 1.0, 10**6, 9*d+1.0, 9*d-1.0, 729*d+1.0, 729*d-1.0):
        if x == 0 or x-9*d == 0 or x-729*d == 0:
            continue
        import math
        if (x>0)==(b1>0) and ((x-9*d)>0)==(b2>0) and ((x-729*d)>0)==(b3>0):
            return True
    # general interval check: signs change only at 0,9d,729d
    pts = sorted([0.0, 9*d, 729*d])
    mids = [(pts[0]-1.0), (pts[0]+pts[1])/2, (pts[1]+pts[2])/2, (pts[2]+1.0)]
    for x in mids:
        if (x>0)==(b1>0) and ((x-9*d)>0)==(b2>0) and ((x-729*d)>0)==(b3>0):
            return True
    return False

def sel2_upper(d, primes_extra=(2,3,5)):
    trips = sel2_candidates(d)
    S = set(primes_extra)
    import sympy as sp
    for p in sp.factorint(abs(d) if d else 1):
        S.add(p)
    S.add(2); S.add(3)
    kept = []
    dropped = []
    for (b1,b2,b3) in trips:
        if not real_possible(b1,b2,b3,d):
            dropped.append(((b1,b2,b3),'R'))
            continue
        ok = True
        reason = ''
        for p in sorted(S):
            # equations: b1 u^2 - b2 v^2 = 9d ; b1 u^2 - b3 w^2 = 729d
            if not has_sol_mod(b1,b2,9*d,p,k=2):
                ok=False; reason=f'mod{p}^2 eq1'; break
            if not has_sol_mod(b1,b3,729*d,p,k=2):
                ok=False; reason=f'mod{p}^2 eq2'; break
        if ok:
            kept.append((b1,b2,b3))
        else:
            dropped.append(((b1,b2,b3),reason))
    # Sel2 dim: log2(#kept); rank <= dim-2
    n = len(kept)
    dim = math.log2(n) if n and (n & (n-1))==0 else None
    return {'d':d,'ncand':len(trips),'nkept':n,'dim':dim,'kept':kept,'dropped':dropped,'S':sorted(S)}

def rhs(d,x):
    return x*(x-9*d)*(x-729*d)

def is_rational_square(fr):
    # fr: Fraction; true if square in Q
    if fr < 0:
        return False
    if fr == 0:
        return True
    n, dd = fr.numerator, fr.denominator
    rn = math.isqrt(n); rd = math.isqrt(dd)
    return rn*rn==n and rd*rd==dd

def point_search(d, Bnum=200, Bden=50):
    pts=[]
    for q in range(1,Bden+1):
        for p in range(-Bnum,Bnum+1):
            import math
            if math.gcd(p,q)!=1:
                continue
            x=Fraction(p,q)
            y2=rhs(d,x)
            if y2>=0 and is_rational_square(y2):
                pts.append((x,y2))
    return pts

if __name__=='__main__':
    import sys
    d=int(sys.argv[1]) if len(sys.argv)>1 else 1
    r=sel2_upper(d)
    print(json.dumps({'d':d,'ncand':r['ncand'],'nkept':r['nkept'],'dim':r['dim'],'S':r['S']}))
    print('kept:',r['kept'][:64])
    print('dropped:',len(r['dropped']))
