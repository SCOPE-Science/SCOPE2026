from itertools import product, permutations

def factors(m,n):
    return [(''.join('1' if ((i+j)%m==m-1) else '0' for j in range(n))) for i in range(m)]

def orbit_count(facs,gens):
    left=set(facs); out=0
    while left:
        seed=left.pop(); out+=1; todo=[seed]; vis={seed}
        while todo:
            s=todo.pop()
            for g in gens:
                t=['']*len(s)
                for j,v in enumerate(s): t[g[j]]=v
                t=''.join(t)
                if t not in vis:
                    vis.add(t); todo.append(t); left.discard(t)
    return out

def group_for(m,n,k):
    if n<m:
        # zero-word + n one-hot words, require k-1 position orbits
        s=n-k+2
        blocks=[list(range(s))]
    else:
        r=n%m
        blocks=[]
        if r==0: blocks=[list(range(m-k+1))]
        else:
            a=next(a for a in range(1,r+1) if 1<=k-a<=m-r)
            b=k-a
            blocks=[list(range(r-a+1)),list(range(r,r+(m-r)-b+1))]
    gens=[]
    for B in blocks:
        for x,y in zip(B,B[1:]):
            g=list(range(n))
            if n<m: g[x],g[y]=g[y],g[x]
            else:
                for base in range(0,n,m):
                    if base+x<n and base+y<n:
                        g[base+x],g[base+y]=g[base+y],g[base+x]
            gens.append(g)
    return gens

checks=0
for m in range(2,13):
 for n in range(1,3*m+3):
    fs=factors(m,n)
    ab=len({f.count('1') for f in fs})
    p=len(set(fs))
    assert p==min(m,n+1)
    for k in range(ab,p+1):
        gens=group_for(m,n,k)
        x=orbit_count(fs,gens)
        assert x==k,(m,n,k,ab,x)
        checks+=1
print('sparse periodic groups: all',checks,'parameter/target checks passed')

subgroups=[[(0,1,2)],[(0,1,2),(1,0,2)],[(0,1,2),(0,2,1)],[(0,1,2),(2,1,0)],[(0,1,2),(1,2,0),(2,0,1)],list(permutations(range(3)))]
for a,b in product(range(2,9),repeat=2):
    u=('0'*a+'1'*b)
    fs=[''.join(u[(i+j)%len(u)] for j in range(3)) for i in range(len(u))]
    vals={orbit_count(fs, G) for G in subgroups}
    assert vals=={len(set(fs))-2,len(set(fs))},(a,b,vals)
print('two positive long runs: all 49 short-factor group spectra verified')
