# Complete semi-cutting spectra of positively weighted cycles: a terminal-gap threshold and cyclotomic roots

## Finding

Let \(C_n\) be a labelled simple cycle, \(n\ge3\), whose edges have arbitrary strictly positive real lengths. Fix a terminal set \(T\subseteq V(C_n)\) with \(t=|T|\ge2\). List its terminals in cyclic order; let \(A_1,\ldots,A_t\) be the edge-disjoint clockwise arcs between consecutive terminals, with \(g_i=|E(A_i)|\ge1\), total length \(L_i>0\), and circumference \(L=\sum_{i=1}^t L_i\).

For a set of deleted edges \(F\), call it *semi-cutting* when \(d_{C_n\setminus F}(u,v)>d_{C_n}(u,v)\) for every distinct pair \(u,v\in T\), with infinite distance allowed. Count all such sets by number of deleted edges:
\[
\mathcal S_{C_n,T}(z)=\sum_{F\text{ semi-cutting}}z^{|F|}.
\]

There is at most one index \(j\) satisfying \(2L_j>L\). Let \(J=\{j\}\) in that case and \(J=\varnothing\) otherwise. Then **the full cardinality polynomial**, for every positive edge-length assignment and every terminal placement, is
\[
\boxed{\mathcal S_{C_n,T}(z)=
\left(\prod_{i\notin J}\big((1+z)^{g_i}-1\big)\right)
\left(\prod_{j\in J}(1+z)^{g_j}\right).}
\]
The sharp minimum deleted-edge count and number of minimum sets are
\[
\boxed{\min |F|=t-|J|,\qquad
\#\{F:\ |F|=t-|J|,\ F\text{ semi-cutting}\}=\prod_{i\notin J}g_i.}
\]
The minimum equals the universal lower bound \(t-1\) exactly when one terminal gap weighs strictly more than half the circumference. If no such gap exists, all minima separate every terminal from every other; otherwise all minima leave the two endpoints of the exceptional long gap connected by its intact arc, even though their original distance strictly increases.

Every complex zero of \(\mathcal S_{C_n,T}\) is either \(-1\) (with multiplicity \(g_j\) when \(J=\{j\}\)) or is of the form \(e^{2\pi i h/g_i}-1\) for an obligatory gap \(i\notin J\) and an integer \(0\le h<g_i\). Thus its roots lie on \(|z+1|=1\), except for a possible root at the center \(z=-1\). It is real-rooted exactly when \(g_i\le2\) for every obligatory gap. The sequence of its nonzero coefficients is log-concave and has no internal zeros.

## Assumptions and scope

All edge lengths are finite and strictly positive real numbers; deletion has unit **cardinality cost**, independent of the edge lengths used to define shortest paths. Vertices and edges are labelled; sets \(F\) are distinct by their selected edges. The metric is shortest-path length, not unweighted graph distance unless all lengths are one. A disconnected pair has distance \(+\infty\). The theorem covers every \(n\ge3\), every \(2\le t\le n\), and equal-length tie cases. In particular a gap with \(2L_i=L\) is obligatory, because its arc is itself a shortest terminal-terminal path.

## Proof

**Gap characterization.** The two simple paths between the endpoints of \(A_i\) have lengths \(L_i\) and \(L-L_i\). If \(2L_i\le L\), then \(A_i\) is one shortest path between those consecutive terminals, including equality. Therefore every semi-cutting \(F\) meets \(E(A_i)\). Conversely, assume \(F\) meets every arc with \(2L_i\le L\). Any simple path between two terminals on a cycle is a union of one or more consecutive entire terminal arcs. A shortest terminal-terminal path that avoided \(F\) could therefore use only arcs not in this obligatory family. Since all lengths are positive, at most one arc can have \(2L_j>L\); if such an arc exists, the path would have to be exactly \(A_j\). But this arc is longer than its complementary path and cannot be shortest. Hence every shortest terminal-terminal path meets \(F\), so deletion strictly increases all terminal-pair distances. This proves the if-and-only-if classification, including tied antipodal arcs.

**Enumeration and extremizers.** The \(t\) arcs partition the \(n\) edges. In an obligatory arc of \(g_i\) edges a nonempty subset must be deleted, giving \((1+z)^{g_i}-1\); in a unique nonobligatory arc every subset is permitted, giving \((1+z)^{g_j}\). Multiplying yields the polynomial. Its least degree is \(t-|J|\); to attain it one must choose exactly one edge in each obligatory arc and none in the exceptional arc. This yields the stated product count. If all arcs are obligatory, one deletion in each gap separates every pair of terminals. If a gap is exceptional, its endpoints remain connected through its untouched arc, demonstrating that a minimum semi-cutting set need not be a terminal multiway cut.

**Roots.** The equation \((1+z)^{g_i}=1\) has precisely the \(g_i\) roots \(z=e^{2\pi i h/g_i}-1\), counted with multiplicity. The optional factor gives \(z=-1\) with multiplicity \(g_j\). A root of unity is real precisely when it is \(1\) or \(-1\). For \(g_i\ge3\), at least one corresponding root is nonreal, whereas \(g_i\in\{1,2\}\) contributes only \(0\) or \(0,-2\). This proves the complete root geometry and the necessary-and-sufficient real-rootedness condition.

**Log-concavity.** Each sequence \(\big(\binom{g}{1},\ldots,\binom{g}{g}\big)\), obtained by removing the initial zero coefficient of \((1+z)^g-1\), is positive, gap-free and log-concave; the coefficient sequence of \((1+z)^g\) is likewise log-concave. Convolution preserves log-concavity for nonnegative gap-free sequences: indeed their bi-infinite Toeplitz matrices \(\big(a_{j-i}\big)\) have nonnegative \(2\times2\) minors because adjacent coefficient ratios are nonincreasing; convolution corresponds to matrix multiplication, and the Cauchy–Binet identity makes its \(2\times2\) minors nonnegative. Applying this finitely supported convolution fact to all gap factors proves log-concavity of the nonzero coefficient sequence, with no internal zeros.

## Verification

The standalone \(\texttt{verify.py}\) enumerates **edge deletions** and independently computes all terminal-pair distances after deletion, without using the proposed gap criterion in the success test. For every unweighted \(C_n\) with \(3\le n\le9\), it checks all terminal subsets of size at least two and every edge-deletion subset (340,304 tested terminal/deletion combinations). It also checks four deterministic, nonconstant positive integer length assignments for each \(3\le n\le8\), comparing 333,120 further combinations. The coefficient formulas, minimum size, and minimum-set multiplicities agree in all these cases. Additional coefficient/log-concavity tests cover a nonexhaustive selection through order \(100\). These finite tests are corroborative; the proof above handles all orders and all positive real weights.

For a concrete boundary transition, take \(C_6\) with terminals \(\{0,2,4\}\). With all unit lengths the three gaps each have two edges of total weight two, so \(\mathcal S=z^3(z+2)^3\) and eight minimum sets use three deletions. Assign the two edges of the gap from vertex \(0\) to vertex \(2\) length four each, and the other four edges length one each. The length totals become \(8,2,2\); then \(\mathcal S=(1+z)^2z^2(z+2)^2\) and four minimum sets use two deletions. At the exact equality boundary \(L_1=L/2\), the first gap is still obligatory.

## Relationship to prior work

Bosek, Serra and Vena, *Structural properties of semi-cutting sets* (first posted 2026-11-15, arXiv:2611.20287), introduce the terminal-distance notion, identify it with a shortest-path edge transversal, and prove the universal bound \(|F|\ge|T|-1\). Their inspected full preprint does not give a cycle terminal-gap criterion, full cardinality polynomial, weighted-cycle classification, cyclotomic root description or coefficient log-concavity. The present result supplies a family-wide equality characterization and complete enumeration, rather than a new proof of that general lower bound.

The older geodesic-transversal work of Manuel, Brešar and Klavžar (arXiv:2101.08042; published in *Applied Mathematics and Computation* 413 (2022), 126621) hits **maximal** geodesics by **vertices**, rather than all shortest paths between a prescribed terminal set by **edges**. Published studies of geodesic transversals of cycles and of edge-geodesic transversals in other graph families therefore do not imply this exact marked-cycle spectrum merely by changing terminology. The search and comparison record, including historical-priority limitations, is in the accompanying review.

## Limitations

The classification applies to a single simple cycle with positive edge lengths and uniform deletion cardinality, not to arbitrary weighted graphs, directed graphs, negative lengths, or other deletion-cost objectives. Its log-concavity statement does not assert real-rootedness in general. Finite verification cannot establish the unrestricted theorem; its proof is combinatorial. No independent validation is asserted. Priority with respect to unindexed or inaccessible earlier work is provisional.

## References

1. Bartłomiej Bosek, Oriol Serra and Lluís Vena, *Structural properties of semi-cutting sets*, arXiv:2611.20287v1, first posted November 15, 2026, https://arxiv.org/abs/2611.20287 .
2. P. D. Manuel, B. Brešar and S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042 (2021), published in *Applied Mathematics and Computation* 413 (2022), article 126621, https://arxiv.org/abs/2101.08042 .
3. Sylvain Guillemot, *FPT algorithms for path-transversal and cycle-transversal problems*, *Discrete Optimization* 8 (2011), 61–71, https://doi.org/10.1016/j.disopt.2010.05.003 .
