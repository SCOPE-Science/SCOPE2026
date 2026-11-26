"""Self-contained exact checks for binary three-length-limited composition profiles.
Run with Python 3: python verify.py
"""
from collections import defaultdict
from math import comb

# Rational generating function P(z)/Q(z).
P = [0, 2, -5, 6, -4, 4, -1, 2, -3, 2]

def multiply(a, b):
    result = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[i+j] += x*y
    return result

Q = [1]
for _ in range(5):
    Q = multiply(Q, [1, -1])
Q = multiply(multiply(Q, [1, 1]), [1, 0, 1])

def rational_counts(N):
    counts = [0]*(N+1)
    for n in range(N+1):
        counts[n] = (P[n] if n < len(P) else 0) - sum(
            Q[j]*counts[n-j] for j in range(1, min(n, len(Q)-1)+1))
    return counts

def literal_signature(w):
    n = len(w)
    one_counts = tuple(w.count(str(i)) for i in (0,1))
    h2 = tuple(sum(sum(map(int,w[j:j+2])) == k for j in range(n-1)) for k in range(3))
    h3 = tuple(sum(sum(map(int,w[j:j+3])) == k for j in range(n-2)) for k in range(4))
    return one_counts + h2 + h3

def run_signature(w):
    n = len(w)
    if w.count('0') in (0,n):
        return ('constant', w[0])
    runs = []
    for c in w:
        if runs and runs[-1][0] == c:
            runs[-1][1] += 1
        else:
            runs.append([c,1])
    r0 = sum(c=='0' for c,k in runs)
    r1 = len(runs)-r0
    s0 = sum(c=='0' and k==1 for c,k in runs)
    s1 = sum(c=='1' and k==1 for c,k in runs)
    e = sum((c=='0' and k>=2) or (c=='1' and k==1)
            for c,k in (runs[0],runs[-1]))
    return (w.count('1'),r0,r1,s0,s1,e)

def direct_counts(N):
    results = []
    for n in range(1,N+1):
        seen1, seen2, to_struct, to_literal = set(),set(),{},{}
        for i in range(1<<n):
            w = f'{i:0{n}b}'
            a=literal_signature(w)
            b=run_signature(w)
            if a in to_struct:
                assert to_struct[a] == b, (n,w,'not injective forward')
            else:
                to_struct[a] = b
            if b in to_literal:
                assert to_literal[b] == a, (n,w,'not injective backward')
            else:
                to_literal[b] = a
            seen1.add(a)
            seen2.add(b)
        assert len(seen1) == len(seen2) == len(to_struct)
        results.append(len(seen1))
    return results

def dp_counts(N):
    # Retain only aggregate spectra plus last two symbols; no full words are stored.
    # (number of ones, adjacent 0/1/2-one compositions,
    #  triple 0/1/2/3-one compositions, penultimate and last bit)
    states = {(b,0,0,0,0,0,0,0,2,b) for b in (0,1)}
    results=[]
    for n in range(1,N+1):
        if n>1:
            new=set()
            for k,a0,a1,a2,t0,t1,t2,t3,prev,tail in states:
                for b in (0,1):
                    a=tail+b
                    t=prev+tail+b
                    new.add((k+b,a0+(a==0),a1+(a==1),a2+(a==2),
                             t0+(prev<2 and t==0),t1+(prev<2 and t==1),
                             t2+(prev<2 and t==2),t3+(prev<2 and t==3),tail,b))
            states=new
        results.append(len({state[:8] for state in states}))
    return results

def formula_sums(N):
    # Count possible profiles by zero/one run totals and positive-composition status.
    # This does not enumerate words or use the rational identity.
    counts=[]
    for n in range(1,N+1):
        count=2
        for z in range(1,n):
            o=n-z
            for r0 in range(1,z+1):
                for r1 in (r0-1,r0,r0+1):
                    if not 1<=r1<=o: continue
                    for s0 in range(r0+1):
                        if z < 2*r0-s0 or (s0==r0 and z!=r0): continue
                        for s1 in range(r1+1):
                            if o < 2*r1-s1 or (s1==r1 and o!=r1): continue
                            if r0==r1:
                                evalues = {
                                   a+b for a in ((0,1) if 0<s0<r0 else ((0,) if s0==r0 else (1,)))
                                           for b in ((0,1) if 0<s1<r1 else ((1,) if s1==r1 else (0,)))
                                }
                                count+=len(evalues)
                            elif r0==r1+1:
                                R=r0;s=s0
                                count+=1+(1<=s<=R-2)+(2<=s<=R-1)
                            else:
                                R=r1;s=s1
                                count+=1+(1<=s<=R-2)+(2<=s<=R-1)
        counts.append(count)
    return counts

if __name__=='__main__':
    N=38
    exact=rational_counts(N)[1:]
    brute=direct_counts(16)
    dynamic=dp_counts(N)
    structural=formula_sums(20)
    assert brute==exact[:16], (brute,exact[:16])
    assert structural==exact[:20], (structural,exact[:20])
    assert dynamic==exact, (dynamic,exact)
    for n in range(2,N+1):
        kappa = 555 if n%2 else (480 if n%4==0 else 456)
        numerator=3*n**4-16*n**3+114*n**2-272*n+kappa
        assert numerator%96==0 and numerator//96==exact[n-1],n
    print('VERIFY_OK direct=1..16 structural=1..20 dynamic=1..38')
    print('COUNTS_1_38='+','.join(str(v) for v in exact))
