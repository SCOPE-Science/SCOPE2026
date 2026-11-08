"""Finite tests for spectral decomposition of three Heisenberg line averages.
This is verification, not a substitute for the all-prime proof.
"""
from itertools import product
import numpy as np

def multiply(a,b,p):
    x,y,w=a; u,v,z=b; h=pow(2,-1,p)
    return ((x+u)%p,(y+v)%p,(w+z+h*(x*v-y*u))%p)

def power(a,t,p):
    return tuple((t*j)%p for j in a)

def regular(p,B):
    G=list(product(range(p),repeat=3)); index={g:i for i,g in enumerate(G)}
    gens=[(1,0,0),(0,1,0),(1,1,B)]
    T=np.zeros((p**3,p**3),float)
    for i,g in enumerate(G):
        for a in gens:
            for t in range(p):
                h=multiply(g,power(a,t,p),p)
                T[i,index[h]]+=1/p
    return T

def irreducible(p,B,tau):
    h=pow(2,-1,p)
    omega=np.exp(2j*np.pi/p)
    gs=[(1,0,0),(0,1,0),(1,1,B)]
    proj=[]
    for x,y,w in gs:
        U=np.zeros((p,p),complex)
        for r in range(p):
            U[r,(r+x)%p]=omega**((tau*(w+h*x*y+y*r))%p)
        P=np.eye(p,dtype=complex)
        # project onto generator's 1-eigenspace by averaging powers
        P=np.zeros((p,p),complex);Ut=np.eye(p,dtype=complex)
        for t in range(p):
            P+=Ut/p
            Ut=Ut@U
        assert np.linalg.norm(P@P-P)<1e-9,(p,B,tau)
        assert abs(np.trace(P)-1)<1e-9
        proj.append(P)
    D=np.trace(proj[0]@proj[1]@proj[2])
    A=(h%p)
    gauss=sum(omega**((tau*(A*t*t+B*t))%p) for t in range(p))/p**2
    assert abs(D-gauss)<1e-9,(p,B,tau,D,gauss)
    eig=np.linalg.eigvalsh(sum(proj))
    predicted=np.sort(np.array([1+2/np.sqrt(p)*np.cos((np.arccos(np.clip((p**1.5)*gauss.real,-1,1))+2*np.pi*j)/3) for j in range(3)]))
    assert np.max(abs(predicted-eig[-3:]))<1e-8,(p,B,tau,predicted,eig)
    return eig,gauss

def run():
    checked=0
    for p in [3,5,7]:
        for B in [0,1]:
            T=regular(p,B)
            eig_reg=np.linalg.eigvalsh(T)
            expected=[3]+[1]*(3*(p-1))+[0]*((p-1)*(p-2))
            for tau in range(1,p):
                spec,gauss=irreducible(p,B,tau)
                expected+=list(spec)*p
                checked+=1
            assert len(expected)==p**3
            err=np.max(abs(np.sort(eig_reg)-np.sort(expected)))
            assert err < 1e-8,(p,B,err)
            rank_reg=int(np.count_nonzero(eig_reg>1e-7))
            want= (19 if B==0 else 25) if p==3 else 3*p*p-2
            assert rank_reg==want,(p,B,rank_reg,want)
            print(f'p={p}, B={B}: rank={rank_reg}, nullity={p**3-rank_reg}, max_spectral_error={err:.2e}')
    print('HEISENBERG_THREE_LINE_SPECTRUM_PASS cases=6 irrep_blocks=',checked)
if __name__=='__main__':run()

def subgroup_census_p3():
    from itertools import combinations
    p=3
    directions=[(1,t) for t in range(p)]+[(0,1)]
    G=list(product(range(p),repeat=3)); ix={g:i for i,g in enumerate(G)}
    # Fraction-free exact rank only for one representative of each possible B,
    # supplemented by exhaustive floating-point rank for the complete census.
    from sympy import Matrix
    for B,expected in ((0,19),(1,25)):
        integral=np.rint(p*regular(p,B)).astype(int)
        assert Matrix(integral.tolist()).rank()==expected
    counts={19:0,25:0}
    for U in combinations(directions,3):
        u1,u2,u3=U
        delta=(u1[0]*u2[1]-u1[1]*u2[0])%p
        inv_delta=pow(delta,-1,p)
        alpha=((u3[0]*u2[1]-u3[1]*u2[0])*inv_delta)%p
        beta=((u1[0]*u3[1]-u1[1]*u3[0])*inv_delta)%p
        assert alpha and beta
        for W in product(range(p),repeat=3):
            B=(W[2]-alpha*W[0]-beta*W[1])%p
            g=[(u[0],u[1],w) for u,w in zip(U,W)]
            T=np.zeros((p**3,p**3),float)
            for i,a in enumerate(G):
                for h in g:
                    for t in range(p):
                        T[i,ix[multiply(a,power(h,t,p),p)]]+=1/p
            eig=np.linalg.eigvalsh(T)
            rank=int(np.count_nonzero(eig>1e-7))
            target=19 if B==0 else 25
            assert rank==target,(U,W,B,rank)
            counts[rank]+=1
    assert counts=={19:36,25:72},counts
    print('HEISENBERG_THREE_LINE_CENSUS_PASS p3_triplets=108 ranks=19:36,25:72 exact_representative_ranks=2')
if __name__=='__main__':subgroup_census_p3()
