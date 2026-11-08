"""Exact-rational consistency checks for the three-coordinate closed-form E-design rule."""
from fractions import Fraction as F
from itertools import product

def det(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def adj(M):
    return [[M[(j+1)%3][(i+1)%3]*M[(j+2)%3][(i+2)%3]
             - M[(j+1)%3][(i+2)%3]*M[(j+2)%3][(i+1)%3]
            for j in range(3)] for i in range(3)]

def solve(M,s):
    d=det(M); A=adj(M)
    return [sum(A[i][j]*s[j] for j in range(3))/d for i in range(3)]

def psd3(M):
    if any(M[i][i]<0 for i in range(3)):
        return False
    if any(M[i][i]*M[j][j] - M[i][j]**2 <0
           for i,j in [(0,1),(0,2),(1,2)]):
        return False
    return det(M)>=0

def matrix(a,b,c):
    o=F(1)
    return [[o,a,b],[a,o,c],[b,c,o]]

def classify(a,b,c):
    C=matrix(a,b,c)
    assert all(0<t<1 for t in [a,b,c]) and det(C)>0
    U=[a*b/c, a*c/b, b*c/a]
    w=[1-u for u in U]
    if all(v>0 for v in w):
        L2=[U[i]/w[i]**2 for i in range(3)]
        H=2*(L2[0]*L2[1]+L2[1]*L2[2]+L2[2]*L2[0])-sum(t*t for t in L2)
        if H>=0:
            pi0=[1/v for v in w]; z=sum(pi0)
            return 'double', [v/z for v in pi0], F(1)/z,w,C
    for s in [(1,-1,-1),(-1,1,-1),(-1,-1,1)]:
        v=solve(C,s)
        q=[s[i]*v[i] for i in range(3)]
        if any(qi<=0 for qi in q):
            continue
        w=[1/qi for qi in q]
        M=[[C[i][j]-(w[i] if i==j else 0) for j in range(3)] for i in range(3)]
        if psd3(M):
            z=sum(q)
            return 'simple', [qi/z for qi in q], F(1)/z,w,C
    raise ValueError(('No KKT candidate',a,b,c))

def matrix_psd_with_rate(pi,lam,C):
    # C - diag(lam/pi) exactly PSD
    M=[[C[i][j]-(lam/pi[i] if i==j else 0) for j in range(3)] for i in range(3)]
    return psd3(M),det(M)

def run():
    counts={'double':0,'simple':0}
    for ia,ib,ic in product(range(1,11),repeat=3):
        a,b,c=F(ia,20),F(ib,20),F(ic,20)
        C=matrix(a,b,c)
        if det(C)<=0: continue
        typ,pi,lam,w,_=classify(a,b,c)
        counts[typ]+=1
        assert sum(pi)==1 and all(z>0 for z in pi)
        valid,ds=matrix_psd_with_rate(pi,lam,C)
        assert valid and ds==0,(a,b,c,typ,pi,lam,ds)
        # Check equality to the reconstructed w and stationary complementary certificate
        assert all(lam/pi[i]==w[i] for i in range(3))
        M=[[C[i][j]-(w[i] if i==j else 0) for j in range(3)] for i in range(3)]
        if typ=='double':
            U=[a*b/c,a*c/b,b*c/a]
            ell2=[U[i]/w[i]**2 for i in range(3)]
            K=[[ell2[i] if i==j else (ell2[3-i-j]-ell2[i]-ell2[j])/2 for j in range(3)] for i in range(3)]
            # Z = diag(r)^(-1) K diag(r)^(-1), with off-diagonal products r_i*r_j=a_ij.
            Z=[[1/w[i]**2 if i==j else K[i][j]/C[i][j] for j in range(3)] for i in range(3)]
            assert psd3(Z), ('dual failure',a,b,c,Z)
            assert all(sum(Z[i][k]*M[k][j] for k in range(3))==0 for i in range(3) for j in range(3))
        if typ=='simple':
            assert sum(1 for s in [(1,-1,-1),(-1,1,-1),(-1,-1,1)]
                       if all(s[i]*solve(C,s)[i] > 0 for i in range(3))
                       and psd3([[C[i][j]-(1/(s[i]*solve(C,s)[i]) if i==j else 0) for j in range(3)] for i in range(3)])) >=1
        # A rigorous upper bound for arbitrary positive pi follows from KKT convexity
    print('VERIFY_OK',counts,'exact rational triples; sum',sum(counts.values()))
    for name,abc in [('rank_two',(F(1,5),F(21,100),F(19,100))),('rank_one',(F(3,10),F(1,10),F(1,20)))]:
        typ,pi,lam,w,_=classify(*abc)
        print(name,typ,'p=',pi,'lambda=',lam,'w=',w)
        assert typ==('double' if name=='rank_two' else 'simple')

if __name__=='__main__':run()
