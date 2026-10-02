"""Stdlib-only replay of the Hessian half of the emergent certificate (mod 7).
Checks: (1) F = X^5-20X^3YZ+30XY^2Z^2-Y^5 is annihilated by x^2+yz, y^3+xz^2, z^3
acting as differential operators mod 7; (2) second Hessian w.r.t. the A2-operator
basis has det 6 (nonzero) at the y-point and det 0 at (1,1,1). Prints HESSIAN_OK."""
import itertools
P = 7
F = {(5,0,0):1,(3,1,1):(-20)%P,(1,2,2):30%P,(0,5,0):(-1)%P}
def dX(p):
    o = {}
    for (i,j,k),c in p.items():
        if i>0: o[(i-1,j,k)]=(o.get((i-1,j,k),0)+c*i)%P
    return {k:v%P for k,v in o.items() if v%P}
def dY(p):
    o = {}
    for (i,j,k),c in p.items():
        if j>0: o[(i,j-1,k)]=(o.get((i,j-1,k),0)+c*j)%P
    return {k:v%P for k,v in o.items() if v%P}
def dZ(p):
    o = {}
    for (i,j,k),c in p.items():
        if k>0: o[(i,j,k-1)]=(o.get((i,j,k-1),0)+c*k)%P
    return {k:v%P for k,v in o.items() if v%P}
D=[dX,dY,dZ]
def apply(ops,p):
    for v in ops: p=D[v](p)
    return p
def addp(a,b):
    o=dict(a)
    for k,v in b.items():
        o[k]=(o.get(k,0)+v)%P
        if o[k]%P==0: del o[k]
    return o
assert addp(apply([0,0],F),apply([1,2],F))=={}, "x^2+yz does not kill F"
assert addp(apply([1,1,1],F),apply([0,2,2],F))=={}, "y^3+xz^2 does not kill F"
assert apply([2,2,2],F)=={}, "z^3 does not kill F"
O2=[(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
def opvars(e): return [0]*e[0]+[1]*e[1]+[2]*e[2]
def mat_at(pt):
    M=[[0]*5 for _ in range(5)]
    for a in range(5):
        for b in range(5):
            lin=apply(opvars(O2[a])+opvars(O2[b]),F)
            s=0
            for (i,j,k),c in lin.items():
                assert i+j+k==1
                s=(s+c*(pt[0] if i else (pt[1] if j else pt[2])))%P
            M[a][b]=s
    return M
def det5(M):
    d=0
    for pm in itertools.permutations(range(5)):
        sgn=-1 if sum(1 for a in range(5) for b in range(a+1,5) if pm[a]>pm[b])%2 else 1
        t=1
        for i in range(5): t=t*M[i][pm[i]]%P
        d=(d+sgn*t)%P
    return d
dy=det5(mat_at((0,1,0))); ds=det5(mat_at((1,1,1)))
print("det Hess@y =",dy,"| det Hess@s =",ds)
assert dy!=0 and ds==0, "HESSIAN FAIL"
print("HESSIAN_OK")
