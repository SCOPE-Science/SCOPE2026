"""Finite-field replay for rank/Jordan strata of Taft-compatible skew derivations.
Pure Python; python taft_action_checker.py; no external dependencies.
"""
from itertools import product
from collections import Counter

def primitive_root(p,m):
    for z in range(2,p):
        if pow(z,m,p)==1 and all(pow(z,d,p)!=1 for d in range(1,m)):
            return z
    raise ValueError((p,m))

def mm(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def rank(A,p):
    B=[r[:] for r in A]; nr=len(B); nc=len(B[0]); row=0
    for j in range(nc):
        pivot=next((i for i in range(row,nr) if B[i][j]%p),None)
        if pivot is None: continue
        B[row],B[pivot]=B[pivot],B[row]
        c=pow(B[row][j],-1,p)
        B[row]=[(c*x)%p for x in B[row]]
        for i in range(row+1,nr):
            if B[i][j]:
                a=B[i][j]; B[i]=[(u-a*v)%p for u,v in zip(B[i],B[row])]
        row+=1
        if row==nr:break
    return row

def candidate_matrix(p,m,N,z,f):
    # D(x^i)=[i]_z x^(i-1) f(x), modulo x^N.
    D=[[0]*N for _ in range(N)]; qi=0
    for i in range(1,N):
        qi=(qi+pow(z,i-1,p))%p
        for j,a in enumerate(f):
            if a and i-1+j<N:D[i-1+j][i]=(D[i-1+j][i]+qi*a)%p
    return D

def formula(p,m,N,f):
    l,r=divmod(N,m)
    nz=[i for i,x in enumerate(f) if x]
    if not nz:return [N]+[0]*m
    s=min(nz)//m
    ans=[N]
    for j in range(1,m):
        b=l-j*s
        ans.append((m-j)*b + min(r,m-j) if b>=0 else 0)
    return ans+[0]

def run():
    cases=[(3,2,list(range(2,13))),(5,2,list(range(2,11))),
           (5,4,list(range(2,11))),(7,3,list(range(2,11))),
           (7,6,list(range(2,11))),(11,5,list(range(2,11)))]
    tested=0; detailed=[]
    for p,m,NN in cases:
        z=primitive_root(p,m)
        for N in NN:
            l,r=divmod(N,m)
            allowed=[i for i in range(N) if i%m==0 and (r==0 or i>0)]
            if len(allowed)>5: continue
            obs=Counter(); expected=Counter()
            for coeffs in product(range(p),repeat=len(allowed)):
                f=[0]*N
                for i,c in zip(allowed,coeffs):f[i]=c
                D=candidate_matrix(p,m,N,z,f)
                # Verify skew Leibniz on basis monomials, x^N quotient.
                for a in range(N):
                    for b in range(N):
                        lhs=[D[k][a+b] if a+b<N else 0 for k in range(N)]
                        rhs=[0]*N
                        for k in range(N):
                            if k>=b:rhs[k]+=D[k-b][a]
                            if k>=a:rhs[k]+=pow(z,a,p)*D[k-a][b]
                            rhs[k]%=p
                        assert lhs==rhs,(p,m,N,f,a,b)
                for i in range(N):
                    for k in range(N):
                        assert D[k][i]*pow(z,i,p)%p==z*pow(z,k,p)*D[k][i]%p
                I=[[int(i==j) for j in range(N)] for i in range(N)]
                R=I
                rks=[N]
                for j in range(1,m+1):
                    R=mm(D,R,p)
                    rks.append(rank(R,p))
                assert rks[-1]==0,(p,m,N,f,rks)
                assert rks==formula(p,m,N,f),(p,m,N,f,rks,formula(p,m,N,f))
                s=next((i//m for i,c in enumerate(f) if c),None)
                obs[(s,tuple(rks))]+=1
                tested+=1
            low=int(bool(r))
            for s in range(low,(N-1)//m+1):
                count=(p-1)*p**((N-1)//m-s)
                f=[0]*N; f[m*s]=1
                expected[(s,tuple(formula(p,m,N,f)))]=count
            expected[(None,tuple([N]+[0]*m))]=1
            assert obs==expected,(p,m,N,obs,expected)
            detailed.append((p,m,N,len(allowed),sum(obs.values()),len(obs)))
    print('TAFT_JORDAN_VERIFIED')
    print('total actions enumerated',tested,'parameter cases',len(detailed))
    print('sample cases',detailed[::max(1,len(detailed)//10)])
if __name__=='__main__':run()
