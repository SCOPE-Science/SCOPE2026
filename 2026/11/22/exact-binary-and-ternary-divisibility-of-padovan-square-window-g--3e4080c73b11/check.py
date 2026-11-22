"""Independent finite verification of the stated Padovan-square local window law."""
from math import gcd
from functools import reduce

A = ((0,1,0),(0,0,1),(1,1,0))
I = ((1,0,0),(0,1,0),(0,0,1))
v = (1,1,1)

def matmul(X,Y,mod=None):
    return tuple(tuple((sum(X[i][h]*Y[h][j] for h in range(3))) % mod if mod else sum(X[i][h]*Y[h][j] for h in range(3)) for j in range(3)) for i in range(3))

def matpow(n,mod):
    X=I; B=A
    while n:
        if n&1: X=matmul(X,B,mod)
        B=matmul(B,B,mod); n//=2
    return X

def padovan(N):
    p=[1,1,1]
    for i in range(3,N):p.append(p[-2]+p[-3])
    return p[:N]

def nu_p(x,p):
    if x==0:return None
    z=0
    while x%p==0:x//=p;z+=1
    return z

def predicted(k,p):
    if p==2: return 2+nu_p(k,2) if k%7==0 else 0
    if p==3: return 1+nu_p(k,3) if k%13==0 else 0
    raise ValueError

P=padovan(450)
u=[x*x for x in P]
Q=(1,-1,1,-1,-1,-1,1)  # constant first through x^6
assert sum(Q)==-1
for n in range(400):
    assert sum(Q[j]*u[n+j] for j in range(7))==0

assert matpow(7,2)==I
assert matpow(13,3)==I
M14=matpow(14,16); M13=matpow(13,27)
B2=tuple(tuple(((M14[i][j]-I[i][j])//4)%2 for j in range(3)) for i in range(3))
C3=tuple(tuple(((M13[i][j]-I[i][j])//3)%3 for j in range(3)) for i in range(3))
assert B2==((0,0,1),(1,1,0),(0,1,1)), B2
assert C3==((2,1,0),(0,2,1),(1,1,2)), C3
assert sum(B2[0][j]*v[j] for j in range(3))%2==1
v2=(P[2],P[3],P[4]); assert sum(C3[0][j]*v2[j] for j in range(3))%3==1
assert (u[10]-u[3])%8==4

for k in range(1,361):
    W=[sum(u[n:n+k]) for n in range(6)]
    d=reduce(gcd,W)
    assert nu_p(d,2)==predicted(k,2),('two',k,d)
    assert nu_p(d,3)==predicted(k,3),('three',k,d)

for p,expect in ((2,lambda r:7 if r<=2 else 7*2**(r-2)),(3,lambda r:13*3**(r-1))):
    for r in range(1,(9 if p==2 else 7)):
        modulus=p**r
        per=expect(r)
        w=[1,1,1]
        for i in range(3,per*2+1): w.append((w[-2]+w[-3])%modulus)
        residues=[z*z%modulus for z in w]
        assert all(residues[i]==residues[i+per] for i in range(per+1)),(p,r,'nonperiod')
        # Every smaller period of a periodic word must divide its least period.
        divisors=[d for d in range(1,per) if per%d==0]
        assert all(any(residues[i]!=residues[i+d] for i in range(per)) for d in divisors),(p,r,'shorter')
print('PASS: Q(E) recurrence verified for 400 indices, Q(1)=-1.')
print('PASS: exact lifting matrices and sharp witness residues at 2 and 3.')
print('PASS: independent gcd of six direct square-window sums for k=1..360, both prime valuations (720 tests).')
print('PASS: least square periods modulo 2^r (r=1..8) and 3^r (r=1..6) from full periodic words (14 periods).')
