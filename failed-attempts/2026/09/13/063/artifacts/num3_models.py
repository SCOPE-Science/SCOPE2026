import numpy as np

def Phi(u):
    u = np.asarray(u, float)
    out = np.zeros_like(u)
    nz = u != 0
    uu = u[nz]
    out[nz] = (uu**2/2)*(np.log(np.abs(uu))-1.5)
    return out

def build_models(n):
    """Level-n Cantor blocks. Returns J (intervals), Qavg (exact avg kernel K>=0),
    Qlow (minorant matrix: off-diag min K, diag interval-capacity self bound)."""
    ivs = [[0.0, 1.0]]
    for _ in range(n):
        n0 = []
        for (a, b) in ivs:
            L = (b-a)/3
            n0.append([a, a+L]); n0.append([b-L, b])
        ivs = n0
    N = len(ivs)
    A = np.array([a for a, b in ivs]); B = np.array([b for a, b in ivs])
    h = B[0]-A[0]
    Qavg = np.zeros((N, N))
    for i in range(N):
        a, b = ivs[i]
        # D = int int log|x-y| ; Kavg = -D/(hi*hj)
        Dab = Phi(b-B)+Phi(a-A)-Phi(b-A)-Phi(a-B)  # check orientation below
        Qavg[i, :] = -Dab/(h*h)
    # Qlow: off diag min K over J_i x J_j = log(1/maxdist); diag log(4/h)
    Qlow = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                Qlow[i, j] = np.log(4.0/h)
            else:
                mx = max(abs(B[i]-A[j]), abs(B[j]-A[i]))
                Qlow[i, j] = np.log(1.0/mx)
    return ivs, Qavg, Qlow

def check_orientation():
    # verify Qavg formula on two far intervals
    ivs = [[0, 1/9], [8/9, 1]]
    A = np.array([a for a, b in ivs]); B = np.array([b for a, b in ivs])
    a, b = ivs[0]
    Dab = Phi(b-B)+Phi(a-A)-Phi(b-A)-Phi(a-B)
    print("Dab(log, expect neg):", Dab)
    print("Kavg (expect ~ +0.1):", -Dab/((1/9)**2))

check_orientation()
