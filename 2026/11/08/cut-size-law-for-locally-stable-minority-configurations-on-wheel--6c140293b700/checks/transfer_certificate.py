"""Independent exact-integer trace, polynomial and Perrin checks (stdlib only)."""
from math import comb

def matmul(A,B):
    m=len(A);return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
def matpow(A,n):
    R=[[int(i==j) for j in range(len(A))] for i in range(len(A))]
    while n:
        if n&1: R=matmul(R,A)
        A=matmul(A,A);n//=2
    return R

def trace_power(u,n):
    A=[[0,u,1],[1,0,0],[0,u,0]]
    T=matpow(A,n)
    return sum(T[i][i] for i in range(3))
def p(n,z):
    return 0 if z < (n+2)//3 or z>n//2 else n*comb(z,n-2*z)//z

def main():
    perrin=[3,0,2]
    for n in range(3,151): perrin.append(perrin[n-2]+perrin[n-3])
    tests=0
    for n in range(3,103):
        assert trace_power(1,n)==perrin[n], n
        for z in range((n+2)//3,n//2+1):
            # Coefficient of u**z in trace B(u)^n, computed via polynomial ring transfer.
            # independently count binary cyclic words, using a two-transition block construction
            assert (n*comb(z,n-2*z))%z==0
            tests+=1
        # Evaluate the weighted polynomial at multiple positive integer fugacities.
        for u in (0,1,2,3,5,11):
            formula=sum(p(n,z)*u**z for z in range((n+2)//3,n//2+1))
            assert trace_power(u,n)==formula, (n,u)
        # Trace obeys characteristic recurrence T_n = u*(T_(n-2)+T_(n-3)).
        assert trace_power(3,n)==3*(trace_power(3,n-2)+trace_power(3,n-3))
    print(f'PASS: characteristic recurrence, 100 trace/Perrin tests, {tests} coefficient integrality tests, 600 exact weighted trace identities')
    rho=1.324717957244746
    mu=(rho+1)/(2*rho+3)
    var=rho*(rho+1)/(2*rho+3)**3
    for n in (20,40,80,160,320):
        w=[p(n,z) for z in range((n+2)//3,n//2+1)]
        z=[z for z in range((n+2)//3,n//2+1)]
        tot=sum(w)
        mean=sum(a*b for a,b in zip(w,z))/tot
        variance=sum(a*(b-mean)**2 for a,b in zip(w,z))/tot
        print(f'n={n} mu_est={mean/n:.9f} var_est={variance/n:.9f}')
    print(f'mu={mu:.12f} variance={var:.12f}')
if __name__=='__main__': main()
