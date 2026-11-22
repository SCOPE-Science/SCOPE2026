"""Reproducible arithmetic checks for the fifth repunit/binomial-transform GCD."""
from math import comb, gcd


def F(z):
    return z**4 + z**3 + z**2 + z + 1


def G(z):
    return z**4 + 6*z**3 + 16*z**2 + 26*z + 31


def bareiss_determinant(matrix):
    a = [row[:] for row in matrix]
    size = len(a)
    sign, previous = 1, 1
    for k in range(size-1):
        if a[k][k] == 0:
            for j in range(k+1,size):
                if a[j][k]:
                    a[k],a[j]=a[j],a[k]
                    sign=-sign
                    break
            else:
                return 0
        pivot=a[k][k]
        for i in range(k+1,size):
            for j in range(k+1,size):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value % previous==0
                a[i][j]=value//previous
        for i in range(k+1,size):
            a[i][k]=0
        previous=pivot
    return sign*a[size-1][size-1]


# Four coefficients of highest powers, then constant; 8x8 Sylvester matrix.
a=[1,1,1,1,1]
b=[1,6,16,26,31]
rows=[[0]*s + a + [0]*(3-s) for s in range(4)]
rows += [[0]*s + b + [0]*(3-s) for s in range(4)]
resultant=bareiss_determinant(rows)
assert resultant == 378125 == 5**5*11**2, resultant
assert [x for x in range(5) if F(x)%5==0 and G(x)%5==0] == [1]
assert [x for x in range(11) if F(x)%11==0 and G(x)%11==0] == [5,9]
assert all(not (F(x)%25==0 and G(x)%25==0) for x in range(25))
assert all(not (F(x)%121==0 and G(x)%121==0) for x in range(121))
for z in range(-500,20001):
    expected=(5 if z%5==1 else 1)*(11 if z%11 in (5,9) else 1)
    assert gcd(F(z),G(z))==expected, z
# Base-density and least-period checks.
values=[gcd(F(z),G(z)) for z in range(55)]
assert {v:values.count(v) for v in (1,5,11,55)}=={1:36,5:9,11:8,55:2}
assert all(values[z]==values[(z+55)%55] for z in range(55))
assert all(any(values[z]!=values[(z+t)%55] for z in range(55)) for t in range(1,55))
# Source definitions by direct binomial transform, not only closed form.
for k in range(1,51):
    base=2**k
    repunit=[(base**j-1)//(base-1) for j in range(6)]
    bt=sum(comb(5,j)*repunit[j] for j in range(6))
    assert repunit[5]==F(base)
    assert bt==G(base)
    expected=(5 if k%4==0 else 1)*(11 if k%10 in (4,6) else 1)
    assert gcd(repunit[5],bt)==expected,k
period=[(5 if k%4==0 else 1)*(11 if k%10 in (4,6) else 1) for k in range(20)]
assert {v:period.count(v) for v in (1,5,11,55)}=={1:13,5:3,11:2,55:2}
assert all(any(period[z]!=period[(z+t)%20] for z in range(20)) for t in range(1,20))
print('PASS resultant=378125=5^5*11^2; mod5 roots {1}, mod11 roots {5,9}; no 25/121 common zeros')
print('PASS exact GCD for bases -500..20000, base period 55 with frequencies 36,9,8,2')
print('PASS independent binomial transform for k=1..50; exponent period 20 with frequencies 13,3,2,2')
