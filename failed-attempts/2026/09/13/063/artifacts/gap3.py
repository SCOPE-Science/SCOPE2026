import numpy as np, math

def Fs(w):
    if w == 0: return 0.0
    return (w*w/2.0)*(math.log(abs(w))-1.5)

def Dlog(a, b, c, d):
    return Fs(b-c)-Fs(b-d)-Fs(a-c)+Fs(a-d)

def Kavg(a, b, c, d):
    return -Dlog(a, b, c, d)/((b-a)*(d-c))

def cantor(n):
    ivs = [[0.0, 1.0]]
    for _ in range(n):
        n0 = []
        for (a, b) in ivs:
            L = (b-a)/3
            n0.append([a, a+L]); n0.append([b-L, b])
        ivs = n0
    return ivs

def Kmin_off(a, b, c, d):
    mx = max(abs(b-c), abs(d-a))
    return math.log(1.0/mx)

def Kmax_off(a, b, c, d):
    mn = min(abs(b-c), abs(d-a), abs(a-c), abs(b-d))
    # careful if intervals overlap (only i==j here)
    return math.log(1.0/mn)

def test_n4():
    n = 4
    cells = cantor(n)
    N = len(cells)
    o = np.array([1.0 if ((a+b)/2 < 1/9+1e-12 or (a+b)/2 > 8/9-1e-12) else 0.0 for (a, b) in cells])
    Qavg = np.zeros((N, N)); Qlow = np.zeros((N, N)); Qup = np.zeros((N, N))
    h = cells[0][1]-cells[0][0]
    D = math.log(4.0/h)
    for i, (a, b) in enumerate(cells):
        for j, (c, d) in enumerate(cells):
            Qavg[i, j] = Kavg(a, b, c, d)
            if i == j:
                Qlow[i, j] = math.log(4.0/h)   # self: rigorous Kavg >= log(4/h)? check
                Qup[i, j] = None
            else:
                Qlow[i, j] = Kmin_off(a, b, c, d)
                Qup[i, j] = Kmax_off(a, b, c, d)
    # self-term comparisons: Kavg[i,i] vs log(4/h) vs K over full-gap bound
    print("h=", h, "log(4/h)=", D, " Kavg self=", Qavg[0, 0])
    print("off-diag avg vs low/high sample (0,1):", Qavg[0, 1], Qlow[0, 1], Qup[0, 1])
    print("off-diag avg vs low/high sample (0,8):", Qavg[0, 8], Qlow[0, 8], Qup[0, 8])
    print("off-diag avg-low max:", np.max(Qavg-Qlow - np.eye(N)*10))
    print("off-diag up-avg max:", np.max((Qup-Qavg) - np.eye(N)*100))
    # oscillation with respect to which points? K(x,y) avg over y for fixed x:
    # For lower bound on I(mu) we need per-row gaps, not per-pair
    # Row i: r_i(x') - r_i(x) with weight w*: compute exact row-average profile
    # relative to candidate w* from Qavg free solve.
    ones = np.ones(N)
    v = np.linalg.solve(Qavg, ones); wf = v/v.sum(); Vf = 1/v.sum()
    print("Vf(Qavg)=", Vf, " outer2a=", o @ wf)
    # For candidate w*, energy at a representative point x_k in cell k:
    # e_k(x) = sum_j w_j Kavg-point(x, cell_j); row spread via sup/inf of K(x,y) over x in cell
    # measure sup_x e(x) - avg bound using per-pair oscillation of K in x
    # K(x,y) in x over cell i, y fixed in cell j: range = log(maxdist/mindist)
    osc = np.zeros((N, N))
    for i, (a, b) in enumerate(cells):
        for j, (c, d) in enumerate(cells):
            if i == j:
                osc[i, j] = float('inf')
            else:
                mx = max(abs(b-c), abs(d-a))
                mn = min(abs(b-c), abs(d-a), abs(a-c), abs(b-d))
                osc[i, j] = math.log(mx/mn)
    e_spread = osc @ np.abs(wf)  # upper bound on sup-inf of e(x) over cell i... (i==j inf -> handle)
    print("e_spread (inf at self, use uniform-density instead):", e_spread[:4])
    # self-cell oscillation of point-energy: y in same cell: K(x,y) unbounded -> need avg formulation

test_n4()
