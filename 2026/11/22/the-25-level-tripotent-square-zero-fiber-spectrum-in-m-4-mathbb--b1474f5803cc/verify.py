#!/usr/bin/env python3
"""Reproduce the tripotent-plus-square-zero fiber census in M_4(F_2).
No external packages; exact integer arithmetic only.
"""
from collections import Counter
from itertools import product
from math import prod

def matmul(A, B, n):
    mask=(1<<n)-1
    result=0
    for i in range(n):
        active=(A>>(i*n))&mask
        row=0
        while active:
            bit=active&-active
            row ^= (B>>((bit.bit_length()-1)*n))&mask
            active-=bit
        result |= row<<(i*n)
    return result

def polynomial_multiply(f,g):
    h=0
    while g:
        if g&1: h ^= f
        f <<= 1; g >>= 1
    return h

def polynomial_rem(f,g):
    d=g.bit_length()-1
    while f and f.bit_length()>d:
        f^=g<<(f.bit_length()-d-1)
    return f

def irreducibles(maxdegree):
    result=[]
    for d in range(1,maxdegree+1):
        for f in range(1<<d,1<<(d+1)):
            if not (f& (1<<d)): continue
            if all(polynomial_rem(f,g)!=0 for k in range(1,d//2+1)
                   for g in range((1<<k),1<<(k+1))):
                result.append((f,d))
    return result

def partitions(k, hi=None):
    if k==0: yield ();return
    if hi is None: hi=k
    for j in range(min(hi,k),0,-1):
        for p in partitions(k-j,j):
            yield (j,)+p

def companion(f):
    n=f.bit_length()-1
    rows=[0]*n
    for i in range(n-1): rows[i+1]|=1<<i
    for i in range(n):
        if (f>>i)&1: rows[i]|=1<<(n-1)
    return rows

def blockdiag(blocks):
    n=sum(len(b) for b in blocks); rows=[]; offset=0
    for b in blocks:
        for row in b: rows.append(row<<offset)
        offset+=len(b)
    assert len(rows)==n
    return sum(row<<(i*n) for i,row in enumerate(rows))

def powpol(f,k):
    h=1
    for _ in range(k):h=polynomial_multiply(h,f)
    return h

def all_rcf_types(n):
    irr=irreducibles(n)
    def rec(i,left,parts):
        if i==len(irr):
            if left==0: yield tuple(parts)
            return
        f,d=irr[i]
        for weight in range(left//d+1):
            for lam in partitions(weight):
                if not lam: yield from rec(i+1,left,parts)
                else: yield from rec(i+1,left-weight*d,parts+[(f,d,lam)])
    yield from rec(0,n,[])

def automorphisms_count(types):
    result=1
    for f,d,lam in types:
        column_lengths=[sum(x>=j for x in lam) for j in range(1,max(lam)+1)]
        E=d*sum(x*x for x in column_lengths)
        # integer version of 2^E * product(1-2^(-d*s))
        counts=Counter(lam)
        denominators=sum(d*s for m in counts.values() for s in range(1,m+1))
        factor=1
        for m in counts.values():
            for s in range(1,m+1): factor*=2**(d*s)-1
        result*=2**(E-denominators)*factor
    return result

def walsh_inplace(a):
    n=len(a);h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                u=a[j];v=a[j+h]
                a[j]=u+v;a[j+h]=u-v
        h*=2

def census():
    n=4; size=1<<(n*n)
    trip=[0]*size; square=[0]*size
    square_list=[]
    for a in range(size):
        a2=matmul(a,a,n)
        if a2==0: square[a]=1;square_list.append(a)
        if matmul(a,a2,n)==a: trip[a]=1
    assert sum(trip)==5317 and len(square_list)==316
    # First route: enumerate every admissible ordered pair, with no aggregation shortcuts.
    direct=[0]*size
    for T,valid in enumerate(trip):
        if valid:
            for N in square_list:
                direct[T^N]+=1
    # Second route: entire-space integral Walsh convolution.
    t=trip.copy();s=square.copy(); walsh_inplace(t);walsh_inplace(s)
    conv=[a*b for a,b in zip(t,s)]; walsh_inplace(conv)
    assert all(v%size==0 for v in conv)
    conv=[v//size for v in conv]
    assert conv==direct
    frequency=Counter(conv)
    assert sum(frequency.values())==size
    assert sum(k*v for k,v in frequency.items())==sum(trip)*sum(square)
    # An independent route: one canonical representative per rational class.
    gl=prod(2**n-2**i for i in range(n))
    rows=[]
    for types in all_rcf_types(n):
        blocks=[companion(powpol(f,j)) for f,d,lam in types for j in lam]
        A=blockdiag(blocks)
        fibers=sum(matmul(A^N,matmul(A^N,A^N,n),n)==(A^N) for N in square_list)
        # formula uses centralizer units of F_2[t]-modules
        aut=automorphisms_count(types)
        assert gl%aut==0
        rows.append((types,gl//aut,fibers,A))
    predicted=Counter()
    for types,cs,k,A in rows: predicted[k]+=cs
    assert sum(cs for _,cs,_,_ in rows)==size
    assert predicted==frequency
    assert frequency[1]==1 and conv[0]==1 and conv[sum(1<<(i*n+i) for i in range(n))]==316
    print('TRIPOTENT_SQUAREZERO_FIBERS_OK',len(rows),sum(frequency.values()),len(frequency))
    print('TRIPOTENTS',sum(trip),'SQUARE_ZERO',len(square_list))
    print('FREQUENCIES',sorted(frequency.items()))
    for types,cs,k,A in rows:
        label=' * '.join(f'{f:#b}:{"-".join(map(str,lam))}' for f,d,lam in types)
        print('CLASS',label,'SIZE',cs,'FIBER',k,'REP',A)
    return rows
if __name__=='__main__':
    import csv,sys
    rows=census()
    if len(sys.argv)>1:
        with open(sys.argv[1],'w',encoding='utf-8',newline='') as output:
            w=csv.writer(output,lineterminator='\n')
            w.writerow(['primary_elementary_divisors','similarity_class_size','fiber_count','row_major_binary_integer'])
            for types,cs,k,A in sorted(rows,key=lambda row:(row[2],row[1],row[3])):
                w.writerow([';'.join(f'{f:#b}^({",".join(map(str,lam))})' for f,d,lam in types),cs,k,A])

