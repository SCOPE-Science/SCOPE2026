"""Independent finite diagnostics for graph-local energy readout formulas.

Run: python3 verify_odd_cycle_readout.py
The proof of all-parameter optimality is analytical; sampling is diagnostic only.
"""
import cmath
import itertools
import math
import random

I = ((1+0j,0j),(0j,1+0j))
X = ((0j,1+0j),(1+0j,0j))
Y = ((0j,-1j),(1j,0j))
Z = ((1+0j,0j),(0j,-1+0j))
PAULI = {'I':I,'X':X,'Y':Y,'Z':Z}

def tensor_mat(a,b):
    ra,ca = len(a),len(a[0]); rb,cb=len(b),len(b[0])
    return tuple(tuple(a[i//rb][j//cb]*b[i%rb][j%cb] for j in range(ca*cb)) for i in range(ra*rb))

def pauli_string(letters):
    out=((1+0j,),)
    for ch in letters:out=tensor_mat(out,PAULI[ch])
    return out

def matvec(a,x):
    return [sum(t*v for t,v in zip(row,x)) for row in a]

def inner(x,y):return sum(v.conjugate()*w for v,w in zip(x,y))

def kronvec(a,b):return [x*y for x in a for y in b]

def cycle(n):return [(i,(i+1)%n) for i in range(n)]

def spherical(rng):
    z=rng.uniform(-1,1)
    phi=rng.uniform(0,2*math.pi)
    t=math.sqrt(1-z*z)
    return (t*math.cos(phi),t*math.sin(phi),z)

def sphere_eigenstate(axis,s):
    x,y,z=axis
    theta=math.acos(max(-1.,min(1.,z)))
    phi=math.atan2(y,x)
    if s==1:return (math.cos(theta/2),cmath.exp(1j*phi)*math.sin(theta/2))
    return (-cmath.exp(-1j*phi)*math.sin(theta/2),math.cos(theta/2))

def hamiltonian(n,edges,h,j):
    dim=1<<n
    out=[[0j]*dim for _ in range(dim)]
    terms=[]
    for v in range(n):
        p=['I']*n;p[v]='Z';terms.append((h,''.join(p)))
    for a,b in edges:
        for ch in ('X','Y'):
            p=['I']*n;p[a]=p[b]=ch;terms.append((j,''.join(p)))
    for coef,letters in terms:
        a=pauli_string(letters)
        for i in range(dim):
            for k in range(dim):out[i][k]+=coef*a[i][k]
    return out

def f_formula(axis,sgn,edges,h,j):
    n=len(axis)
    local=h*sum(sgn[i]*axis[i][2] for i in range(n))
    pair=j*sum(sgn[a]*sgn[b]*(axis[a][0]*axis[b][0]+axis[a][1]*axis[b][1]) for a,b in edges)
    return local+pair

def q_formula(axis,edges,h,j):
    return h*h*sum(v[2]*v[2] for v in axis)+j*j*sum((axis[a][0]*axis[b][0]+axis[a][1]*axis[b][1])**2 for a,b in edges)

def q_outcomes(axis,edges,h,j):
    return sum(f_formula(axis,s,edges,h,j)**2 for s in itertools.product((-1,1),repeat=len(axis)))/(1<<len(axis))

def q_cycle(n,h,j):
    c=n/2*(1-math.cos(math.pi/n))
    return min(h*h,j*j*c)

def twist(n):
    return [(math.cos(math.pi*(n-1)*i/(2*n)),math.sin(math.pi*(n-1)*i/(2*n)),0.) for i in range(n)]

def remove_one(n):
    return [(0.,0.,1.)]+[(1.,0.,0.) if i%2 else (0.,1.,0.) for i in range(1,n)]

def approx(a,b,tol=2.e-10):
    if abs(a-b)>tol*(1+abs(a)+abs(b)):
        raise AssertionError((a,b))

checks=0
rng=random.Random(624982)
for n in (3,5,7,9,11):
    e=cycle(n)
    for h,j in ((1.,1.),(.1,1.),(3.,.45),(0.7,1.3),(1.5,0.1)):
        minimum=q_cycle(n,h,j)
        approx(min(q_formula(twist(n),e,h,j),q_formula(remove_one(n),e,h,j)),minimum)
        checks+=1
        for _ in range(110):
            axes=[spherical(rng) for i in range(n)]
            # Random testing is not a universal minimization certificate.
            if q_formula(axes,e,h,j)+1e-12<minimum:raise AssertionError('unexpected lower value')
            checks+=1
for n,edges in ((3,cycle(3)),(4,[(0,1),(1,2),(2,3)]),(5,cycle(5))):
    h,j=0.7,1.2
    for _ in range(25):
        axes=[spherical(rng) for i in range(n)]
        approx(q_formula(axes,edges,h,j),q_outcomes(axes,edges,h,j))
        checks+=1

# Direct matrix-vector Born rule, independent of the Pauli moment expansion.
for edges in (cycle(3),[(0,1),(1,2)]):
    H=hamiltonian(3,edges,1.,1.)
    for _ in range(20):
        axes=[spherical(rng) for i in range(3)]
        fs=[]
        for s in itertools.product((-1,1),repeat=3):
            v=[1+0j]
            for a,sgn in zip(axes,s):v=kronvec(v,sphere_eigenstate(a,sgn))
            fv=inner(v,matvec(H,v))
            approx(fv.imag,0.)
            approx(fv.real,f_formula(axes,s,edges,1.,1.))
            fs.append(fv.real)
            checks+=1
        approx(sum(v*v for v in fs)/8,q_formula(axes,edges,1.,1.))
        checks+=1

# The 3-cycle state has precisely the advertised optimal energy variance.
delta=1/256
for axes,target in ((twist(3),.75),(remove_one(3),1.)):
    fs=[f_formula(axes,s,cycle(3),1.,1.) for s in itertools.product((-1,1),repeat=3)]
    es=[.5+8*delta*f for f in fs]
    assert all(0<e<1 for e in es)
    approx(sum(es)/8,.5)
    approx(sum((e-.5)**2 for e in es)/8,64*delta*delta*target)
    checks+=3
approx(math.sqrt(48)*delta,math.sqrt(3)/64)
checks+=1

# Explicit separable-convex-decomposition weights for the 3-cycle source.
d=16
m=3+2*3
assert 1-m*d*delta==7/16
assert m*d*delta==9/16
checks+=2
print('VERIFY_OK',checks,'diagnostics; odd-cycle critical c3=',3/4)
