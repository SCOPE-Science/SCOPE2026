"""Exact binary-symplectic verification of hypercube graph-basis automorphisms.
Only standard library. The analytical proof establishes the result for every d.
"""
from itertools import product

def hypercube(d):
    n=1<<d
    return [[int((i^j).bit_count()==1) for j in range(n)] for i in range(n)]

def gf2_nullspace(rows, ncols):
    a=rows[:]
    pivot=[]; r=0
    for col in range(ncols):
        k=next((k for k in range(r,len(a)) if (a[k]>>col)&1),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        for j in range(len(a)):
            if j!=r and ((a[j]>>col)&1): a[j]^=a[r]
        pivot.append(col);r+=1
    free=[i for i in range(ncols) if i not in pivot]
    basis=[]
    for f in free:
        x=1<<f
        for i,p in reversed(list(enumerate(pivot))):
            if ((a[i]&x).bit_count()%2): x|=1<<p
        basis.append(x)
    return basis

def solve(d):
    A=hypercube(d);n=len(A)
    # 4n variables a,b,c,d: index t*n+i
    eq=[]
    for i in range(n):
        for j in range(n):
            row=0
            if A[i][j]: row^=1<<(0*n+j);row^=1<<(3*n+i)
            if i==j:row^=1<<(2*n+i)
            for k in range(n):
                if A[i][k] and A[k][j]: row^=1<<(1*n+k)
            eq.append(row)
    basis=gf2_nullspace(eq,4*n)
    assert len(basis)==4, (d,len(basis))
    good=[]
    for mask in range(1<<len(basis)):
        x=0
        for i,g in enumerate(basis):
            if mask>>i&1:x^=g
        a,b,c,e=([x>>(t*n+i)&1 for i in range(n)] for t in range(4))
        if not all((a[i]*e[i]^b[i]*c[i])==1 for i in range(n)):continue
        even=[i for i in range(n) if i.bit_count()%2==0]
        odd=[i for i in range(n) if i.bit_count()%2==1]
        ae=a[even[0]];ao=a[odd[0]];be=b[even[0]];bo=b[odd[0]]
        assert all(a[i]==ae and b[i]==be and c[i]==(d%2)*bo and e[i]==ao for i in even)
        assert all(a[i]==ao and b[i]==bo and c[i]==(d%2)*be and e[i]==ae for i in odd)
        assert ae*ao^((d%2)*be*bo)==1
        # independently test symplectic graph-space preservation for all 2^n generators
        for k in range(n):
            v=[A[i][k] for i in range(n)]
            xx=[(a[i]*(i==k))^(b[i]*v[i]) for i in range(n)]
            zz=[(c[i]*(i==k))^(e[i]*v[i]) for i in range(n)]
            assert zz==[sum(A[i][j]*xx[j] for j in range(n))%2 for i in range(n)]
        # resulting graph-basis label linear map L = D + A B
        L=[[int(i==j)*e[i] ^ (A[i][j]*b[j]) for j in range(n)] for i in range(n)]
        # invertible via GF2 rank
        r= n-len(gf2_nullspace([sum(L[i][j]<<j for j in range(n)) for i in range(n)],n))
        assert r==n
        good.append((ae,ao,be,bo))
    target=4 if d%2==0 else 6
    assert len(good)==target,(d,len(good),good)
    print('d',d,'vertices',n,'linear_kernel_dimension',len(basis),'symmetry_cosets',len(good),'parameters',good)

for dim in range(1,6):solve(dim)
print('VERIFY_OK: exact GF2 linear solution spaces and all Clifford determinant and graph-space conditions for d=1..5')
