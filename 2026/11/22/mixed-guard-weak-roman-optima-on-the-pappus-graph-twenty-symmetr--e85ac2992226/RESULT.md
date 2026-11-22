# Mixed-guard weak Roman optima on the Pappus graph: twenty symmetry types and two relocation metrics

## Finding

For the eighteen-vertex Pappus graph \(P\), the minimum weak Roman defending weight is exactly \(\gamma_r(P)=8\). There are precisely \(2691\) minimum functions \(f:V(P)\to\{0,1,2\}\), divided according to the number of vertices receiving two guards:

| Vertices labeled \(2\) | Vertices labeled \(1\) | Functions | Full-automorphism orbits |
|---:|---:|---:|---:|
| 0 | 8 | 1755 | 13 |
| 1 | 6 | 882 | 6 |
| 2 | 4 | 54 | 1 |
| **Total** | | **2691** | **20** |

The one-guard *jump* graph on these \(2691\) functions, allowing one guard to be reassigned between any distinct vertices while retaining optimal weak Roman defense, is connected with \(18846\) edges, radius \(8\), diameter \(9\), and eccentricity counts \(1323\) at distance \(8\) and \(1368\) at distance \(9\). Its one-guard *slide* subgraph, restricting the source and destination to an edge of \(P\), is also connected, with \(6372\) edges, radius \(9\), diameter \(12\), and eccentricity counts \(567,1422,486,216\) at distances \(9,10,11,12\), respectively.

This is a classification of optimal *functions* and their unit-guard transfer graphs, not an assertion that all functions are isomorphic or that transfers correspond to an actual attack-response strategy over multiple attacks.

## Assumptions and scope

A weak Roman dominating function on a finite graph \(G\) is a map \(f:V(G)\to\{0,1,2\}\) such that for every vertex \(v\) with \(f(v)=0\), some neighbor \(u\) with \(f(u)>0\) admits the transfer \(f'(u)=f(u)-1\), \(f'(v)=1\), with all other values unchanged, after which no zero-labeled vertex lacks a positive-labeled neighbor. The weight is \(w(f)=\sum_{v\in V(G)}f(v)\). A minimum function is one of smallest weight, and selected vertex names are distinguished while counting functions.

Represent \(P\) as the bipartite incidence graph of nine points \(p_{x,y}\), \(x,y\in\mathbb F_3\), and nine lines of the forms \(x=c\), \(y=c\), and \(y-x=c\) for \(c\in\mathbb F_3\). Label points \(3x+y\), lines \(x=c\) by \(9+c\), lines \(y=c\) by \(12+c\), and lines \(y-x=c\) by \(15+c\). Adjacency means incidence. This is the Pappus \((9_3)\) Levi graph, not the occasionally named nine-vertex point collinearity graph.

For a jump, the guard source \(u\) must have positive weight and the distinct destination \(v\) must have weight at most one. Set \(f'(u)=f(u)-1\), \(f'(v)=f(v)+1\); the move is allowed if \(f'\) is again minimum weak Roman. A slide additionally requires \(uv\in E(P)\). Both transfer graphs are undirected under reversal of the transfer.

## Proof

**Exact finite reduction.** Write \(S=\{v:f(v)>0\}\) and \(T=\{v:f(v)=2\}\), with \(T\subseteq S\). Then \(w(f)=|S|+|T|\). Let \(\operatorname{dom}(S)\) mean that every vertex lies in \(S\) or has a neighbor in \(S\). The weak Roman condition is *exactly* the conjunction of \(\operatorname{dom}(S)\) with, for every \(v\notin S\), either (a) \(N(v)\cap T\ne\varnothing\), or (b) some \(u\in N(v)\cap(S\setminus T)\) satisfies \(\operatorname{dom}((S\setminus\{u\})\cup\{v\})\). In (a), moving a guard from a doubly guarded neighbor leaves the support containing \(S\), so domination survives automatically; in (b), the displayed set is precisely the support after moving a singly guarded neighbor. The criterion is therefore necessary and sufficient, with no relaxation.

**Exhaustion.** The provided standard-library Python checker enumerates every disjoint pair of selected singleton and doubleton vertex sets of weight at most \(8\). For every pair it evaluates the preceding exact criterion using precomputed domination of all \(2^{18}\) vertex supports. No weight below \(8\) succeeds. At weight \(8\) the only successful multiplicities are \(1755\) with no doubled vertex, \(882\) with one, and \(54\) with two; all cases with three or four doubles fail. The independent C++ checker traverses the \(3^{18}\) distinct ternary labelings in a different standard Pappus vertex ordering, discards weights above \(8\), and directly simulates an allowed response to each zero vertex. It reproduces exactly the same counts. These are exhaustive proofs for the specified finite graph, not sampling-based extrapolations.

**Full symmetry.** The three affine line classes admit \(108\) point-side-preserving affine automorphisms: all allowable invertible affine coordinate maps are enumerated and their induced line maps verified. A directly checked point-line duality doubles this to \(216\). The Python checker also exhaustively tests all \(9!\) point permutations, finding exactly \(108\) that preserve the nine line triples. Since the graph is connected bipartite, any automorphism preserves or swaps its two shores; hence these \(216\) transformations comprise its full automorphism group. Acting on all \(2691\) minimum functions gives orbit-size multiplicities: one orbit of size \(27\), eight of size \(108\), and four of size \(216\) in the all-singleton class; one orbit of size \(18\), two of size \(108\), and three of size \(216\) in the one-double class; and one orbit of size \(54\) in the two-double class. A representative for each of the twenty orbits, in the affine vertex numbering, appears in `orbit_representatives.tsv`.

**Transfers and distances.** Every one-unit assignment transfer from each of the \(2691\) optimum functions is generated, checked against the complete optimum set, and recorded either as a jump or, when its endpoints are adjacent, as a slide. The independently formed edge lists are undirected. Breadth-first search from *every* optimum function in both graphs verifies connectedness and the stated total edges, radii, diameters, and entire eccentricity histograms. Since all vertices and edges are exhaustively enumerated and every breadth-first distance is exact, these figures are finite graph theorems.

## Verification

The complete, reproducible certificates are `verify_affine.py` (standard-library, incidence geometry, exact pair enumeration, all \(9!\) point symmetries, orbit and transfer-distance checks), `verify_ternary.cpp` (independent ternary-code enumeration), and `orbit_representatives.tsv` (twenty reproducible representatives). Run:

```bash
python3 verify_affine.py
c++ -O3 -std=c++17 verify_ternary.cpp -o verify_ternary
./verify_ternary
```

Both checkers passed on the supplied code. The fixed Pappus vertex numbering is explicit, so no third-party graph library or external data set is required.

## Relationship to prior work

Henning and Hedetniemi (2003) introduced weak Roman defense and its guard-transfer definition; the 2014 bounds paper compares weak Roman, secure, and two-rainbow domination without establishing this complete Pappus optimizer and transfer-graph census. A previous computational report on *secure domination of the Pappus graph* already gives the \(1755\) eight-guard all-singleton configurations, their thirteen symmetry orbits, and their \(12798\)-edge jump and \(4320\)-edge slide graphs. **Those all-singleton facts are not claimed as new.** In the weak Roman model, the additional \(936\) optimum functions with one or two doubled vertices form seven new symmetry orbits; adding them changes the two connected transfer graphs to the larger enumerated graphs, with different sharp diameters. It is this complete weighted-optimum extension and both full transfer metrics that constitute the finding.

## Limitations

The classification concerns this particular eighteen-vertex incidence graph. It proves neither an infinite-family formula nor new numerical results for other cubic cages. The exact counts are finite exhaustive computations with independently implemented algorithms, not a formal proof-assistant certificate. The known all-singleton subcase overlaps an earlier computational finding, and historical coverage beyond the inspected sources is not guaranteed; independent scholarly audit has not been performed. A transfer preserves weak Roman feasibility but need not model simultaneous attackers or an indefinitely adaptive protection game.

## References

1. M. A. Henning and S. T. Hedetniemi, *Defending the Roman Empire—A new strategy*, Discrete Mathematics **266** (2003), 239–251. https://doi.org/10.1016/S0012-365X(02)00811-7
2. *Bounds on weak roman and 2-rainbow domination numbers*, Discrete Applied Mathematics **178** (2014), 27–32. https://doi.org/10.1016/j.dam.2014.06.016
3. I. N. Kagno, *Desargues' and Pappus' graphs and their groups*, American Journal of Mathematics **69** (1947), 859–863. https://doi.org/10.2307/2371806
4. *Pappus Graph*, Wolfram MathWorld. https://mathworld.wolfram.com/PappusGraph.html
5. *Thirteen secure-guard orbits and two relocation metrics on the Pappus graph*, prior computational research report (2026; no independent audit claimed). Referenced solely to acknowledge covered all-singleton claims.
