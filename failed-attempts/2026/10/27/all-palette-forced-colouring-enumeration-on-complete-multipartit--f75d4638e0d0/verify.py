#!/usr/bin/env python3
"""Independent exhaustive small-graph test of the forced-colouring count.
Public mathematical reproducibility; accepts no external dependencies.
"""
from itertools import product
from collections import defaultdict
from math import comb, factorial

def stirling2(n,k):
    if n == 0: return int(k==0)
    if k==0: return 0
    T=[[0]*(k+1) for _ in range(n+1)];T[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):T[i][j]=j*T[i-1][j]+T[i-1][j-1]
    return T[n][k]

def mul(a,b):
    c=defaultdict(int)
    for i,ai in a.items():
        for j,bj in b.items():c[i+j]+=ai*bj
    return dict(c)

def plus(a,b,scale=1):
    z=defaultdict(int,a)
    for k,v in b.items():z[k]+=scale*v
    return dict(z)

def formula(part_sizes,L):
    N=sum(part_sizes); r=len(part_sizes)
    if L<r: return {}
    proper=0
    for sizes in product(*(range(1,min(n,L)+1) for n in part_sizes)):
        t=sum(sizes)
        if t>L:continue
        ways=factorial(L)//factorial(L-t)
        for n,k in zip(part_sizes,sizes):ways*=stirling2(n,k)
        proper+=ways
    ans={N:proper}
    # Surjective proper final palettes with t_i >= 1.
    for sizes in product(*(range(1,min(n,L)+1) for n in part_sizes)):
        if sum(sizes)!=L:continue
        coeff=factorial(L)
        multiN=0; mono=[]
        for n,t in zip(part_sizes,sizes):
            coeff*=stirling2(n,t)
            if t>1:multiN+=n
            else:mono.append(n)
        h={0:1}
        for n in mono: h=mul(h,{k:comb(n,k) for k in range(1,n+1)})
        h=plus(h,{sum(mono):1},-1)
        for j in range(len(mono)):
            q={0:1}
            for i,n in enumerate(mono):
                if i!=j:q=mul(q,{k:comb(n,k) for k in range(1,n+1)})
            h=plus(h,q)
        for k,v in h.items():ans[k+multiN]=ans.get(k+multiN,0)+coeff*v
    return {k:v for k,v in sorted(ans.items()) if v}

def predicted_minimum(part_sizes,L):
    N=sum(part_sizes);r=len(part_sizes)
    if L<r:return None
    extra=L-r
    options=[N]
    for j in range(r):
        others=[i for i in range(r) if i!=j]
        for use in product((0,1),repeat=len(others)):
            chosen=[i for bit,i in zip(use,others) if bit]
            if any(part_sizes[i]<2 for i in chosen):continue
            if (extra==0 and chosen) or (extra>0 and (not chosen or len(chosen)>extra)):
                continue
            cap=sum(part_sizes[i]-1 for i in chosen)
            if cap>=extra:
                options.append(r-1+cap)
    return min(options)

def brute(part_sizes,L):
    N=sum(part_sizes)
    if L<2:return {}
    block=[]
    for i,n in enumerate(part_sizes):block.extend([i]*n)
    near=[tuple(j for j in range(N) if block[j]!=block[i]) for i in range(N)]
    count=defaultdict(int)
    for seed in product(range(-1,L),repeat=N):
        colors=list(seed)
        if any(colors[j]!=-1 and colors[j]==colors[i] for i in range(N) if colors[i]!=-1 for j in near[i]):continue
        for _ in range(N):
            todo=[]
            for i,c in enumerate(colors):
                if c!=-1:continue
                used={colors[j] for j in near[i] if colors[j]!=-1}
                if len(used)==L-1:
                    todo.append((i,(set(range(L))-used).pop()))
            if not todo:break
            for i,c in todo:colors[i]=c
        if -1 not in colors and all(colors[i]!=colors[j] for i in range(N) for j in near[i]):
            count[N-seed.count(-1)]+=1
    return dict(sorted(count.items()))

def predicted_assignment_set(part_sizes,L):
    block=tuple(i for i,n in enumerate(part_sizes) for _ in range(n))
    N=len(block); predicted=set()
    for completed in product(range(L),repeat=N):
        palettes=[{completed[j] for j in range(N) if block[j]==i}
                  for i in range(len(part_sizes))]
        if sum(map(len,palettes))!=len(set(completed)):continue
        for seeded in product((0,1),repeat=N):
            candidate=tuple(completed[j] if seeded[j] else -1 for j in range(N))
            if all(seeded):
                predicted.add(candidate)
                continue
            if len(set(completed))!=L:continue
            if any(len(palettes[i])>1 and any(not seeded[j] for j in range(N) if block[j]==i)
                   for i in range(len(part_sizes))):continue
            empty=sum(1 for i in range(len(part_sizes)) if len(palettes[i])==1 and
                      all(not seeded[j] for j in range(N) if block[j]==i))
            if empty<=1:predicted.add(candidate)
    return predicted

def brute_assignment_set(part_sizes,L):
    N=sum(part_sizes)
    block=tuple(i for i,n in enumerate(part_sizes) for _ in range(n))
    near=[tuple(j for j in range(N) if block[j]!=block[i]) for i in range(N)]
    good=set()
    for seed in product(range(-1,L),repeat=N):
        colors=list(seed)
        if any(colors[i]!=-1 and colors[i]==colors[j] for i in range(N) for j in near[i]):continue
        for _ in range(N):
            forces=[]
            for i,c in enumerate(colors):
                if c!=-1:continue
                used={colors[j] for j in near[i] if colors[j]!=-1}
                if len(used)==L-1:forces.append((i,(set(range(L))-used).pop()))
            if not forces:break
            for i,c in forces:colors[i]=c
        if -1 not in colors and all(colors[i]!=colors[j] for i in range(N) for j in near[i]):
            good.add(seed)
    return good

if __name__=='__main__':
    cases = [((1,1),2),((2,1),2),((2,2),2),((2,2),3),((2,2),4),((3,2),3),((3,2),4),((2,1,1),3),((2,1,1),4),((2,2,1),3),((2,2,1),4),((2,2,1),5),((3,1,1),3),((3,1,1),4),((1,1,1,1),4),((2,2,2),3),((2,2,2),4)]
    for n,L in cases:
        f=formula(n,L);b=brute(n,L)
        assert f==b,(n,L,f,b)
        assert min(f)==predicted_minimum(n,L),(n,L,f,predicted_minimum(n,L))
        print(f'PASS parts={n} palette={L} seeded_count={f} assignments={(L+1)**sum(n)}')
    for n,L in [((2,2),3),((3,2),4),((2,1,1),4),((2,2,1),4)]:
        x=predicted_assignment_set(n,L)
        y=brute_assignment_set(n,L)
        assert x==y,(n,L,len(x),len(y),next(iter(x^y)) if x^y else None)
        print(f'PASS structural_classification parts={n} palette={L} assignments={len(x)}')
    print('ALL_EXHAUSTIVE_CASES_PASS')
