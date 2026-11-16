# Sharp noncommutative square roots of Haar measure on the three-cycle

## Finding
Let \(G=\mathbb Z/3\mathbb Z\) and let \(\mu=\sum_{j=0}^2 A_j\delta_j\) be a positive \(2\times2\) matrix-valued measure with \(A_j=A_j^*\succeq0\) and \(\sum_jA_j=I_2\). Define ordered convolution by \((\mu*\mu)(k)=\sum_{j=0}^2A_jA_{k-j}\), indices modulo three, and the normalized matrix Haar measure \(H=\frac13 I_2\sum_j\delta_j\).

**Complete classification.** The identity \(\mu*\mu=H\) holds if and only if, after one simultaneous unitary conjugation of the three matrices, there is a unique parameter \(0\le t\le1\) for which
\[
 A_j=\frac13\bigl(I_2+t\omega^{-j}E_{12}+t\omega^jE_{21}\bigr),\qquad\omega=e^{2\pi i/3}.
\]
Here \(E_{12}\) and \(E_{21}\) are the two off-diagonal matrix units.

Every \(t>0\) yields three pairwise noncommuting positive matrices although \(\mu*\mu=H\). Their exact sharp commutator size and trace-norm deviation are
\[
\|[A_j,A_k]\|_{\mathrm{op}}=\frac{\sqrt3}{9}t^2\quad(j\ne k),\qquad
\sum_{j=0}^2\|A_j-I_2/3\|_{S_1}=2t.
\]
Consequently, the maximum pairwise commutator norm is \(\sqrt3/9\), attained precisely when all three atoms have rank one. Among groups with at most three elements and matrix sizes at most two, \(G\) and matrix size two are the first where a non-Haar positive square root of Haar exists: on the two-cycle every matrix-valued square root is Haar; on the three-cycle every scalar positive square root is Haar.

## Assumptions and scope
All matrix values are complex Hermitian positive semidefinite, normalized by total mass \(I_2\); positivity refers to the measure's values, not to complete positivity of a convolution operator. Convolution uses the ordered matrix product, without a normalization factor in the finite-group sum. Unitarily equivalent measures use a single constant unitary for all three atoms. The theorem concerns the **convolution square equal to Haar**, not convolution idempotence \(\mu*\mu=\mu\), and does not classify other groups or larger matrices.

## Proof
Set \(\omega=e^{2\pi i/3}\) and define the matrix Fourier transform \(\widehat\mu(k)=\sum_{j=0}^2\omega^{kj}A_j\), \(k=0,1,2\). This normalization makes \(\widehat{\mu*\mu}(k)=\widehat\mu(k)^2\). The total-mass constraint gives \(\widehat\mu(0)=I_2\); Hermiticity gives \(\widehat\mu(2)=\widehat\mu(1)^*\). Since \(\widehat H(0)=I_2\) and both other Fourier coefficients vanish, Fourier inversion shows
\[
\mu*\mu=H\quad\Longleftrightarrow\quad B^2=0,\qquad B:=\widehat\mu(1).
\]
A square-zero complex \(2\times2\) matrix is either zero or rank one. In the nonzero case \(\mathrm{ran}(B)=\ker(B)\) is a one-dimensional subspace, whose orthogonal complement maps into its range. Choosing orthonormal vectors in these two lines and adjusting one phase makes \(B=tE_{12}\), with \(t=\|B\|_{\mathrm{op}}>0\); the zero case is \(t=0\). Fourier inversion now gives exactly
\[
A_j=\frac13\bigl(I_2+t\omega^{-j}E_{12}+t\omega^jE_{21}\bigr).
\]
Each atom has eigenvalues \((1+t)/3\) and \((1-t)/3\). Thus positivity is equivalent to \(0\le t\le1\), proving necessity and sufficiency, and \(t\) is uniquely recoverable as \(\|\widehat\mu(1)\|_{\mathrm{op}}\).

For distinct indices, the commutator is diagonal and has eigenvalues \(\pm i\sqrt3\,t^2/9\). Thus its operator norm is \(\sqrt3\,t^2/9\). The difference \(A_j-I_2/3\) has eigenvalues \(\pm t/3\); summing its trace norms gives \(2t\). The atoms have rank one exactly at \(t=1\), proving every sharp equality statement. If \(t>0\), the nonzero commutators also show \(\mu\ne H\), while \(\mu^{*n}=H\) for all integers \(n\ge2\), since \(H*\mu=H\).

For \(G=\mathbb Z/2\mathbb Z\), the only nontrivial Fourier coefficient is the Hermitian matrix \(A_0-A_1\); its square vanishing forces it to vanish. For scalar coefficients on \(\mathbb Z/3\mathbb Z\), the scalar Fourier coefficient \(B\) satisfies \(B^2=0\) and therefore \(B=0\). These prove the asserted minimalities.

## Verification
The supplied standalone `check.py` uses exact SymPy algebra to confirm the cyclic convolution identities, positivity determinants, and commutator-square identities symbolically in the real parameter \(t\). Actual checker output: `CHECK_OK symbolic_convolution=3 positivity_determinants=3 commutator_squares=3`. The complete classification, sharpness and minimality rest on the preceding mathematical proof; no finite numerical sample is treated as a universal proof.

## Relationship to prior work
Jabbari's matrix Kawada–Itô theorem proves automatic commutativity for a positive matrix measure satisfying **\(\mu*\mu=\mu\)**. Our measure satisfies **\(\mu*\mu=H\)**, with \(\mu\ne H\) when \(t>0\); applying Jabbari's result to \(H\) says nothing about commutativity of \(\mu\). The paper's nonpositive-square example on a free group (Example 4.1) likewise does not have a positive Haar square. Chu, Hilberdink and Howroyd give a matrix-valued Choquet–Deny criterion for bounded fixed functions \(f*\sigma=f\); their Fourier invertibility tests do not classify nilpotent nonzero Fourier coefficients of Haar square roots. The displayed matrices are closely related to the standard three-direction qubit measurement, but the convolution-square classification and sharp commutator statement are separate Fourier claims.

## Limitations
The result is restricted to normalized positive \(2\times2\) measures on the three-cycle. It does not assert that convolution preserves positivity for general matrix-valued measures, nor that a two-step convolution root extends to a continuous positive convolution semigroup. Publication priority against older quantum-measurement and finite-time-mixing literature remains provisional; no independent mathematical audit has been performed.

## References
1. A. Jabbari, *The Matrix Kawada–Itô Theorem and Harmonic Rigidity on Locally Compact Groups*, arXiv:2611.09755v1, first publicly posted 2026-11-06, https://arxiv.org/abs/2611.09755.
2. C.-H. Chu, T. Hilberdink and J. Howroyd, *A Matrix-Valued Choquet–Deny Theorem*, Proc. Amer. Math. Soc. 129 (2001), 229–235, first electronically published 2000-03-29, https://doi.org/10.1090/S0002-9939-00-05694-X.
