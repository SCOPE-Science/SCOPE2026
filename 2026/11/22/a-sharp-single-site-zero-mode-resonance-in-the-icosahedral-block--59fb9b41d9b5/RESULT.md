# A sharp single-site zero-mode resonance in the icosahedral blockade Hamiltonian

## Finding
On the twelve-vertex icosahedral graph, let \(H(t)\) be the zero-detuning, nearest-neighbor-perfect-blockade spin-flip Hamiltonian with unit amplitudes at eleven sites and real amplitude \(t\) at the remaining vertex. Its exact zero-energy multiplicity is
\[
\boxed{\dim\ker H(t)=\begin{cases}17,&t=1\text{ or }t=-1,\\5,&t\in\mathbb R\setminus\{-1,1\}.\end{cases}}
\]
At \(t=1\) the full characteristic polynomial is
\[
\begin{aligned}
\det(xI-H(1))={}&x^{17}(x^2-3)^4(x^2-1)^4\\
&\cdot(x^4-30x^2+84)(x^4-16x^2+44)^3\\
&\cdot(x^4-10x^2+12)^5.
\end{aligned}
\]
The universal excitation-parity imbalance guarantees five zero modes for every choice of real site amplitudes; the remaining twelve at \(t=\pm1\) are a sharp homogeneous-drive enhancement. In the parity sectors, the uniform zero-mode multiplicities are eleven (even excitation number) and six (odd), whereas for \(|t|\ne1\) they are five and zero.

## Assumptions and scope
Label the vertices \(0,1,\ldots,11\). Vertices \(0\) and \(11\) are the poles; \(u_i=1+i\), \(v_i=6+i\) for \(i\in\mathbb Z/5\mathbb Z\) form two pentagons. The edge set consists of exactly the thirty edges
\[
\{0u_i,\ 11v_i,\ u_iu_{i+1},\ v_iv_{i+1},\ u_iv_i,\ u_iv_{i-1}:i\in\mathbb Z/5\mathbb Z\}.
\]
This is the standard icosahedral graph: each vertex has degree five, and there are twenty triangular faces. An allowed excitation configuration is an independent vertex set \(A\). The Hilbert space has orthonormal basis \(\{|A\rangle:A\text{ independent}\}\). Define
\[
\langle B|H(t)|A\rangle=\begin{cases}
 t,&A\triangle B=\{0\},\\
 1,&A\triangle B=\{v\},\ v\ne0,\\
 0,&\text{otherwise},
\end{cases}
\]
where both \(A\) and \(B\) must be allowed. This is a Hermitian projected spin-flip or PXP Hamiltonian, with no detuning or diagonal term and no additional interactions. An overall nonzero Rabi normalization does not change kernel dimensions.

## Proof
**1. Constrained state count.** There are twelve independent singletons and \(\binom{12}{2}-30=36\) independent pairs. For a complete explicit count of triples, the six families of edges above show that the graph of distance-two pairs is another icosahedral graph, with twenty triangles; these are precisely the independent triples. The remaining six nonedges are antipodal pairs and cannot belong to an independent triple. Thus there are no independent quadruples, and the independence polynomial is
\[
 I_G(q)=1+12q+36q^2+20q^3.
\]
Consequently the even and odd excitation-parity sectors have dimensions \(37\) and \(32\).

**2. Exact homogeneous characteristic polynomial.** Order all independent configurations by increasing twelve-bit mask, separately within each parity sector. A single flip changes excitation parity, so
\[
 H(t)=\begin{pmatrix}0&B(t)\\B(t)^T&0\end{pmatrix},\quad
 B(t)_{A,C}=\begin{cases}t,&A\triangle C=\{0\},\\1,&|A\triangle C|=1,\ A\triangle C\ne\{0\},\\0,&\text{otherwise}.\end{cases}
\]
Here rows are the thirty-seven even configurations and columns the thirty-two odd ones. Exact integer characteristic-polynomial computation gives
\[
\begin{aligned}
\det(zI_{32}-B(1)^TB(1))={}&z^6(z-3)^4(z-1)^4\\
&\cdot(z^2-30z+84)(z^2-16z+44)^3\\
&\cdot(z^2-10z+12)^5.
\end{aligned}
\]
The factors other than \(z^6\) have nonzero constant terms, hence \(\operatorname{rank}B(1)=26\), since \(B(1)^TB(1)\) and \(B(1)\) have identical real kernels. The two kernel dimensions are \(37-26=11\) and \(32-26=6\), totaling seventeen. The displayed characteristic polynomial of \(H(1)\) follows from the block determinant identity \(\det(xI-H)=x^{37-32}\det(x^2I_{32}-B^TB)\).

**3. A sharp, parameter-uniform determinant certificate.** The following zero-based row indices, relative to the increasing even-configuration mask order, specify thirty-two distinct rows:

`[0,1,3,2,4,5,6,7,8,9,10,11,14,12,18,17,16,15,19,20,21,23,22,13,25,26,31,30,29,27,24,32]`.

Retain every odd-configuration column in increasing mask order. Exact symbolic determinant calculation of the resulting square submatrix \(M(t)\) gives
\[
\boxed{\det M(t)=2(t^2-1)^6.}
\]
For each real \(t\) with \(|t|\ne1\), this nonzero minor implies \(\operatorname{rank}B(t)=32\), the maximal possible rank. The total zero-mode multiplicity is therefore \((37-32)+(32-32)=5\). Finally, conjugating by the diagonal unitary \(U|A\rangle=(-1)^{\mathbf1_{0\in A}}|A\rangle\) changes the sign of precisely the flips at vertex zero. Thus \(H(-1)=UH(1)U^*\), completing the classification.

Both exact identities in steps 2 and 3 are finite, algorithmically checkable determinant calculations on explicitly given integer or polynomial matrices, not extrapolations from numerical eigenvalues. Their independent verification is described next.

## Verification
Run `python verify_exact.py` with Python 3.10+ and SymPy. It generates the graph from the six edge families, checks its local combinatorics and independent-set counts, forms the exact \(37\times32\) parity block, verifies the entire factorized Gram characteristic polynomial by symbolic subtraction, and verifies the displayed symbolic \(32\times32\) minor determinant.

Independently run `python verify_independent.py` with Python 3.10+ and NetworkX. It uses NetworkX's separately constructed icosahedral graph rather than the six-family construction, calculates the complete \(32\)-degree Gram characteristic polynomial using only integer matrix products and Newton identities, and independently checks the uniform rank and a full-column-rank witness modulo primes. The scripts test the full finite configuration spaces, not samples of configurations or floating-point approximations.

## Relationship to prior work
Lesanovsky (arXiv:1010.2349, first posted 12 October 2010) develops nearest-neighbor Rydberg blockade spin dynamics on a one-dimensional ring and a specially shifted solvable Hamiltonian. The unshifted ideal projected spin-flip term motivates the present model, but that paper does not give this icosahedral finite spectrum. Buijsman (arXiv:2203.09264) discusses excitation-parity zero-mode lower bounds on one-dimensional PXP chains. Its general chiral block argument yields the five-mode lower bound here but neither the extra twelve modes nor their exact single-site loss. Byun, Kim and Ahn (PRX Quantum 3, 030305, 2022) demonstrate Rydberg implementations of three other Platonic graphs (tetrahedron, cube and octahedron) and do not give this Hamiltonian's spectrum.

The published *Integral icosahedral independence homology as an antipodal vertex lattice* studies the homotopy and integral symmetry of this same graph's independence complex, with face vector \((12,36,20)\). Its Euler characteristic gives the excitation-parity imbalance, but the homology statement alone does not imply the weighted configuration-flip adjacency rank or the sharp determinant \(2(t^2-1)^6\). Searches of both variants of the statement and the relevant primary literature did not identify an earlier equivalent exact zero-mode classification. This is a best-knowledge novelty assessment, not an exhaustive priority certificate.

## Limitations
This theorem is for the twelve-site icosahedral graph, ideal nearest-neighbor blockade, zero detuning, and the specified real site-amplitude profile. The extra twelve zero modes are not stable under the explicitly tested single-site amplitude change. It does not assert zero modes of the unconstrained physical Hamiltonian with finite blockade strength or long-range interactions, or an infinite-volume result. Independent scientific validation and exhaustive historical-priority confirmation are not supplied.

## References
- I. Lesanovsky, *Many-body spin interactions and the ground state of a dense Rydberg lattice gas*, arXiv:1010.2349 (initial public preprint 2010-10-12), https://arxiv.org/abs/1010.2349.
- W. Buijsman, *Number of zero-energy eigenstates in the PXP model*, Phys. Rev. B **106**, 045104 (2022), arXiv:2203.09264, https://arxiv.org/abs/2203.09264.
- A. Byun, M. Kim and J. Ahn, *Finding the Maximum Independent Sets of Platonic Graphs Using Rydberg Atoms*, PRX Quantum **3**, 030305 (2022), https://doi.org/10.1103/PRXQuantum.3.030305.
- *Integral icosahedral independence homology as an antipodal vertex lattice*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-icosahedral-independence-homology-as-an-antipodal-verte--4ce34e2d4cf9 (claim used only for comparison of invariants).
