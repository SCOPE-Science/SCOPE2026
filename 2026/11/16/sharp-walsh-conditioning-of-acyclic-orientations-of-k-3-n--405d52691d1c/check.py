#!/usr/bin/env python3
"""Exact signed orientation Fourier verification for complete bipartite 3-by-n graphs."""
import csv
import itertools
import pathlib
import sys
from collections import Counter

CHAINS=[]
for perm in itertools.permutations(range(3)):
    v=0
    chain=[0]
    for row in perm:
        v |= 1 << row
        chain.append(v)
    CHAINS.append(tuple(chain))
INTERSECTIONS=[(tuple(c),1) for c in CHAINS]
INTERSECTIONS += [((0,v,7),-1) for v in range(1,7)]
INTERSECTIONS.append(((0,7),1))
FACTORS=tuple(tuple(sum(1 if (u&v).bit_count()%2==0 else -1 for v in c) for u in range(8)) for c,sgn in INTERSECTIONS)

def formula(cols):
    answer=0
    for (_,sgn),fac in zip(INTERSECTIONS,FACTORS):
        term=sgn
        for u in cols:
            term*=fac[u]
        answer+=term
    return answer

def toposort_acyclic(x,n):
    indeg=[0]*(n+3)
    children=[[] for _ in range(n+3)]
    for j in range(n):
        for i in range(3):
            bit=(x>>(3*j+i))&1
            source,target=(3+j,i) if bit else (i,3+j)
            children[source].append(target)
            indeg[target]+=1
    work=[v for v in range(n+3) if indeg[v]==0]
    seen=0
    while work:
        v=work.pop()
        seen+=1
        for w in children[v]:
            indeg[w]-=1
            if indeg[w]==0:work.append(w)
    return seen==n+3

def chains_acyclic(x,n):
    columns=[(x>>(3*j))&7 for j in range(n)]
    for a in columns:
        for b in columns:
            if (a&~b) and (b&~a):return False
    return True

def fwht(data):
    length=len(data)
    stride=1
    while stride<length:
        for i in range(0,length,2*stride):
            for j in range(i,i+stride):
                a,b=data[j],data[j+stride]
                data[j],data[j+stride]=a+b,a-b
        stride*=2
    return data

def verify(n):
    N=1<<(3*n)
    indicator=[]
    for x in range(N):
        a=toposort_acyclic(x,n)
        b=chains_acyclic(x,n)
        assert a==b,(n,x)
        indicator.append(int(a))
    orientation_count=sum(indicator)
    spectrum=fwht(indicator)
    expected=6*4**n-6*3**n+2**n
    assert orientation_count==expected,(n,orientation_count,expected)
    h=Counter(spectrum)
    assert sum(h.values())==N
    assert sum(v*v*c for v,c in h.items())==N*orientation_count
    assert h[0]==N//2
    assert min(abs(v) for v in spectrum if v)!=0
    assert min(abs(v) for v in spectrum if v)==2
    for u,val in enumerate(spectrum):
        cols=[(u>>(3*j))&7 for j in range(n)]
        assert val==formula(cols),(n,u,val,formula(cols))
        assert (val==0)==(u.bit_count()%2==1),(n,u,val)
        if val:assert val%4==2
    assert spectrum[0]==expected
    return orientation_count,h

def general_checks():
    # The finite calculation here checks exact identities; the separate symbolic
    # argument in RESULT.md supplies the unbounded proof.
    for n in range(2,101):
        u_even=[1]*(n-1)+[7]
        u_odd=[2,3]+[1]*(n-2)
        assert formula(u_even)==1+(-1)**n
        assert formula(u_odd)==(-1)**n-1
        assert (6*4**n-6*3**n+2**n)%4==2
        assert formula([0]*n)==6*4**n-6*3**n+2**n

def main():
    rows=[]
    for n in range(2,6):
        count,h=verify(n)
        for val,multiplicity in sorted(h.items()):
            rows.append((n,count,val,multiplicity))
    general_checks()
    path=pathlib.Path(__file__).with_name('spectrum_n2_n5.csv')
    if '--write' in sys.argv:
        with path.open('w',encoding='utf-8',newline='') as fd:
            writer=csv.writer(fd,lineterminator='\n')
            writer.writerow(['n','acyclic_orientations','signed_walsh_multiplier','frequency_multiplicity'])
            writer.writerows(rows)
    else:
        with path.open(newline='',encoding='utf-8') as fd:
            reader=csv.reader(fd)
            parsed=list(reader)
        assert parsed[0]==['n','acyclic_orientations','signed_walsh_multiplier','frequency_multiplicity']
        assert [tuple(map(int,row)) for row in parsed[1:]]==rows
    print('K3N_ACYCLIC_WALSH_CONDITIONING_PASS n=2..5 all_frequencies=37440 signed_spectrum_histograms=verified n_to_100=exact_integer_checks')

if __name__=='__main__':main()
