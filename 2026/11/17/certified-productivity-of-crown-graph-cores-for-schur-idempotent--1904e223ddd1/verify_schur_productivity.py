"""Exact rational replay of a finite Schur-multiplier core productivity witness.

Usage: python verify_schur_productivity.py schur_productive_certificate.json
This script uses only Python's standard library. No numerical eigensolver is needed.
"""
import json
import sys
from fractions import Fraction as F


def get_blocks(n,R,u):
    h=len(u)-1
    out=[]
    for label in ['large','small']+list(range(1,h)):
        if label=='large':
            diag=F(n-1,n)*u[0]**2
            off=[F(u[k]*u[k+1],n*R**k) for k in range(h)]
            multiplicity=1
        elif label=='small':
            diag=F(1,n)*u[0]**2
            off=[F(u[k]*u[k+1],n*R**k) for k in range(h)]
            multiplicity=n-1
        else:
            l=label
            diag=F(0)
            off=[F((R-1)*u[k]*u[k+1],R**(k-l+1)) for k in range(l,h)]
            multiplicity=1
        dimension=len(off)+1
        entries=[[F(0) for _ in range(dimension)] for _ in range(dimension)]
        entries[0][0]=diag
        for k,c in enumerate(off):
            entries[k][k+1]=entries[k+1][k]=c
        out.append((str(label),multiplicity,entries))
    return out


def main(path):
    with open(path,encoding='utf8') as stream:
        data=json.load(stream)
    n,R,u,q=data['n'],data['R'],data['u'],data['reflection_scale']
    assert n==15 and R==1000
    assert u==[1000,691,622,556,493,432,373,317,262,208,155,103,51]
    assert q==10000000
    blocks=get_blocks(n,R,u)
    assert len(blocks)==len(data['matrices'])==13
    # If ||H^2-I||_infty <= 2/100000 for symmetric H,
    # then ||H||_op <= sqrt(1+2/100000) <= 1+1/100000.
    kappa=F(1,100000)
    total=F(0)
    largest_error=F(0)
    for (label,multiplicity, A),record in zip(blocks,data['matrices']):
        assert record['label']==label
        Z=record['integer_reflection']
        d=len(A)
        assert len(Z)==d and all(len(row)==d for row in Z)
        assert all(isinstance(z,int) and not isinstance(z,bool) and -q<=z<=q for row in Z for z in row)
        assert all(Z[i][j]==Z[j][i] for i in range(d) for j in range(d))
        error_rows=[]
        for i in range(d):
            error=sum(abs(sum(Z[i][k]*Z[k][j] for k in range(d)) - (q*q if i==j else 0)) for j in range(d))
            error_rows.append(F(error,q*q))
        error=max(error_rows)
        assert error<=2*kappa,(label,float(error))
        largest_error=max(largest_error,error)
        trace=sum(F(Z[i][j],q)*A[i][j] for i in range(d) for j in range(d))
        assert trace>0
        total+=multiplicity*trace
    norm_sq=sum(v*v for v in u)
    # Trace duality: norm_1(A) >= tr(H A)/(1+kappa).
    # Levene's exact reduction formula then gives
    # ||T_{J_15-I_15}(1000 repeated 12 times)||_Schur >= total/[(1+kappa)*norm_sq].
    excess=total-2*(1+kappa)*norm_sq
    assert excess>0, (float(total/((1+kappa)*norm_sq)),float(excess))
    assert total > F(20029,10000)*(1+kappa)*norm_sq
    certified_lower=total/((1+kappa)*norm_sq)
    print('VERIFIED exact rational certificate')
    print('Core = J_15 - I_15; branching = 1000 at each of 12 levels')
    print('Number of symmetric dual reflection matrices:',len(blocks))
    print('Largest exact infinity-norm defect below 2/100000:',float(largest_error))
    print('Certified lower bound for Schur norm:',float(certified_lower))
    print('Certified excess above 2:',float(excess/((1+kappa)*norm_sq)))
    print('All matrix arithmetic and inequalities checked with exact Fraction integers.')


if __name__=='__main__':
    assert len(sys.argv)==2,'Usage: python verify_schur_productivity.py certificate.json'
    main(sys.argv[1])
