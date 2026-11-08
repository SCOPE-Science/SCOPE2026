#!/usr/bin/env python3
"""Independent finite verification of t-clique-free complexes of complete split graphs.
Requires only Python 3 standard library. Test families and signed chain traces.
"""
from itertools import combinations
from math import comb


def rank_mod(mat,p):
    if not mat:return 0
    mat=[[v%p for v in row] for row in mat]
    nr,nc=len(mat),len(mat[0]); r=0
    for col in range(nc):
        piv=next((i for i in range(r,nr) if mat[i][col]),None)
        if piv is None:continue
        mat[r],mat[piv]=mat[piv],mat[r]
        inv=pow(mat[r][col],-1,p)
        mat[r]=[(v*inv)%p for v in mat[r]]
        for i in range(r+1,nr):
            if (q:=mat[i][col]):
                mat[i]=[(a-q*b)%p for a,b in zip(mat[i],mat[r])]
        r+=1
        if r==nr:break
    return r


def complex_faces(m,n,t):
    q=m+n; adj=[[False]*q for _ in range(q)]
    for i in range(q):
        for j in range(i+1,q):
            adj[i][j]=adj[j][i]=(i<m or j<m)
    # No forbidden t-cliques; independently check all t-subsets of each candidate.
    faces=[()]
    for bits in range(1,1<<q):
        s=tuple(i for i in range(q) if bits>>i&1)
        ok=not any(all(adj[i][j] for i,j in combinations(vs,2)) for vs in combinations(s,t))
        if ok:faces.append(s)
    return faces


def homology_mod(faces,p):
    Fs={}
    for f in faces:
        if f:Fs.setdefault(len(f)-1,[]).append(f)
    ranks={}
    for d,v in Fs.items():
        if d==0:continue
        indices={f:i for i,f in enumerate(Fs[d-1])}
        mat=[[0]*len(v) for _ in Fs[d-1]]
        for j,f in enumerate(v):
            for a in range(len(f)):
                mat[indices[f[:a]+f[a+1:]]][j] = (-1)**a
        ranks[d]=rank_mod(mat,p)
    out={}
    for d,v in Fs.items():
        dim=len(v)-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:dim-=1
        if dim:out[d]=dim
    return out


def sign_of_order(nums):
    return (-1)**sum(nums[i]>nums[j] for i in range(len(nums)) for j in range(i+1,len(nums)))


def char_traces(faces,perm,t):
    tr_by_d={}
    for f in faces:
        if not f:continue
        pf=tuple(perm[i] for i in f)
        if set(pf)==set(f):
            d=len(f)-1
            tr_by_d[d]=tr_by_d.get(d,0)+sign_of_order(pf)
    # For reduced chain Lefschetz, subtract trace 1 on degree 0
    return sum(((-1)**d)*v for d,v in tr_by_d.items())-1


def exterior_trace(m,k,perm):
    trace=0
    for subset in combinations(range(m),k):
        img=tuple(perm[i] for i in subset)
        if set(subset)==set(img):trace+=sign_of_order(img)
    return trace


def permutations(m,n):
    perms=[]
    perms.append(tuple(range(m+n)))
    if m>=2:perms.append((1,0,*range(2,m+n)))
    if n>=2:perms.append(tuple(range(m))+(m+1,m)+tuple(range(m+2,m+n)))
    if m>=3:perms.append((1,2,0,*range(3,m+n)))
    if n>=3:perms.append(tuple(range(m))+(m+1,m+2,m)+tuple(range(m+3,m+n)))
    return perms


def run():
    cases=0; tr_tests=0; faces_max=0
    for m in range(2,6):
      for n in range(2,5):
       for t in range(3,min(m+1,6)+1):
        fs=complex_faces(m,n,t);cases+=1; faces_max=max(faces_max,len(fs)-1)
        # The expected classification includes all boundary values.
        predicted={t-2:comb(m,t-1)}
        for p in (2,3):
            actual=homology_mod(fs,p)
            assert actual==predicted,(m,n,t,p,actual,predicted)
        for perm in permutations(m,n):
            tr=char_traces(fs,perm,t)
            expected=(-1)**(t-2)*exterior_trace(m,t-1,perm)
            assert tr==expected,(m,n,t,perm,tr,expected)
            tr_tests+=1
        if m==3 and n==2 and t==3:
            print('EXAMPLE m=3,n=2,t=3: faces=%d, H1 rank=%d'%(len(fs)-1,predicted[1]))
    print('PARAMETER_CASES',cases)
    print('SIGNED_EQUIVARIANT_LEFSCHETZ_CHECKS',tr_tests)
    print('MAX_NONEMPTY_FACES',faces_max)
    print('MODULAR_HOMOLOGY_PRIMES',2,3)
    print('ALL_VERIFY_OK')
if __name__=='__main__':run()
