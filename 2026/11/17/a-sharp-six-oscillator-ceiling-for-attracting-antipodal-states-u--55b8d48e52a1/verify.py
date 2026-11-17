"""Exact finite-dimensional stability and phase-reduction checks for a mixed-coupling phase network."""
from fractions import Fraction as Q
from math import comb

def matrix(n, small, a=Q(3), b=Q(5)):
    # A is effective pairwise coupling, B is higher-order coupling.
    s=[1]*(n-small)+[-1]*small
    M=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for v in range(n):
            for j in range(n):
                M[i][v]+=a*Q(s[i]*s[j],n)*((v==j)-(v==i))
                for ell in range(n):
                    M[i][v]+=b*Q(s[i]*s[ell],n*n)*(2*(v==j)-(v==ell)-(v==i))
    return M

def mul(J,v): return [sum(J[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]

def test():
    checks=0
    for n in range(3,17):
        for m in range(1,n):
            for A,B in [(Q(3),Q(5)),(Q(7,2),Q(17,3))]:
                J=matrix(n,m,A,B)
                p=n-m;S=p-m
                eig1=-Q(S,n)*(A+B)
                eig2= Q(S,n)*(A+B)
                eigrel=A+B*(1-Q(8*p*m,n*n))
                assert mul(J,[Q(1)]*n)==[0]*n
                for k in range(p-1):
                    v=[Q(0)]*n;v[k]=1;v[k+1]=-1
                    assert mul(J,v)==[eig1*x for x in v], (n,m,'majority',k)
                for k in range(p,n-1):
                    v=[Q(0)]*n;v[k]=1;v[k+1]=-1
                    assert mul(J,v)==[eig2*x for x in v], (n,m,'minority',k)
                ab=sum(J[0][p:]);ba=sum(J[p][:p])
                assert -ab-ba==eigrel, (n,m,'relative')
                checks+=1
    print('VERIFY_OK exact_antipodal_jacobian_cases=',checks)
    for n in range(3,9):
        den=8*(n-1)-n*n
        if den>0:
            th=Q(n*n*n,(n-1)*den)
            print('N_THRESHOLD',n,str(th))
        else: print('N_NO_SOLITARY_STABILITY',n)
    print('FINITE_CHECK_ONLY: algebraic proof in RESULT.md establishes all sizes and boundaries.')
if __name__=='__main__':test()
