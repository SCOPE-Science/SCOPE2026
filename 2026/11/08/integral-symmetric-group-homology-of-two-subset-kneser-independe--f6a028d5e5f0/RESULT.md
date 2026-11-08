# Integral symmetric-group homology of two-subset Kneser independence complexes

## Finding
For every integer \(n\ge4\), let \(G_n=\operatorname{KG}(n,2)\) be the Kneser graph whose vertices are two-element subsets of \([n]\), with edges between disjoint two-subsets. Let \(X_n=\operatorname{Ind}(G_n)\), so its faces are the pairwise-intersecting families of two-subsets. Write \(E_n=\mathbb Z^{[n]}\) and \(L_n=\ker(\varepsilon:E_n\to\mathbb Z)\), where \(\varepsilon(e_i)=1\).

The relabeling action of \(S_n\) on \(X_n\) has the following complete **integral** reduced homology classification:
\[
\widetilde H_j(X_n;\mathbb Z)\cong
\begin{cases}
\bigwedge^{3}L_n,&j=2,\\
0,&j\ne2.
\end{cases}
\]
The isomorphism is natural for every permutation of \([n]\), not just an abstract isomorphism of abelian groups. In particular, \(\widetilde H_2(X_n;\mathbb Z)\) is torsion-free of rank \(\binom{n-1}{3}\). On rationalizing, it is the irreducible hook Specht module \(S^{(n-3,1,1,1)}\). If a permutation \(g\) has \(f\) fixed points, \(t\) two-cycles and \(u\) three-cycles, its trace is
\[
\operatorname{tr}(g\mid\widetilde H_2(X_n;\mathbb Q))
=\binom f3-ft+u-\binom f2+t+f-1.
\]
Thus no nonzero rational class survives all \(S_n\) relabelings. This complex is exactly the nonmatching complex \(\mathsf{NM}_2(n)\) of Linusson–Shareshian–Welker (2004). Its nonequivariant wedge-of-two-spheres classification is not new here. The integral \(S_n\)-module answers the two-edge-matching case of their explicit Question 1.13 on equivariant homology.

## Assumptions and scope
Graphs are finite simple graphs. Simplicial faces are nonempty independent vertex subsets, with the empty simplex used in reduced chain conventions. \(n\) is an arbitrary integer at least four. All group actions are induced by permuting the labels \([n]\); the theorem makes no assertion about other graph automorphisms for \(n=4\). The orientation convention on the exceptional triangle associated to distinct \(i,j,k\) is the ordered vertex list \((\{i,j\},\{j,k\},\{k,i\})\). All homology coefficients in the main claim are integral.

## Proof
**1. Exhaustive structural classification of faces.** Regard each Kneser vertex as an edge of the complete graph on \([n]\). A family of edges is independent in \(G_n\) exactly when every two edges intersect. If it contains two distinct edges \(\{a,b\}\) and \(\{a,c\}\), any further edge either contains \(a\) or equals \(\{b,c\}\). In the latter case any fourth distinct edge cannot intersect all three. Therefore every face is contained in one of the following: a full star simplex \(\Sigma_i=\{\{i,j\}:j\ne i\}\), or a triangle \(T_{ijk}=\{\{i,j\},\{j,k\},\{k,i\}\}\). For \(n\ge4\), the latter triangle does not lie in any \(\Sigma_i\), and its entire boundary does.

**2. The star subcomplex.** Put \(U_n=\bigcup_i\Sigma_i\). Each \(\Sigma_i\) is a simplex and \(\Sigma_i\cap\Sigma_j\) is the single vertex \(\{i,j\}\); every triple intersection is empty. Inside each geometrically realized simplex join its barycenter \(b_i\) to its vertices \(\{i,j\}\). Their union is a graph \(T_n\) isomorphic to a barycentric subdivision of the complete graph on \([n]\). The inclusion \(T_n\hookrightarrow U_n\) is an \(S_n\)-equivariant homotopy equivalence on underlying spaces: build the union one star simplex at a time, using the gluing theorem since its radial tree and full simplex are contractible and attach along the same discrete boundary vertices. The map and the induced integral homology isomorphism commute with relabeling. Thus \(H_j(U_n;\mathbb Z)=0\) for \(j\ge2\), and \(H_1(U_n;\mathbb Z)\) is the integral cycle lattice of \(K_n\).

**3. Relative attachment, with all signs.** The only simplices of \(X_n\setminus U_n\) are the interiors of the \(\binom n3\) triangles \(T_{ijk}\), so \(C_j(X_n,U_n)=0\) for \(j\ne2\). Its relative two-chain group has the canonical \(S_n\)-equivariant orientation identification
\[
C_2(X_n,U_n;\mathbb Z)\cong\bigwedge^3E_n,\qquad
e_i\wedge e_j\wedge e_k\longmapsto[\{i,j\},\{j,k\},\{k,i\}].
\]
An interchange of two ground labels interchanges two triangle vertices and therefore introduces the required exterior sign. Each edge of the triangle boundary is contained in the corresponding star simplex and, through the radial graph, represents the path through that star's barycenter. Therefore the connecting map \(\delta:C_2(X_n,U_n)\to H_1(U_n)\) is **exactly** the ordinary oriented triangular boundary
\[
\partial_2(e_i\wedge e_j\wedge e_k)=
e_j\wedge e_k-e_i\wedge e_k+e_i\wedge e_j
\]
in the complete-graph cycle lattice \(\ker(\partial_1:\bigwedge^2E_n\to E_n)\), where \(\partial_1(e_i\wedge e_j)=e_j-e_i\). These identifications are integral and \(S_n\)-equivariant.

**4. Integral surjectivity, kernel and degrees.** For \(2\le i<j\le n\), the triangles \(\partial_2(e_1\wedge e_i\wedge e_j)\) form an integral basis of \(H_1(K_n;\mathbb Z)\): with a spanning tree of edges incident to label one, their coefficients on the remaining chord edges form an identity matrix. In particular, \(\delta\) is surjective integrally. The long exact sequence of the pair gives \(\widetilde H_1(X_n)=0\), \(H_2(X_n)=\ker\partial_2\), and no higher reduced homology. As \(\partial_2\) equals contraction by \(\varepsilon\), the splitting \(E_n=\mathbb Ze_1\oplus L_n\) gives
\[
\bigwedge^3E_n=(e_1\wedge\bigwedge^2 L_n)\oplus\bigwedge^3 L_n,
\qquad \ker\partial_2=\bigwedge^3L_n.
\]
The kernel sublattice and its identification with \(\bigwedge^3L_n\) are canonical, even though a splitting was used to verify the equality. This proves the complete integral assertion for every \(n\ge4\).

**5. Character and irreducibility.** The permutation module \(E_n\otimes\mathbb Q\) is \(\mathbf1\oplus L_n\otimes\mathbb Q\), so
\[
\sum_{r\ge0}\operatorname{tr}(g\mid\bigwedge^rL_n\otimes\mathbb Q)z^r
=\frac{\prod_{\ell\ge1}(1-(-z)^\ell)^{c_\ell(g)}}{1+z}.
\]
Its cubic coefficient is the stated expression in the counts of one-, two-, and three-cycles. The standard representation-theoretic identity \(\bigwedge^3(L_n\otimes\mathbb Q)\cong S^{(n-3,1,1,1)}\) gives irreducibility and the absence of invariant vectors.

## Verification
The standalone file `verify_kneser.py` enumerates every face independently from the star-and-triangle description, then computes the signed simplicial Lefschetz sum of every permutation of \([n]\) for \(n=4,5,6,7\). All \(5{,}904\) group actions match the character formula. It also performs direct simplicial boundary-rank calculations modulo two and three, checks that each oriented triangle boundary is a graph cycle, checks that the spanning-tree fundamental-cycle matrix has an identity chord minor, and verifies that the face-vector Euler characteristic equals \(1+\binom{n-1}{3}\). Run with `python3 verify_kneser.py`; the exact recorded output is in `verify_kneser.out`. The general theorem is established by the preceding uniform integral argument; these finite checks are not a substitute for it.

## Relationship to prior work
The 2004 preprint of Linusson, Shareshian and Welker, *Complexes of graphs with bounded matching size* (arXiv:math/0410345), defines \(\mathsf{NM}_k(n)\) to consist of graphs with no matching of size \(k\). **Exactly the same object** as \(X_n\) occurs when \(k=2\): pairwise-intersecting edge sets are the faces. Their Theorem 1.1 already establishes the nonequivariant homotopy type \(\bigvee^{\binom{n-1}{3}} S^2\), and Question 1.13 explicitly asks for the \(S_n\)-module structure of \(\widetilde H_{3k-4}(\mathsf{NM}_k(n))\). The contribution here answers that question **for the natural case \(k=2\)**, determining the complete integral module as well as its rational irreducible character. Their Section 4.1 matching-theoretic Morse argument computes the wedge count but does not identify this integral symmetric-group module. Their nearby Theorem 1.11 and Conjecture 1.12 refer instead to the no-perfect-matching specialization, not to a uniform equivariant result for \(\mathsf{NM}_2(n)\) for all \(n\).

Barmak's 2010 preprint, Theorem 4.11, provides another nonequivariant proof of the same \(\operatorname{Ind}(\operatorname{KG}(n,2))\) sphere wedge, using a star cluster depending on a distinguished label. Braun's stable-Kneser complexes use a proper cyclically restricted vertex set. Feng–Wang's later work treats higher subset sizes; the 2026 triple-subset calculation also has a distinct degree pattern. Related indexed studies of Kneser *open-neighborhood* and Čech complexes concern different simplicial objects. The exterior-power chain differential is classical; the claim here is its **natural integral equivariant realization** for this graph complex, beyond the published 2004 nonequivariant result. No claim is made to solve Question 1.13 for \(k>2\).

## Limitations
The claim does not determine an equivariant homotopy type or the classification for Kneser graphs on subsets larger than two. For \(n=4\), the natural \(S_4\) relabeling group need not be the full automorphism group of the disconnected Kneser graph. The corresponding rational Specht module does not by itself determine the integral lattice; the integral construction is essential. No independent mathematical audit or definitive global publication-priority assessment is asserted. A non-indexed equivariant treatment of the same object could cover the result.

## References
1. S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345 (first posted 2004-10-15), Theorem 1.1, Question 1.13 and Section 4.1. https://arxiv.org/abs/math/0410345
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418 (first submitted 2010-07-02); Advances in Mathematics 241 (2013), Theorem 4.11. https://arxiv.org/abs/1007.0418
3. B. Braun, *Independence Complexes of Stable Kneser Graphs*, Electronic Journal of Combinatorics 18 (2011), P118. DOI:10.37236/605.
4. Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566 (2024), on larger subset sizes.
5. Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394 (2026), on three-subset graphs.
