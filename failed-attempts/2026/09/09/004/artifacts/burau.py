# Certified Alexander toolkit via unreduced Burau on KnotAtlas braid words (sympy only).
# 8_20: n=3, word=[1,1,1,-2,-1,-1,-1,-2] (KnotTheory/Gittings). Closure = knot? checked: permutation is a 3-cycle.
import sympy as sp
t=sp.Symbol('t')
def perm(w,n):
    p=list(range(n))
    for g in w:
        i=abs(g)-1
        a,b=p[i],p[i+1]
        p[i],p[i+1]=b,a
    return p
def unred(n,i,sgn):
    M=sp.eye(n)
    B=sp.Matrix([[1-t,t],[1,0]])
    if sgn<0: B=B.inv()
    M[i-1,i-1]=B[0,0];M[i-1,i]=B[0,1];M[i,i-1]=B[1,0];M[i,i]=B[1,1]
    return M
def braidburau(w,n):
    B=sp.eye(n)
    for g in w: B=B*unred(n,abs(g),1 if g>0 else -1)
    return sp.simplify(B)
def alexander(w,n):
    B=braidburau(w,n)
    Mr=(sp.eye(n)-B)[0:n-1,0:n-1]
    d=sp.expand(Mr.det())
    return d
if __name__=='__main__':
    w=[1,1,1,-2,-1,-1,-1,-2]; n=3
    print("perm:",perm(w,n))
    d=alexander(w,n)
    print("Delta =",d)
    print("|Delta(-1)| =",abs(complex(d.subs(t,-1))))
    print("trefoil:",sp.expand(alexander([1,1,1],2)))
    print("unknot 1-strand:",1)
