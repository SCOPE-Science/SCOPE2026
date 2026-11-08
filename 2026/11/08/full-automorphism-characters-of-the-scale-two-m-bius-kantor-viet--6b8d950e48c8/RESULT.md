# Full automorphism characters of the scale-two Möbius–Kantor Vietoris–Rips complex

## Finding

Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph with vertices \(u_i,v_i\), indices modulo eight, and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). Give its vertices shortest-path distance and put \(K=\operatorname{VR}_{\leq2}(M)\), the flag complex of pairs at distance at most two. Write \(G=\operatorname{Aut}(M)\), of order \(96\).

**Theorem (symmetry refinement).** The two nonzero reduced rational homology modules of \(K\) have dimensions \(9\) and \(2\) in degrees two and three, respectively. The integral third-homology module is the permutation lattice on the two bipartition classes of \(M\). Thus, for every \(g\in G\),
\[
 \chi_3(g)=\begin{cases}2,&g\text{ preserves the two classes individually},\\0,&g\text{ exchanges them}.
 \end{cases}
\]
Let \(\mathcal F(K)\) denote the nonempty faces of \(K\). If \(g\sigma=\sigma\), denote by \(\operatorname{sgn}(g|_\sigma)\) the sign of the permutation induced on the vertices of that face. The **full degree-two rational character**, for every one of the \(96\) automorphisms, is explicitly
\[
 \chi_2(g)=\sum_{\substack{\varnothing\ne\sigma\in\mathcal F(K)\\g\sigma=\sigma}}
 (-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)-1+\chi_3(g).
\]
The ordered character-value pairs \((\chi_2(g),\chi_3(g))\) have multiplicities
\[
 (9,2):1,\quad(3,0):6,\quad(1,2):27,\quad(1,0):12,
 \quad(-1,2):12,\quad(-1,0):30,\quad(-3,2):8.
\]
Consequently \(\widetilde H_2(K;\mathbb Q)^G=0\) whereas \(\widetilde H_3(K;\mathbb Q)^G\cong\mathbb Q\). The complexification of the nine-dimensional second-homology module is the multiplicity-free sum of exactly **three** pairwise nonisomorphic irreducibles. In particular, the finite orbit space has rational reduced homology
\[
\widetilde H_j(K/G;\mathbb Q)\cong
\begin{cases}\mathbb Q,&j=3,\\0,&j\ne3.\end{cases}
\]
The full **nonequivariant** integral homotopy classification \(K\simeq\bigvee^9S^2\vee\bigvee^2S^3\) was obtained previously and is explicitly **not** claimed as new here.

## Assumptions and scope

All graphs are finite, simple and undirected; edges of \(M\) have unit length. The inclusive scale-two condition means all pairwise graph distances are at most two, and the Vietoris–Rips construction uses the graph **vertices**, not interior points of its metric realization. The action is by graph automorphisms on oriented simplicial chains over \(\mathbb Z\), then on rational homology. A character consists of all elementwise traces, not merely conjugacy-class counts; the formula above evaluates the trace for any explicitly supplied automorphism and the table counts all \(96\) group elements. The displayed invariant ranks are rational ranks. The quotient assertion concerns ordinary rational homology, not integral quotient homology or quotient homotopy type.

## Proof

**1. Faces and homology dimensions.** Graph-shortest-path calculations give each vertex exactly one antipode at distance four and graph-distance distribution \((1,3,6,5,1)\) at distances zero through four. Enumerating all cliques in the threshold-two graph gives exactly \(16,72,112,48\) simplices of dimensions zero through three, and none higher. Exact binary elimination of the three nontrivial original simplicial boundary matrices yields ranks \(15,57,46\). Thus \(\widetilde H_1(K;\mathbb F_2)=0\), \(\dim\widetilde H_2(K;\mathbb F_2)=9\) and \(\dim\widetilde H_3(K;\mathbb F_2)=2\). The last two rational ranks are also independently known from the earlier integral homotopy classification, but we reconstruct the rational dimensions using the explicit cycles below: the rank of a rational boundary cannot be less than its rank modulo two, while the exhibited two independent integral cycles impose the reverse upper bound on the top boundary rank. Consequently the rational ranks are exactly \(9\) and \(2\), with no rational degree-one homology.

**2. Two integral sphere cycles.** The graph is bipartite. On each of its two eight-vertex bipartition classes, the only omitted edges of the threshold-two graph are the four pairs of antipodal vertices (distance four). Thus its full induced subcomplex is the join of four copies of \(S^0\), hence the boundary of a four-dimensional crosspolytope, an integral \(S^3\). Choosing one orientation on each, write its fundamental chain as
\[
 c_B=(p_1-q_1)*(p_2-q_2)*(p_3-q_3)*(p_4-q_4).
\]
Direct signed-boundary cancellation verifies that both chains are cycles; their three-face supports are disjoint and each contains coefficient \(\pm1\). Since there are no four-simplices and the kernel of the rational third boundary has dimension two, every integral three-cycle is an **integer** linear combination of these two: its coefficients are determined by inspecting one tetrahedron from each support. Hence they are an integral basis of \(H_3(K;\mathbb Z)\).

**3. Integral automorphism action.** Every graph automorphism either preserves or exchanges the two bipartition classes. It sends antipodal pairs to antipodal pairs, so it maps each fundamental sphere chain to the positive or negative fundamental chain of its image part. For all \(96\) automorphisms, direct orientation calculations show that the sign is **positive** in both cases: on the ordered integral cycle basis, every part-preserving element acts by the \(2\times2\) identity and every part-exchanging element by the coordinate-swap matrix. This proves the stated integral module and \(\chi_3\) formula.

**4. Signed Lefschetz calculation.** For a simplicial automorphism \(g\), the trace on the degree-\(j\) chain group is the sum of \(\operatorname{sgn}(g|_\sigma)\) over its fixed \(j\)-simplices. Euler–Poincaré in its equivariant form identifies the alternating chain trace with the alternating homology trace. Because \(H_0(K;\mathbb Q)\) is the trivial module, \(H_1(K;\mathbb Q)=0\), and all homology above dimension three vanishes,
\[
 L(g)=1+\chi_2(g)-\chi_3(g).
\]
Solving yields the exact formula in the theorem. Exhaustive enumeration of the \(96\) graph automorphisms and the \(248\) nonempty simplices gives precisely the seven stated character pairs and multiplicities. The verifier tests both the signed face formula and the actual integral action on the sphere cycles, with no appeal to floating point approximations.

**5. Invariants, irreducibles and the quotient.** Character averaging gives
\[
 \frac1{96}\sum_g\chi_2(g)=0,\quad
 \frac1{96}\sum_g\chi_3(g)=1,\quad
 \frac1{96}\sum_g\chi_2(g)^2=3.
\]
The first two equal the dimensions of the invariant subspaces. The last is the complex character inner product with itself; as every irreducible multiplicity is a nonnegative integer, it equals three only if the module consists of three mutually nonisomorphic irreducibles, each with multiplicity one (or one irreducible of multiplicity \(\sqrt3\), impossible). For a finite group acting simplicially, rational homology of the orbit space agrees with invariant rational homology by exactness of averaging; this proves the stated quotient ranks. \(\square\)

## Verification

Run `python3 verify_symmetry.py` with standard Python 3 from this package directory. It constructs the graph, all graph distances, all scale-two simplices, the original mod-two boundary ranks and the two exact integral oriented sphere cycles. It **exhaustively enumerates** all \(96\) graph automorphisms through distance-preserving backtracking, checks adjacency on every pair for every enumerated element, computes their induced integral actions on both fundamental cycles, computes all signed fixed-face Lefschetz traces, and validates every multiplicity and character average. The packaged `symmetry_output.txt` is the stdout of the verifier and concludes `ALL_CHECKS_PASS`. These are exact finite computations; a full enumeration is a proof for this specific finite graph. Mathematical definitions and trace-to-homology reasoning are supplied above independently of any log.

## Relationship to prior work

The earlier complete graph-metric Rips filtration of the Möbius–Kantor graph (research record `7a962f4f-0505-4412-bbeb-c682c5a3f31d`) establishes its nonequivariant integral sphere-wedge homotopy type and persistence; the new theorem refines **only the group action** and symmetry quotient, which do not follow from homotopy ranks. A separate result `1c198fd64c4e` calculates cyclic symmetry on the graph's **ordinary independence-complex** homology; that is a different simplicial complex with different homology degrees and group action. A general hexagon-packing scale-two Rips theorem `70b9bc9b3abb` assumes pairwise edge-disjoint six-cycles, which this graph does not satisfy. Adamaszek's graph-power theorems provide foundational homotopy methods, not this finite full-group character. Knill's newer study of the Möbius–Kantor graph investigates graph symmetries and Lefschetz phenomena; a full-text comparison was not completed, so coverage by its unretrieved full text remains a residual risk. The characterization of the graph as an important symmetric configuration and the nonequivariant homotopy are **not** presented as original.

## Limitations

This is an exact result for the single scale-two vertex Rips complex of the specified graph. It neither classifies integral second-homology lattices as group modules nor constructs an equivariant homotopy equivalence. It does not classify other graph scales or generalized Petersen graphs, and it makes no claim about integral quotient torsion. Publication priority requires further human literature review, especially for inaccessible plausible symmetry sources; the present checks establish best-knowledge distinctness rather than absolute priority.

## References

1. Michał Adamaszek, “Clique complexes and graph powers,” arXiv:1104.0433 (first public submission 2011-04-03), *Israel Journal of Mathematics* 196 (2013), 295–319. https://arxiv.org/abs/1104.0433
2. Oliver Knill, “Remarks about the Moebius-Kantor graph,” arXiv:2605.30799 (first public submission 2026-05-29); accessible abstract only for the present comparison. https://arxiv.org/abs/2605.30799
3. “Complete Vietoris–Rips filtration of the Möbius–Kantor graph,” earlier research record `7a962f4f-0505-4412-bbeb-c682c5a3f31d`; previously established nonequivariant homotopy and persistence.
4. “Cyclic symmetry on Möbius–Kantor independence homology,” research record `1c198fd64c4e`; related graph, different complex.
5. “A hexagon-packing classification of scale-two graph Rips complexes,” research record `70b9bc9b3abb`; different six-cycle overlap hypothesis.
