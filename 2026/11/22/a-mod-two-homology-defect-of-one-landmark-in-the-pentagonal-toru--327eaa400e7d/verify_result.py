#!/usr/bin/env python3
"""Standalone exact F2 chain-rank verification for the 5 x 5 toroidal geodesic general-position complex and its point-puncture pair."""
from itertools import combinations
from collections import deque

N=25
V=[(i,j) for i in range(5) for j in range(5)]

def dist_formula(a,b):
    i,j=V[a]; k,l=V[b]
    return min(abs(i-k),5-abs(i-k))+min(abs(j-l),5-abs(j-l))

def bfs(a):
    d=[-1]*N;d[a]=0;todo=deque([a])
    while todo:
        t=todo.popleft(); i,j=V[t]
        for x,y in (((i+1)%5,j),((i-1)%5,j),(i,(j+1)%5),(i,(j-1)%5)):
            z=5*x+y
            if d[z]<0:d[z]=d[t]+1;todo.append(z)
    return d

D=[bfs(a) for a in range(N)]
assert all(D[a][b]==dist_formula(a,b) for a in range(N) for b in range(N))
BAD=set()
for a,b,c in combinations(range(N),3):
    if D[a][b]+D[b][c]==D[a][c] or D[a][c]+D[c][b]==D[a][b] or D[b][a]+D[a][c]==D[b][c]:BAD.add((a,b,c))

def enumeration_by_extensions():
    faces=[set() for _ in range(7)]
    old={()}
    for k in range(1,8):
        cur=set()
        for small in old:
            last=small[-1] if small else -1
            for v in range(last+1,N):
                s=small+(v,)
                if k<3 or all(trip not in BAD for trip in combinations(s,3)):
                    cur.add(s)
        faces[k-1]=cur;old=cur
    return faces

def enumeration_by_skeleton():
    faces=[set() for _ in range(7)]
    for k in range(1,8):
        for s in combinations(range(N),k):
            if k==3 and s in BAD:continue
            if k>=4 and any(sub not in faces[k-2] for sub in combinations(s,k-1)):continue
            faces[k-1].add(s)
    return faces
F=enumeration_by_extensions();G=enumeration_by_skeleton()
assert F==G
assert tuple(len(x) for x in F)==(25,300,1400,2450,1360,50,0)
F=F[:-1]
Y=[{s for s in f if 0 not in s} for f in F]
R=[{s for s in f if 0 in s} for f in F]
assert tuple(len(x) for x in Y)==(24,276,1232,2058,1088,38)
assert tuple(len(x) for x in R)==(1,24,168,392,272,12)

def xor_rank(rows):
    piv={}
    for row in rows:
        q=row
        while q:
            bit=q.bit_length()-1
            if bit in piv:q^=piv[bit]
            else:piv[bit]=q;break
    return len(piv)

def chain_data(f):
    ranks=[]
    for dim in range(1,len(f)):
        lower=sorted(f[dim-1]); upper=sorted(f[dim]);idx={s:j for j,s in enumerate(lower)}
        cols=[];rowbits=[0]*len(lower)
        for j,ss in enumerate(upper):
            col=0
            for sub in combinations(ss,dim):
                if sub in idx:
                    i=idx[sub];col^=1<<i;rowbits[i]^=1<<j
            cols.append(col)
        a=xor_rank(cols);b=xor_rank(rowbits)
        assert a==b,(dim,a,b)
        ranks.append(a)
        if dim>=2:
            prev_idx={s:i for i,s in enumerate(sorted(f[dim-2]))}
            for ss in upper:
                sq=0
                for sub in combinations(ss,dim):
                    if sub not in idx:continue
                    for sub2 in combinations(sub,dim-1):
                        if sub2 in prev_idx:sq^=1<<prev_idx[sub2]
                assert sq==0,(dim,ss)
    return ranks

rx=chain_data(F);ry=chain_data(Y);rr=chain_data(R)
assert rx==[24,276,1074,1290,50],rx
assert ry==[23,253,935,1038,38],ry
assert rr==[1,23,139,241,12],rr

def bettis(f,ranks,reduced):
    return [len(s)-(ranks[k-1] if k else 0)-(ranks[k] if k<len(ranks) else 0)-(1 if reduced and k==0 else 0) for k,s in enumerate(f)]
bx=bettis(F,rx,True);by=bettis(Y,ry,True);br=bettis(R,rr,False)
assert bx==[0,0,50,86,20,0],bx
assert by==[0,0,44,85,12,0],by
assert br==[0,0,6,12,19,0],br
# Compute the actual homology inclusion maps as ranks of [B_k(X), i(Z_k(Y))] minus rank B_k(X).
def boundary_columns(top,bot):
    index={s:i for i,s in enumerate(sorted(bot))}
    out=[]
    for ss in sorted(top):
        q=0
        for sf in combinations(ss,len(ss)-1):
            if sf in index:q^=1<<index[sf]
        out.append(q)
    return out

def kernel_vectors(cols):
    piv={};cycles=[]
    for j,col in enumerate(cols):
        q=col;co=1<<j
        while q:
            b=q.bit_length()-1
            if b in piv:q^=piv[b][0];co^=piv[b][1]
            else:piv[b]=(q,co);break
        if q==0:cycles.append(co)
    return cycles

def inclusion_rank(k):
    xk=sorted(F[k]);yk=sorted(Y[k])
    kernel=kernel_vectors(boundary_columns(Y[k],Y[k-1]))
    assert len(kernel)==len(yk)-ry[k-1]
    piv={}
    def insert(q):
        while q:
            bit=q.bit_length()-1
            if bit in piv:q^=piv[bit]
            else:piv[bit]=q;return True
        return False
    for col in boundary_columns(F[k+1],F[k]):insert(col)
    baseline=len(piv)
    target={ss:i for i,ss in enumerate(xk)}
    indices=[target[s] for s in yk]
    for co in kernel:
        lifted=0
        while co:
            bit=co&-co;j=bit.bit_length()-1
            lifted^=1<<indices[j];co^=bit
        insert(lifted)
    return len(piv)-baseline
map_ranks={k:inclusion_rank(k) for k in (2,3,4)}
assert map_ranks=={2:44,3:74,4:12}
assert bx[2]-map_ranks[2]==br[2]
assert bx[3]-map_ranks[3]==br[3]
assert (by[3]-map_ranks[3])+(bx[4]-map_ranks[4])==br[4]
assert by[2]-map_ranks[2]==0 and by[4]-map_ranks[4]==0
print('PASS: two independent face-enumerations, BFS/formula metrics, column/row ranks, boundary compositions, direct chain-level inclusion maps')
print('Full face counts',list(map(len,F)),'boundary ranks',rx,'reduced Betti',bx)
print('Punctured face counts',list(map(len,Y)),'boundary ranks',ry,'reduced Betti',by)
print('Relative face counts',list(map(len,R)),'boundary ranks',rr,'relative Betti',br)
print('Inclusion ranks H_2,H_3,H_4',map_ranks)
