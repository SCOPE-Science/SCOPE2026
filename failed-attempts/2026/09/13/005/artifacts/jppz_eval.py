"""Route (ii): evaluate eps_*Ch^{[x]}(r=7,k=7;a=(-3,-2,-1,-1)) pushed to Mbar_{2,4},
then h = 7^{2-2} int Ch^{[7]}/prod(1-mu_i psi_i), mu=(3,2,1,1), via JPPZ Cor 4 + exact psi engine.
Chiodo x-scaling: Ch^{[x]} = c with ch_m -> x * ch_m, i.e. replace B-factors by x*B and edge r/2 -> x*r/2.
Equivalently in JPPZ vertex/leg/edge exponentials multiply every B_{m+1}(.)/m(m+1) exponent by x.
Weightings: k-weighting mod r: legs a_i; at vertex: sum incident w + k*(2g_v-2+n_v) = 0 mod r (JPPZ Def).
Edge: w(h)+w(h')=0 mod r. Here k=7=0 mod 7 so vertex condition = sum of incident half-edge weights 0 mod 7.
Legs: a_i mod 7 = (4,5,6,6).
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial as F
import itertools, sys
sys.path.insert(0, "output/artifacts")
from psi_engine import psi

R = 7; K = 7; X = 7
A = (4, 5, 6, 6)  # -3,-2,-1,-1 mod 7
MU = (3, 2, 1, 1)

def Bpoly(n, x):
    def bern(m):
        a = [Fraction(0)]*(m+1); a[0] = Fraction(1)
        for mm in range(1, m+1):
            s = sum(a[k]*Fraction(F(mm+1), F(k)*F(mm+1-k)) for k in range(mm))
            a[mm] = -s/Fraction(mm+1)
        return a[m]
    from math import comb as C
    return sum(Fraction(C(n, k))*bern(k)*(x**(n-k)) for k in range(n+1))

MMAX = 6
# coefficients: vertex: -(-1)^{m-1} B_{m+1}(k/r)/m(m+1) times X; legs: +(-1)^{m-1} B(a_i/r)/m(m+1) times X
cv = {m: -(((-1)**(m-1))) * Bpoly(m+1, Fraction(K, R)) / (m*(m+1)) * X for m in range(1, MMAX+1)}
cl = {}
for a in set(A):
    cl[a] = {m: (((-1)**(m-1))) * Bpoly(m+1, Fraction(a, R)) / (m*(m+1)) * X for m in range(1, MMAX+1)}
# edge: exponent E(w) = sum_{m>=1} (-1)^{m-1} B(w/r)/m(m+1) [psi_h^m - (-psi_h')^m] times X
ce = {}
for w in range(R):
    ce[w] = {m: (((-1)**(m-1))) * Bpoly(m+1, Fraction(w, R)) / (m*(m+1)) * X for m in range(1, MMAX+1)}

print("cv:", {m: cv[m] for m in range(1,4)})
print("cl[4]:", {m: cl[4][m] for m in range(1,4)})

# Enumerate stable graphs of genus 2 with 4 legs (unlabelled legs get labelled 0..3 with fixed A).
# Represent each graph: vertices with genus, legs assignment, edges (half-edge pairs).
# We generate: smooth; 1-edge (sep splits / nonsep loop); 2-edge; 3-edge. Automorphism orders computed.
graphs = []
def add_graph(vgen, legs, edges):
    # legs: tuple per vertex of leg indices; edges: list of (v1,v2) (v1==v2 loop)
    graphs.append((tuple(vgen), tuple(tuple(sorted(L)) for L in legs), tuple(edges)))

add_graph([2], [(0,1,2,3)], [])
# 1-edge graphs
for mask in range(1, (1<<4)-1):
    I1 = tuple(i for i in range(4) if mask>>i & 1)
    I2 = tuple(i for i in range(4) if not mask>>i & 1)
    if I1[0] != 0 and len(I1) > 0:  # canonical: leg0 on side 1... still need both orders? fix leg0 in I1
        continue
    for g1 in range(3):
        for g2 in range(3):
            if g1+g2 != 2: continue
            n1, n2 = len(I1)+1, len(I2)+1
            if 2*g1-2+n1 <= 0 or 2*g2-2+n2 <= 0: continue
            add_graph([g1,g2],[I1,I2],[(0,1)])
add_graph([1], [(0,1,2,3)], [(0,0)])
print("graphs with <=1 edge:", len(graphs))
for g in graphs: print(g)
