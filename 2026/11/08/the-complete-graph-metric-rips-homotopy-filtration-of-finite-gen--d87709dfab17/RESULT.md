# The complete graph-metric Rips homotopy filtration of finite generalized quadrangles

## Finding
Let \(\mathcal Q\) be any finite **thick** generalized quadrangle of order \((s,t)\), where \(s,t\ge2\), and let \(G\) be its bipartite point–line incidence graph with every edge of length one. Set \(b=(st)^2\) and let \(R_r=\operatorname{VR}_{\le r}(V(G))\) be its inclusive graph-metric Vietoris–Rips complex. The homotopy types at all integer thresholds are
\[
R_0\simeq\bigvee^{|V(G)|-1}S^0,\quad
R_1\simeq R_2\simeq\bigvee^b S^1,\quad
R_3\simeq\bigvee^{b^2}S^3,\quad
R_r\simeq\ast\quad(r\ge4).
\]
Here \(|V(G)|=(s+t+2)(st+1)\); the formula for \(R_0\) means \(|V(G)|\) isolated points, and \(\ast\) means a contractible complex. More strongly, \(R_2\) simplicially collapses **onto the naturally embedded graph** \(R_1=G\). At radius three there is an exact simplicial equality
\[
R_3=\operatorname{Cl}(\operatorname{Col}(\mathcal Q))*\operatorname{Cl}(\operatorname{Con}(\mathcal Q)),
\]
where \(\operatorname{Col}\) is the point-collinearity graph and \(\operatorname{Con}\) is the dual line-concurrence graph, each factor having homotopy type \(\bigvee^b S^1\).

Consequently, over the integers, the **complete positive-dimensional persistence barcode** is \(b\) copies of \([1,3)\) in dimension one and \(b^2\) copies of \([3,4)\) in dimension three, with no other positive-dimensional intervals or torsion. Reduced dimension-zero persistence consists of \(|V(G)|-1\) copies of \([0,1)\). These intervals refer to the **distance threshold** \(r\), not a convention in which the Rips radius is half the distance threshold.

## Assumptions and scope
A generalized quadrangle of order \((s,t)\) is a finite point–line incidence structure satisfying: each line contains exactly \(s+1\) points; each point lies on exactly \(t+1\) lines; any two distinct points are on at most one common line; and for every nonincident point \(p\) and line \(\ell\), exactly one point of \(\ell\) is collinear with \(p\). The dual properties hold by the same axioms. In particular its incidence graph is bipartite, connected, of girth eight and diameter four. The standard incidence count gives
\[
|P|=(s+1)(st+1),\qquad |L|=(t+1)(st+1),\qquad |E(G)|=(s+1)(t+1)(st+1).
\]
The theorem is conditional on the existence of the specified generalized quadrangle; it does not assert that all integer pairs \((s,t)\) are realized. The metric is the intrinsic unweighted graph metric, not a metric on any coordinate embedding.

## Proof
**1. Distance trichotomy and graph cycle rank.** A point \(p\) and a line \(\ell\) have distance one if incident and distance three otherwise: in the latter case, by the defining axiom, the unique point \(q\) on \(\ell\) collinear with \(p\) gives \(p\! -\! m\! -\! q\! -\!\ell\) for the unique line \(m\) through \(p,q\). Two distinct points have distance two exactly when collinear; if not, their distance is four, since for any line through the first, the axiom supplies a point on that line collinear with the second. The analogous statements hold for two lines. Thus the diameter is four. The graph is connected, so its first Betti number is
\[
|E(G)|-|P|-|L|+1=(st+1)(st-1)+1=(st)^2=b.
\]
As the graph is bipartite and triangle-free, \(R_1=G\).

**2. An explicit relative elementary collapse at distance two.** For every vertex \(v\) of \(G\), denote its open neighborhood by \(N(v)\). The full subcomplex on \(\{v\}\cup N(v)\) is a simplex \(B_v\) at distance threshold two. Every Rips-two clique is contained in some \(B_v\). For a clique containing only one bipartition class, any three pairwise distance-two vertices have one common neighbor: otherwise, their three pairwise connectors would give a six-cycle, contradicting girth eight; the same argument handles larger cliques. For a mixed clique, every cross-part pair must be incident; uniqueness of a line through two points forbids simultaneous inclusion of two or more vertices from both classes. It follows that all mixed cliques lie in an appropriate closed neighborhood. Moreover, every pair of vertices of distance two has exactly one common neighbor, because two common neighbors would produce a four-cycle.

For each \(v\), and in **decreasing order** of \(|S|\), take every \(S\subseteq N(v)\) with \(|S|\ge2\) and remove the pair of faces \(S\subset S\cup\{v\}\). This is an elementary collapse: the unique common-neighbor property ensures that all cofaces of \(S\) lie in the single simplex \(B_v\), and the larger cofaces have already been removed by earlier pairs. The pairs belonging to different centers cannot conflict, because a set of at least two mutually distance-two neighbors determines its center uniquely. After all these pairs, only vertices and original incidence edges remain, exactly \(G\). Thus \(R_2\searrow G\), with the embedding \(R_1\hookrightarrow R_2\) a homotopy equivalence and an integral first-homology isomorphism. The total number of elementary pairs is \(\sum_{v\in V(G)}(2^{\deg(v)}-\deg(v)-1)\).

**3. The exact join at threshold three.** All point–line pairs now have distance at most three. Within the point class, a pair has distance at most three exactly when its points are collinear; dually, two lines have distance at most three exactly when concurrent. Every cross pair being adjacent means the threshold-three flag complex is the full simplicial join of the two factor clique complexes, as displayed above. No information about nonincidence pairs is discarded in forming this join.

**4. Uniform collapse of both join factors.** Every clique of size at least two in the point-collinearity graph lies on a unique geometry line. The assertion for triples follows from girth eight: three pairwise-collinear points on three distinct connecting lines would form a forbidden incidence six-cycle. Larger cliques then follow from triples. Accordingly, the point-factor clique complex is the union of one simplex on the \(s+1\) points of each geometry line; distinct line simplices intersect in at most one vertex. In every such simplex choose a distinguished point \(c_\ell\); for every \(S\) among its other vertices with \(|S|\ge2\), remove \(S\subset S\cup\{c_\ell\}\) in descending cardinality. Each pair is free because simplices of different lines share no edge. The factor therefore collapses to a connected graph consisting of the \(s\) distinguished-point edges on each of the \(|L|\) lines. Its cycle rank is
\[
s|L|-|P|+1=s(t+1)(st+1)-(s+1)(st+1)+1=b.
\]
Connectivity follows from the point-collinearity graph's diameter at most two, and replacing each original line clique by a star does not disconnect the graph. Hence \(\operatorname{Cl}(\operatorname{Col}(\mathcal Q))\simeq\bigvee^b S^1\). Duality supplies a collapse of the line-concurrence factor onto a connected graph with \(t|P|\) edges and \(|L|\) vertices, likewise of cycle rank \(b\).

For connected based finite CW complexes, \(X*Y\simeq\Sigma(X\wedge Y)\), so the join of the two circle wedges has homotopy type \(\bigvee^{b^2}S^3\), proving the radius-three statement integrally. The diameter-four assertion makes \(R_4\) the full simplex, hence all later stages contractible.

**5. Persistence maps and endpoints.** The explicit relative collapse in step 2 shows that the \(b\) independent integral degree-one classes born when the incidence edges appear at threshold one persist without change through threshold two. The radius-three join is simply connected and has free integral homology only in degree three, so those degree-one classes die exactly at three, while its \(b^2\) degree-three classes are born there. They die at four because the full simplex appears. All maps between stages with vanishing positive-dimensional homology are necessarily zero. This proves all barcode multiplicities, boundaries and the claimed absence of other positive-dimensional classes; the inclusion of the connected graph at one also gives the reduced dimension-zero bars.

## Verification
The accompanying standalone `verify.py` uses Python's standard library to construct the classical symplectic generalized quadrangles \(W(2)\) and \(W(3)\) from four-dimensional alternating forms. It **independently** recomputes every graph distance, enumerates maximal cliques by Bron–Kerbosch, verifies that these equal the claimed neighborhood/line/pencil maximal simplices, checks **every elementary free-face removal** at radius two and for both radius-three factors, and reduces the independent simplicial boundary matrices over \(\mathbb F_2\). It confirms, respectively, \(b=16,81\) and \(b^2=256,6561\). Run `python3 verify.py`; the exact recorded output is in `verify_output.txt`. These are finite stress tests; the proof above is unconditional over all existing finite thick generalized quadrangles and is not inferred from the tested cases. The code does not compute the full radius-three boundary matrices, whose homotopy type is established by the explicit join proof.

## Relationship to prior work
McCabe (2026, arXiv:2607.06524), §3.1, uses incidence graphs of generalized polygons to derive lower bounds on approximation sizes. His Lemma 3.5 (based on Adamaszek's graph-power theorem) establishes homotopy invariance through distance scale two for girth-eight incidence graphs, but does not classify the scale-three complex or any dimension-three persistence interval. Cioabă–Guo–Ji–Mim (first public 2025, arXiv:2508.05871), §3, describe the simplices of generalized-quadrangle point-graph clique complexes and compute higher Laplacian spectra; they do not identify the incidence-graph scale-three join or the complete filtration. A prior concrete computation classifies the scale-three Rips complex for the Tutte–Coxeter graph, namely \(\mathrm{GQ}(2,2)\), as \(256\) three-spheres; this is precisely the \(s=t=2\) specialization of the present all-orders statement. Its original statement is restricted to that graph and does not assert the arbitrary-parameter theorem. The present theorem supplies a uniform proof and the full integral barcode for all existing finite thick quadrangles, including nonsymmetric and nonclassical cases. The comparison does not assert that differently phrased, unindexed prior results cannot exist.

## Limitations
This is a nonequivariant homotopy classification, not a determination of automorphism representations on homology. Only finite **thick generalized quadrangles** with their incidence-graph shortest-path metric are covered. The result is not asserted for arbitrary bipartite girth-eight graphs, weighted metrics, generalized hexagons, or nonexisting parameter pairs. The barcode uses the distance-threshold convention; some literature parametrizes Vietoris–Rips complexes by half that threshold. Independent external audit has not been performed.

## References
1. K. McCabe, *Lower Bounds for Approximating the Vietoris-Rips Filtration*, arXiv:2607.06524, first posted 2026-07-07, https://arxiv.org/abs/2607.06524 (especially §3.1 and Lemma 3.5).
2. S. M. Cioabă, K. Guo, C. Ji, and M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, arXiv:2508.05871, first posted 2025-08-07, https://arxiv.org/abs/2508.05871 (especially §3, Lemma 3.2).
3. M. Adamaszek, *Clique complexes and graph powers*, Israel J. Math. 196 (2013), 295–319; arXiv:1104.0433, https://arxiv.org/abs/1104.0433.
4. *The scale-\(3\) Rips complex of the Tutte–Coxeter graph is a wedge of \(256\) three-spheres*, publicly available original result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-scale-3-rips-complex-of-the-tutte-coxeter-graph-is-a-wedge-o--9454ecd0bd54 (special case only).
