"""Reproducibility diagnostics for the sine-delay map and its large-feedback escape coordinate."""
import math
import sympy as sp

def iterate(alpha,beta,gamma,delta,mu,x,y,z,n):
    out=[(x,y,z)]
    for _ in range(n):
        x,y,z=y,math.sin(z),alpha+beta*x+gamma*y-delta*math.sin(z)+mu*z
        out.append((x,y,z))
    return out

def phase(alpha,beta,gamma,delta,mu,x,y,z,n=23):
    return iterate(alpha,beta,gamma,delta,mu,x,y,z,n)[-1][2]/(mu**n)

def root_bisection(func,a,b,steps=80):
    assert func(a)<0<func(b)
    for _ in range(steps):
        mid=(a+b)/2
        if func(mid)>0:b=mid
        else:a=mid
    return (a+b)/2

L,c,b,g,d,m = sp.symbols('L c b g d m')
J=sp.Matrix([[0,1,0],[0,0,c],[b,g,m-d*c]])
expected=L**3-(m-d*c)*L**2-g*c*L-b*c
assert sp.expand(J.charpoly(L).as_expr()-expected)==0
s=sp.symbols('s',real=True)
assert sp.simplify(sp.diff((m-1)*s+(b+g-d)*sp.sin(s),s) - (m-1+(b+g-d)*sp.cos(s)))==0

p=(-3.76,0.9,0.9,1,5.0)
assert p[-1]>1+sum(map(abs,p[1:4]))
x0,y0=0.7,-0.4
zstar=root_bisection(lambda z:phase(*p,x0,y0,z),-8.,8.)
vals=[]
for dz in (-0.07,-0.02,0.,0.02,0.07):
    H=phase(*p,x0,y0,zstar+dz)
    vals.append((dz,H))
assert all(vals[i][1]<vals[i+1][1] for i in range(4))
assert vals[0][1]<0<vals[-1][1]
for z0 in (zstar-0.07,zstar+0.07):
    data=iterate(*p,x0,y0,z0,15)
    assert all((data[i][2]<data[i+1][2] if z0>zstar else data[i][2]>data[i+1][2]) for i in range(5,14))
    H=phase(*p,x0,y0,z0)
    # Variation of constants gives a uniform bounded correction to mu**n*H.
    errs=[abs(data[n][2]-p[-1]**n*H) for n in range(4,15)]
    assert max(errs)<6
sfix=float(sp.nsolve((p[-1]-1)*s+(p[1]+p[2]-p[3])*sp.sin(s)+p[0],0))
seq=iterate(*p,x0,y0,zstar,12)
assert abs(seq[-1][2]-sfix)<2e-4

# Counterexample to any coefficient-uniform boundary with mu < 1+B.
B=1.0; mu=1.8
positive=float(sp.nsolve((mu-1)*s-B*sp.sin(s),0.8))
assert positive>0 and abs((mu-1)*positive-B*math.sin(positive))<1e-12
print('VERIFY_OK')
print('phase samples',vals)
print('bounded fiber z0',zstar,'fixed phase',sfix,'last z',seq[-1][2])
print('three distinct equilibria at beta=gamma=alpha=0, delta=1, mu=1.8:',-positive,0,positive)
