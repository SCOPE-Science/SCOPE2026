"""Finite diagnostic checks for the positive three-species flow; the proof is analytic."""
from fractions import Fraction as F
from itertools import product
from math import log, isfinite


def velocity(x, y, z, a, b, c):
    return (x*(1-y+c*x-a*x*z), y*(x-1), z*(a*x*x-b))


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


# A finite diagnostic of identities, evaluated exactly in rational arithmetic.
checks = 0
params = [F(1, 2), F(1), F(3, 2), F(2)]
states = [F(1, 3), F(3, 4), F(5, 4)]
for a,b,c,x,y,z in product(params[:2],params[:3],params[:2],states,states[:2],states[:2]):
    dx,dy,dz = velocity(x,y,z,a,b,c)
    assert dy/y == x-1
    assert dz/z-2*a*dy/y == a*(x-1)**2+a-b
    checks += 1
assert checks == 2*3*2*3*2*2  # 144 exact samples, two identities each

# Critical equilibrium segment and its exact characteristic polynomial.
for a,c,Y in product((F(1),F(2),F(3)), (F(1,2),F(1)), (F(1,4),F(1,2))):
    Z = (1+c-Y)/a
    assert Z > 0
    assert velocity(F(1),Y,Z,a,a,c) == (0,0,0)
    J = [[Y-1,-1,-a],[Y,0,0],[2*a*Z,0,0]]
    for lam in (F(0),F(1),F(2),F(-1)):
        A = [[(lam if i==j else F(0))-J[i][j] for j in range(3)] for i in range(3)]
        assert det3(A) == lam*(lam*lam-(Y-1)*lam+(Y+2*a*a*Z))

# Elementary RK4 diagnostic around a stable point of the critical segment.
a=b=2.0
c=1.0
u = [1.05,0.55,0.72]
h = 0.02
W0 = log(u[2])-2*a*log(u[1])
y0 = u[1]
mean_x=0.0
mean_sq=0.0
T=80.0
N=int(T/h)
def f(u):return velocity(*u,a,b,c)
def step(u,h):
    k1=f(u)
    k2=f([u[i]+h*k1[i]/2 for i in range(3)])
    k3=f([u[i]+h*k2[i]/2 for i in range(3)])
    k4=f([u[i]+h*k3[i] for i in range(3)])
    return [u[i]+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3)]
for j in range(N):
    v = step(u,h)
    assert all(t>0 and isfinite(t) for t in v)
    mean_x += h*((u[0]+v[0])/2)
    mean_sq += h*((u[0]-1)**2+(v[0]-1)**2)/2
    u=v
W1=log(u[2])-2*a*log(u[1])
assert abs((mean_x/T-1)-(log(u[1])-log(y0))/T) < 3e-7
assert abs(mean_sq/T-(b/a-1)-(W1-W0)/(a*T)) < 3e-7
assert abs(u[0]-1) < 2e-5
assert abs(u[1]+a*u[2]-(1+c)) < 2e-5
print('THREE_SPECIES_CRITICAL_BUDGET_OK exact_samples=%d critical_jacobians=%d numerical_steps=%d' % (checks, 12, N))
