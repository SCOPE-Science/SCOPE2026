"""Independent exact transfer reconstruction for one-sweep stable outputs."""
from itertools import product
STATES=[(0,0),(0,1),(1,0)]

def allowed(a,b,c):
    return not(a==b==c==0) and not(a==b==1 or b==c==1)

def nor(a,b):return int(not (a or b))

def weight(p,q):
    return sum(nor(p,z)==q for z in (0,1))

def seam_weight(p,q,r):
    return sum(nor(p,a)==q and nor(a,b)==r for a,b in product((0,1),repeat=2))

def get_matrices():
    T=[[0]*3 for _ in range(3)]; D=[[0]*3 for _ in range(3)]
    U=[[0]*3 for _ in range(3)]
    for i,(u,p) in enumerate(STATES):
        for j,(v,q) in enumerate(STATES):
            if p==v and allowed(u,p,q):
                T[i][j]=weight(p,q)
                U[i][j]=1
        for j,(s,r) in enumerate(STATES):
            for q in (0,1):
                if (allowed(u,p,q) and allowed(p,q,s) and allowed(q,s,r)
                    and s==nor(q,r)):
                    D[i][j]+=seam_weight(p,q,r)
    return T,D,U

def mult(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def ident():return [[int(i==j) for j in range(3)] for i in range(3)]
def power(A,n):
    out=ident()
    while n:
        if n&1:out=mult(out,A)
        A=mult(A,A);n//=2
    return out

def trace(A):return sum(A[i][i] for i in range(3))

def main():
    T,D,U=get_matrices()
    assert T==[[0,1,0],[0,0,2],[1,1,0]],T
    assert D==[[1,1,0],[0,1,3],[1,1,2]],D
    assert U==[[0,1,0],[0,0,1],[1,1,0]],U
    cube=power(T,3)
    assert cube==[[2*T[i][j]+2*int(i==j) for j in range(3)] for i in range(3)]
    for n in range(3,36):
        R=2*trace(mult(power(T,n-3),D))
        P=trace(power(U,n))
        if n>=6:
            assert R==2*(2*trace(mult(power(T,n-5),D)))+2*(2*trace(mult(power(T,n-6),D)))
            assert P==trace(power(U,n-2))+trace(power(U,n-3))
        print(n,P,R)
    print('exact transfer checks passed')
if __name__=='__main__':main()
