# Exact primitive three-wave populations on three classical cubic incidence graphs

## Finding
For synchronous, threshold-one, three-state Greenberg–Hastings (GH) excitation on the connected Möbius–Kantor, Pappus, and Desargues incidence graphs, the respective numbers of labelled **primitive temporal three-periodic configurations** are exactly \(54{,}036\), \(134{,}478\), and \(645{,}180\). Consequently, the numbers of primitive three-orbits are respectively \(18{,}012\), \(44{,}826\), and \(215{,}060\). These are all the configurations of least temporal period three, not the total recurrent populations (which can have other periods).

## Assumptions and scope
Every vertex has one color in \(\{0,1,2\}\). A vertex in color 1 changes to 2, a vertex in color 2 changes to 0; a vertex in color 0 changes to 1 if and only if at least one neighbor has color 1, and otherwise remains 0. Every vertex updates simultaneously. Configurations are labelled vertex assignments, without quotient by graph automorphisms. A temporal orbit contains three distinct configurations, counted once.

The Möbius–Kantor graph is \(GP(8,3)\), and the Desargues graph is \(GP(10,3)\), where \(GP(n,k)\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\) and edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+k}\). The Pappus Levi graph has points \(0,\ldots,8\), with nine lines whose point triples, in order, are \((0,1,4),(1,2,5),(2,3,0),(3,4,7),(4,5,8),(5,6,3),(6,7,1),(7,8,2),(8,0,6)\). The vertices are the points and lines, with incidence edges. Every graph is connected, cubic and bipartite, with equally sized parts of sizes eight, nine, and ten.

## Proof
**Wave characterization.** In a configuration of exact temporal period three, a vertex that ever has color 1 must pass through \(1,2,0,1\), and therefore advances every step. A vertex that never has color 1 cannot have color 2 (which can only be preceded by color 1), and hence stays at 0. A permanently resting vertex cannot have a permanently cycling neighbor, since the neighbor would be excited once each three steps. Connectivity implies that either every vertex stays 0 or every vertex cycles through the three colors. The latter case is equivalent to the local condition: for every vertex initially colored \(c\), at least one neighbor is colored \(c+1\pmod3\). Conversely, this condition guarantees synchronous color rotation at each update and hence a primitive three-cycle.

**Exact finite counting.** Let \(P\) and \(L\) be the two shores, each with \(m\) vertices, and let \(R_i\subset P\) be the three points incident with line \(i\). Fix one point to color 0. Every cyclic global color shift of a valid coloring is valid, and exactly one of the three shifted colorings fixes this point to 0. Thus multiply the restricted count by three. Enumerate all \(3^{m-1}\) remaining point color assignments \(p\). A line of color \(c\) is admissible precisely when \(R_i\) contains a point of color \(c+1\pmod3\). For an admissible choice \(c\) of line \(i\), let \(M(i,c)\subseteq R_i\) be the incident points with color \(c-1\pmod3\). The point conditions hold exactly when the union of the \(m\) masks \(M(i,c_i)\) equals all of \(P\).

This is an exhaustive disjoint partition, and two independent finite algorithms in `levi_wave_verify.py` evaluate it: direct recursion over all line choices, and subset-mask dynamic programming summing multiplicities for each union. They agree on all three graphs and give respectively \(54{,}036\), \(134{,}478\), and \(645{,}180\). There are no additional period-three configurations by the wave characterization. Dividing by three yields the orbit counts.

## Verification
Run `python3 levi_wave_verify.py` under Python 3.9 or later. No external packages are required. The saved output in `levi_wave_verify.out` reports the two independently implemented finite counts for each graph, checks the specified totals, and includes a direct \(3^6=729\)-state synchronous-update cross-check on the smaller cubic bipartite graph \(K_{3,3}\), which has 36 primitive-three configurations. The graph encodings, site update convention and all finite ranges are explicit in the file.

## Relationship to prior work
Greenberg–Hastings excitation and propagating waves on graphs are classical. Gravner, Lyu and Sivakoff (2016) characterize long-term excitation activity of the three-color model on arbitrary connected graphs by path/cycle winding; they do not tabulate these three exact primitive-three orbit populations. Abreu, Labbate and Sheehan (2010) study the incidence-graph geometry and two-factor properties of the Pappus configuration, not the present dynamics. Earlier exact short-period excitation studies of other named cubic graphs are relevant methodologically but give no direct numerical implication for the three named graphs.

## Limitations
The proof concerns the temporal-three sector only. It does not determine transients, higher-period orbits, attraction probabilities, or the total periodic-state populations. The counts have self-review, not independent external validation. Absolute historical priority is not certified; a missed specialized tabulation is a residual risk.

## References
1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, first posted 1993-04-02.
2. M. Abreu, D. Labbate and J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, arXiv:1002.1891, first posted 2010-02-09.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first posted 2016-10-24.
