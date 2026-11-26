"""Independent exact coefficient computation from Catalan first-return renewal."""
from math import comb
N=70
# primitive Dyck excursion series D(z) = sum_{m>=1} Cat(m-1)*z^(2m)
d=[0]*(N+1)
for m in range(1,N//2+1):
    d[2*m]=comb(2*m-2,m-1)//m
# U(z)=(1-D(z))/(1-2z)
u=[0]*(N+1);u[0]=1
for n in range(1,N+1):u[n]=2*u[n-1]-d[n]
H=[[0]*(N+1) for _ in range(N//2+1)]
H[0]=u[:]
for k in range(1,N//2+1):
    for n in range(N+1):
        H[k][n]=sum(d[j]*H[k-1][n-j] for j in range(2,n+1,2))
for n in range(N+1):
    assert sum(H[k][n] for k in range(N//2+1))==2**n
    assert H[0][n]==(1 if n==0 else 2**(n-1)+comb(n-1,(n-1)//2))
    assert max(k for k in range(N//2+1) if H[k][n])==n//2
    if n>=2:assert H[n//2][n]==(1 if n%2==0 else 2)
    if n%2==1 and n>=3:
        assert all(H[k][n]==2*H[k][n-1] for k in range(N//2+1))
print('PASS max_length=',N,'total_coefficients=',sum((n//2)+1 for n in range(N+1)))
for n in (8,12,20,30,50,70):
    print(f'n={n}',[H[k][n] for k in range(min(7,n//2+1))],
          'p0=',f'{H[0][n]}/{2**n}',
          'p1=',f'{H[1][n]}/{2**n}')
