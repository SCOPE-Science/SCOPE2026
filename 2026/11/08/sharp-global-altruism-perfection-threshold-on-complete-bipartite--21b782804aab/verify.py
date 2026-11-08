#!/usr/bin/env python3
"""Independent exact checks for the bipartite equal-treatment coalition theorem.
Run: python3 verify.py. Uses only Python's standard library.
"""
from fractions import Fraction
from itertools import product


def threshold(a,b):
    assert a>=1 and b>=1
    if a==b==1: return Fraction(0)
    return max(Fraction(1),Fraction(2*(a-1),b+1),Fraction(2*(b-1),a+1))

def is_friend(u,v,a):
    return (u<a)!=(v<a)

def cut_components(a,b,i,side):
    n=a+b
    center={i}|({j for j in range(n) if is_friend(i,j,a)})
    fc=ec=0
    for u in range(n):
        for v in range(u+1,n):
            if (u in side)==(v in side): continue
            w=int(u in center)+int(v in center)
            if is_friend(u,v,a): fc+=w
            else: ec+=w
    return fc,ec

def exhaustive_cut_threshold(a,b,i):
    n=a+b; others=[j for j in range(n) if j!=i]
    best=Fraction(0)
    for bits in product((0,1),repeat=n-1):
        side={i}|{j for j,z in zip(others,bits) if z}
        if len(side)==n: continue
        f,e=cut_components(a,b,i,side)
        assert f>0, (a,b,i,side)
        best=max(best,Fraction(e,f))
    return best

def partitions(n):
    v=[0]*n
    def go(k,m):
        if k==n:
            yield tuple(v);return
        for x in range(m+2):
            v[k]=x
            yield from go(k+1,max(m,x))
    yield from go(1,0)

def utility(a,b,i,part,alpha):
    n=a+b; neigh=[i]+[j for j in range(n) if is_friend(i,j,a)]
    ans=Fraction(0)
    for j in neigh:
        for k in range(n):
            if j==k or part[j]!=part[k]:continue
            ans+=(alpha if is_friend(j,k,a) else -1)
    return ans

def main():
    checks=0
    for a in range(1,9):
        for b in range(1,9):
            if a+b>11: continue
            exa=exhaustive_cut_threshold(a,b,0)
            exb=exhaustive_cut_threshold(a,b,a)
            expect=threshold(a,b)
            assert max(exa,exb)==expect,(a,b,exa,exb,expect)
            checks+=2
    full=0
    for a in range(1,5):
        for b in range(1,5):
            if a+b>7:continue
            n=a+b; critical=threshold(a,b)
            for alpha in sorted({Fraction(0),max(Fraction(0),critical-Fraction(1,10)),critical,critical+Fraction(1,10),Fraction(n)}):
                isperfect=True
                g=(0,)*n
                base=[utility(a,b,i,g,alpha) for i in range(n)]
                for pi in partitions(n):
                    for i in range(n):
                        if utility(a,b,i,pi,alpha)>base[i]:isperfect=False
                        full+=1
                assert isperfect==(alpha>=critical),(a,b,alpha,critical,isperfect)
    for a in range(1,35):
        for b in range(1,35):
            p=a-1
            endpoint=max(Fraction(int(a+b>2)),Fraction(a-1,2*b),Fraction(2*(b-1),a+1))
            for x in range(1,a+1):
                for y in range(b+1):
                    f=(x+1)*(b-y)+(a-x)*y
                    e=(a-x)+2*y*(b-y)
                    if f: assert Fraction(e,f)<=endpoint,(a,b,x,y)
                    checks+=1
    print('PASS: cut thresholds agree with independent pair-by-pair exhaustive cuts')
    print('PASS: full set partitions match sharp threshold for every tested model, including boundaries')
    print(f'PASS: {checks} threshold comparisons and {full} exact agent-partition payoff comparisons')
    print('K_1,5:',threshold(1,5),'K_4,4:',threshold(4,4),'K_2,10:',threshold(2,10))

if __name__=='__main__': main()
