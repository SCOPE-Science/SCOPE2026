"""Exact-arithmetic checks for the Pell--Narayana dyadic image theorem.

No external dependencies. Finite tests corroborate, but do not replace,
the matrix/Mahler and isometry arguments in RESULT.md.
"""

def mm(A,B,mod=None):
    C = [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    if mod is not None:
        C = [[x%mod for x in row] for row in C]
    return C

I = [[int(i==j) for j in range(3)] for i in range(3)]
K = [[0,1,0],[0,0,1],[1,0,2]]
V0 = [0,1,1]

def mpow(A,n,mod=None):
    R=I
    while n:
        if n&1: R=mm(R,A,mod)
        A=mm(A,A,mod)
        n//=2
    return R

def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]

def nu(x):
    return (abs(x)&-abs(x)).bit_length()-1 if x else float('inf')

def vals(n):
    a,b,c=0,1,1
    out=[]
    for _ in range(n):
        out.append(a)
        a,b,c=b,c,2*c+a
    return out

# Certified small integer matrix calculations used in the proof.
assert mpow(K,3)==[[1,0,2],[2,1,4],[4,2,9]]
assert all((mpow(K,6)[i][j]-I[i][j])%4==0 for i in range(3) for j in range(3))
assert all((mpow(K,24)[i][j]-I[i][j])%16==0 for i in range(3) for j in range(3))

claims=[(2,3,1,1,5),(0,6,2,3,5),(9,24,4,9,13),(21,24,4,9,15)]
for n,h,s,d,v2 in claims:
    U=mpow(K,h); D=[[U[i][j]-I[i][j] for j in range(3)] for i in range(3)]
    assert all(x%(2**s)==0 for row in D for x in row)
    v=mv(mpow(K,n),V0)
    c1=mv(D,v)[0]; c2=mv(D,mv(D,v))[0]
    assert nu(c1)==d, (n,h,'c1',nu(c1))
    assert nu(c2)==v2, (n,h,'c2',nu(c2))
    for j in range(3,60):
        assert s*j>=d+(j.bit_length()-1)+1, (n,h,j)
    print('isometry-certificate',n,h,'first coefficient valuation',d,
          'second coefficient valuation',v2,'matrix entry valuation',s)

D6=[[mpow(K,6)[i][j]-I[i][j] for j in range(3)] for i in range(3)]
v=mv(mpow(K,3),V0)
c=[]
for j in range(4):
    c.append(v[0]); v=mv(D6,v)
assert c==[2,256,29184,3330304], c
assert all(z%256==0 for z in c[1:]); print('singular branch Mahler coefficients',c)

checks=0
for k in range(1,14):
    m=2**k
    period=3*2**(k-1)
    a,b,c=0,1,1
    values=set()
    for n in range(period):
        values.add(a)
        if n%3 in (1,2): assert a%2==1
        if n%6==0: assert a%8==0
        if n%6==3: assert a%256==2
        a,b,c=b,c,(2*c+a)%m
        checks+=4
    assert (a,b,c)==(0,1,1), ('period bound',k)
    target={x for x in range(m) if x%2==1 or x%8==0 or x%256==2}
    assert values==target, ('image',k,values^target)
    expected=2 if k==1 else (2**(k-1)+2**max(k-3,0)+2**max(k-8,0))
    assert len(values)==expected
    print('k',k,'modulus',m,'period',period,'image',len(values))
print('PASS:',checks,'finite recurrence/containment checks; all dyadic image sets through k=13.')
