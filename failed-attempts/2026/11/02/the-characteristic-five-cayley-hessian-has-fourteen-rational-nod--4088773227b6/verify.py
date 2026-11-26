"""Exact computational reproducibility checks for the characteristic-five Cayley Hessian quartic."""
import itertools
import sympy as sp

x=sp.symbols('x0:4')
e1=sum(x)
e3=sum(sp.prod(x[i] for i in c) for c in itertools.combinations(range(4),3))
e4=sp.prod(x)
f=e3
h=sp.expand(e1*e3-4*e4)
assert sp.expand(sp.det(sp.hessian(f,x))+4*h)==0
print('HESSIAN_DETERMINANT_IDENTITY=PASS')

polys=[sp.Poly(sp.diff(h,v),*x,modulus=5).as_expr() for v in x]
points=[]
for j in range(4):
    varying=x[j+1:]
    change={x[i]:0 for i in range(j)}
    change[x[j]]=1
    res=[p.subs(change) for p in polys]
    if varying:
        groebner=sp.groebner(res,*varying,modulus=5,order='lex')
        assert all(sp.Poly(groebner.reduce(z**5-z)[1],*varying,modulus=5).is_zero for z in varying)
    else:
        assert all(int(g)%5==0 for g in res)
    for tail in itertools.product(range(5),repeat=len(varying)):
        P=[0]*j+[1]+list(tail)
        if all(int(g.subs(dict(zip(x,P))))%5==0 for g in polys):
            points.append(P)
assert len(points)==14
assert all(sum(int(v!=0) for v in P) in (1,2,4) for P in points)
for P in points:
    j=next(i for i,z in enumerate(P) if z)
    varying=[x[i] for i in range(4) if i!=j]
    local=h.subs({x[j]:1})
    val=dict(zip(varying,(P[i] for i in range(4) if i!=j)))
    mat=sp.hessian(local,varying).subs(val)
    assert int(mat.det())%5!=0
print('GEOMETRIC_SINGULAR_LOCUS=14_F5_NODES;ALL_QUADRATIC_RANK3=PASS')

# Polynomial quotient F5[t]/(t^2+3), where t^2=2 is nonsquare.
def field(degree):
    if degree==1:
        return 5,lambda a,b:(a+b)%5,lambda a,b:(a*b)%5
    assert degree==2
    q=25
    a=lambda u,v:((u%5+v%5)%5)+5*(((u//5)+(v//5))%5)
    m=lambda u,v: ((u%5)*(v%5)+2*(u//5)*(v//5))%5+5*(((u%5)*(v//5)+(u//5)*(v%5))%5)
    return q,a,m

def pointcount(degree):
    q,add,mul=field(degree)
    n=0
    for j in range(4):
        for tail in itertools.product(range(q),repeat=3-j):
            P=[0]*j+[1]+list(tail)
            e1=add(add(P[0],P[1]),add(P[2],P[3]))
            e3=0
            for k in range(4):
                t=[P[i] for i in range(4) if i!=k]
                e3=add(e3,mul(mul(t[0],t[1]),t[2]))
            e4=mul(mul(P[0],P[1]),mul(P[2],P[3]))
            val=add(mul(e1,e3),mul(1,e4)) # -4 equals +1 in F5
            if val==0:n+=1
    return n
n1=pointcount(1)
n2=pointcount(2)
assert (n1,n2)==(56,826)
print('H_F5_POINTS=56;H_F25_POINTS=826')
assert (n1+14*5,n2+14*25)==(126,1176)
print('RESOLUTION_F5_POINTS=126;RESOLUTION_F25_POINTS=1176')
# Weil bound and equality at q=25 force all eigenvalues over F5 to be +/-5.
trace1=126-(1+5**2)
trace2=1176-(1+25**2)
assert (trace1,trace2)==(100,550)
assert (trace1//5,trace2//25)==(20,22)
print('NORMALIZED_FROBENIUS=PLUS21_MINUS1;WEIL_BOUND_SATURATION=PASS')
print('VERIFY_OK')
