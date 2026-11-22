"""Independent finite-domain and asymptotic checks for active-lattice first-contact polarity."""
import math
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

def formula(D, epsilon, gamma, N):
    assert D > 0 and 0 <= epsilon <= D and gamma > 0 and N >= 1
    beta, eta = epsilon / D, gamma / D
    rho = (1-beta*beta)/(1+beta*beta+eta+math.sqrt((eta+2)*(eta+2*beta*beta)))
    k = .5*(1+beta*math.sqrt((eta+2)/(eta+2*beta*beta)))
    return k+(.5-k)*rho**N, rho, k

def independent_finite_domain(D,epsilon,gamma,N,M):
    # Reflect at -M, absorb at N. Solve two-spin backward generator directly.
    size=2*(N+M)
    mat=lil_matrix((size,size),dtype=float)
    rhs=np.zeros(size)
    for x in range(-M,N):
        for spin_index,spin in enumerate((1,-1)):
            i=2*(x+M)+spin_index
            off=0.
            for dest,rate in ((x+1,D+spin*epsilon),(x-1,D-spin*epsilon)):
                if dest < -M:
                    continue
                off+=rate
                if dest==N:
                    if spin==1: rhs[i]-=rate
                else:
                    mat[i,2*(dest+M)+spin_index]+=rate
            mat[i,2*(x+M)+1-spin_index]+=gamma
            off+=gamma
            mat[i,i]-=off
    u=spsolve(mat.tocsr(),rhs)
    return .5*(u[2*M]+u[2*M+1]),u

def main():
    checks=0
    for D,beta,eta in ((1.,.13,.2),(1.,.6,.8),(1.,.9,2.4),
                       (2.,.75,1.3),(.7,.45,5.),(1.,0.,1.3),(1.,1.,2.)):
        for N in (1,2,3,6,11):
            for M in (50,100,160):
                result,_,_=formula(D,D*beta,D*eta,N)
                independent,_=independent_finite_domain(D,D*beta,D*eta,N,M)
                assert abs(result-independent)<2e-11,(D,beta,eta,N,M,result,independent)
                checks+=1
        _,rho,k=formula(D,D*beta,D*eta,4)
        assert 0<=rho<1 and .5<=k<=1
        checks+=1
    for beta in (.05,.25,.5,.75,.95):
        for N in (1,2,5,20):
            ps=[formula(1,beta,eta,N)[0] for eta in (1.,10.,1e3,1e7)]
            assert abs(ps[-1]-(1+beta)/2)<1e-6
            checks+=1
            p_small=formula(1,beta,1e-8,N)[0]
            target=1-.5*((1-beta)/(1+beta))**N
            assert abs(p_small-target)<1e-5
            checks+=1
            if 0<beta<1 and N<=5:
                pprev=formula(1,beta,1,N)[0]
                pnext=formula(1,beta,1,N+1)[0]
                assert pnext>pprev
                checks+=1
        c=1/(1+3.)
        assert abs((beta*beta*c*c) -(beta*beta*c)**2 - beta*beta*(1-beta*beta)*c*c)<1e-14
        assert beta*beta*(1-beta*beta)*c*c>0
        checks+=1
    print(f'{checks} assertions passed: finite-domain generator, endpoints, distance ordering and both tumbling limits')

if __name__=='__main__':
    main()
