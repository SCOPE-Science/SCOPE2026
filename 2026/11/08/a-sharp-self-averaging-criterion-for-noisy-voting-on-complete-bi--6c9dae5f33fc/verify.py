"""Exact finite-state checks for noisy copying on complete bipartite contact graphs.
Usage: python verify.py. Standard library only.
"""
from fractions import Fraction as F
from itertools import product


def stationary(a,b,mu):
    states=list(product(range(a+1),range(b+1)))
    n=len(states); ix={s:i for i,s in enumerate(states)}
    # Q[row,current destination] contains exact generator jump rates.
    Q=[[F(0) for _ in range(n)] for _ in range(n)]
    for s,(i,j) in enumerate(states):
        jumps=[((i+1,j),(a-i)*(F(j,b)+mu/2)),
               ((i-1,j),i*(F(b-j,b)+mu/2)),
               ((i,j+1),(b-j)*(F(i,a)+mu/2)),
               ((i,j-1),j*(F(a-i,a)+mu/2))]
        for dest,rate in jumps:
            if not rate: continue
            k=ix[dest]; Q[s][k]+=rate; Q[s][s]-=rate
    A=[[Q[j][i] for j in range(n)] for i in range(n)]; rhs=[F(0) for _ in range(n)]
    A[-1]=[F(1) for _ in range(n)];rhs[-1]=F(1)
    # Exact rational pivoted elimination, without external linear algebra packages.
    for c in range(n):
        h=next(r for r in range(c,n) if A[r][c])
        if h!=c: A[c],A[h]=A[h],A[c];rhs[c],rhs[h]=rhs[h],rhs[c]
        f=A[c][c]
        for j in range(c,n): A[c][j]/=f
        rhs[c]/=f
        for r in range(n):
            if r==c or not A[r][c]:continue
            f=A[r][c]
            for j in range(c,n): A[r][j]-=f*A[c][j]
            rhs[r]-=f*rhs[c]
    assert sum(rhs)==1 and all(z>0 for z in rhs)
    return states,rhs


def check(a,b,mu):
    states,weights=stationary(a,b,mu)
    N=a+b; P=a*b;s=F(1,a)+F(1,b); t=2*mu*(2+mu)
    same=s/(s+t);cross=(1+mu)*same
    theoretical=(F(N*N)+2*mu*(3+mu)*P)/(N*(N+2*mu*(2+mu)*P))
    mean=F(0);second=F(0);SA=F(0);SB=F(0);within_a=F(0);within_b=F(0);across=F(0)
    for (i,j),pi in zip(states,weights):
        za=2*i-a;zb=2*j-b;z=F(za+zb,N)
        mean+=pi*z;second+=pi*z*z;SA+=pi*za;SB+=pi*zb
        if a>1: within_a+=pi*F(za*za-a,a*(a-1))
        if b>1: within_b+=pi*F(zb*zb-b,b*(b-1))
        across+=pi*F(za*zb,a*b)
    assert mean==0 and SA==0 and SB==0
    assert second==theoretical and across==cross,(a,b,mu,second,theoretical,across,cross)
    if a>1: assert within_a==same,(a,b,mu,within_a,same)
    if b>1: assert within_b==same,(a,b,mu,within_b,same)
    assert cross>same
    return 2+int(a>1)+int(b>1)

if __name__=='__main__':
    tests=0; checks=0
    for a in range(1,5):
        for b in range(1,5):
            for mu in [F(1,4),F(1,1),F(5,2)]:
                checks+=check(a,b,mu);tests+=1
    # Strict fixed-N monotonicity of the independently derived expression.
    for N in range(3,30):
        for mu in [F(1,4),F(1),F(5,2)]:
            vals=[]
            for a in range(1,(N//2)+1):
                P=a*(N-a)
                vals.append((F(N*N)+2*mu*(3+mu)*P)/(N*(N+2*mu*(2+mu)*P)))
            assert all(x>y for x,y in zip(vals,vals[1:]));checks+=len(vals)-1
    print(f'PASS: {tests} exact stationary laws and {checks} rational assertions.')
