#!/usr/bin/env python3
"""Independent bitwise, all-state periodic-orbit and basin comparison."""
from collections import Counter


def maps(n):
    m=(1<<n)-1
    def left(x):return ((x<<1)&m)|(x>>(n-1))
    def right(x):return (x>>1)|((x&1)<<(n-1))
    def f18(x):return (~x&m)&(left(x)^right(x))
    def f126(x):return (left(x)^x)|(x^right(x))
    def diff(x):return x^right(x)
    return f18,f126,diff


def orbit_partition(n,f):
    N=1<<n
    succ=[f(x) for x in range(N)]
    label=[None]*N; cycles={}
    for s in range(N):
        if label[s] is not None:continue
        seen={};path=[];v=s
        while label[v] is None and v not in seen:
            seen[v]=len(path);path.append(v);v=succ[v]
        if label[v] is not None:
            lab=label[v]
        else:
            ring=path[seen[v]:]
            lab=min(ring)
            cycles[lab]=tuple(ring)
        for x in path:label[x]=lab
    return succ,cycles,Counter(label)


def main():
    expected_4_b18=[(1,12),(2,2),(2,2)]
    expected_4_b126=[(1,8),(2,4),(2,4)]
    for n in range(1,16):
        f18,f126,D=maps(n)
        a,ca,ba=orbit_partition(n,f18)
        b,cb,bb=orbit_partition(n,f126)
        assert sorted(len(c) for c in ca.values())==sorted(len(c) for c in cb.values())
        for lab,cyc in cb.items():
            img=[D(x) for x in cyc]
            assert len(set(img))==len(cyc)
            assert min(img) in ca and set(ca[min(img)])==set(img)
        if n==4:
            assert sorted((len(c),ba[lab]) for lab,c in ca.items())==sorted(expected_4_b18)
            assert sorted((len(c),bb[lab]) for lab,c in cb.items())==sorted(expected_4_b126)
            assert len(set(a))==7 and len(set(b))==6
        if n==11:
            assert sum(len(c)==11 for c in ca.values())==2
            assert sum(len(c)==11 for c in cb.values())==2
        if n in (4,8,11,15):
            print('circumference',n,'orbits by least period',dict(sorted(Counter(map(len,cb.values())).items())))
    print('DIRECT_ORBIT_OK')

if __name__=='__main__':main()
