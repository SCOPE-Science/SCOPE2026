# First equal-leverage Fourier sampling split between E-optimality and conditioning

## Finding
For every integer \(n\ge4\), form the first real Fourier band on the equispaced cyclic grid, with the orthonormal column matrix \(U_n\) defined below. If four *distinct, unweighted* coordinates are sampled, a selection that maximizes its smallest singular value need not minimize its spectral condition number, even though every candidate row has exactly equal squared norm \(3/n\).

The first separation in grid order occurs at \(n=9\). At that order, the unique E-optimal dihedral orbit is represented by \(J_E=\{0,1,3,6\}\), and the unique condition-number-optimal orbit is represented by \(J_\kappa=\{0,2,4,6\}\). For \(J_E\), the squared singular values are precisely \(\{1/3,1/3,2/3\}\), giving minimum squared singular value \(1/3\) and squared spectral condition number \(2\). For \(J_\kappa\), rigorous rational bounds give
\[
0.31701<\lambda_{\min}(U_{J_\kappa}^{\mathsf T}U_{J_\kappa})<0.31708,
\qquad
0.51693<\lambda_{\max}(U_{J_\kappa}^{\mathsf T}U_{J_\kappa})<0.51700.
\]
Hence the latter has strictly smaller squared condition number than \(2\), but strictly smaller minimum squared singular value than \(1/3\). All maximizers/minimizers are the indicated dihedral images (not merely examples). For grid orders \(4\le n\le8\), the two optimizer sets coincide.

## Assumptions and scope
For integer \(n\ge4\) and \(j\in\{0,\ldots,n-1\}\), define the row
\[
u_j=\left(\frac1{\sqrt n},\sqrt{\frac2n}\cos\frac{2\pi j}{n},\sqrt{\frac2n}\sin\frac{2\pi j}{n}\right).
\]
Let \(U_n\in\mathbb R^{n\times3}\) have these rows; its columns are orthonormal for \(n\ge3\). Select an *unordered* four-element index set \(J\) with no repeated coordinates and no rescaling, and write \(U_J\) for the corresponding \(4\times3\) matrix. E-optimal means maximizing \(\sigma_{\min}(U_J)\); condition-number-optimal means minimizing \(\kappa_2(U_J)=\sigma_{\max}/\sigma_{\min}\). The assertion concerns exact arithmetic and only the grid orders \(4\le n\le9\). Rotations and reflections act on indices by \(j\mapsto\pm j+t\pmod n\).

## Proof
The orthonormality and equal leverage follow from roots-of-unity sums. For \(J\) of size four let \(C_k=\sum_{j\in J}\cos(2\pi k j/n)\) and \(S_k=\sum_{j\in J}\sin(2\pi k j/n)\). Direct trigonometry gives the exact three-by-three Gram matrix
\[
G_J=\frac1n\begin{pmatrix}4&\sqrt2 C_1&\sqrt2 S_1\\
\sqrt2 C_1&4+C_2&S_2\\
\sqrt2 S_1&S_2&4-C_2\end{pmatrix}.
\]
The eigenvalues of \(G_J\) are the squared singular values. Rotation/reflection conjugates \(G_J\) orthogonally and so preserves both criteria. The finite exhaustive dihedral classification for \(n=5,6,7,8,9\) has respectively \(1,3,4,8,10\) orbits, which cover \(5,15,35,70,126\) distinct sample sets. Their exact rational spectral enclosures and strict separating inequalities are checked by the attached self-contained `VERIFY.py`. That program uses no floating-point arithmetic or third-party libraries: rational Machin-series bounds for \(\pi\), rigorous alternating-series trigonometric bounds, a rational square-root enclosure, and Sylvester determinant tests for the smallest and largest eigenvalues. It independently recomputes every orbit and verifies that the winning bounds strictly separate both objectives from *all* competing orbits. Its printed intervals are only a readable coarsening of exact rational certificates.

The simultaneous optimizer representatives for \(n=5,6,7,8\) are respectively \(\{0,1,2,3\}\), \(\{0,1,2,4\}\), \(\{0,1,3,5\}\), and \(\{0,2,4,6\}\); for \(n=4\) only the full sample set exists. For \(n=9\), the E-optimal representative \(J_E\) has Fourier phase sums \(\sum_{j\in J_E}\zeta^j=\zeta\) and \(\sum_{j\in J_E}\zeta^{2j}=\zeta^2\), where \(\zeta=e^{2\pi i/9}\), using \(\zeta^3+\zeta^6=-1\). Thus in the unitarily equivalent complex frequency basis its Gram matrix is diagonally unitarily conjugate to \((3I+\mathbf1\mathbf1^\mathsf T)/9\), yielding the exact eigenvalues \(1/3,1/3,2/3\). For \(J_\kappa\), the verifier gives \(\kappa_2^2<0.51700/0.31701<2\), while its smallest eigenvalue is less than \(0.31708<1/3\). The strict global optimizer comparisons and multiplicities follow from the certified orbit table.

## Verification
Run `python3 VERIFY.py` with a Python standard-library interpreter. Successful output is `VERIFY_OK: 26 exhaustive dihedral orbits; exact rational spectral bounds and strict global optimization comparisons`. The certificate uses exact fractions throughout, not discretized eigenvalues. To reconstruct it, its embedded table specifies rational endpoints with denominator \(100000\); every bound is checked against an interval Gram matrix via exact rational arithmetic. The proof of the trigonometric bounds uses \(16\arctan(1/5)-4\arctan(1/239)\) for \(\pi\), alternating arctangent series, and alternating Taylor remainder bounds on \([0,\pi/2]\). Explicit interval comparisons cover every four-set orbit for all five nontrivial grid orders.

## Relationship to prior work
Bergermann's deterministic Krylov sketching study (arXiv:2604.07158, Sections 3–4) motivates choosing coordinate rows through singular-value and conditioning/whitening considerations; this theorem tests whether those criteria identify the same four-row design on a canonical exactly orthonormal, equal-leverage model. It is a design-objective comparison, not an analysis of the runtime or convergence of a Krylov algorithm. A separate related result for **two-column, two-row** sketches establishes coincidence under uniform leverage, whereas the present result concerns three columns and four selected rows. Established optimal trigonometric experimental designs may be related, but they can allow continuous/weighted designs or use different criteria, so historical priority is not claimed unconditionally.

## Limitations
The statement is a complete finite classification for cyclic grid orders \(4\le n\le9\), not a classification for every larger order or for arbitrary orthonormal or Krylov bases. It uses unweighted coordinate extraction without replacement, and optimizes two specific spectral criteria. No accuracy, noise, iteration-count or runtime advantage is inferred. Independent mathematical validation has not been performed.

## References
1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158, initially public 2026-04-08. https://arxiv.org/abs/2604.07158
2. H. Wu, *Optimal designs for first-order trigonometric regression on a partial cycle* (2002), related trigonometric regression-design literature, with exact-design coverage not established here.
3. AMS, *Mathematics Subject Classification 2020*, 65F35 (numerical matrix conditioning and scaling). https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=65F35
