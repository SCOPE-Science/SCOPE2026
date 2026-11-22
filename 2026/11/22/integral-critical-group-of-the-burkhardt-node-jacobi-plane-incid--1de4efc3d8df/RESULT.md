# Integral critical group of the Burkhardt node–Jacobi-plane incidence graph

## Finding
Let \(X\subset\mathbb P^5_{\mathbb C}\) be the Burkhardt quartic threefold defined by \(\sigma_1=\sigma_4=0\), where \(\sigma_i\) denotes the \(i\)-th elementary symmetric polynomial in six coordinates. Let \(\mathcal N\) be its set of \(45\) ordinary nodes and \(\mathcal J\) its set of \(40\) Jacobi planes. Let \(\Gamma\) be the **unweighted bipartite incidence graph**, with vertex set \(\mathcal N\sqcup\mathcal J\) and an edge \(P-J\) exactly when \(P\in J\).

**Theorem.** The finite integral graph critical group, equivalently the degree-zero divisor-class group of \(\Gamma\) modulo chip firing, is
\[
\boxed{K(\Gamma)\simeq
 (\mathbb Z/2\mathbb Z)^{14}\oplus\mathbb Z/4\mathbb Z
 \oplus(\mathbb Z/12\mathbb Z)^6\oplus(\mathbb Z/60\mathbb Z)^3
 \oplus(\mathbb Z/120\mathbb Z)^5\oplus\mathbb Z/360\mathbb Z
 \oplus(\mathbb Z/720\mathbb Z)^4\oplus(\mathbb Z/2160\mathbb Z)^{10}.}
\]
These are the full nonunit invariant factors in divisibility order. The graph has \(85\) vertices, \(360\) edges and
\[
 \boxed{\#K(\Gamma)=\tau(\Gamma)=2^{108}3^{54}5^{23}},
\]
where \(\tau\) counts spanning trees. Its group exponent is \(2160\).

## Assumptions and scope
The geometric variety is considered over \(\mathbb C\); the graph counts each geometric node and Jacobi plane once, without orienting incidences or identifying conjugates. The critical group is the cokernel of any reduced integer **graph Laplacian**, not the cokernel of the rectangular node-to-plane incidence matrix. No assertion is made about the Picard group, class group or Brauer group of \(X\). The result depends only on the classical complex incidence configuration and thus is independent of projective coordinate choices.

## Proof
**1. Reconstructing the graph.** Fix a primitive cube root \(\omega\) of unity. The classical symmetric Burkhardt model has \(15\) nodes of the form \([1:-1:0:0:0:0]\), with coordinate permutations, and \(30\) nodes of the form \([1:1:\omega:\omega:\omega^2:\omega^2]\), with coordinate permutations modulo common projective scaling by \(\omega\). The \(40\) Jacobi planes are indexed by three-element subsets \(\{i,j,k\}\) with \(i<j<k\), together with a choice \(s\in\{1,2\}\), and have equations \(x_j=\omega^s x_i\), \(x_k=\omega^{2s}x_i\), \(\sigma_1=0\). The completeness of these lists is the established geometry in Cheltsov–Przyjalkowski–Shramov, Section 2.

For the first kind of node, indexed by the unordered pair of its two nonzero positions, incidence means the triple of plane indices avoids that pair. For the second kind, index a node by a six-word \(c\in\{0,1,2\}^6\) with exactly two occurrences of each digit, modulo simultaneous addition of a constant modulo \(3\). Such a node is incident to the plane \((i,j,k;s)\) exactly when
\[
 c_j-c_i\equiv s\pmod 3,\qquad c_k-c_i\equiv2s\pmod3.
\]
These rules follow directly by substituting the node coordinates into the plane equations. There are \(15+30=45\) distinct nodes and \(20\cdot2=40\) planes. Every node lies on \(8\) Jacobi planes: for a two-support node, choose a triple from the remaining four coordinates and either orientation; for a three-colour node, choose one position of each colour, which determines the orientation uniquely. Every plane contains \(9\) nodes: three two-support nodes and six three-colour nodes. Thus there are \(360\) graph edges.

**2. A complete finite Gram identity.** Let \(B\) be the \(45\)-by-\(40\) zero-one matrix obtained from the preceding explicit rule, and let \(G=BB^{\mathsf T}\). Direct case counting from that rule gives the exact integer identities
\[
 G\mathbf 1=72\mathbf1,\qquad G^2=12G+96J_{45},\qquad\operatorname{tr}G=360,
\]
where \(J_{45}\) is the all-ones matrix. This step is a finite universal identity with no geometric parameter: the bundled checker independently enumerates all \(45\cdot40\) incidences using both the three-colour rule and explicit homogeneous coordinates with the embedding \(\omega\mapsto2\in\mathbb F_7\), and checks every one of the \(45^2\) entries of the Gram identity. Consequently, on the perpendicular complement of the all-ones vector, the eigenvalues of \(G\) are \(0\) and \(12\). The trace forces multiplicities \(20\) and \(24\), respectively; the remaining eigenvalue is \(72\) with multiplicity one. In particular \(\operatorname{rank}_{\mathbb Q}B=25\).

**3. Spectrum and group order.** The full integer graph Laplacian is
\[
 L=\begin{pmatrix}8I_{45}&-B\\-B^{\mathsf T}&9I_{40}\end{pmatrix}.
\]
The eigenvalues of \(L\) are
\[
 0^{(1)},\quad17^{(1)},\quad5^{(24)},\quad12^{(24)},\quad8^{(20)},\quad9^{(15)}.
\]
For each nonzero eigenvalue \(\lambda\) of \(G\), the corresponding pair of Laplacian eigenvalues solves \((8-t)(9-t)=\lambda\); kernel directions of \(B\) and \(B^{\mathsf T}\) supply the remaining \(9\)- and \(8\)-eigenvalues. The zero eigenvalue of \(L\) has multiplicity one, so the graph is connected. The matrix-tree theorem gives
\[
 \tau(\Gamma)=\frac{17\cdot 5^{24}\cdot12^{24}\cdot8^{20}\cdot9^{15}}{85}=2^{108}3^{54}5^{23}.
\]
In particular there can be no torsion primes other than \(2\), \(3\) and \(5\).

**4. Exact integral Smith factors.** Delete one row and corresponding column of \(L\) to obtain an \(84\)-by-\(84\) reduced Laplacian \(A\). Compute the Smith valuations using exact elimination over \(\mathbb Z/p^{12}\mathbb Z\), always selecting an entry of smallest \(p\)-adic valuation in the active submatrix, and using invertible row and column operations to eliminate its row and column. Such a pivot divides every active entry by \(p^v\) and leaves a unit, which is invertible modulo \(p^{12-v}\); thus all operations are legitimate and determine the Smith valuations below \(12\). The complete distributions, **including unit valuations**, are:

| Prime | Valuation and multiplicity |
|---|---|
| \(2\) | \(0:40,\ 1:14,\ 2:10,\ 3:6,\ 4:14\) |
| \(3\) | \(0:55,\ 1:14,\ 2:5,\ 3:10\) |
| \(5\) | \(0:61,\ 1:23\) |

All \(84\) pivots are nonzero modulo their selected prime power, and the weighted valuation sums are \(108\), \(54\) and \(23\), exactly the independent tree-count exponents. Applying the same procedure to reduced matrices obtained by deleting a node vertex and by deleting a plane vertex gives identical distributions. To reconstruct the global invariant factors, sort the \(84\) valuations at each prime in nondecreasing order and multiply the prime powers positionwise. This gives \(40\) units followed by the nonunit factors listed in the theorem, in divisibility order. The exact script supplies the full deterministic integer certificate; finite enumeration here is exhaustive because the configuration has precisely the listed \(45\) nodes and \(40\) planes.

## Verification
Run `python3 burkhardt_critical_verify.py` with a standard Python 3 installation, requiring no nonstandard libraries or external data. It builds the graph from the finite combinatorial coordinates; separately reconstructs every incidence via projective homogeneous coordinates with \(\omega\mapsto2\in\mathbb F_7\); checks all degrees, connectivity and all entries of the Gram identity; computes the three prime-local Smith valuation distributions modulo the exact prime powers; tests two different deleted vertices; checks divisibility of the resulting invariant factors; and compares their total prime exponents with the independently derived spectral spanning-tree count. Expected final line: `BURKHARDT_85_CRITICAL_GROUP_VERIFIED_OK`.

## Relationship to prior work
Cheltsov–Przyjalkowski–Shramov (2016, Section 2) determine the two node orbits and explicit Jacobi planes, and study Weil divisor classes and intersections of planes on smooth hyperplane sections; these are different from graph-chip-firing equivalence on the \(85\)-vertex incidence graph. Bruin–Nasserden (2017/2018) determine arithmetic invariants and zeta functions of the Burkhardt quartic, not this graph's integral Laplacian. Szemberg–Szpond (2026, Sections 4–7) give a complementary Pascal realization and node-plane incidence counts, but no graph critical-group decomposition. The closest indexed public calculation, *The integral order-two defect of the Burkhardt node–Jacobi-plane incidence lattice* (2026), computes the Smith factors of the **rectangular incidence map** \(B:\mathbb Z^{40}\to\mathbb Z^{45}\): \(1^{15},2^{10}\). The present claim instead concerns the reduced Laplacian \(\begin{psmallmatrix}8I&-B\\-B^{\mathsf T}&9I\end{psmallmatrix}\); the rectangular Smith factors alone do not determine that Laplacian's integral Smith form. Graph Laplacian spectra and spanning-tree counts likewise determine group order but do not determine cyclic invariant factors. This calculation therefore records new integral information relative to the inspected sources, subject to historical-priority limitations.

## Limitations
This is an exact, finite invariant of the complex geometric incidence graph, not a geometric Jacobian or a Brauer/Picard/class-group calculation for the threefold. The prime-local elimination is a reproducible exact computation rather than a closed conceptual formula for a general family of incidence structures. An earlier calculation in a specialist design-theory table or a historical source with a different terminology could already imply this decomposition; absence from the inspected literature is not proof of publication priority. The complete 1990 paper of de Jong–Shepherd-Barron–Van de Ven was not accessible for full comparison.

## References
1. I. Cheltsov, V. Przyjalkowski, C. Shramov, *Burkhardt quartic, Barth sextic, and the icosahedron*, arXiv:1606.04372, first public version 2016-06-14, Section 2. https://arxiv.org/html/1606.04372v2
2. N. Bruin, B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold*, arXiv:1705.09006, first public version 2017-05-25, especially Sections 3, 5, and 7. https://arxiv.org/html/1705.09006v3
3. T. Szemberg, J. Szpond, *From a Pascal construction to the Burkhardt quartic*, arXiv:2606.30772, first public version 2026-06-29, Sections 4–7. https://arxiv.org/abs/2606.30772
4. I. Cheltsov, Y. Tschinkel, Z. Zhang, *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, Selecta Math. 31 (2025), published online 2024-12-13, Section 8. https://doi.org/10.1007/s00029-024-01001-w
5. *The integral order-two defect of the Burkhardt node–Jacobi-plane incidence lattice*, publicly indexed research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-integral-order-two-defect-of-the-burkhardt-node-jacobi-plane--85dfc2d5a8f4
6. A. J. de Jong, N. I. Shepherd-Barron, A. Van de Ven, *On the Burkhardt quartic*, Math. Ann. 286 (1990), 309–328. https://doi.org/10.1007/BF01453578 (abstract/metadata consulted; complete text not inspected).
