# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified sub-5 circular flows in the cyclically-5-connected girth-6 stratum,
with an exact perfect-matching-index table: Flower snarks J7 and J9 admit verified
(9,2)-flows, and no cyclically-5-connected girth-6 separator was found in the surveyed family

## Abstract

The suggested implication pi(G)>=5 => Phi_c(G)>=5 for bridgeless cubic graphs was
dispelled by Macajova–Skoviera (arXiv:2008.04775) only in the stratum of cyclically
4-edge-connected snarks of girth at least 5. Whether the separation pi>=5 versus
Phi_c<5 survives the standard nontriviality strengthening to cyclically 5-edge-connected
snarks of girth at least 6 is open. We do not close that question here. Instead we
deliver the admission-approved fallback datum, with every number replayable from stored
adjacency lists by stdlib-only certificate programs:

- The Flower snarks J7 (28 vertices) and J9 (36 vertices) are cyclically-5-edge-connected
  snarks of girth 6 with exact perfect-matching index pi=4 and certified circular flow
  number Phi_c<=9/2=4.5<5 via explicit nowhere-zero modular (9,2)-flows whose range and
  Kirchhoff conditions verify edge by edge.
- An exact-pi table across the constructed family (Petersen 5, Blanusa-like 18-vertex
  Kochol snark 4, double-Kochol 26-vertex snark K26 5, Flower J5 4, Goldberg chain 40
  (colourable) 3, J7 4, J9 4), including an explicit 26-vertex pi>=5 witness at
  girth 5 that bounds the gap: covering-hardness (pi>=5) is achievable by Kochol
  replacement, but every pi>=5 member found sits below the girth/connectivity bar,
  and every member at or above the bar has pi<=4.

This is a new citable extremal datum in the (cyclic-5, girth>=6) stratum: no database
(Brinkmann census: counts/oddness only; Karabas et al.: defect/oddness existence;
Mazak et al.: criticality) tabulates pi versus Phi_c there, and the sole prior
separator family is certified only at (cyclic-4, girth>=5).

## 1. Definitions and audit rule

All graphs are finite simple cubic. pi(G) = minimum number of perfect matchings covering
E(G) (pi(G)=3 iff G is 3-edge-colourable). Phi_c(G) = minimum r such that G admits a
nowhere-zero modular r-flow: with r=p/q in lowest terms, an orientation plus values
f:E->{q,...,p-q} with signed Kirchhoff sum 0 mod p at every vertex (equivalent to the
real-valued definition; Goddyn–Tarsi–Zhang). G is a snark if bridgeless, cubic, and not
3-edge-colourable. Cyclic connectivity >=5 means no edge-cut of size <=4 whose removal
leaves two components each containing a cycle (cycle-separating cut). Girth is the
shortest-cycle length (BFS certificate).

AUDIT RULE. Every claim replays from the stored adjacency list alone:
(1) girth by per-vertex BFS shortest-cycle; (2) bridgelessness by DFS lowlink and
cyclic>=5 by exhaustive DSU enumeration of all C(m,1)+...+C(m,4) edge subsets with a
cycle-in-each-side test; (3) snark status by exhaustive perfect-matching enumeration
plus triple-partition UNSAT for 3-edge-colourability; (4) pi by the same enumeration
plus an explicit k-cover (branch-and-bound set cover over matching bitmasks);
(5) flow bound by checking each stored value in [q,p-q] and each vertex sum = 0 mod p.
Certificate programs: output/artifacts/toolkit.py (stdlib only).

## 2. Witnesses

Witness W7 = Flower snark J7 (Isaacs), 28 vertices, 42 edges (adjacency: output/artifacts/J7_graph.json).
Witness W9 = Flower snark J9, 36 vertices, 54 edges (output/artifacts/J9_graph.json).
Construction used (standard J_k for odd k>=5): hub vertices B_i joined to A_i, C_i, D_i;
A-cycle A_0-...-A_{k-1}-A_0; C/D part forming a 2k-cycle with one twist. Exact edge lists
are in the artifacts; the verifier never trusts the generator, only the stored adjacency.

## 3. Verified properties (computed proof; each replayed)

Theorem (fallback datum). For each W in {J7, J9}:
(a) W is cubic, bridgeless, and has girth exactly 6;
(b) W is a snark (3-edge-colouring UNSAT; J7: 128 perfect matchings, no triple partitions
    E; J9: 512 perfect matchings, no triple partitions E);
(c) W is cyclically-5-edge-connected: exhaustive scan finds no cycle-separating cut of
    size 1, 2, 3, or 4 — J7: 42+861+11480+111930 subsets all negative (re-run 1.9 s);
    J9: 54+1431+24804+316251 subsets all negative (4.8 s);
(d) pi(W)=4 exactly: uncolourability gives pi>=4; stored 4-tuples of perfect matchings
    cover all edges (J7: explicit cover of all 42 edges; J9 likewise), so pi<=4;
(e) Phi_c(W)<=9/2=4.5<5: stored (9,2)-flows (values in {2,...,7}, Kirchhoff sum 0 mod 9
    at all 28 resp. 36 vertices) verify True in the independent checker
    (output/artifacts/J7_flow92.json, J9_flow92.json). Found by exact backtracking with
    vertex-completion pruning (J7: 127215 nodes; J9: 1639985 nodes), then frozen.

The checks (a)–(e) were re-executed from the JSON adjacency lists alone in a fresh
process (girth 6, bridgeless, uncolourability, Kirchhoff True for both witnesses;
J7 cyclic scan re-run empty). This is proof by finite certificate, not heuristic.

## 4. Family table and the gap boundary (computed evidence)

Exact pi values (PM enumeration + cover branch-and-bound), all replayable:

| graph | n | girth | cyclic | 3-col | #PM | pi | flow cert |
|---|---|---|---|---|---|---|---|
| Petersen | 10 | 5 | 5* | no | 6 | 5 (4-UNSAT, 5-SAT) | 5-flow only |
| Blanusa-like Kochol-18 | 18 | 5 | 3 | no | 16 | 4 | 5-flow only |
| Kochol-26 (K26, double replacement) | 26 | 5 | 3 | no | 40 | 5 (4-UNSAT, 5-SAT) | 5-flow only |
| Flower J5 | 20 | 5 | >=4? (<=3 empty) | no | 32 | 4 | 5-flow only |
| Goldberg chain 40 | 40 | 5 | — | yes | 365 | 3 | 4-flow (colourable) |
| Flower J7 | 28 | 6 | >=5 (cert) | no | 128 | 4 (cert) | (9,2)-flow (cert) |
| Flower J9 | 36 | 6 | >=5 (cert) | no | 512 | 4 (cert) | (9,2)-flow (cert) |

*Petersen cyclic connectivity is 5 by the same DSU program (classical value; not load-bearing).
Negative evidence (not a theorem): surveyed slices containing pi>=5 members (Kochol
iterates incl. K26; dot products P.P/P.J5/J5.J5/J5.J7 over sampled independent-edge
pairs; truncations; single-D_Ps K4-superpositions over all 64 flip masks — all
3-edge-colourable, hence D alone is not heavy) never reached girth>=6 with pi>=5;
pi>=5 members found (Petersen, K26) have girth 5 and cyclic<=3–4 and showed no sub-5
flow under exact+heuristic search. The 82-vertex basic heavy superposition of
Macajova–Skoviera (minimal for that recipe) is girth 5/cyclic-4 by construction, so that
recipe cannot supply the strengthened separator either. Existence of any (cyclic-5,
girth>=6, pi>=5, Phi_c<5) graph under 60 vertices remains OPEN.

## 5. Flow-search methodology (for reproducibility)

Simulated-annealing modular-flow search succeeded on 3-edge-colourable controls
(cube/K4 at r=4) but stalled on every snark at every r<5 — expected: sub-5 flows of
snarks are combinatorially isolated. The certified flows were found instead by exact
depth-first search over residues {q,...,p-q} with incremental Kirchhoff pruning
(fail a vertex the moment its third incident edge is assigned and the sum is nonzero
mod p). At (p,q)=(9,2) this closes in 0.2 s (J7) / 2.2 s (J9). Lower ratios timed out
at 30M-node caps (13/3, 17/4, 4/1), and r=11/3 exhausted quickly with UNSAT at 4641
nodes — recorded as search data, not as lower-bound theorems. Exact Phi_c of J7/J9
is therefore NOT claimed; only the certified upper bound 9/2 is.

## 6. Originality and limits

Neighbour comparison (no subtraction implies the datum): Macajova–Skoviera 2008.04775
separates only at (cyclic-4, girth>=5); Brinkmann et al. 1206.6690 tabulates no pi/Phi_c;
Karabas et al. 2106.12205 gives no pi/Phi_c values; Mazak et al. 2406.16618 concerns
vertex-criticality, not covering vs flow. The (cyclic-5, girth>=6) pi-vs-Phi_c table
entry (J7/J9: pi=4, Phi_c<=4.5, with cyclic/girth certificates) is new as an explicit
machine-checkable datum.
LIMITS. (i) We do NOT exhibit a (cyclic-5, girth>=6) snark with pi>=5 — the headline
target is open; the title states this plainly. (ii) Exact Phi_c(J7), Phi_c(J9) unknown;
4.5 is an upper bound. (iii) Cyclic>=5 is certified by exhaustive search to size 4 only
(which is exactly the definition); higher cuts not enumerated (not needed).
(iv) pi=5 of K26/Petersen is exact within complete PM enumeration (npm 40/6) — small
enough to be exhaustive, no sampling. (v) All certificates assume simple graphs as
stored; generators are convenience only — verifiers read adjacency lists.

## 7. Reproduce in seconds

python3 -c "
import sys, json; sys.path.insert(0,'output/artifacts')
from toolkit import *
for nm in ('J7','J9'):
    d=json.load(open(f'output/artifacts/{nm}_graph.json')); adj=[list(x) for x in d['adj']]
    assert girth(adj)==6 and not bridges(adj)
    col,_,npm=is_3_edge_colourable(adj); assert not col
    fl=json.load(open(f'output/artifacts/{nm}_flow92.json')); E=[tuple(e) for e in fl['E']]
    fv={tuple(e):fl['f'][i] for i,e in enumerate(E)}; orient={tuple(e):tuple(e) for e in E}
    assert verify_circular_flow(adj,E,orient,fv,9,2)[0]
    print(nm,'OK: girth6 bridgeless snark npm=%d Phi<=9/2'%(npm))"

## References

- E. Macajova, M. Skoviera, Perfect matching index vs. circular flow number of a cubic graph, arXiv:2008.04775 (2020). Sole prior separator; (cyclic-4, girth>=5); 82-vertex smallest basic example.
- E. Macajova, M. Skoviera, Cubic graphs that cannot be covered with four perfect matchings, arXiv:2008.01398. Tetrahedral-flow theory / heavy-superposition theorem used to scope the search.
- G. Brinkmann et al., Generation and Properties of Snarks, arXiv:1206.6690. Census to 36 vertices; no pi/Phi_c table.
- A. Karabas et al., Girth, oddness, and colouring defect of snarks, arXiv:2106.12205. Defect/girth existence; no pi/Phi_c values.
- J. Mazak et al., Strictly critical snarks with girth or cyclic connectivity 6, arXiv:2406.16618. Criticality, not pi/Phi_c.
- L. A. Goddyn, M. Tarsi, C. Zhang, On (k,d)-colorings and fractional nowhere-zero flows, JGT 28 (1998). Modular/react r-flow equivalence underlying the certificate.
