# Complete integral Vietoris–Rips filtration of the Desargues incidence graph

## Finding
Let \(D\) be the twenty-vertex Desargues graph, realized as the bipartite inclusion graph on the two-element and three-element subsets of a fixed five-element set. Equip its vertex set with the shortest-path metric with unit-length graph edges. At each inclusive real threshold \(r\ge0\), its Vietoris–Rips complex has the following **integral homotopy type**:

\[
\operatorname{VR}_{\le r}(D)\simeq
\begin{cases}
\text{20 isolated vertices},&0\le r<1,\\
\bigvee^{11}S^1,&1\le r<2,\\
\bigvee^{19}S^2,&2\le r<3,\\
S^3,&3\le r<4,\\
S^9,&4\le r<5,\\
\ast,&r\ge5.
\end{cases}
\]

Consequently the complete reduced integral persistence barcode has nineteen degree-zero bars \([0,1)\), eleven degree-one bars \([1,2)\), nineteen degree-two bars \([2,3)\), one degree-three bar \([3,4)\), and one degree-nine bar \([4,5)\), with no other reduced bars. No torsion arises at any scale. This is a result about graph **vertices**, not all points of the continuously realized metric graph.

## Assumptions and scope
Fix \(U=\{0,1,2,3,4\}\), and let \(P\) and \(L\) be the respective sets of two-element and three-element subsets of \(U\). The vertices of \(D\) are the twenty members of \(P\sqcup L\); its graph edges are precisely \(A\sim B\) with \(A\in P\), \(B\in L\), and \(A\subset B\). This is the standard Desargues graph \(H(5,2)\), also isomorphic to \(GP(10,3)\), not the distinct ten-vertex graph sometimes called Desargues. Define \(\operatorname{VR}_{\le r}(D)\) to have precisely those nonempty vertex subsets whose every pair has graph distance at most \(r\). Homotopy equivalence concerns geometric realizations of finite simplicial complexes. The complex is unchanged between consecutive integer thresholds.

For reproducibility, enumerate \(P\), then \(L\), in the order given by increasing five-bit indicator masks, labeling the resulting vertices \(0,\dots,19\). A simplex is represented by a nonzero twenty-bit integer. The accompanying standard-library program is an executable exhaustive certificate for the two nontrivial Morse reductions.

## Proof
**1. Distances and the extreme thresholds.** The graph is bipartite, connected and three-regular, hence has twenty vertices and thirty edges. For distinct \(A,A'\in P\), their distance is two when they intersect and four when disjoint. For distinct \(B,B'\in L\), their distance is two when their intersection has size two and four when its size is one. For \(A\in P\), \(B\in L\), the distances are respectively one, three or five according as \(|A\cap B|\) is two, one or zero. These formulas follow by tracing alternating inclusions of two- and three-subsets; the checker independently verifies every one of the 190 unordered pairs by breadth-first search. There are exactly thirty, sixty, sixty, thirty and ten unordered vertex pairs at distances one through five. In particular the diameter is five.

At threshold zero there are twenty distinct points. At threshold one the Rips complex is exactly the connected bipartite graph, which has cycle rank \(30-20+1=11\), so it is a wedge of eleven circles. At threshold five the Rips complex is the full simplex, hence contractible. Exactly ten pairs are at distance five, namely each two-subset and its complementary three-subset. These ten pairs partition all twenty vertices. Thus the threshold-four Rips complex is the independence complex of a perfect matching, equivalently the join of ten zero-spheres, homeomorphic to \(S^9\). Its face vector is \((20,180,960,3360,8064,13440,15360,11520,5120,1024)\); the argument for its sphere type is direct and does not rely on computation.

**2. Complete finite face sets at thresholds two and three.** A subset is a face if and only if it is a clique in the graph joining vertices at distance at most the threshold. The verifier constructs the graph metric from the inclusion relation and produces faces by adding vertices in index order to earlier valid cliques. Independently, it examines all \(2^{20}\) twenty-bit masks, using the exact clique recursion: a mask is a face if and only if deleting its least set bit leaves a face and the deleted vertex is adjacent in the distance-power graph to every remaining vertex. The two complete enumerations agree, yielding respectively the following face vectors:
\[
\begin{aligned}
(f_0,f_1,f_2,f_3)_{r=2}&=(20,90,120,30),\\
(f_0,\ldots,f_6)_{r=3}&=(20,150,540,1000,960,450,80).
\end{aligned}
\]
There are respectively 260 and 3200 nonempty faces. All faces are included, without dimensional truncation or sampling.

**3. Explicit acyclic discrete-Morse reductions.** On each entire nonempty face set, begin with every face available. Process the pivot vertices in the fixed order \(0,1,\ldots,19\). At pivot \(v\), pair every still-available face \(\sigma\) not containing \(v\) with the still-available face \(\sigma\cup\{v\}\), whenever both are present, and remove the paired faces from availability. The program gives the exact procedure, including the deterministic mask ordering. Every pair consists of a face and one of its immediate cofaces and no face is reused.

For threshold two there are 120 matching pairs; precisely one critical vertex and nineteen critical two-dimensional faces remain. For threshold three there are 1599 pairs; precisely one critical vertex and one critical three-dimensional face remain. These counts alone do **not** certify acyclicity. Accordingly, for each threshold the verifier constructs the complete directed Hasse incidence graph, reversing each matched lower-to-upper incidence and orienting every other incidence downward. It checks all 660 (respectively 13,980) incidences and performs a complete topological sort of all 260 (respectively 3200) face-poset vertices. Both directed Hasse graphs are acyclic.

By the discrete Morse theorem, each complex is homotopy equivalent to a CW complex having exactly its listed critical cells. A CW complex with one zero-cell, no one-cells and nineteen two-cells is \(\bigvee^{19}S^2\); one with one zero-cell and one three-cell and no other cells is \(S^3\). These are **integral homotopy** conclusions; no inference from mod-two Betti numbers to integral homotopy is used. For additional independent diagnostics the program also calculates the full reduced mod-two homology of the same face sets, finding rank nineteen in degree two at threshold two and rank one in degree three at threshold three, and zero otherwise.

**4. Persistence.** These are the only nonzero reduced homology degrees at any of the six stages. All nonzero reduced classes at a given stage therefore die at the next integer threshold, and all classes present in a new positive degree are born there. Connectedness at threshold one kills nineteen reduced degree-zero classes. Thus the intervals are precisely those displayed in the finding, over the integers or any field. The filtration is finite and exhausts all scales because the graph distances are integers and the diameter is five. \(\square\)

## Verification
Run `python3 verify_desargues.py` using Python 3 and no third-party packages. The verifier constructs the graph from five-element subsets, independently checks all pair distances against the intersection-size formula, exhaustively validates all \(2^{20}\) possible vertex masks for each of the two nontrivial stages, recomputes both complete acyclic matchings, checks every Hasse incidence and confirms their directed acyclicity with a full topological sort. An exact binary boundary-matrix reduction independently checks the mod-two Betti vectors. It checks the remaining stages by elementary graph and cross-polytope identities. Successful output ends with `ALL_CHECKS_PASS`; `verification_output.txt` supplies the recorded output. Neither that log alone nor a finite-field homology calculation replaces the topological proof: the finite matching certificate and its complete acyclicity check are essential.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (first posted 2011-04-03, arXiv:1104.0433), particularly Proposition 2.2, proves collapse to the graph at scale two for girth at least seven. The Desargues graph has girth **six**, and its threshold-two complex is instead a wedge of nineteen two-spheres. That paper classifies powers of cycles, not the twenty-vertex Desargues graph. Adamaszek and Adams study the **entire hypercube** under Hamming distance, including a threshold-two wedge of three-spheres; the Desargues graph is the proper two-middle-layer induced subgraph of the five-cube, and its threshold-two two-sphere homotopy does not follow from the full hypercube theorem.

The published *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs* proves a two-sphere wedge for **projective planes**, whose two same-side vertices always have a common neighbor. The Desargues \((10_3)\) configuration is not a projective plane: disjoint two-subsets have graph distance four, and its incidence graph has diameter five rather than three. The published *Affine-plane incidence Rips complexes have two sphere dimensions* likewise requires affine-plane incidence axioms, absent here. The hexagon-packing theorem for girth-six graph Rips complexes requires every two simple six-cycles to be edge-disjoint; the Desargues graph has twenty distinct six-cycles, and each graph edge lies in four of them. None of those results implies the present classification.

A published calculation of a **Čech ball-intersection nerve** on the Desargues graph gives a wedge of forty-nine two-spheres at Čech scale three; the simplices are defined by ball intersections, not by pairwise distance, so it does not determine the Rips filtration. Results about its ordinary independence and matching complexes also have different face conditions. Parks and Marchette supply general graph-power persistence bounds but no detected exact Desargues filtration. Larrión, Pizaña and Villarroel-Flores compare fundamental groups of clique complexes of bipartite graph squares; they do not compute the higher integral homotopy or the remaining Rips stages.

## Limitations
The theorem concerns the specified finite graph, unit-edge **vertex** distances and inclusive threshold convention; it does not classify general bipartite Kneser graphs, arbitrary incidence configurations, metric realizations including edge interiors, or the automorphism action on homology. It supplies an exhaustive finite proof for the two exceptional stages, not a uniform structural theorem for a variable-size family. A covering unindexed thesis, computation or preprint cannot be excluded by the available searches; independent mathematical audit has not been performed. The output is not a formal proof-assistant artifact.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), especially Proposition 2.2 and Section 6.
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first public 2021-03-01), particularly Theorem 1.
3. A. D. Parks and D. J. Marchette, *Persistent homology in graph power filtrations*, *Royal Society Open Science* 3 (2016), 160228, DOI: 10.1098/rsos.160228.
4. F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *The fundamental group of the clique graph*, *European Journal of Combinatorics* 30 (2009), 288–294, DOI: 10.1016/j.ejc.2007.12.006.
5. *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, published mathematical result (2026).
6. *Affine-plane incidence Rips complexes have two sphere dimensions*, published mathematical result (2026).
7. *A hexagon-packing classification of scale-two graph Rips complexes*, published mathematical result (2026).
8. *Scale-three Čech nerve of the Desargues graph is a wedge of 49 two-spheres*, published mathematical result (2026).
9. *Desargues graph*, DistanceRegular.org, intersection array and bipartite-antipodal characterization (site last updated 2017-01-19).
