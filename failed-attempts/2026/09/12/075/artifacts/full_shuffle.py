"""Full shuffle step: spider at all faces -> absorb legs -> contract deg-2 -> peel pendants -> gauge.
Verify: Z_n(a,b) = prefactor * Z_{n-1}(a',b') with EXPLICIT (a',b') for the uniform-face family.
We hypothesize closure within uniform-face family with (a',b') proportional to (b/D1?, ...).
Instead of guessing, EXTRACT (a',b') from the reduced graph edge weights numerically, then identify symbolic map."""
import math
from validate_ops import WGraph, build_aztec_cj, brute_Z, spider

def shuffle_step(n, a, b, verbose=False):
    G = build_aztec_cj(n, a, b)
    z_before = brute_Z(G)
    faces = [(i,j) for i in range(n) for j in range(n)]
    Delta_prod = 1.0
    # spider each face; corners cyclic: B(2i,2j+1), W(2i+1,2j), B(2i+2,2j+1), W(2i+1,2j+2)
    for (i,j) in faces:
        corners=[('B',(2*i,2*j+1)),('W',(2*i+1,2*j)),('B',(2*i+2,2*j+1)),('W',(2*i+1,2*j+2))]
        # check cyclic: B-W edges exist?
        D=spider(G, corners)
        Delta_prod *= D
    # Now: every original vertex should have degree = old degree + 1 (one leg per incident face).
    # Absorb legs: new edge weight of leg (v,u) with u inner of degree 3? Inner u has edges: leg + 2 inner-square edges.
    # Standard absorption: delete u, connect v to the two inner neighbours with weights leg*inner_edge... but that creates non-Aztec edges.
    # TRUE shuffle structure (Propp): after spider at ALL faces, each original edge is replaced... hmm, actually the correct statement:
    #   spider creates inner squares; the ORIGINAL vertices become degree-2 (leg + one surviving original edge?) NO — original edges were all consumed.
    # Let me inspect degrees.
    from collections import Counter
    degs=Counter(G.deg(v) for v in G.V)
    print(f"n={n} after spiders: V={len(G.V)} E={len(G.E)} deg-dist={dict(degs)}")
    return G, Delta_prod, z_before

G, Dp, zb = shuffle_step(2, 0.7, 1.3)
print("Delta_prod=",Dp,"Z_before=",zb)
