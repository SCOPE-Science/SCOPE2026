#!/usr/bin/env python3
"""Independent finite checks for 2-local maps of split square-zero algebras.
No external packages are required. Usage: python3 verify.py
"""
from itertools import product, permutations
from math import factorial, prod

def add(x, y, q):
    return tuple((a+b)%q for a,b in zip(x,y))

def mul(t, x, q):
    return tuple(t*a%q for a in x)

def mat_apply(m, v, q):
    n=len(v)
    return tuple(sum(m[i*n+j]*v[j] for j in range(n))%q for i in range(n))

def rank(rows, q):
    a=[list(r) for r in rows]; i=0
    for j in range(len(a[0])):
        piv=next((r for r in range(i,len(a)) if a[r][j]%q),None)
        if piv is None: continue
        a[i],a[piv]=a[piv],a[i]
        inv=pow(a[i][j],-1,q)
        a[i]=[(t*inv)%q for t in a[i]]
        for k in range(len(a)):
            if k!=i:
                z=a[k][j]%q
                a[k]=[(a[k][t]-z*a[i][t])%q for t in range(len(a[0]))]
        i+=1
        if i==len(a):break
    return i

def test(q,n):
    allvec=list(product(range(q),repeat=n))
    z=(0,)*n
    nonzero=[v for v in allvec if v!=z]
    proj=[]; line={}; scale={}
    for v in nonzero:
        first=next(a for a in v if a!=0)
        w=mul(pow(first,-1,q),v,q)
        if w not in line:
            line[w]=len(proj); proj.append(w)
        line[v]=line[w];scale[v]=first
    N=len(proj)
    assert N==(q**n-1)//(q-1)
    gl=[]
    for m in product(range(q),repeat=n*n):
        if rank([m[i*n:i*n+n] for i in range(n)],q)==n:
            gl.append(tuple(mat_apply(m,v,q) for v in allvec))
    assert len(gl)==prod(q**n-q**j for j in range(n))
    vindex={v:i for i,v in enumerate(allvec)}
    compat={}
    for i in range(len(allvec)):
        for j in range(i,len(allvec)):
            compat[i,j]={(g[i],g[j]) for g in gl}
    glset=set(gl)
    count=0; local3=0; nonlinear=0
    for perm in permutations(range(N)):
        for factors in product(range(1,q),repeat=N):
            img=[z]*len(allvec)
            for v in nonzero:
                ip=line[v]
                img[vindex[v]]=mul((scale[v]*factors[ip])%q,proj[perm[ip]],q)
            img=tuple(img)
            for i in range(len(allvec)):
                for j in range(i,len(allvec)):
                    assert (img[i],img[j]) in compat[i,j], (q,n,i,j)
            count+=1
            is_three_local=all(img[vindex[add(a,b,q)]]==add(img[vindex[a]],img[vindex[b]],q)
                                for a in allvec for b in allvec)
            assert is_three_local==(img in glset), (q,n)
            local3+=int(is_three_local)
            nonlinear+=int(not is_three_local)
    assert count==factorial(N)*(q-1)**N
    assert local3==len(gl)
    print(f'q={q}, n={n}, projective points={N}, 2-local={count}, 3-local={local3}, nonlinear 2-local={nonlinear}, all tested from pair definition')

for q,n in ((2,1),(2,2),(3,2),(2,3)):
    test(q,n)
print('VERIFY_OK')
