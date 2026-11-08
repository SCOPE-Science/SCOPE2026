from fractions import Fraction
from math import gcd

def determinant(a):
    a=[list(map(Fraction,row)) for row in a]
    n=len(a); det=Fraction(1)
    for k in range(n):
        t=next((i for i in range(k,n) if a[i][k]),None)
        if t is None:return Fraction(0)
        if t!=k:a[k],a[t]=a[t],a[k];det=-det
        z=a[k][k];det*=z
        for i in range(k+1,n):
            if a[i][k]:
                rat=a[i][k]/z
                for j in range(k+1,n):a[i][j]-=rat*a[k][j]
                a[i][k]=Fraction(0)
    return det

def rank(a):
    a=[list(map(Fraction,row)) for row in a]
    nr=len(a);nc=len(a[0]); k=0
    for j in range(nc):
        t=next((i for i in range(k,nr) if a[i][j]),None)
        if t is None:continue
        a[k],a[t]=a[t],a[k]
        z=a[k][j]
        for i in range(k+1,nr):
            if a[i][j]:
                rat=a[i][j]/z
                for l in range(j+1,nc):a[i][l]-=rat*a[k][l]
                a[i][j]=Fraction(0)
        k+=1
        if k==nr:break
    return k

def mat(m,h,tmax):
    N=2*m
    U=[[Fraction(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        U[i][(i-1)%N]+=Fraction(1,2)
        U[i][(i+1)%N]+=Fraction(1,2)
    out=[]
    for x in [0,h]:
        row=[Fraction(int(i==x)) for i in range(N)]
        for t in range(tmax):
            out.append(row)
            row=[sum(row[j]*U[j][k] for j in range(N)) for k in range(N)]
    return out

if __name__=='__main__':
    cases=0
    for m in range(2,10):
        N=2*m
        for h in range(1,N):
            a=mat(m,h,m)
            d=determinant(a)
            expected=Fraction(1,2**(m*(m-1))) if gcd(h,N)==1 else Fraction(0)
            assert abs(d)==expected,(m,h,d,expected)
            if gcd(h,m)==1 and h%2==0:
                assert rank(mat(m,h,m+1))==N
                assert rank(a)==N-1
            if gcd(h,m)>1:
                assert rank(mat(m,h,m+1))<N
            cases+=1
        print('PASS',m)
    print('CHECK_OK exact_determinants',cases)

# Additional exact rank checks for every sensor separation and both horizons.
def check_all_ranks():
    count = 0
    for half_order in range(2, 12):
        for offset in range(1, 2 * half_order):
            depth = gcd(offset, half_order)
            critical = rank(mat(half_order, offset, half_order))
            saturated = rank(mat(half_order, offset, half_order + 1))
            want_critical = 2 * half_order - depth + 1 - int((offset // depth) % 2 == 0)
            want_saturated = 2 * half_order - depth + 1
            assert critical == want_critical, (half_order, offset, critical, want_critical)
            assert saturated == want_saturated, (half_order, offset, saturated, want_saturated)
            count += 1
    print('CHECK_OK exact_ranks=', count)

if __name__ == '__main__':
    check_all_ranks()
