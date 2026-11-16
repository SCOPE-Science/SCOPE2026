#!/usr/bin/env python3
"""Exact Fourier certificates for the two length-three Catalan avoidance classes.

Usage: python check.py --write DIRECTORY  OR  python check.py --verify DIRECTORY
Uses only the Python standard library and integer arithmetic.
"""
import argparse
import csv
import itertools
from collections import Counter
from fractions import Fraction
from pathlib import Path

PATTERNS = ((1,2,3),(1,3,2))

def pair_coordinates(n):
    return tuple(itertools.combinations(range(1,n+1),2))

def inversion_mask(perm):
    edges = pair_coordinates(len(perm))
    return sum(1<<t for t,(i,j) in enumerate(edges) if perm[i-1]>perm[j-1])

def contains(perm,pat):
    for i,j,k in itertools.combinations(range(len(perm)),3):
        a,b,c = perm[i],perm[j],perm[k]
        code=(1+(b<a)+(c<a),1+(a<b)+(c<b),1+(a<c)+(b<c))
        if code==pat:return True
    return False

def brute(n,pat):
    return {tuple(p) for p in itertools.permutations(range(1,n+1)) if not contains(p,pat)}

def insert_max(n,pat):
    family={()}
    for m in range(1,n+1):
        updated=set()
        for old in family:
            for k in range(m):
                left,right=old[:k],old[k:]
                if pat==(1,2,3):
                    # The new maximum can complete 123 only after an ascent.
                    if any(left[i]<left[j] for i in range(len(left)) for j in range(i+1,len(left))):continue
                else:
                    # The new maximum can occur only in the middle of 132.
                    if any(a<b for a in left for b in right):continue
                updated.add(left+(m,)+right)
        family=updated
    return family

def hadamard(a):
    a=a[:]
    step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):
                x,y=a[j],a[j+step]
                a[j]=x+y;a[j+step]=x-y
        step*=2
    return a

def direct_transform(masks,dim):
    return [sum(-1 if (u&v).bit_count()&1 else 1 for v in masks) for u in range(1<<dim)]

def csv_bytes(header,rows):
    import io
    s=io.StringIO(newline='')
    w=csv.writer(s,lineterminator='\n')
    w.writerow(header)
    w.writerows(rows)
    return s.getvalue().encode('utf-8')

def main():
    ap=argparse.ArgumentParser()
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path)
    g.add_argument('--verify',type=Path)
    args=ap.parse_args()
    results={};histrows=[];specrows=[];kernelrows=[]
    for n in range(1,6):
        for pat in PATTERNS:
            label=''.join(map(str,pat))
            family=brute(n,pat)
            from_insertion=insert_max(n,pat)
            assert family==from_insertion,(n,label,'insertion mismatch')
            dim=n*(n-1)//2
            masks=tuple(sorted(map(inversion_mask,family)))
            assert len(set(masks))==len(masks)
            a=[0]*(1<<dim)
            for mask in masks:a[mask]=1
            w1=hadamard(a)
            w2=direct_transform(masks,dim)
            assert w1==w2,(n,label,'direct mismatch')
            assert sum(x*x for x in w1)==(1<<dim)*len(masks)
            hist=Counter(w1)
            zeros=hist[0]
            projection=hadamard([int(x!=0) for x in w1])
            norm=Fraction(sum(abs(x) for x in projection),1<<dim)
            if n==5 and label=="132":
                kernel2=direct_transform([u for u,x in enumerate(w1) if x],dim)
                assert projection==kernel2
                kernelrows.extend((x,value) for x,value in enumerate(projection))
            results[n,label]=dict(n=n,pattern=label,count=len(family),dimension=dim,zeros=zeros,rank=len(w1)-zeros,norm=norm,masks=masks,spectrum=w1,hist=hist)
            for x,count in sorted(hist.items()):histrows.append((n,label,x,count))
            if n==5:
                for u,x in enumerate(w1):specrows.append((label,u,x))
    assert [(results[n,'123']['rank'],results[n,'132']['rank']) for n in range(1,6)]==[(1,1),(1,1),(8,8),(49,46),(1024,817)]
    assert results[4,'123']['zeros']==15 and results[4,'132']['zeros']==18
    assert results[5,'123']['zeros']==0 and results[5,'132']['zeros']==207
    assert results[5,'132']['norm']==Fraction(3797,512)
    assert results[5,'123']['norm']==1
    assert all(x%4==2 for x in results[5,'123']['spectrum'])
    marginals=[]
    edges=pair_coordinates(5)
    for t,e in enumerate(edges):
        count=sum(bool(mask&(1<<t)) for mask in results[5,'123']['masks'])
        assert count%2==0
        marginals.append((e[0],e[1],count))
    assert [x[2] for x in marginals]==[28,28,30,34,28,28,30,28,28,28]
    u=(1<<edges.index((1,3)))|(1<<edges.index((2,5)))
    assert results[5,'132']['spectrum'][u]==0
    contingency=Counter(((m>>edges.index((1,3)))&1,(m>>edges.index((2,5)))&1) for m in results[5,'132']['masks'])
    assert (contingency[0,0],contingency[0,1],contingency[1,0],contingency[1,1])==(4,6,15,17)
    certs={
        'signed_histograms.csv':csv_bytes(('n','avoided_pattern','multiplier','multiplicity'),histrows),
        'spectrum5.csv':csv_bytes(('avoided_pattern','frequency_mask','walsh_multiplier'),specrows),
        'inversion_marginals_123_n5.csv':csv_bytes(('position_i','position_j','inversion_count'),marginals),
        'projection_kernel_132_n5.csv':csv_bytes(('group_element_mask','unnormalized_kernel'),kernelrows),
    }
    base=args.write or args.verify
    if args.write:
        base.mkdir(parents=True,exist_ok=True)
        for path,data in certs.items():(base/path).write_bytes(data)
    else:
        for path,data in certs.items():
            assert (base/path).read_bytes()==data,('certificate mismatch',path)
    print('CATALAN_PATTERN_WALSH_SEPARATION_PASS n4_rank=49,46 n5_rank=1024,817 zero132_n5=207 norm132_n5=3797/512')
    for n in range(1,6):
        print('n',n,'count',results[n,'123']['count'],'123',results[n,'123']['rank'],'132',results[n,'132']['rank'])

if __name__=='__main__':main()
