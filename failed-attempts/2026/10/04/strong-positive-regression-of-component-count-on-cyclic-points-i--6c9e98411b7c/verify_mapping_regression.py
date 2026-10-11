#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import Counter, defaultdict
import math

def mapping_stats(f):
    n=len(f)
    state=[0]*n
    cyclic=[False]*n
    for s in range(n):
        if state[s]:
            continue
        pos={}
        path=[]
        x=s
        while state[x]==0 and x not in pos:
            pos[x]=len(path); path.append(x); x=f[x]
        if x in pos:
            for y in path[pos[x]:]: cyclic[y]=True
        for y in path: state[y]=1
    # weak components by undirected exploration
    adj=[set() for _ in range(n)]
    for i,j in enumerate(f):
        adj[i].add(j); adj[j].add(i)
    seen=[False]*n; comp=0
    for i in range(n):
        if not seen[i]:
            comp+=1; stack=[i]; seen[i]=True
            while stack:
                x=stack.pop()
                for y in adj[x]:
                    if not seen[y]: seen[y]=True; stack.append(y)
    return sum(cyclic), comp

def falling(n,m):
    z=1
    for j in range(m): z*=n-j
    return z

def stirling_cycle_row(n):
    row=[0]*(n+1); row[0]=1
    for m in range(1,n+1):
        new=[0]*(n+1)
        for k in range(1,m+1):
            new[k]=row[k-1]+(m-1)*row[k]
        row=new
    return row

def exact_formula_stats(n):
    q=[Fraction(0)]*(n+2)
    for m in range(1,n+1): q[m]=Fraction(falling(n,m),n**m)
    p=[Fraction(0)]*(n+1)
    for m in range(1,n+1): p[m]=q[m]-q[m+1]
    H=[Fraction(0)]*(n+1); H2=[Fraction(0)]*(n+1)
    for m in range(1,n+1):
        H[m]=H[m-1]+Fraction(1,m)
        H2[m]=H2[m-1]+Fraction(1,m*m)
    EL=sum(q[1:n+1],Fraction(0))
    EC=sum(q[m]/m for m in range(1,n+1))
    ELC=sum(q[m]*(1+H[m-1]) for m in range(1,n+1))
    cov=ELC-EL*EC
    varC_cond=sum(p[m]*(H[m]-H2[m]) for m in range(1,n+1))
    EHsq=sum(p[m]*H[m]*H[m] for m in range(1,n+1))
    varC=varC_cond+EHsq-EC*EC
    EL2=sum((2*m-1)*q[m] for m in range(1,n+1))
    varL=EL2-EL*EL
    return q,p,H,H2,EL,EC,cov,varL,varC

def run():
    mappings_checked=0
    joint_cells_checked=0
    tail_checks=0
    conditional_cycle_checks=0
    covariance_checks=0
    stochastic_checks=0
    variance_checks=0
    asymptotic_sanity_checks=0

    for n in range(2,8):
        joint=Counter()
        for f in product(range(n), repeat=n):
            joint[mapping_stats(f)]+=1
            mappings_checked+=1
        total=n**n
        q,p,H,H2,EL,EC,cov,varL,varC=exact_formula_stats(n)

        # Marginal cyclic-point law and conditional component law.
        rows={m:stirling_cycle_row(m) for m in range(1,n+1)}
        for m in range(1,n+1):
            obs=sum(c for (l,k),c in joint.items() if l==m)
            assert Fraction(obs,total)==p[m]
            tail_checks+=1
            for k in range(1,m+1):
                expected=p[m]*Fraction(rows[m][k], math.factorial(m))
                got=Fraction(joint[(m,k)],total)
                assert got==expected
                joint_cells_checked+=1
                conditional_cycle_checks+=1

        EL_obs=sum(Fraction(l*c,total) for (l,k),c in joint.items())
        EC_obs=sum(Fraction(k*c,total) for (l,k),c in joint.items())
        ELC_obs=sum(Fraction(l*k*c,total) for (l,k),c in joint.items())
        assert EL_obs==EL and EC_obs==EC and ELC_obs-EL_obs*EC_obs==cov and cov>0
        covariance_checks+=4

        # Conditional laws strictly increase in first-order stochastic order.
        for m in range(1,n):
            r1=rows[m]; r2=rows[m+1]
            for t in range(1,m+2):
                a=sum(Fraction(r1[k],math.factorial(m)) for k in range(t,m+1))
                b=sum(Fraction(r2[k],math.factorial(m+1)) for k in range(t,m+2))
                assert b>=a
                stochastic_checks+=1
            assert any(sum(Fraction(r2[k],math.factorial(m+1)) for k in range(t,m+2)) > sum(Fraction(r1[k],math.factorial(m)) for k in range(t,m+1)) for t in range(1,m+2))

        assert varL>0 and varC>0
        variance_checks+=2

    # Large-n numerical checks for asymptotic constants.
    target_cov=math.sqrt(math.pi/2)*(1-math.log(2))
    target_corr=(1-math.log(2))*math.sqrt(2*math.pi/(4-math.pi))
    for n in [1000,5000,20000,100000]:
        qs=[]; cur=1.0
        H=[]; H2=[]; h=0.0; h2=0.0
        for m in range(1,n+1):
            cur*= (n-m+1)/n
            qs.append(cur)
            h+=1/m; h2+=1/(m*m); H.append(h); H2.append(h2)
        ps=[qs[m]-(qs[m+1] if m+1<n else 0.0) for m in range(n)]
        EL=sum(qs); EC=sum(qs[m]/(m+1) for m in range(n))
        ELC=EL+sum(qs[m]*H[m-1] for m in range(1,n))
        cov=ELC-EL*EC
        EL2=sum((2*(m+1)-1)*qs[m] for m in range(n)); varL=EL2-EL*EL
        evcond=sum(ps[m]*(H[m]-H2[m]) for m in range(n))
        ehsq=sum(ps[m]*H[m]*H[m] for m in range(n)); varC=evcond+ehsq-EC*EC
        corr=cov/math.sqrt(varL*varC)
        assert abs(cov/math.sqrt(n)-target_cov) < 0.08
        assert abs(corr*math.sqrt(math.log(n))-target_corr) < 0.08
        asymptotic_sanity_checks+=2

    print('VERIFY_OK '
          f'mappings_checked={mappings_checked} '
          f'joint_cells_checked={joint_cells_checked} '
          f'tail_checks={tail_checks} '
          f'conditional_cycle_checks={conditional_cycle_checks} '
          f'covariance_checks={covariance_checks} '
          f'stochastic_checks={stochastic_checks} '
          f'variance_checks={variance_checks} '
          f'asymptotic_sanity_checks={asymptotic_sanity_checks}')

if __name__=='__main__': run()
