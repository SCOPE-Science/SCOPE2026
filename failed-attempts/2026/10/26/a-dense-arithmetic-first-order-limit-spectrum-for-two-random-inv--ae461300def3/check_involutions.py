"""Finite exact checks for two independently uniform involutions.

Run: python check_involutions.py
Only standard-library dependencies. These finite identities corroborate,
but do not replace, the asymptotic and logical arguments.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import factorial

@lru_cache(None)
def involutions(n):
    def rec(remaining, pairs):
        if not remaining:
            p=list(range(n))
            for a,b in pairs:
                p[a]=b; p[b]=a
            yield tuple(p)
            return
        a=remaining[0]
        yield from rec(remaining[1:],pairs)
        for b in remaining[1:]:
            tail=tuple(x for x in remaining[1:] if x!=b)
            yield from rec(tail,pairs+((a,b),))
    return tuple(rec(tuple(range(n)),()))

def components(a,b):
    n=len(a)
    seen=set(); output=[]
    for x in range(n):
        if x in seen: continue
        todo=[x]; group=set()
        while todo:
            v=todo.pop()
            if v in group: continue
            group.add(v); todo.extend((a[v],b[v]))
        seen|=group
        m=len(group)
        edges=sum(a[v]!=v for v in group)//2 + sum(b[v]!=v for v in group)//2
        assert edges in (m-1,m)
        if edges==m:
            assert m%2==0
            typ=('C',m,'')
        else:
            if m==1:
                pattern=''
            else:
                nbr={v:[] for v in group}
                for color,perm in (('R',a),('B',b)):
                    for v in group:
                        if perm[v]!=v:
                            nbr[v].append((perm[v],color))
                ends=[v for v in group if len(nbr[v])==1]
                assert len(ends)==2
                previous=None; current=ends[0]; s=[]
                while True:
                    nxt=[(v,c) for v,c in nbr[current] if v!=previous]
                    if not nxt: break
                    assert len(nxt)==1
                    v,c=nxt[0]; s.append(c)
                    previous,current=current,v
                assert len(s)==m-1
                assert all(s[i]!=s[i+1] for i in range(len(s)-1))
                pattern=min(''.join(s),''.join(reversed(s)))
            typ=('P',m,pattern)
        output.append(typ)
    return Counter(output)

def aut(t):
    if t[0]=='C': return t[1]
    return 1 if t[1]%2 else 2

def ff(x,r):
    v=1
    for j in range(r): v*=x-j
    return v

def verify():
    probes=[{'P1':1},{'P1':2},{'P2R':1},{'P2B':1},
            {'P2R':1,'P2B':1},{'P1':1,'P2R':1},
            {'C2':1},{'P3':1},{'C4':1},
            {'P1':1,'C2':1},{'P1':3}]
    alias={'P1':('P',1,''),'P2R':('P',2,'R'),
           'P2B':('P',2,'B'),'P3':('P',3,'BR'),
           'C2':('C',2,''),'C4':('C',4,'')}
    checked=0
    for n in range(1,8):
        inv=involutions(n)
        I=len(inv)
        assert I==sum(factorial(n)//(factorial(n-2*k)*2**k*factorial(k)) for k in range(n//2+1))
        sums=[0]*len(probes)
        seen_types=set()
        for a,b in product(inv,repeat=2):
            ct=components(a,b)
            assert sum(typ[1]*count for typ,count in ct.items())==n
            seen_types.update(ct)
            for idx,pr in enumerate(probes):
                val=1
                for name,mult in pr.items(): val*=ff(ct[alias[name]],mult)
                sums[idx]+=val
            checked+=1
        for idx,pr in enumerate(probes):
            M=sum(alias[name][1]*count for name,count in pr.items())
            expected=Fraction(0) if M>n else Fraction(factorial(n),factorial(n-M))*Fraction(len(involutions(n-M)),I)**2
            for name,mult in pr.items(): expected*=Fraction(1,aut(alias[name])**mult)
            observed=Fraction(sums[idx],I*I)
            assert observed==expected,(n,pr,observed,expected)
        print('INVOLUTION_PAIR_EXACT',n,I,I*I,len(seen_types))
    print('INVOLUTION_COMPONENT_MOMENTS_OK',checked,len(probes))

if __name__=='__main__':
    verify()
