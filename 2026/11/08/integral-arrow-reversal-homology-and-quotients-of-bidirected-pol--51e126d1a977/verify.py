"""Finite checks for direction-reversal quotients of bidirected cycle multipath complexes.
Standard library only. All simplices are generated independently as directed-arrow subsets.
"""
from itertools import combinations
from collections import defaultdict
from math import gcd

def edges(m):
    return [(i,(i+1)%m) for i in range(m)] + [((i+1)%m,i) for i in range(m)]

def admissible(subset, arr, m):
    # Check path components by indegree/outdegree and cycles, not word encoding.
    inp=[0]*m;out=[0]*m;succ={}
    for j in subset:
        u,v=arr[j]
        out[u]+=1;inp[v]+=1;succ[u]=v
        if out[u]>1 or inp[v]>1:return False
    for start in range(m):
        if start not in succ:continue
        v=start;seen=set()
        while v in succ and v not in seen:
            seen.add(v);v=succ[v]
        if v in seen:return False
    return True

def faces(m):
    arr=edges(m)
    # independent method: recursive subset generation and graph path tests
    allf={():True}; frontier=[()]
    for t in range(1,m):
        nextf=[]
        for x in frontier:
            for j in range(x[-1]+1 if x else 0,2*m):
                v=x+(j,)
                if admissible(v,arr,m):allf[v]=True;nextf.append(v)
        frontier=nextf
    return list(allf)

def sign_perm_image(idx,image):
    z=[image[i] for i in idx]
    return -1 if sum(z[i]>z[j] for i in range(len(z)) for j in range(i+1,len(z)))%2 else 1

def reversal_map(m):return [i+m for i in range(m)]+[i for i in range(m)]

def rotation_map(m,k):return [((i+k)%m) for i in range(m)]+[m+((i+k)%m) for i in range(m)]

def signed_lf(m,fs,g):
    # Augmented-chain Lefschetz, includes C_-1 trace=1.
    tr=1
    for face in fs:
        if not face:continue
        if tuple(sorted(g[i] for i in face))==face:
            tr+=(-1)**len(face)*sign_perm_image(face,g)
    return -tr

def predicted(m,k,with_reverse):
    topdeg=m-2
    j=(m-1)//2 if m%4==1 else (m-2)//2
    lowrank=3 if m%4==0 else 1
    if with_reverse:
        toptr=0
        lowtr=(-(-1)**k + (2 if k%4==0 else (-2 if k%4==2 else 0))) if m%4==0 else -1
    else:
        toptr=2*((-1)**((m-1)*k))
        lowtr=(3 if k%4==0 else -1) if m%4==0 else 1
    return (-1)**topdeg*toptr+(-1)**j*lowtr

def rank_mod_p(rows, p):
    # Sparse column vectors stored as row index -> coefficient; elimination over F_p.
    piv={}
    for row in rows:
        x={i:v%p for i,v in row.items() if v%p}
        while x:
            pivot=min(x)
            if pivot not in piv:
                inv=pow(x[pivot],-1,p)
                piv[pivot]={a:b*inv%p for a,b in x.items()}
                break
            factor=x[pivot]
            for a,b in piv[pivot].items():
                y=(x.get(a,0)-factor*b)%p
                if y:x[a]=y
                elif a in x:del x[a]
    return len(piv)

def quotient_betti(m,fs,prime):
    a=reversal_map(m)
    def canonical(face):
        mate=tuple(sorted(a[i] for i in face))
        return min(face,mate)
    bydim=defaultdict(set)
    for f in fs:
        if f:bydim[len(f)-1].add(canonical(f))
    levels={d:sorted(v) for d,v in bydim.items()}
    inds={d:{x:i for i,x in enumerate(v)} for d,v in levels.items()}
    ranks={};maxd=max(levels)
    for d in range(1,maxd+1):
        cols=[]
        for simplex in levels[d]:
            col=defaultdict(int)
            for i in range(len(simplex)):
                sub=simplex[:i]+simplex[i+1:]
                c=canonical(sub)
                coeff=(-1)**i
                if sub != c: coeff*=sign_perm_image(sub,a)
                col[inds[d-1][c]]+=coeff
            cols.append(col)
        ranks[d]=rank_mod_p(cols,prime)
    # degree 0 augmented boundary rank 1 since quotient nonempty
    return {d:len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d in levels}

def main():
    count=0; signed=0
    for m in range(5,11):
        fs=faces(m);count+=len(fs)
        a=reversal_map(m)
        assert all(not f or tuple(sorted(a[i] for i in f)) != f for f in fs)
        for k in range(m):
            r=rotation_map(m,k)
            for flip in (False,True):
                g=[a[x] for x in r] if flip else r
                direct=signed_lf(m,fs,g)
                want=predicted(m,k,flip)
                assert direct==want,(m,k,flip,direct,want)
                signed+=1
        print('TRACE_OK',m,len(fs),2*m)
    print('ALL_TRACES_OK',signed,'faces_total',count)
    for m in range(5,9):
        fs=faces(m)
        j=(m-1)//2 if m%4==1 else (m-2)//2
        want={m-2:1}
        if m%4==0:want[j]=2
        for p in (1009,1013):
            betti=quotient_betti(m,fs,p)
            good={d:v for d,v in betti.items() if v}
            assert good==want,(m,p,good,want)
        print('QUOTIENT_HOMOLOGY_OK',m,want,'primes',1009,1013)
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
