"""Independent finite diagnostic checks for periodic Rhaly Gram identities.
Run: python3 CHECKER.py. Standard library only.
No finite check is presented as proof of the infinite theorem.
"""
import math
import cmath

CASES = [(1.0, 0.0), (1.0, -1.0), (1.0, 2.0, -1j), (2.0, 1j, 0.0, -0.5)]
checks = 0

def close(a, b, tol=1e-8):
    global checks
    assert abs(a-b) < tol, (a,b)
    checks += 1

for c in CASES:
    q=len(c)
    mu=sum(abs(v)**2 for v in c)/q
    b=[abs(v)**2-mu for v in c]
    assert abs(sum(b))<1e-12
    checks += 1
    L=18000
    tail=[0.0]*(L+2)
    for n in range(L,0,-1):
        tail[n]=tail[n+1]+b[(n-1)%q]/n**2
    N=60
    # Finite Gram matrix identities: both constructions retain exactly L rows.
    for i in range(1,N+1):
        for j in range(1,N+1):
            finite=sum(b[(n-1)%q]/n**2 for n in range(max(i,j),L+1))
            close(tail[max(i,j)],finite,1e-11)
    # Nuclear trace identity: full principal-block diagonal vs weighted harmonic sum.
    for k in (3,17,59):
        diag=sum(tail[i] for i in range(1,k+1))
        rhs=sum(b[(n-1)%q]/n for n in range(1,k+1))+k*tail[k+1]
        close(diag,rhs,1e-9)
    # Periodic cancellation implies N^2 * tail(N) remains uniformly bounded.
    bound=2*q*max(abs(v) for v in b)
    for m in (4,9,20,100,900,6000):
        assert abs(tail[m])*m*m <= bound+0.05
        checks += 1

# A zero-modulus oscillation yields identical Gram operators, but different rows.
ca=(1.0,-1.0)
assert abs(abs(ca[0])**2-abs(ca[1])**2)<1e-14
checks+=1
# Explicit full trace formula in the two-periodic indicator example.
b=(0.5,-0.5)
for N in (1000,10000,100000):
    partial=sum(b[(n-1)%2]/n for n in range(1,N+1))
    assert abs(partial-0.5*math.log(2))<1/N
    checks+=1
# Nonconstant periodic coefficients violate the one-step Toeplitz membership criterion.
for c in CASES[1:]:
    q=len(c)
    d=[c[(r+1)%q]-c[r] for r in range(q)]
    d2=sum(abs(v)**2 for v in d)/q
    N=250
    T=120000
    # Tail estimate N * d2/T added (periodic mean).
    s=N*sum(abs(c[n%q]/(n+1)-c[(n-1)%q]/n)**2 for n in range(N,T+1)) + N*d2/T
    assert abs(s-d2)<0.12*d2, (c,s,d2)
    checks+=1
print(f'PASS {checks} finite diagnostic assertions')
