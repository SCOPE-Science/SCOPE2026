# Plane-dual prisms and bipyramids separate recurrent avalanche dissipation

## Finding

**Theorem.** For every integer \(n\ge4\), let \(P_n=C_n\square K_2\) be the prism graph and let \(B_n=C_n\vee\overline{K}_2\) be its plane dual (the bipyramid with an equatorial \(n\)-cycle and two nonadjacent apices). Use the standard conservative Abelian sandpile with one absorbing sink and the usual degree toppling thresholds. Choose a prism sink at the top rim vertex \(a_0\), and choose a bipyramid sink at one apex \(s\).

A *positive nondissipative principal avalanche* is a single-grain addition to a nonsink vertex of a recurrent stable configuration, followed by complete legal stabilization, that has at least one nonsink toppling and sends **zero** grains to the absorbing sink. Then:

1. \(P_n\) admits a positive nondissipative principal avalanche for every \(n\ge4\), and one can choose an avalanche consisting of precisely one toppling.
2. \(B_n\) admits no positive nondissipative principal avalanche for any \(n\ge4\) with the apex sink, regardless of the recurrent stable configuration or nonsink addition vertex.
3. The two graphs have isomorphic Abelian sandpile (critical) groups, as required by plane-graph duality.

Therefore the existence of recurrent, positive-toppling, zero-sink-loss avalanche events is **not** determined by a sandpile-group isomorphism or by plane duality with these specified sinks.

For \(n=4\), \(P_4\cong Q_3\) is the cube and \(B_4\cong K_{2,2,2}\) is the octahedron. Both have exactly \(384\) recurrent stable configurations. With every recurrent configuration and every nonsink addition vertex weighted equally, the cube has exactly \(64\) positive nondissipative events among \(384\cdot7=2688\) additions, while the octahedron has zero among \(384\cdot5=1920\) additions. The corresponding exact event probabilities are \(1/42\) and \(0\). On the cube, \(45\) such events originate at graph distance two from the sink and \(19\) at graph distance three. All \(64\) consist of a single toppling.

## Assumptions and scope

Vertices of \(P_n\) are \(a_0,\ldots,a_{n-1}\) and \(b_0,\ldots,b_{n-1}\), subscripts modulo \(n\), with rim edges \(a_ia_{i+1}\), \(b_ib_{i+1}\) and rung edges \(a_ib_i\). All prism vertices have degree three; \(a_0\) is absorbing. Vertices of \(B_n\) are rim vertices \(r_0,\ldots,r_{n-1}\) and nonadjacent apices \(s,t\), with rim edges \(r_ir_{i+1}\) and all spoke edges \(sr_i,tr_i\). The degree of each rim vertex is four; each apex has degree \(n\); \(s\) is absorbing.

A stable height vector \(c\) on nonsink vertices satisfies \(0\le c(v)<\deg(v)\). Adding one grain at a nonsink vertex and repeatedly toppling any unstable nonsink vertex yields a unique stable state and unique toppling counts. Each toppling of a vertex adjacent to the sink transfers one grain across that incident edge and is counted as one grain of dissipation. A recurrent configuration is characterized by Dhar's burning criterion: starting with the sink burned, repeatedly burn any unburned vertex \(v\) for which \(c(v)\) is at least the number of incident edges to unburned vertices; every nonsink vertex must eventually burn.

The theorem is about a finite graph for each \(n\), and about the specified absorbing vertex on each graph. No positive-temperature dynamics, stochastic toppling rule, other sink choice, or thermodynamic-limit critical exponent is asserted.

## Proof

**1. Prism recurrence and one-grain confinement.** Let \(v=b_2\), which is not adjacent to sink \(a_0\) for every \(n\ge4\). Define \(c\) on nonsink vertices by \(c(v)=2\), by \(c(w)=1\) for each of its three neighbors \(w\in\{a_2,b_1,b_3\}\), and by \(c(z)=2\) on all other nonsink vertices. (The height at the sink is irrelevant.) All heights lie in \(\{0,1,2\}\), so the vector is stable.

The graph induced by \(P_n\setminus N[v]\), with \(N[v]=\{b_2,a_2,b_1,b_3\}\), is connected and contains the sink \(a_0\). Indeed, its top rim minus \(a_2\) is a path containing the sink, and any surviving lower-rim vertex \(b_i\) is joined to its surviving upper mate \(a_i\) by a rung. For every vertex \(z\notin N[v]\) other than the sink, \(c(z)=2\). Inductively these vertices burn along paths from the sink, since each has at least one previously burned neighbor and degree three, leaving at most two unburned neighbors. Once they have burned, each vertex \(w\in N(v)\) has only \(v\) as an unburned neighbor, since the three neighbors of \(b_2\) are pairwise nonadjacent for \(n\ge4\). Their heights equal one, so all three burn. Finally \(v\), at height two, burns with no unburned neighbors. Thus \(c\) is recurrent by the burning criterion.

Adding one grain at \(v\) raises its height from two to three and makes it topple. The resulting height at \(v\) is zero. Each of its three neighbors rises from one to two, still stable; no other height changes. The resulting state is stable, so this is exactly one toppling. Since \(v\) has no edge to \(a_0\), the total number of grains reaching the sink is zero. This proves part 1 for every \(n\ge4\).

**2. Dual bipyramid obstruction.** Take any recurrent stable height vector \(c\) on \(B_n\), with absorbing apex \(s\). For each rim vertex, \(c(r_i)\le3\); for the other apex, \(c(t)\le n-1\). Initially all nonsink vertices are unburned. The number of their nonsink neighbors is \(n\) at \(t\), so the burning criterion cannot burn \(t\) first. At every rim vertex this number is three (two rim neighbors plus \(t\)), so at least one rim vertex \(r_j\) must satisfy \(c(r_j)=3\): otherwise no vertex would be eligible to burn and the state would fail recurrence.

Now add one grain at an arbitrary nonsink vertex and stabilize. If any rim vertex topples, it sends at least one grain directly to the absorbing apex \(s\), so the avalanche is dissipative. If no rim vertex topples, but the other apex \(t\) topples, it sends a grain to **each** rim vertex. The initially saturated \(r_j\) then reaches height at least four and necessarily topples, a contradiction. Hence an avalanche with zero sink dissipation cannot contain any toppling. This proves part 2, independent of how many topplings or what legal toppling order would occur otherwise.

**3. Duality and equal groups.** Embed the prism as the boundary of a convex \(n\)-gonal prism. Its \(n\) quadrilateral side faces form an \(n\)-cycle of face-adjacencies; its two \(n\)-gonal faces are adjacent to every side face and not to each other. Therefore its planar dual is exactly \(B_n\). For connected plane graphs without bridges, the cycle–cut lattice description of the graph Jacobian gives an isomorphism of critical groups of the primal and dual. Thus their sandpile groups are isomorphic, even though parts 1 and 2 show different zero-dissipation avalanche behavior.

**4. Exact cubical illustration.** The independent enumeration programs enumerate recurrent configurations on \(Q_3\) and \(K_{2,2,2}\) in two logically separate ways: the Dhar burning test on every stable height vector, and breadth-first closure under all grain-addition operators starting from the maximal stable state. Their complete sets of recurrent states and all principal avalanche counts agree. The number of recurrent states on either graph is \(384\). Among the cube's \(2688\) events, \(1162\) have no topplings, whereas \(1226\) send no grains to the sink. The difference is \(64\) positive nondissipative events. For the octahedron, both the number of no-toppling events and the number of zero-burst events are \(1133\), so the difference is zero. Dividing by the corresponding equally weighted event counts gives \(64/2688=1/42\) and zero. The independent enumeration also verifies the cube distance split \(45+19=64\) and single-toppling character.

## Verification

The three standalone Python programs embedded alongside this manuscript require Python \(\ge3.10\) and only its standard library. Run `python verify_burning.py` for exhaustive stable-configuration and burning-criterion enumeration, `python verify_independent.py` for independent addition-orbit enumeration and exact toppling/burst histograms, and `python verify_family.py` for constructive recurrence witnesses and finite checks on bipyramids. The first two use unrelated recurrent-state generation methods and different legal toppling schedules. Their printed checks require exactly \(384\) recurrent cube states and \(384\) recurrent octahedron states and the exact \(64\) versus \(0\) nondissipative counts. The third checks the explicit prism witness at \(n=4,5,6,8,12,30\) and exhaustively verifies the bipyramid obstruction for \(n=3,4,5,6\).

The all-\(n\) claims follow from the analytic burning arguments and planar duality. These finite scripts are reproducibility checks; they are **not** offered as substitutes for proofs covering unbounded \(n\).

## Relationship to prior work

Chan, Glass, Macauley, Perkinson, Werner and Yang (2014) establish compatibility of sandpile groups and spanning-tree actions with planar duality; that is the established group-theoretic premise, not a novelty claim. Austin, Chambers, Funke, García Puente and Keough (2016) define multivariate avalanche polynomials, including a burst-size evaluation, and evaluate trees, cycles, complete graphs and wheels. Their general framework is broader in representation but their evaluated graph families do not give this primal–dual prism/bipyramid nondissipative-event separation or the cube–octahedron zero-burst count. The event is a particularly sharp structural comparison of recurrent avalanche response that is *not* forced by graph-Jacobian isomorphism.

## Limitations

The infinite-family distinction depends on the stated sink choice (rim sink on the prism, apex sink on the bipyramid). It does not establish any result for all sinks on the bipyramid, any finite-temperature or infinite-volume critical exponent, or universality of avalanche statistics. The exact \(n=4\) fraction uses the uniform measure on recurrent states and on nonsink grain-addition sites, not a claim about arbitrary biased driving. Although relevant accessible primary texts were compared, a previously unindexed equivalent explicit theorem remains a possible historical-priority risk. No independent external mathematical validation is claimed.

## References

1. M. Chan, D. Glass, M. Macauley, D. Perkinson, C. Werner, and Q. Yang, *Sandpiles, Spanning Trees, and Plane Duality*, arXiv:1406.5147, first posted June 19, 2014. https://arxiv.org/abs/1406.5147
2. D. Austin, M. Chambers, R. Funke, L. D. García Puente, and L. Keough, *The Avalanche Polynomial of a Graph*, arXiv:1605.02713, first posted May 9, 2016. https://arxiv.org/abs/1605.02713
3. R. Cori and D. Rossin, *On the Sandpile Group of Dual Graphs*, European Journal of Combinatorics (2000), DOI:10.1006/eujc.1999.0366. The full text was not available in the compared accessible material; the plane-duality premise is independently documented in reference 1.
