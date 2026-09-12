"""Symbolic shuffle orbit with sympy: track (x,y) face weights + phase through 4 steps.
State: (x, y, phase) where phase=+1 means even faces carry x. Single shuffle maps:
  Delta_x = 2x^2 (even faces), Delta_y = 2y^2 (odd faces) [for uniform-face cells; b-generalizes a^2+b^2? here cells uniform so Delta=2x^2].
  Wait: for uniform-face cells, Delta = x^2+x^2 = 2x^2. For general (a,b) topic case b=1: Deltas 2a^2, 2b^2=2.
  New weights: x' = x/(2x^2) = 1/(2x), y' = 1/(2y). Phase: new even faces carry...? inner square edge from even-face spider has weight x/Delta_x = 1/(2x); these edges form the new even or odd faces?
  From shuffle_reduce numerics, determine phase flip: new even-face weight = 1/(2x) or 1/(2y)?
  Then iterate 4 steps symbolically and check closure + compute total prefactor; verify against closed-form c-ratios.
"""
import sympy as sp
x,y=sp.symbols('x y', positive=True)
# One shuffle: counts: E = ceil(n^2/2) even faces, O = floor(n^2/2) odd faces (for size n).
# Z_n(x,y,ph) = (2x^2)^E (2y^2)^O * Z_{n-1}(x1,y1,ph1), (x1,y1) = (1/(2x) or 1/(2y) depending on phase flip).
# Determine flip numerically: shuffle_reduce(3, .7, 1.3): new even faces (of reduced Aztec_2) carry which of {0.714=1/(2a), 0.385=1/(2b)}?
# Reduced graph vertex labels are all P (inner) — need geometric positions. Reconstruct positions: inner vertex of face (i,j) sits at face center (2i+1,2j+1).
# Modify spider to record positions.
from validate_ops import WGraph, build_aztec_cj, brute_Z
def spider_pos(G, corners, pos):
    v0,v1,v2,v3=corners
    ws=[]
    for (xx,yy) in [(v0,v1),(v1,v2),(v2,v3),(v3,v0)]:
        ws.append(G.E.pop(tuple(sorted((xx,yy)))))
    Delta=ws[0]*ws[2]+ws[1]*ws[3]
    Pts=[]
    for k,vk in enumerate(corners):
        p=(f"P{k}",)+pos[vk]  # inherit position tag
        G.V[p]=1-G.V[vk]; Pts.append(p)
    for k,vk in enumerate(corners):
        G.add_edge(vk,Pts[k],1.0)
    W=[ws[(k+2)%4]/Delta for k in range(4)]
    for k in range(4):
        G.add_edge(Pts[k],Pts[(k+1)%4],W[k])
    return Delta, Pts
