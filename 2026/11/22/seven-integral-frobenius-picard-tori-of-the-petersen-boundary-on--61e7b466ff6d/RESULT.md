# Seven integral Frobenius Picard tori of the Petersen boundary on quintic del Pezzo surfaces

## Finding
Let \(S\) be any smooth degree-five del Pezzo surface over \(k=\mathbb F_q\), in any characteristic, and let \(D\) be the reduced \(k\)-divisor comprising **all ten geometric exceptional curves**. Its connected Picard scheme \(T=\operatorname{Pic}^0(D)\) is a six-dimensional torus. The complete *integral isomorphism type* of \(T\), not merely its isogeny class or point count, depends only on the cycle type of geometric Frobenius in the classical \(S_5\)-action on the ten lines.

Write \(R_d=\operatorname{Res}_{\mathbb F_{q^d}/k}\mathbb G_m\) and
\[
N_2=\ker\bigl(N_{\mathbb F_{q^2}/k}:R_2\to\mathbb G_m\bigr),\quad
N_4=\operatorname{Res}_{\mathbb F_{q^2}/k}\ker\bigl(N_{\mathbb F_{q^4}/\mathbb F_{q^2}}:\operatorname{Res}_{\mathbb F_{q^4}/\mathbb F_{q^2}}\mathbb G_m\to\mathbb G_m\bigr).
\]
For \(C_m\) denoting an abstract cyclic group of order \(m\), all seven possibilities are:

| Frobenius type | Exact torus over \(k\) | \(T(k)\) as an abstract finite abelian group |
|---|---|---|
| \((1,1,1,1,1)\) | \(\mathbb G_m^6\) | \(C_{q-1}^{6}\) |
| \((2,1,1,1)\) | \(R_2^3\) | \(C_{q^2-1}^{3}\) |
| \((2,2,1)\) | \(R_2^2\times N_2^2\) | \(C_{q^2-1}^{2}\times C_{q+1}^{2}\) |
| \((3,1,1)\) | \(R_3^2\) | \(C_{q^3-1}^{2}\) |
| \((3,2)\) | \(R_6\) | \(C_{q^6-1}\) |
| \((4,1)\) | \(R_4\times N_4\) | \(C_{q^4-1}\times C_{q^2+1}\) |
| \((5)\) | \(R_5\times\mathbb G_m\) | \(C_{q^5-1}\times C_{q-1}\) |

These are **integral** identifications of Galois character modules and therefore isomorphisms of algebraic tori; in particular the quadratic norm-one factors must not be replaced by split factors based only on rational character identities. Every type is realizable over every finite field by the known twist classification of degree-five del Pezzo surfaces.

## Assumptions and scope
The field is finite of arbitrary characteristic, and the surface is geometrically smooth with \(K_S^2=5\). The divisor is the entire reduced ten-curve boundary, not an anticanonical pentagon of five components or a union of exceptional curves on a surface of a different degree. The ten geometric components are smooth rational curves, intersect pairwise transversely where they meet, and have no triple intersections. The dual graph is the Petersen Kneser graph on the two-element subsets of a five-element set; it has ten vertices and fifteen edges. Thus the arithmetic genus of \(D\) is \(15-10+1=6\). Individual components and nodes need not be \(k\)-rational. The formulas classify the *connected* Picard group, not the multidegree component group of the full Picard functor or the Picard group of \(S\).

## Proof
**1. Geometry and torus character lattice.** The classical degree-five del Pezzo identification labels the ten exceptional curves by two-element subsets of \(\{0,1,2,3,4\}\); two curves meet exactly when their labels are disjoint. Since the graph has no triangles, the fifteen intersections are distinct ordinary nodes. Every geometric component normalizes to \(\mathbb P^1\), hence its connected Picard variety is trivial. The normalization-gluing exact sequence for a nodal curve identifies the character lattice of its connected Picard torus with
\[
X^*(T_{\bar k})=H_1(P,\mathbb Z)=\ker(\partial:\mathbb Z^{E(P)}\to\mathbb Z^{V(P)}),
\]
including the *signed* edge-orientation action. The rank is six. Frobenius acts through the natural permutation group \(S_5\) on the five labels; the Galois action on \(H_1\) is obtained by restricting this signed graph action to a representative of its conjugacy class.

**2. Integral, not merely rational, cyclic blocks.** Order graph vertices lexicographically as two-subsets and orient each edge from smaller to larger vertex index. Order the fifteen edges lexicographically. Choose the nine-edge spanning tree with oriented endpoints
\[
(0,7),(0,8),(0,9),(1,5),(1,6),(1,9),(2,4),(2,6),(3,4),
\]
where these numbers are **zero-based indices** in the ordered vertex list. The remaining six edges are chords. For each chord, take the integral fundamental cycle whose chord coefficient is \(+1\). These six cycles are an integral basis of \(H_1(P,\mathbb Z)\), because every cycle is uniquely determined by its chord coefficients.

For each of the seven ordered cycle-type representatives \(\sigma\in S_5\), compute the exact six-by-six signed action matrix \(M_\sigma\) in this fundamental-cycle basis. Define a positive integer \(d\)-block \(P_d\) as the permutation matrix of a single \(d\)-cycle, define \(P_{-1}=(-1)\), and define \(P_{-2}=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\). The explicit integer matrices \(U_\sigma\) in `verification/certificates.json` satisfy, in every case,
\[
\det U_\sigma=\pm1,\qquad M_\sigma U_\sigma=U_\sigma B_\sigma,
\]
where the blocks of \(B_\sigma\), in the table's order, are
\[
(1,1,1,1,1,1),\ (2,2,2),\ (2,2,-1,-1),\ (3,3),\ (6),\ (4,-2),\ (5,1).
\]
The complete certificate reconstructs the graph, the fundamental cycles, all edge signs, and the signed action; it independently checks each determinant and all 36 entries of each conjugacy identity. It additionally checks the graph-action matrices for all \(120\) permutations and verifies that the seven conjugacy classes have respective sizes \(1,10,15,20,20,30,24\). Because integral conjugacy is preserved on replacing a permutation by a conjugate, this covers *every* possible Frobenius action, not merely seven numerical examples.

**3. Descent and exact groups.** Under the contravariant equivalence between \(k\)-tori and finite-rank integral continuous Galois lattices, a positive cyclic block \(P_d\) is the character lattice of \(R_d\). The one-dimensional block \(P_{-1}\) is the character lattice of \(N_2\). The signed two-cycle block \(P_{-2}\) is the character lattice of \(N_4\): over \(\mathbb F_{q^2}\), it becomes a pair of one-dimensional sign blocks, exchanged by the degree-two descent. Hence the displayed integral block decompositions prove all seven torus isomorphisms. Lang's theorem and the standard finite-field norm map give \(R_d(k)=\mathbb F_{q^d}^{\times}\cong C_{q^d-1}\), \(N_2(k)\cong C_{q+1}\), and \(N_4(k)\cong C_{q^2+1}\). Taking products gives all seven finite abelian group descriptions.

## Verification
Run `python3 verification/verify.py` using Python 3 with no third-party dependencies. The checker reads `verification/certificates.json`, constructs all ten graph vertices and fifteen edges, checks that the stated tree supports an exact fundamental-cycle lattice, verifies the action of every element of \(S_5\), and establishes the seven explicit integer conjugacies and their unimodularity by exact Bareiss determinants. It also compares \(\det(qI-M_\sigma)\) with the claimed rational-point-group orders for seven small prime powers. The actual packaged `verification/verification_output.txt` ends in `PETERSEN_SEVEN_INTEGRAL_TORUS_TYPES_OK`. The finite arithmetic verification is an exhaustive certificate of the only nonstandard finite-lattice step; it does not substitute sample field counts for the general descent proof.

## Relationship to prior work
Roulleau (2010), González-Sánchez–Harrison–Polo-Blanco–Schicho (2010), and later del Pezzo twist classifications establish the classical ten-curve Petersen configuration and the seven Frobenius conjugacy classes. They do not provide the full seven-fold **integral** Galois-lattice decomposition of the connected Picard torus of the complete nodal boundary.

The closest published published-finding corpus calculation, *A primitive index-two map from the exterior-square root lattice to the Petersen generalized-Jacobian lattice*, computes an integral **full-\(S_5\)** equivariant embedding \(\bigwedge^2A_4\hookrightarrow H_1(P,\mathbb Z)\) and its degree-two isogeny of tori. That is a different assertion: neither rational representation equivalence nor a degree-two isogeny determines integral isomorphism types for **each cyclic Frobenius restriction**. The full text explicitly does not classify individual twist forms. *Integral Frobenius trace lattices and arithmetic cones of degree-five del Pezzo surfaces* classifies the **surface** Picard invariant sublattices and cone rays, not this connected Picard torus. *Motivic collapse of the four Frobenius types of pentagon-boundary degree-five del Pezzo surfaces* concerns only a five-curve anticanonical pentagon and its open complement, not the ten-curve graph. The all-degree quintic twist table here adds precise norm-one descent in the \((2,2,1)\) and \((4,1)\) cases and a degree-six induced torus in the \((3,2)\) case.

## Limitations
The claim depends on the classical degree-five del Pezzo twist classification and the standard normalization-gluing theorem; those antecedents are not new. It concerns only the full ten-component reduced divisor, and only the connected Picard torus. The seven finite abelian group formulas follow from, and are not independent of, the integral classification. A separate specialized treatment of the integral Petersen cycle module under cyclic subgroups could provide an equivalent statement under different terminology; literature priority is provisional, and no independent mathematical audit is claimed. Nothing here asserts that the torus is determined by the rational character alone, or that the complete surface Picard lattice is isomorphic to the boundary Picard character lattice.

## References
1. X. Roulleau, *The Fano surface of the Fermat cubic threefold, the del Pezzo surface of degree 5 and a ball quotient*, arXiv:1001.5111, first public 2010-01-28, https://arxiv.org/abs/1001.5111 .
2. J. González-Sánchez, M. Harrison, I. Polo-Blanco, J. Schicho, *Algorithms for Del Pezzo Surfaces of Degree 5*, arXiv:1009.4044, first public 2010-09-21, https://arxiv.org/abs/1009.4044 .
3. S. Casalaina-Martin, J. Kass, F. Viviani, *The Local Structure of Compactified Jacobians*, arXiv:1107.4166, https://arxiv.org/abs/1107.4166 .
4. *A primitive index-two map from the exterior-square root lattice to the Petersen generalized-Jacobian lattice*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-primitive-index-two-map-from-the-exterior-square-root-lattice--88a956595fd2/RESULT.md .
5. *Integral Frobenius trace lattices and arithmetic cones of degree-five del Pezzo surfaces*, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-integral-frobenius-trace-lattices-and-arithmetic-cones-of-degree--14de99fa5b64/RESULT.md .
6. *Motivic collapse of the four Frobenius types of pentagon-boundary degree-five del Pezzo surfaces*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-motivic-collapse-of-the-four-frobenius-types-of-pentagon-boundar--2e66c1f48d10/RESULT.md .
