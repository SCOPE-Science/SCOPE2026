# Integral critical group of the exceptional-curve–conic-pencil incidence graph on a quartic del Pezzo surface

## Finding
For every smooth complex degree-four del Pezzo surface \(S\), form the bipartite graph \(\Gamma(S)\) between its sixteen exceptional \((-1)\)-curves and the ten conic-fibration divisor classes. A curve \(C\) is adjacent to a conic class \(F\) if and only if \(F\cdot C=0\) (equivalently, \(C\) is vertical and therefore occurs in a reducible fiber). Then the connected graph has 26 vertices, 80 edges and integral critical group
\[
K(\Gamma(S))\cong\mathbb Z/5\mathbb Z\oplus(\mathbb Z/20\mathbb Z)^4\oplus\mathbb Z/80\mathbb Z\oplus(\mathbb Z/320\mathbb Z)^4.
\]
The spanning-tree number is \(2^{36}5^{10}=671088640000000000\) and the exponent is \(320\). In particular, the reduced Laplacian has fifteen unit invariant factors and the ten nonunit factors \(5,20,20,20,20,80,320,320,320,320\).

## Assumptions and scope
The ground field is \(\mathbb C\); no arithmetic Frobenius action is asserted. Every smooth quartic del Pezzo is the blowup of five points in general position in \(\mathbb P^2\). In the standard Picard basis, \(L\) denotes the pullback of a line and \(E_i\) the exceptional divisor for \(i=1,\ldots,5\), with \(L^2=1\), \(E_i^2=-1\), \(L\cdot E_i=E_i\cdot E_j=0\) for distinct indices. The sixteen exceptional curves have classes
\[
E_i\quad (5),\qquad L-E_i-E_j\quad(i<j;\ 10),\qquad Q=2L-\sum_{i=1}^5E_i\quad(1).
\]
The ten base-point-free conic classes are
\[
F_i=L-E_i,\qquad G_i=2L-\sum_{j\ne i}E_j=-K_S-F_i\qquad (i=1,\ldots,5).
\]
Graph vertices are these *classes* (not points of fibers), and an edge is a line–pencil incidence, not an incidence among lines.

## Proof
**Step 1: Canonical incidence matrix.** For a conic class \(F\), a reducible fiber is a sum \(C+C'\) of exceptional curves, both meeting \(F\) trivially. The ten explicit classes above each have exactly four such unordered decompositions, with eight distinct exceptional components (checked by adding the listed divisor classes; all possible pairs are exhausted by the finite list of sixteen). This yields a \(16\times10\) incidence matrix \(B\) with five ones per row and eight ones per column, hence 80 edges. The two classes \(F_i,G_i\) form complementary column pairs: every exceptional curve is vertical for exactly one of them, while an exceptional curve is vertical for an even number of the first five \(F_i\). Moreover all sixteen even-weight five-bit strings occur exactly once. Thus, up to row order,
\[
B_{b,F_i}=b_i,\qquad B_{b,G_i}=1-b_i,\qquad b\in\{0,1\}^5,\ \sum_i b_i\equiv0\pmod2.
\]
Every row and column is nonempty, and any two columns from different coordinate pairs share four neighbors, proving connectedness. More directly, all columns are linked through the even-bit rows, which in turn meet columns.

**Step 2: Spectral and tree invariant.** The graph Laplacian is
\[
\mathcal L=\begin{pmatrix}5I_{16}&-B\\-B^{\mathsf T}&8I_{10}\end{pmatrix}.
\]
The Gram matrix \(B^{\mathsf T}B\) has diagonal entries 8, zero between complementary coordinates, and 4 between distinct coordinate pairs. Its eigenvalues are \(40\) once, \(8\) five times and 0 four times. The eigenvalues of \(\mathcal L\) are therefore \(0\) once, \(13\) once, \(5\) ten times, \(8\) four times, and the two roots of \(t^2-13t+32\), each five times. The matrix-tree theorem gives
\[
\tau(\Gamma)=\frac{13\cdot5^{10}\cdot8^4\cdot32^5}{26}=2^{36}5^{10}.
\]

**Step 3: Integral Smith form.** The previous spectrum does not determine torsion invariants. Form the explicitly determined \(26\times26\) *integer* matrix \(\mathcal L\) of Step 2, delete any one row and the corresponding column, and apply Euclidean Smith reduction with unit row/column swaps, sign changes, and integer row/column additions. The included self-contained `verify.py` constructs \(B\) independently from all 40 exceptional-pair decompositions, checks the parity model and block Gram identity, and performs an exact Smith reduction while tracking two unimodular matrices \(U,V\) and verifying \(U\mathcal L'V=D\). It verifies that all off-diagonal entries vanish and every diagonal entry divides the next. For three choices of deleted vertex (an exceptional curve and two conic pencils), the diagonal is
\[
(\underbrace{1,\ldots,1}_{15},5,\underbrace{20,\ldots,20}_{4},80,\underbrace{320,\ldots,320}_{4}).
\]
Every operation is integer-unimodular, so this is a reproducible integral Smith certificate, not an inference from a floating-point spectrum. The independent Bareiss determinant calculation equals \(2^{36}5^{10}\), consistent with Step 2. By the definition of the graph critical group as the cokernel of a reduced integer Laplacian, the displayed decomposition follows.

## Verification
Run `python3 verify.py` from the directory containing this document. It uses the Python 3 standard library only. It reconstructs all sixteen divisor classes and ten conic classes, enumerates exactly forty exceptional-component pairs, cross-checks the independent even-parity matrix model, computes and verifies integer Smith transformation matrices, and checks determinants for three sinks. The expected final line begins `DEL_PEZZO_CONIC_INCIDENCE_CRITICAL_GROUP_VERIFIED_OK`. An independent algebra package calculation using SymPy's `smith_normal_form` and integer determinant agreed on one reduced Laplacian, but that package is not required to replay the attached certificate.

## Relationship to prior work
Batyrev–Popov's 2003 work supplies the classical del Pezzo root/Cox-ring framework. Stillman–Testa–Velasco (first public preprint October 8, 2006) explicitly enumerate exceptional curve classes and conic classes and their decompositions in the Cox-ring context. Rybakov (2005) treats conic-bundle and degree-four del Pezzo zeta functions over finite fields. The present claim does **not** reclassify the classical sixteen curves, ten conic pencils or their reducible fibers: it determines the *integer critical group of the 26-vertex bipartite incidence graph* resulting from these data. A prior formula for the sixteen-vertex Clebsch graph alone is not a Smith form for this 26-vertex graph. A general theorem on bipartite parity-incidence graphs could in principle imply this finite case; none was established in the inspected relevant sources, so priority remains provisional.

## Limitations
The assertion concerns the combinatorial Laplacian of this natural incidence graph, not the Néron–Severi discriminant group or an arithmetic Galois module. The full Smith-form evidence is exact finite integer calculation with a replayable certificate; the mathematical interpretation relies on the classical blowup classification. No assertion of independent formal proof, exhaustive literature priority, or a new geometric moduli classification is made.

## References
- V. Batyrev and O. Popov, *The Cox ring of a Del Pezzo surface*, arXiv:math/0309111 (first submitted 2003-09-05), https://arxiv.org/abs/math/0309111.
- M. Stillman, D. Testa and M. Velasco, *Gröbner bases, monomial group actions, and the Cox rings of Del Pezzo surfaces*, arXiv:math/0610261 (first submitted 2006-10-08), https://arxiv.org/abs/math/0610261; see the discussion of exceptional classes and conic-degree quadratic relations.
- S. Rybakov, *Zeta functions of conic bundles and del Pezzo surfaces of degree 4 over finite fields*, Moscow Mathematical Journal 5 (2005).
