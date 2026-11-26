from itertools import product

def inv(a,p):
    return pow(a,-1,p)

def rank_mod(rows,p):
    a=[[(x%p) for x in row] for row in rows]
    m=len(a); n=len(a[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        z=inv(a[r][c],p)
        a[r]=[(z*x)%p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                t=a[i][c]
                a[i]=[(a[i][j]-t*a[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def dist_formula(q):
    return {6:1,5:q-1,4:q*(3*q*q-4*q-2),3:q**5-2*q**4-2*q**3+4*q*q+q}

def enumerate_dist(q):
    cnt={3:0,4:0,5:0,6:0}
    for a,b,c in product(range(1,q),repeat=3):
      for x,y,z in product(range(q),repeat=3):
        rows=[[-x,x,0,a-b,0,0],[0,-z,z,0,b-c,0],[-y,0,y,-z,x,a-c]]
        d=6-rank_mod(rows,q)
        cnt[d]+=1
    # central scalar matrices induce the same automorphism; divide by q-1.
    return {d:v//(q-1) for d,v in cnt.items()}

def matmul(A,B,q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%q for j in range(3)) for i in range(3))

def upper(t):
    a,x,y,b,z,c=t
    return ((a,x,y),(0,b,z),(0,0,c))

def tup(A): return (A[0][0],A[0][1],A[0][2],A[1][1],A[1][2],A[2][2])

def inv_upper(U,q):
    a,x,y=U[0]; b,z=U[1][1],U[1][2]; c=U[2][2]
    ai,bi,ci=inv(a,q),inv(b,q),inv(c,q)
    return ((ai,(-ai*x*bi)%q,(ai*(x*bi*z-y)*ci)%q),(0,bi,(-bi*z*ci)%q),(0,0,ci))

def orbit_count(q):
    T=[upper(t) for t in product(range(q),repeat=6)]
    B=[upper((a,x,y,b,z,c)) for a in range(1,q) for b in range(1,q) for c in range(1,q) for x,y,z in product(range(q),repeat=3)]
    seen=set(); orbits=0
    for X in T:
        tx=tup(X)
        if tx in seen: continue
        orbits+=1
        for U in B:
            Y=matmul(matmul(U,X,q),inv_upper(U,q),q)
            seen.add(tup(Y))
    return orbits

for q in (2,3,5,7,11):
    got=enumerate_dist(q); want=dist_formula(q)
    assert got==want,(q,got,want)
    assert sum(got.values())==q**3*(q-1)**2
for q in (2,3):
    got=orbit_count(q); want=q**3+3*q**2+q
    assert got==want,(q,got,want)
print('VERIFY_OK distributions=q2,q3,q5,q7,q11 direct_orbits=q2,q3')
