#!/usr/bin/env python3
"""Exact Pappus perfect-matching Boolean Fourier spectrum and inverse.

Run with Python 3.9+; only the standard library is required.
"""
from collections import Counter
from fractions import Fraction
from math import lcm


def build_incidence():
    points = 'ABCabcXYZ'
    lines = ('ABC', 'abc', 'AbX', 'aBX', 'AcY', 'aCY', 'BcZ', 'bCZ', 'XYZ')
    assert len(points) == len(lines) == 9
    assert all(sum(p in ln for ln in lines) == 3 for p in points)
    edges = sorted((i, 9+j) for i, ln in enumerate(lines)
                   for j,p in enumerate(points) if p in ln)
    return edges


def build_lcf():
    offsets = (5,7,-7,7,-7,-5)*3
    edges = {tuple(sorted((i,(i+1)%18))) for i in range(18)}
    edges |= {tuple(sorted((i,(i+offsets[i])%18))) for i in range(18)}
    return sorted(edges)


def enumerate_matchings(edges):
    adj = [[] for _ in range(18)]
    for index, (u,v) in enumerate(edges):
        adj[u].append((v,index));adj[v].append((u,index))
    out = []
    def rec(uncovered, mask):
        if not uncovered:
            out.append(mask); return
        v = min(uncovered)
        for w, ix in adj[v]:
            if w in uncovered:
                rec(uncovered - {v,w}, mask | (1<<ix))
    rec(set(range(18)),0)
    assert len(set(out)) == len(out)
    return out


def fwht(array):
    arr = array[:]
    h=1
    while h<len(arr):
        for lo in range(0,len(arr),2*h):
            for j in range(lo,lo+h):
                a,b=arr[j],arr[j+h]
                arr[j],arr[j+h]=a+b,a-b
        h*=2
    return arr


def invariants(edges, matchings):
    assert len(edges)==27 and len(matchings)==42
    deg=Counter(u for e in edges for u in e)
    assert all(deg[v]==3 for v in range(18))
    for m in matchings:
        assert m.bit_count()==9
        covered=[0]*18
        for i,(u,v) in enumerate(edges):
            if m & (1<<i): covered[u]+=1;covered[v]+=1
        assert covered==[1]*18
    assert all(sum((m>>e)&1 for m in matchings)==14 for e in range(27))
    adj=[[] for _ in range(18)]
    for e in edges:
        u,v=e;adj[u].append(v);adj[v].append(u)
    # deterministic BFS spanning tree, 17 edges -> 10 chords
    seen={0}; queue=[0]; tree=set()
    while queue:
        u=queue.pop(0)
        for v in sorted(adj[u]):
            if v not in seen:
                seen.add(v);queue.append(v);tree.add((min(u,v),max(u,v)))
    assert len(seen)==18 and len(tree)==17
    chords=sorted(set(edges)-tree)
    assert len(chords)==10
    pos={e:i for i,e in enumerate(edges)}
    support=[0]*1024
    for m in matchings:
        cm=sum(((m>>pos[e])&1)<<i for i,e in enumerate(chords))
        support[cm]+=1
    assert sum(support)==42 and max(support)==1
    # The matching differences generate the full 10-dimensional cycle space.
    masks=[i for i,v in enumerate(support) if v]
    base=masks[0]
    pivots={}
    for m in masks[1:]:
        x=m^base
        while x:
            k=x.bit_length()-1
            if k not in pivots:
                pivots[k]=x;break
            x^=pivots[k]
    assert len(pivots)==10
    spectrum=fwht(support)
    # Independent signed-permanent recurrence for all 1024 incidence signings.
    # It uses row-by-row subset DP, rather than matching enumeration or FWHT.
    if all(u<9 and v>=9 for u,v in edges):
        chord_bit={e:i for i,e in enumerate(chords)}
        opts=[]
        for row in range(9):
            opts.append([(v-9, 1<<chord_bit[(row,v)] if (row,v) in chord_bit else 0)
                         for u,v in edges if u==row])
        for sign_mask in range(1024):
            dp=[0]*512; dp[0]=1
            for row in range(9):
                nxt=[0]*512
                for used in range(512):
                    if used.bit_count()!=row or not dp[used]:continue
                    for col,chord in opts[row]:
                        if not (used>>col)&1:
                            nxt[used|(1<<col)] += dp[used]*(-1 if sign_mask&chord else 1)
                dp=nxt
            assert dp[511]==spectrum[sign_mask]
    assert all((x%4)==2 for x in spectrum)
    magnitudes=Counter(abs(v) for v in spectrum)
    assert magnitudes=={2:504,6:342,10:81,14:96,42:1}
    L=lcm(*(abs(v) for v in spectrum))
    assert L==210
    integers=fwht([L//v for v in spectrum])
    # g(x)=integer[x]/(1024*210), and T*g=identity
    norm=Fraction(sum(abs(k) for k in integers),1024*L)
    assert norm==Fraction(1637,210)
    assert sum(k!=0 for k in integers)==1024
    return magnitudes, norm, Counter(integers), support, spectrum, integers


def check_convolution(support,integers):
    # Verify all 1024 convolution identities in reduced group algebra.
    # The inverse is not centered at zero; this code's WHT convention sets
    # (support * integers)[0] = 1024*210, the rest zero.
    trans=fwht(integers)
    assert all(a*b==1024*210 for a,b in zip(fwht(support),trans))
    # The displayed equality implies inverse convolution by Fourier inversion.
    assert sum(support[i]*integers[i] for i in range(1024))==1024*210
    # Independent selected coefficient checks in the standard basis.
    for shift in (1,2,3,7,31,255,512,1023):
        assert sum(support[i]*integers[i^shift] for i in range(1024))==0


def main():
    cases=[]
    for name,builder in [('incidence',build_incidence),('LCF',build_lcf)]:
        edges=builder()
        match=enumerate_matchings(edges)
        m,n,counts,s,w,k=invariants(edges,match)
        check_convolution(s,k)
        cases.append((m,n,Counter(abs(z) for z in k)))
        print(name, 'edges',len(edges),'perfect_matchings',len(match),
              'quotient_characters',len(w),'unsigned_spectrum',sorted(m.items()),
              'inverse_norm',str(n))
    assert cases[0]==cases[1]
    print('PAPPUS_WALSH_EXACT_PASS')

if __name__=='__main__': main()
