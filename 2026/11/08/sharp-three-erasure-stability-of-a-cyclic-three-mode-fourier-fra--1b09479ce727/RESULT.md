# Sharp three-erasure stability of a cyclic three-mode Fourier frame

## Finding
For every integer \(N\ge6\), let \(V_N\) be the \(N\)-by-\(3\) partial Fourier matrix
\[
(V_N)_{x,k}=N^{-1/2}\exp(2\pi i xk/N),\qquad x\in\mathbb Z_N,\ k\in\{0,1,2\}.
\]
For any three-element erasure set \(E\subset\mathbb Z_N\), let \(V_{N,E^c}\) be the retained matrix. Define
\[
u=1+2\cos(2\pi/N),\qquad v=1+2\cos(4\pi/N),\qquad
A_N=1-\frac{3+\tfrac12(v+\sqrt{v^2+8u^2})}{N}.
\]
The sharp lower squared singular-value bound is
\[
\boxed{\lambda_{\min}(V_{N,E^c}^{*}V_{N,E^c})\ge A_N>0.}
\]
**Equality occurs precisely for the \(N\) cyclically consecutive erasure triples**
\(E=\{j,j+1,j+2\}\pmod N\), with \(j\in\mathbb Z_N\). The complete spectrum of the retained Gramian at every such extremizer is
\[
\boxed{\left\{
1-\frac{3-v}{N},\quad
1-\frac{3+\tfrac12(v+\sqrt{v^2+8u^2})}{N},\quad
1-\frac{3+\tfrac12(v-\sqrt{v^2+8u^2})}{N}
\right\}.}
\]
No equality or spectral characterization is asserted for the upper frame-bound extremum over all erasure masks.

## Assumptions and scope
Rows correspond to all distinct sites of the cyclic group \(\mathbb Z_N\). The three *columns* are precisely the consecutive characters of frequencies \(0,1,2\), with standard complex Euclidean inner products and the factor \(N^{-1/2}\). Exactly three labelled, distinct time-site measurements are erased, and all surviving measurements carry unit relative weight. The lower frame bound is the smallest **eigenvalue of the retained Gramian**, equivalently the squared smallest singular value, rather than the unsquared singular value. A cyclically consecutive triple is a translate of \(\{0,1,2\}\), including those wrapping around the modular boundary. The minimum is taken over all \(\binom N3\) erasure masks, without a statistical model.

## Proof
**1. Reduction to a three-point periodic Fourier concentration operator.** Orthogonality of characters gives \(V_N^*V_N=I_3\). Hence
\[
V_{N,E^c}^*V_{N,E^c}=I_3-V_{N,E}^*V_{N,E}.
\]
The nonzero spectra of \(V_{N,E}^*V_{N,E}\) and \(V_{N,E}V_{N,E}^*\) coincide. If \(x,y\in E\), their latter matrix entry is
\[
\frac1N\sum_{k=0}^2e^{2\pi i k(x-y)/N}
=\frac1N e^{2\pi i(x-y)/N}\big(1+2\cos(2\pi(x-y)/N)\big).
\]
Conjugation by diagonal phases therefore yields the **real symmetric** matrix \(N^{-1}C_E\), with diagonal \(3\) and off-diagonal entries
\[
K(d)=1+2\cos(2\pi d/N),\qquad d=x-y\pmod N.
\]
Consequently the worst erased concentration is \(N^{-1}\max_E\lambda_{\max}(C_E)\), and the minimum retained lower bound is its complement to one.

**2. Spectral value for a consecutive triple.** Write \(u=K(1)\), \(v=K(2)\). Since \(N\ge6\), \(u>v\ge0\). For \(E=\{0,1,2\}\),
\[
C_0=\begin{pmatrix}3&u&v\\u&3&u\\v&u&3\end{pmatrix}.
\]
The odd-reflection eigenvector \((1,0,-1)\) has eigenvalue \(3-v\). The even-reflection plane has eigenvalues \(3+\tfrac12(v\pm\sqrt{v^2+8u^2})\). As \(u>v\ge0\), the plus root is strictly the largest. This gives both claimed expressions once global maximality is proved.

**3. Every nonconsecutive triple is strictly suboptimal when \(N\ge8\).** Let the circular distance between two distinct sites be the smaller of their positive modular separations. Because \(K(d)\) decreases from \(3\) to \(-1\) as circular distance grows from zero to \(N/2\), and because \(v=K(2)\ge1\) for \(N\ge8\), every pair at circular distance at least two has \(|K(d)|\le v\). A nonconsecutive three-point subset has at most one pair at circular distance one; two such pairs would force a consecutive triple. Thus, after relabelling its sites, its entrywise absolute matrix is bounded by the nonnegative matrix
\[
B=\begin{pmatrix}3&u&v\\u&3&v\\v&v&3\end{pmatrix}.
\]
For any real symmetric matrix \(C\), the Rayleigh quotient and the modulus inequality give \(\lambda_{\max}(C)\le\rho(|C|)\); monotonicity of spectral radius for nonnegative matrices gives \(\rho(|C_E|)\le\rho(B)\). On the other hand, \(C_0\) is entrywise nonnegative and, after possibly permuting its vertices, strictly dominates \(B\): it has two off-diagonal edges equal to \(u\), where \(B\) has only one, and its third edge equals \(v\). As \(u>v\ge1\), both matrices are irreducible and Perron–Frobenius strict monotonicity yields \(\rho(B)<\rho(C_0)=\lambda_{\max}(C_0)\). Therefore no nonconsecutive triple can attain equality for any \(N\ge8\).

**4. The exceptional small cycle of length six.** Here \(K(1)=2\), \(K(2)=0\), and \(K(3)=-1\). For a nonconsecutive triple, at most one pair is adjacent, so the same absolute-value comparison gives an upper spectral bound equal to that of \(B\) with edges \((u,c,c)=(2,1,1)\). Its top eigenvalue is \(4+\sqrt3\). The consecutive matrix has top eigenvalue \(3+2\sqrt2\), strictly greater because \(2\sqrt2>1+\sqrt3\) (equivalently \(2>\sqrt3\)).

**5. The exceptional small cycle of length seven.** The three distinct values \(K(1),K(2),K(3)\) are the three roots of \(p(z)=z^3-2z^2-z+1\). This follows immediately by collecting conjugate seventh roots of unity in \(1+\zeta+\cdots+\zeta^6=0\) (or expanding their elementary symmetric polynomials). Exact evaluations
\[
p(2)=-1,\quad p(9/4)=1/64,\quad p(-5/6)=-29/216,\quad p(-3/4)=13/64,
\]
and \(p(0)=1, p(1)=-1\), together with \(K(1)>K(2)>K(3)\), show
\[
2<u<9/4,\qquad 0<v<1,\qquad -5/6<K(3)<-3/4.
\]
Thus every nonadjacent pair has \(|K(d)|<c=5/6\). Any nonconsecutive triple is majorized in absolute value by a nonnegative matrix with off-diagonal edges \((u,c,c)\). Its top eigenvalue is
\[
3+\frac{u+\sqrt{u^2+8c^2}}2
<3+\frac{9/4+33/10}2=\frac{231}{40}<\frac{29}{5}.
\]
(The square-root comparison is rational: \((9/4)^2+8(5/6)^2<(33/10)^2\).) The consecutive top eigenvalue is strictly greater than \(3+\sqrt2u>3+2\sqrt2>29/5\). Hence only consecutive triples are extremal also for \(N=7\).

**6. Sharpness, positivity and equality count.** The cases in Steps 3–5 exhaust every \(N\ge6\). Cyclic translation leaves all pair separations and hence the spectrum unchanged; its \(N\) consecutive triples are distinct for \(N\ge6\). For every retained set \(E^c\), at least three distinct sampling sites remain. The corresponding \(3\)-by-\(3\) submatrix in columns \(1,z,z^2\) is a Vandermonde matrix at three distinct \(N\)-th roots, so it is invertible. Every retained Gramian is therefore positive definite; in particular its attained minimum \(A_N\) is positive. This completes the proof for all orders and the exact equality classification.

## Verification
Running `python CHECK.py` with Python 3 and NumPy independently constructs normalized complex Fourier matrices, checks orthonormality of the three columns, and directly computes retained/erased Gram eigenvalues for **every** three-site erasure mask for all \(6\le N\le36\). It verifies the predicted sharp constant and exactly the \(N\) consecutive equality masks. A separate test of the proof's absolute-kernel inequality runs through \(N=150\). The completed replay returned `CHECK_OK assertions=137685`. These are independent finite checks only; the preceding inequalities and Perron–Frobenius argument prove the theorem for arbitrary \(N\).

## Relationship to prior work
Salanevich and Strachan [1] establish structured-frame robustness estimates for Gabor and mutually unbiased bases systems under measurement erasures; their general bounds do not give the exact three-row Fourier frame constant or all worst erasure masks. Classical discrete periodic prolate work of Zhu and collaborators [2] concerns eigenvalue concentration for fixed consecutive time and frequency intervals, not optimization across all three-site time masks of equal size. Batenkov and collaborators [3] establish sharp *scale* bounds for conditioning of clustered-node partial Fourier/Vandermonde systems; they do not state the present exact all-grid three-erasure optimum or unique cyclic geometry. Abreu and Speckbacher [7] prove that among measurable sets of given length, arcs/intervals optimize continuous integral bandlimited concentration, including trigonometric polynomials on a circle. Such integral-over-sets statements do not directly compare equal-mass *atomic* point-sampling sets constrained to a discrete grid, nor give the exact coefficient here; the conceptual interval-extremality relationship is expressly acknowledged.

A published exact two-character cyclic harmonic-frame erasure theorem determines all erasure counts for a **two-dimensional** frequency band, but explicitly does not claim three Fourier rows. A published consecutive-three-site Riesz-conditioning theorem optimizes the positions of three **frequency** nodes for three fixed spatial sites; it does not compare three-site erasure masks for a fixed frequency band. Published positive Fourier quadrature for three consecutive sites concerns adjustable measurement weights and tightness rather than worst-case row deletion. The new statement does not follow from these theorems by a direct parameter choice or symmetry of the Gram operator.

## Limitations
The result is specific to three consecutive Fourier modes, unweighted sampling on a single finite cyclic group, and exactly three distinct erasures. It does not assert that consecutive masks are worst for arbitrary larger bands, different erasure cardinalities, or nonuniform weights. The upper spectral bound across all masks is not optimized. An equivalent older finite-prolate rearrangement theorem or specialized three-row erasure calculation may exist outside the inspected sources; the literature comparison is not an independent priority certification.

## References
1. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325v1, first public 2025-09-01.
2. Z. Zhu, S. Karnik, M. A. Davenport, J. Romberg and M. B. Wakin, *The Eigenvalue Distribution of Discrete Periodic Time-Frequency Limiting Operators*, arXiv:1707.05344v1, 2017.
3. D. Batenkov, L. Demanet, G. Goldman and Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, arXiv:1809.00658v1, 2018; *SIAM J. Matrix Anal. Appl.*, 2020.
4. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, published mathematical research finding, 2026.
5. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published mathematical research finding, 2026.
6. *Sharp positive Fourier sampling on three consecutive cyclic sites*, published mathematical research finding, 2026.
7. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley-Wiener space*, arXiv:2607.19192v1, first public 2026-07-21.
