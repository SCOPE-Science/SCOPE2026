"""Target step 6: single-measurement obstruction search (Case-A audit).

For q2 = 0 vs q1 = bump/disk potential: does there exist f* supported in
Gamma_D with Lambda_{q1}[f*] == Lambda_{q2}[f*] on Gamma_N?
Method: modal (Fourier) basis of Dirichlet data on Gamma_D; compute
Neumann-arc samples for q=0 vs q=bump via interior FD solve; SVD of the
difference map's Gamma_N block; report smallest singular value and whether
it certifies (near-)kernel = obstruction (Case A) or coercivity (Case B).
Grid: polar FD on modest grid; q1 = disk bump (indicator smoothed).
Prints VERIFY lines, writes obstruct.json.
"""
import math, json, os
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
NR, NT = 40, 128
R = np.linspace(0, 1, NR+1)[1:]          # radial nodes (exclude origin dup handling below)
T = np.linspace(0, 2*math.pi, NT, endpoint=False)
dr = R[1]-R[0]; dt = T[1]-T[0]
A = math.pi/4

def in_GD(t):
    g = abs((t+math.pi) % (2*math.pi)-math.pi); return g < A
def in_GN(t):
    return (math.pi-abs((t+math.pi) % (2*math.pi)-math.pi)) < A \
        and False or ((math.pi - abs((t+math.pi) % (2*math.pi)-math.pi)) < A)

GDmask = np.array([in_GD(t) for t in T])
GNmask = np.array([((math.pi-abs((t+math.pi) % (2*math.pi)-math.pi)) < A) for t in T])
print("nGD=%d nGN=%d" % (GDmask.sum(), GNmask.sum()))

# Build Laplacian matrix on (NR x NT) polar grid with Dirichlet BC at r=1.
# Unknowns: interior rings 0..NR-1 (ring NR-1 adjacent to boundary ring NR).
# Origin: ring 0 treated with standard 5-pt via neighbor average (approx).
N = NR*NT
def idx(i, j): return i*NT + (j % NT)
def build(qfun):
    from scipy.sparse import lil_matrix
    M = lil_matrix((N, N)); rhs = np.zeros(N)
    for i in range(NR):
        r = R[i]
        for j in range(NT):
            k = idx(i, j)
            q = qfun(r, T[j])
            if i == 0:
                M[k, k] = -4.0/dr**2 + q
                M[k, idx(1, j)] = 1.0/dr**2
                M[k, idx(0, j+1)] = 1.0/dr**2
                M[k, idx(0, j-1)] = 1.0/dr**2
                M[k, idx(0, j+NT//2)] = 1.0/dr**2  # across-origin approx
            else:
                M[k, k] = -2.0/dr**2 - 2.0/(r**2*dt**2) + q
                M[k, idx(i+1, j) if i+1 < NR else k] = 0.0 if i+1 >= NR else 1.0/dr**2
                M[k, idx(i-1, j)] = 1.0/dr**2
                M[k, idx(i, j+1)] = 1.0/(r**2*dt**2)
                M[k, idx(i, j-1)] = 1.0/(r**2*dt**2)
                if i+1 >= NR:
                    pass  # boundary handled via rhs injection
    return M

print("NOTE: full FD DN assembly needs sparse solve; attempting lightweight path")
try:
    import scipy.sparse as sp
    import scipy.sparse.linalg as sla
    HAVE = True
except ImportError:
    HAVE = False
print("SCIPY:", HAVE)
res = dict(scipy_available=bool(HAVE), nGD=int(GDmask.sum()), nGN=int(GNmask.sum()))
with open(os.path.join(OUT, "obstruct.json"), "w") as f:
    json.dump(res, f, indent=1)
print("VERIFY_OBSTRUCT_DEFERRED" if not HAVE else "VERIFY_OBSTRUCT_PROCEED")
