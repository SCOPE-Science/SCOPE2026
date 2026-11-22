#!/usr/bin/env python3
"""Exact finite checks of a prime-degree Fermat line-graph rank theorem.

Standard library only. The general-prime proof is mathematical; these checks
corroborate its incidence, factorization, and exceptional finite cases.
"""

def rank_mod(rows, p):
    a = [list(row) for row in rows]
    if not a: return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        i = next((k for k in range(r,m) if a[k][c] % p), None)
        if i is None: continue
        a[r], a[i] = a[i], a[r]
        inv = pow(a[r][c] % p,-1,p)
        a[r][c:] = [(z*inv)%p for z in a[r][c:]]
        for k in range(r+1,m):
            v = a[k][c] % p
            if v:
                a[k][c:] = [(x-v*y)%p for x,y in zip(a[k][c:],a[r][c:])]
        r += 1
        if r == m: break
    return r

def graph(p):
    labels = [(f,a,b) for f in range(3) for a in range(p) for b in range(p)]
    n = len(labels)
    adj = [[0]*n for _ in range(n)]
    for i, (f,a,b) in enumerate(labels):
        for j in range(i+1,n):
            g,c,e = labels[j]
            if f == g: hit = a == c or b == e
            elif (f,g) == (0,1): hit = (a+e-b-c)%p == 0
            elif (f,g) == (0,2): hit = (c-a-b-e-1)%p == 0
            else: hit = (c+e-a-b)%p == 0
            adj[i][j] = adj[j][i] = int(hit)
    lap = [[(4*p-2 if i==j else -adj[i][j])%p for j in range(n)] for i in range(n)]
    assert all(sum(row)==4*p-2 for row in adj)
    return labels,adj,lap

def structure(p,labels):
    u=12*p
    def ix(f,d,t): return (4*f+d)*p+(t%p)
    # H is the involutory permutation pairing six axis fibers and
    # the corresponding three pairs of cross-family diagonal fibers.
    perm=list(range(u))
    for f,da,g,db,shift in ((0,2,1,2,0),(0,3,2,2,1),(1,3,2,3,0)):
        for t in range(p):
            x,y=ix(f,da,t),ix(g,db,t+shift)
            perm[x]=y;perm[y]=x
    assert all(perm[perm[i]]==i for i in range(u))
    cols=[]
    for f,a,b in labels:
        cols.append((ix(f,0,a),ix(f,1,b),ix(f,2,a-b),ix(f,3,a+b)))
    # E is the evaluation map for the four directions of each family.
    e=[[int(j in sel) for j in range(u)] for sel in cols]
    # Explicit 18 kernel identities, six for each coordinate family.
    k=[[0]*18 for _ in range(u)]
    for f in range(3):
        for t in range(p):
            identities=((1,-1,0,0),(1,0,-1,0),(1,0,0,-1),
                        (-t,t,t,0),(-t,-t,0,t),(-2*t*t,-2*t*t,t*t,t*t))
            for j,coeff in enumerate(identities):
                for di,x in enumerate(coeff):
                    k[ix(f,di,t)][6*f+j]=x%p
    return cols,e,perm,k

def projective_check(p,labels,adj):
    q={3:13,5:31,7:29,11:23,13:53}.get(p)
    if q is None:return
    lam=next(x for x in range(2,q) if pow(x,p,q)==q-1 and x!=q-1)
    zeta=pow(lam,2,q)
    def vec(f,a,b):
        x,y=lam*pow(zeta,a,q)%q,lam*pow(zeta,b,q)%q
        if f==0: return ((x,1,0,0),(0,0,y,1))
        if f==1: return ((x,0,1,0),(0,y,0,1))
        return ((x,0,0,1),(0,y,1,0))
    bases=[vec(*v) for v in labels]
    def det_zero(rows):
        m=[list(row) for row in rows];rank=0
        for j in range(4):
            i=next((i for i in range(rank,4) if m[i][j]%q),None)
            if i is None: continue
            m[rank],m[i]=m[i],m[rank]
            inv=pow(m[rank][j],-1,q)
            for h in range(j,4):m[rank][h]=m[rank][h]*inv%q
            for i in range(rank+1,4):
                c=m[i][j]
                if c:
                    for h in range(j,4):m[i][h]=(m[i][h]-c*m[rank][h])%q
            rank+=1
        return rank<4
    for i in range(len(labels)):
        for j in range(i+1,len(labels)):
            assert int(det_zero(bases[i]+bases[j]))==adj[i][j],(p,i,j)
    print('projective_determinants_confirmed',p,'q',q,'pairs',len(labels)*(len(labels)-1)//2)

def run(p):
    labels,adj,lap=graph(p)
    cols,e,perm,k=structure(p,labels)
    # Directly checks the factorization L=-EHE^t modulo p.
    for i,sel in enumerate(cols):
        mapped=tuple(perm[x] for x in sel)
        for j,other in enumerate(cols):
            s=sum(x in other for x in mapped)
            assert (lap[i][j]+s)%p==0,(p,i,j)
    assert all(sum(k[x][j] for x in col)%p==0
               for col in cols for j in range(18))
    ranke=rank_mod(e,p)
    rankk=rank_mod(list(zip(*k)),p)
    assert ranke==12*p-18 and rankk==18
    gram=[[sum(k[t][i]*k[perm[t]][j] for t in range(12*p))%p
           for j in range(18)] for i in range(18)]
    rg=rank_mod(gram,p)
    expected={3:7,5:2}.get(p,0)
    assert rg==expected
    r=rank_mod(lap,p)
    assert r==12*p-36+rg
    pr=3*p*p-1-r
    assert pr=={3:19,5:48}.get(p,3*p*p-12*p+35)
    print('prime',p,'n',3*p*p,'eval_rank',ranke,'kernel_dim',18,
          'kernel_pairing_rank',rg,'laplacian_rank',r,'critical_p_rank',pr)
    if p<=13:projective_check(p,labels,adj)

if __name__=='__main__':
    for p in (3,5,7,11,13):run(p)
    print('FERMAT_WILD_CRITICAL_RANK_OK')
