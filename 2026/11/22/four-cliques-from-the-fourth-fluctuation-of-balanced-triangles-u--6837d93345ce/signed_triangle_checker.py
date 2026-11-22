"""Exact verification for the triangle-balance fourth-cumulant identity.

Usage: python signed_triangle_checker.py
Requires Python 3 standard library only. All moments computed as integers.
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def one_graph(n, mask, verify=True):
    edges=list(combinations(range(n), 2))
    chosen=[e for k,e in enumerate(edges) if mask>>k&1]
    edge_id={e:i for i,e in enumerate(chosen)}
    tri=[]
    for a,b,c in combinations(range(n),3):
        pairs=((a,b),(a,c),(b,c))
        if all(e in edge_id for e in pairs):
            tri.append(sum(1<<edge_id[e] for e in pairs))
    k4=sum(all((a,b) in edge_id for a,b in combinations(q,2))
           for q in combinations(range(n),4))
    m=len(chosen); t=len(tri)
    count=1<<m; ss2=ss4=bs=bs2=bs3=bs4=0
    for signs in range(count):
        s=sum(-1 if (signs&x).bit_count()&1 else 1 for x in tri)
        b=(t+s)//2
        ss2+=s*s
        ss4+=s**4
        bs+=b
        bs2+=b*b
        bs3+=b**3
        bs4+=b**4
    assert ss2==count*t, (n,mask,'variance')
    assert count*ss4-3*ss2**2==count**2*(24*k4-2*t), (n,mask,'fourth')
    # The fourth cumulant of the centered B variable (not its fourth central moment).
    if verify:
        Eb=Fraction(bs,count)
        v=Fraction(bs2,count)-Eb**2
        mu4=(Fraction(bs4,count)-4*Eb*Fraction(bs3,count)
             +6*Eb**2*Fraction(bs2,count)-3*Eb**4)
        kap=mu4-3*v*v
        assert v==Fraction(t,4)
        assert kap==Fraction(3*k4,2)-Fraction(t,8)
        assert (2*kap+v)/3==k4
    return count


def main():
    graphs=signings=0
    for n in range(1,6):
        for mask in range(1<<comb(n,2)):
            signings+=one_graph(n,mask)
            graphs+=1
    for n in (6,):
        full=(1<<comb(n,2))-1
        for mask in (full,full^(1<<0),full^(1<<1)^(1<<7),0):
            signings+=one_graph(n,mask)
            graphs+=1
    print(f'PASS: {graphs} labeled graphs, {signings} exact sign assignments; 5 assertions per graph')

if __name__=='__main__': main()
