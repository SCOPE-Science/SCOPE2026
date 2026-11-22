"""Exact checks for finite correlation laws of uniform set partitions.

Uses integer Bell recurrences and rational arithmetic; no numerical sampling.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def bell_numbers(N):
    B = [1]
    for n in range(N):
        B.append(sum(comb(n, k) * B[k] for k in range(n + 1)))
    return B


def partitions(n):
    p = [()]
    for i in range(n):
        out = []
        for blocks in p:
            out.append(blocks + ((i,),))
            for k in range(len(blocks)):
                tmp = list(blocks)
                tmp[k] = tmp[k] + (i,)
                out.append(tuple(tmp))
        p = out
    return p


def pair_states(part):
    a = {}
    for j, b in enumerate(part):
        for x in b:
            a[x] = j
    return (a[0] == a[1], a[0] == a[2], a[1] == a[2])


def event(mask, st):
    return all(st) or any(st[k] and (mask & (1 << k)) for k in range(3))


def rank(n, mask, edges):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for j, (x,y) in enumerate(edges):
        if mask & (1 << j):
            a,b = root(x), root(y)
            parent[a] = b
    return n - len({root(i) for i in range(n)})


def check():
    B = bell_numbers(128)
    count = 0
    # Any admissible exchangeable three-label equivalence law has probabilities
    # q, p-q (three singleton-edge outcomes), 1-3p+2q (all distinct).
    # Independently verify the iff criterion on a dense rational grid.
    for d in (4, 7, 10, 13, 17):
        for i in range(d + 1):
            p = Fraction(i, d)
            for j in range(i + 1):
                q = Fraction(j, d)
                if 1-3*p+2*q < 0:
                    continue
                delta=q*(1+p)-2*p*p
                covs=[]
                for s in range(8):
                    for t in range(8):
                        cov=(q+(s&t).bit_count()*(p-q))-(q+s.bit_count()*(p-q))*(q+t.bit_count()*(p-q))
                        covs.append(cov)
                        count+=1
                assert (min(covs)>=0) == (delta>=0), (p,q,delta,min(covs))
    # Contrast: the Pitman-Yor discount family has positive Delta,
    # while its Dirichlet/Ewens boundary has zero Delta.
    for alpha in [Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(3,4)]:
        for theta in [Fraction(1,4), Fraction(1), Fraction(3), Fraction(-1,8)]:
            if theta<=-alpha:
                continue
            p=(1-alpha)/(1+theta)
            q=(1-alpha)*(2-alpha)/((1+theta)*(2+theta))
            delta=q*(1+p)-2*p*p
            assert delta == alpha*(1-alpha)*(theta+alpha)/((1+theta)**2*(2+theta))
            assert (delta == 0)==(alpha==0)
            assert delta>=0
            count+=1
    for m in range(2,21):
        p,q=Fraction(1,m),Fraction(1,m*m)
        assert q*(1+p)-2*p*p == -Fraction(m-1,m**3)
        count+=1
    sample = {}
    for n in range(3,129):
        p, q = Fraction(B[n-1],B[n]), Fraction(B[n-2],B[n])
        assert 0 < q < p < 1
        assert q > p*p
        assert q <= Fraction(n,n-1)*p*p
        neg = q*(1+p)-2*p*p
        altpos = p-(2*p-q)**2
        assert neg < 0 and altpos > 0
        negpairs = []
        for s in range(8):
            for t in range(s,8):
                z = s&t
                v = (q+z.bit_count()*(p-q)) - (q+s.bit_count()*(p-q))*(q+t.bit_count()*(p-q))
                want_negative = (s&t)==0 and sorted([s.bit_count(),t.bit_count()]) == [1,2]
                assert (v<0) == want_negative and v!=0, (n,s,t,v)
                if want_negative: negpairs.append((s,t))
                count += 1
        assert len(negpairs)==3
        if n in (3,4,5,6,8,20,100,128): sample[n] = (str(neg),str(altpos))
    # Directly generate all partitions, independently of Bell formulas.
    for n in range(3,7):
        parts=partitions(n)
        assert len(parts)==B[n]
        states=[pair_states(part) for part in parts]
        for s in range(8):
            A=sum(event(s,st) for st in states)
            p,q=Fraction(B[n-1],B[n]),Fraction(B[n-2],B[n])
            assert Fraction(A,B[n])==q+s.bit_count()*(p-q)
            for t in range(8):
                AB=sum(event(s,st) and event(t,st) for st in states)
                assert Fraction(AB,B[n])==q+(s&t).bit_count()*(p-q)
                count += 1
    # All edge-set contraction probabilities, and positive covariance of all principal events.
    for n in (3,4):
        edges=list(combinations(range(n),2))
        E=len(edges)
        ranks=[rank(n,m,edges) for m in range(1<<E)]
        for s in range(1<<E):
            for t in range(1<<E):
                r1,r2,r12=ranks[s],ranks[t],ranks[s|t]
                lhs=B[n-r12]*B[n]-B[n-r1]*B[n-r2]
                assert lhs >= 0
                assert (lhs>0) == (s!=0 and t!=0)
                # independent direct complete enumeration for n <=4.
                P=partitions(n)
                def sat(part,m):
                    ix={x:i for i,block in enumerate(part) for x in block}
                    return all(ix[u]==ix[v] for j,(u,v) in enumerate(edges) if m>>j&1)
                assert sum(sat(part,s) for part in P)==B[n-r1]
                count+=1
    return count,sample

if __name__ == '__main__':
    count, sample=check()
    print('PASS: exact checks =',count)
    print('Negative and crossing-positive covariance witnesses:')
    for n,data in sample.items():print(n,*data)
