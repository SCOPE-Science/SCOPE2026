# Integral homotopy of the five-by-five periodic triangular hard-hexagon complex

## Finding
Let \(T\) be the simple graph with vertices \(V=(\mathbb Z/5\mathbb Z)^2\) and edges whenever the difference of endpoints is in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\). Its independence complex \(K=\operatorname{Ind}(T)\), consisting of all subsets without adjacent vertices, has the integral homotopy type
\[
K\simeq\bigvee^{51}S^3\vee\bigvee^{15}S^4.
\]
In particular its only nonzero reduced integral homology groups are \(\widetilde H_3(K;\mathbb Z)=\mathbb Z^{51}\) and \(\widetilde H_4(K;\mathbb Z)=\mathbb Z^{15}\). The two rational Betti numbers were already obtained in the ground-state calculation of Huijse–Mehta–Moran–Schoutens–Vala, and are not presented as new: the new assertion is the exact **integral homotopy decomposition**.

## Assumptions and scope
All coordinates and graph differences are reduced modulo five. Number vertices lexicographically as \(v=5i+j\) for \(0\le i,j<5\), and order faces by the induced increasing vertex order. The graph is simple, undirected, and six-regular. All topology is for the **ordinary** (not directed or weighted) independence complex. Its largest simplices have seven vertices, and the face counts in dimensions \(0,\ldots,6\) are
\[
(25,225,900,1600,1140,300,25).
\]
These are exactly the 4,215 nonempty simplices; the empty simplex is separately included when computing reduced chains. No assertion is made for arbitrary sizes or boundary twists.

## Proof
**(1) Exhaustive face enumeration.** A face is encoded by a 25-bit mask. Extend each independent subset by increasing vertex labels whenever the new vertex has no occupied neighbor; the resulting simplicial face set has 4,216 masks including the empty mask. Independently, enumerate independent five-cycle patterns in each row and retain five-tuples for which adjacent rows, including the wraparound pair, avoid vertical and diagonal conflicts. The two enumerated sets agree exactly.

**(2) A complete acyclic matching.** Start with all 4,215 nonempty faces still unmatched. For each vertex \(v=0,1,\ldots,24\) in order, pair every remaining face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both remain; remove each paired pair from the remaining set. This deterministically gives 2,074 matched covering pairs and critical faces numbering one in dimension zero, 51 in dimension three and 15 in dimension four. To verify acyclicity, orient **all** covering relations in the Hasse diagram up on matched pairs and down on every other covering relation. There are exactly 17,225 relations, and Kahn topological sorting visits all 4,215 vertices of this directed graph, proving it contains no directed cycle. Discrete-Morse theory therefore produces a CW complex homotopy equivalent to \(K\) with the indicated cells and no others.

**(3) Integral attaching coefficients.** Use the conventional signed simplicial boundary on faces with vertices in increasing order. For every three-face \(\tau\), define an integral projection \(P(\tau)\) onto the free abelian group on the 51 critical three-faces. A critical three-face projects to itself. A three-face matched **as an upper face** to a two-face projects to zero. If a three-face \(\tau\) is matched **as a lower face** to a four-face \(\rho\), let \(\epsilon(\rho,\eta)\in\{\pm1\}\) be the incidence sign of the facet \(\eta\) in \(\partial\rho\), and define
\[
P(\tau)=-\epsilon(\rho,\tau)\sum_{\eta\subset\rho,\,|\eta|=4,\,\eta\ne\tau}\epsilon(\rho,\eta)P(\eta).
\]
The acyclic matching makes this elimination well-founded. The 51-by-15 matrix whose columns are \(P(\partial\rho)\) for the critical four-faces \(\rho\), with all signs retained, is **identically zero**. The standalone verifier constructs the actual 765 entries and tests every one.

**(4) Homotopy conclusion.** The Morse CW complex has exactly one zero-cell and no cells of dimensions one or two; its three-skeleton is \(\bigvee^{51}S^3\). Each four-cell is attached along a map \(S^3\to\bigvee^{51}S^3\). The Hurewicz isomorphism \(\pi_3(\bigvee^{51}S^3)\cong H_3(\bigvee^{51}S^3;\mathbb Z)\) identifies each attaching map with its integral degree column, which is zero by step (3). Hence all 15 attaching maps are nullhomotopic, and their attachments split as 15 extra four-sphere summands. This proves the claimed **homotopy equivalence**, not merely an equality of Betti numbers.

## Verification
Run the accompanying `verify.py` using Python 3 and only the standard library. It independently enumerates faces by two methods, constructs the matching, checks every Hasse relation, computes the complete signed integral Morse boundary, and separately computes simplicial boundary ranks over \(\mathbb F_2\). The recorded `verification_output.txt` is the actual output of this program. The independent mod-two ranks in degrees one through six are \((24,201,699,850,275,25)\), yielding homology dimensions \((1,0,0,51,15,0,0)\) in degrees zero through six. The mod-two check alone cannot prove integral homotopy; the essential additional evidence is the complete acyclic matching and the signed zero matrix.

## Relationship to prior work
Huijse, Mehta, Moran, Schoutens and Vala [1], Section II and Appendix B.4, study the **same** fully periodic five-by-five triangular lattice and give the known 66 supersymmetric ground states, split as 51 and 15 in adjacent particle-number sectors (their Witten index is 36). The standard independence-complex/fermion-cohomology correspondence identifies these with the rational homology ranks in the two degrees above. Thus neither those ranks nor the 66 total are claimed as new. Their calculation gives no integral attaching-map certificate or homotopy equivalence of \(K\) to a wedge of spheres. Jonsson [2], Section 6, constructs homology cross-cycles for triangular grids but does not identify this full homotopy type. Adamaszek [3] studies special lattice cycles and related lattice families rather than the exact five-by-five triangular-torus integral homotopy type. Relevant previously indexed square-grid, hypercube and other graph-complex calculations concern different graphs or different complexes.

## Limitations
The result concerns one 25-vertex graph and proves only its ordinary, nonequivariant integral homotopy type. It does not determine symmetry representations, larger tori, torsion in other lattice sizes, or a canonical equivariant wedge decomposition. Previously reported rational Betti numbers are acknowledged as known. The computational proof is finite and fully enumerates the stated complex; no inference about the infinite triangular lattice is made. Equivalent previously unindexed work remains a publication-priority risk. Independent mathematical review has not been performed.

## References
[1] L. Huijse, D. Mehta, N. Moran, K. Schoutens, J. Vala, *Supersymmetric lattice fermions on the triangular lattice: superfrustration and criticality*, first public arXiv posting December 14, 2011, arXiv:1112.3314, Section II and Appendix B.4. https://arxiv.org/abs/1112.3314

[2] J. Jonsson, *Certain Homology Cycles of the Independence Complex of Grid Graphs*, *Discrete & Computational Geometry* 43 (2010), 927–950, especially Section 6. Author-hosted full text: https://people.kth.se/~jakobj/doc/papers/crosstorus.pdf

[3] M. Adamaszek, *Special cycles in independence complexes and superfrustration in some lattices*, first public arXiv posting September 22, 2011, arXiv:1109.4914. https://arxiv.org/abs/1109.4914
