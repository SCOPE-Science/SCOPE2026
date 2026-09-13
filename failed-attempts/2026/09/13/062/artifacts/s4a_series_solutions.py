"""S4a: truncated Puiseux/power-series solution space of L0=1+x*Phi+x^3*Phi^2, k=3.
L(f) = f(x) + x*f(x^3) + x^3*f(x^9). Ansatz f=sum_{n>=0} a_n x^n; truncate L(f)=0 mod x^N."""
import sympy as sp
N=30; k=3
a=sp.symbols('a0:%d'%N)
f=lambda x: sum(a[n]*x**n for n in range(N))
# exponents: n, 3n+1, 9n+3 < N
M=sp.zeros(N, N)
for n in range(N):
    M[n,n]+=1
    if 3*n+1<N: M[3*n+1,n]+=1
    if 9*n+3<N: M[9*n+3,n]+=1
print("rank:",M.rank(),"nullity:",N-M.rank())
ns=M.nullspace()
for v in ns[:3]:
    print([v[i] for i in range(min(12,N))])
