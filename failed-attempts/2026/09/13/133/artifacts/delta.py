import numpy as np

B = np.array([[2.,1.],[1.,1.]])
Binv = np.array([[1.,-1.],[-1.,2.]])
lam = (3+np.sqrt(5))/2
mu = (3-np.sqrt(5))/2
# orthonormal eigenvectors
eu = np.array([-0.8506508083520399, -0.5257311121191336])
es = np.array([0.5257311121191336, -0.8506508083520399])
assert abs(np.linalg.norm(eu)-1)<1e-12 and abs(np.linalg.norm(es)-1)<1e-12

def r(x):
    x = np.asarray(x)
    return 1 + 0.04*np.sin(2*np.pi*x[...,0]) + 0.03*np.cos(2*np.pi*x[...,1])

def apply_B(x, n):
    # x: (...,2) in torus; apply B^n mod 1
    if n>=0:
        M = np.linalg.matrix_power(B, n)
    else:
        M = np.linalg.matrix_power(Binv, -n)
    return (x @ M.T) % 1.0

def Delta(x, a, b, N=12):
    """temporal distance for base point x (2,), unstable size a, stable size b."""
    xu = (x + a*eu) % 1.0
    xs = (x + b*es) % 1.0
    xus = (x + a*eu + b*es) % 1.0
    tot = 0.0
    for k in range(0, N+1):
        tot += (r(apply_B(xu,k)) - r(apply_B(xus,k)) - r(apply_B(x,k)) + r(apply_B(xs,k)))
        # = H_s(xu,xus)-H_s(x,xs) partial = -G_k
    for j in range(1, N+1):
        tot += (r(apply_B(x,j*-1)) - r(apply_B(xu,j*-1)) + r(apply_B(xus,j*-1)) - r(apply_B(xs,j*-1)))
    return tot

# convergence check
x = np.array([0.13, 0.71])
for N in [4,8,12,16,20]:
    print(N, Delta(x, 0.02, 0.02, N))

# period-3 orbit check
p0 = np.array([0.75, 0.5])
print("B p0", (B@p0)%1, "B^2 p0", (np.linalg.matrix_power(B,2)@p0)%1, "B^3", (np.linalg.matrix_power(B,3)@p0)%1)
print("r fixed0", r(np.array([0.,0.])))
print("r orbit", r(p0), r((B@p0)%1), r((np.linalg.matrix_power(B,2)@p0)%1))
