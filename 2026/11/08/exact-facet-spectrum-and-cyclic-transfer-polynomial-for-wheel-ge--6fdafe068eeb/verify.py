#!/usr/bin/env python3
"""Independent finite checks for maximal general-position sets of wheel graphs."""
from collections import Counter, defaultdict
from itertools import combinations


def add(A,B):
    C=Counter(A)
    for k,v in B.items(): C[k]+=v
    return {k:v for k,v in C.items() if v}
def shift(A,degree): return {k+degree:v for k,v in A.items()}
def difference(A,B):
    C=Counter(A)
    for k,v in B.items(): C[k]-=v
    return {k:v for k,v in C.items() if v}
def prediction(limit):
    R={m:{} for m in range(-6,2)}
    R[2]={1:2};R[3]={2:3};R[4]={2:6};R[5]={3:5};R[6]={3:2,4:3}
    for m in range(7,limit+1):
        R[m]=difference(add(add(shift(R[m-2],1),shift(R[m-3],2)),shift(R[m-4],2)),shift(R[m-6],3))
    return R

def rim_good(mask,m):
    return all(not all((mask>>((i+j)%m)) & 1 for j in range(3)) for i in range(m))

def structural_facet(mask,m):
    if not rim_good(mask,m):return False
    for i in range(m):
        if not (mask>>i)&1 and rim_good(mask|(1<<i),m):return False
    return True

def cyclic_run_facet(mask,m):
    if mask==0 or mask==(1<<m)-1:return False
    start=next(i for i in range(m) if (mask>>i)&1 and not((mask>>((i-1)%m))&1))
    runs=[]
    pos=start
    while True:
        a=0
        while (mask>>(pos%m))&1:
            a+=1;pos+=1
        b=0
        while not((mask>>(pos%m))&1):
            b+=1;pos+=1
        runs.append((a,b))
        if pos%m==start:break
        if pos-start>m:raise AssertionError('run traversal')
    return all(a in (1,2) and b in (1,2) and (b!=2 or (a==2 and runs[(i+1)%len(runs)][0]==2)) for i,(a,b) in enumerate(runs))

def wheel_dist(m):
    N=m+1
    A=[[False]*N for _ in range(N)]
    for i in range(1,N):
        A[0][i]=A[i][0]=True
        j=1+(i%m)
        A[i][j]=A[j][i]=True
    distances=[]
    for s in range(N):
        d=[-1]*N;d[s]=0;todo=[s]
        for v in todo:
            for w in range(N):
                if A[v][w] and d[w]<0:
                    d[w]=d[v]+1;todo.append(w)
        distances.append(d)
    return distances

def gp_from_dist(mask,distances,N):
    selected=[i for i in range(N) if (mask>>i)&1]
    for a,b,c in combinations(selected,3):
        if any(distances[x][y]+distances[y][z]==distances[x][z] for x,y,z in ((a,b,c),(a,c,b),(b,a,c))):return False
    return True

def check():
    NMAX=17
    R=prediction(NMAX)
    rim_count=0
    wheel_subsets=0
    rim_subsets=0
    rim_facets=0
    for m in range(4,NMAX+1):
        actual=Counter()
        good={mask for mask in range(1<<m) if rim_good(mask,m)}
        rim_subsets+=1<<m
        for mask in good:
            flag=structural_facet(mask,m)
            assert flag==cyclic_run_facet(mask,m),(m,mask)
            if flag:actual[mask.bit_count()]+=1
        rim_count+=len(good);rim_facets+=sum(actual.values())
        assert dict(actual)==R[m],(m,dict(actual),R[m])
        assert set(actual)==set(range((m+1)//2,2*m//3+1))
        if m<=11:
            dist=wheel_dist(m)
            good_full=set()
            for mask in range(1<<(m+1)):
                flag=gp_from_dist(mask,dist,m+1)
                if flag:good_full.add(mask)
                rim=mask>>1
                predicted=(rim_good(rim,m) if not(mask&1) else (rim.bit_count()<=1 or (rim.bit_count()==2 and any((rim>>i)&1 and (rim>>((i+1)%m))&1 for i in range(m)))))
                assert flag==predicted,(m,mask,flag,predicted)
            full_facets=Counter(mask.bit_count() for mask in good_full if all((mask|(1<<i)) not in good_full for i in range(m+1) if not (mask>>i)&1))
            expected=Counter(actual) if m>=5 else Counter({2:2})
            expected[3]+=m
            assert full_facets==expected,(m,full_facets,expected)
            wheel_subsets+=1<<(m+1)
    # The base m=3 is the four-vertex complete graph; only V itself is maximal.
    assert gp_from_dist(0b1111,wheel_dist(3),4)
    print(f'VERIFY_OK rim_orders=4..{NMAX} rim_masks={rim_subsets} valid_rim={rim_count} rim_facets={rim_facets} brute_wheels=4..11 wheel_masks={wheel_subsets} independent_geodesics=PASS cyclic_runs=PASS rational_recurrence=PASS spectra=PASS')

if __name__=='__main__':check()
