# Antipodal fixed forests of complete graphs are graphic-matroid sphere wedges

## Finding
For each integer \(m\ge 2\), label the vertices of the complete graph \(K_{2m}\) by \((i,\epsilon)\), where \(i\in\{1,\ldots,m\}\) and \(\epsilon\in\{0,1\}\). Let \(\tau(i,\epsilon)=(i,1-\epsilon)\). Write \(\mathcal F(K_{2m})\) for its forest (graphic-matroid independence) simplicial complex.

Let \(G_m\) have vertices \(0,1,\ldots,m\), one edge joining \(0\) to each \(i\), and two distinct parallel edges joining every pair \(i,j\) with \(1\le i<j\le m\). The geometric fixed-point space admits a canonical PL homeomorphism
\[
 |\mathcal F(K_{2m})|^{\langle\tau\rangle}\cong_{\mathrm{PL}}|\mathcal F(G_m)|.
\]
Its complete reduced integral homology is free and concentrated in dimension \(m-1\). More precisely,
\[
 |\mathcal F(K_{2m})|^{\langle\tau\rangle}\simeq\bigvee^{b_m}S^{m-1},\quad
 b_m=(-1)^m m![z^m]\exp\!\left(\sum_{s\ge1}\frac{s^{s-2}(-2)^{s-1}(1-s)}{s!}z^s\right),
\]
where the labeled-tree count at \(s=1\) is interpreted as one. The first nontrivial values are \(b_2=2\), \(b_3=24\), \(b_4=396\), \(b_5=8480\), and \(b_6=224760\).

## Assumptions and scope
A face of a graph's forest complex is any subset of its **labeled edges** that contains no (multi)graph cycle; in particular two parallel edges form a cycle of length two. The full empty face is included in the combinatorial complex; geometric realization uses the usual nonaugmented convention. The fixed points are points of the **geometric realization**, not just invariant individual edge vertices. The conclusion concerns the prescribed involution with no fixed original vertices, and all \(m\ge2\).

## Proof
**Edge-orbit model.** The involution has precisely \(m^2\) orbits on the edges of \(K_{2m}\). For each \(i\) there is one fixed diameter edge joining \((i,0)\) to \((i,1)\). For each unordered pair \(i,j\), there are two length-two orbits: the two same-layer edges and the two cross-layer edges. Associate these respectively with the apex edge \(0i\) and the two distinguishable parallel edges \(ij\) of \(G_m\). On every invariant face, all edges of each orbit have equal barycentric coordinate; replacing the orbit by its barycenter yields the canonical affine identification between the fixed space and the geometric realization of the orbit-admissibility simplicial complex.

**Forest preservation, both directions.** Fix a set of chosen edge orbits, and let \(B\) be the corresponding signed multigraph on vertices \(1,\ldots,m\) using only the two-edge orbits; signs distinguish the two lifts. If \(B\) has a cycle (including a parallel-edge cycle), its two-sheet lift to \(K_{2m}\) has a closed lifted walk and therefore contains a cycle. If \(B\) is a forest, its lift is the disjoint union of two copies of each tree component: choose a layer for any root vertex and transport consistently along the unique tree paths. Adding each selected diameter orbit joins two corresponding copies of its tree component at one vertex. Thus the lifted graph stays acyclic if and only if *at most one* diameter is selected in each component of \(B\). These are precisely the conditions that \(B\), together with the corresponding apex edges \(0i\), be acyclic in \(G_m\). Therefore the orbit-admissibility complex is exactly \(\mathcal F(G_m)\), and the previously described affine maps are mutually inverse PL homeomorphisms.

**Homotopy.** The multigraph \(G_m\) is connected, has \(m+1\) vertices, and every edge lies on a cycle for \(m\ge2\). Its graphic matroid has rank \(m\) and no coloop. The standard shellability theorem for matroid independence complexes therefore makes its realization homotopy equivalent to a wedge of spheres in dimension \(m-1\), including possibly zero spheres; nonvanishing follows from the explicit count below.

**Exact count.** A forest using no apex edges is a forest \(B\) on \(m\) labels with each selected edge independently colored by one of two parallel-edge types. Every component of \(B\) of size \(s\) is one of \(s^{s-2}\) labeled trees, has \(2^{s-1}\) edge colorings, and can carry either no apex edge or a single apex edge at one of its \(s\) vertices. If \(t\) marks edges, its total component weight is \(s^{s-2}(2t)^{s-1}(1+s t)\). The labeled exponential formula yields the forest face polynomial
\[
 P_m(t)=\sum_{F\in\mathcal F(G_m)}t^{|F|}=m![z^m]\exp\!\left(\sum_{s\ge1}\frac{s^{s-2}(2t)^{s-1}(1+s t)}{s!}z^s\right).
\]
For the nonaugmented realization, reduced Euler characteristic is \(-P_m(-1)\). Equating this with \((-1)^{m-1}b_m\) proves the stated coefficient formula. The special singleton convention makes the component factor valid at \(s=1\), where the isolated base vertex may carry one apex edge.

## Verification
The standalone `proof/verify_antipodal.py` directly enumerates all subsets of edge-orbits in the original complete graph for \(m=1,2,3,4\), independently tests lifted acyclicity and multigraph acyclicity using union-find, and compares the full face vectors. The four tested instance sizes have \(2,16,512,65536\) orbit subsets. This confirms the identification in finite cases and the resulting top Betti values \(0,2,24,396\); the all-parameter theorem follows from the proof, not these finite checks. Run `python3 proof/verify_antipodal.py` to reproduce `proof/verify_output.txt` using only the Python standard library.

## Relationship to prior work
Shellability and homotopy concentration for general matroid independence complexes are prior mathematical facts, including the shelling theorem of Ardila, Castillo and Samper. The novel claim here is the explicit **geometric fixed-space** identification for the free vertex involution of the complete-graph forest complex, together with its derived all-parameter forest enumeration. Neither a generic matroid shellability statement nor the forest complex of a different graph determines which complete-graph edge orbits form a forest under this involution. The comparison is restricted to inspected and indexed sources; a mathematically equivalent formulation might appear elsewhere under the terminology of signed covering graphs or invariant spanning forests.

## Limitations
The theorem does not classify fixed spaces for arbitrary permutations, graph involutions with fixed original vertices, or the integral action of the residual symmetry group on the homology lattice. The displayed wedge equivalence need not be natural under every residual automorphism. Finite verification through \(m=4\) is only a cross-check, not a universal proof, and this finding has not received independent mathematical auditing.

## References
1. F. Ardila, F. Castillo, J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870 (first public version 2014-10-14); *Electronic Journal of Combinatorics* 23 (2016), P3.8, doi:10.37236/5042. In particular, the general independence-complex shellability theorem.
2. Classical Cayley labeled-tree enumeration and the labeled exponential formula, used as standard combinatorial results in the coefficient derivation.
