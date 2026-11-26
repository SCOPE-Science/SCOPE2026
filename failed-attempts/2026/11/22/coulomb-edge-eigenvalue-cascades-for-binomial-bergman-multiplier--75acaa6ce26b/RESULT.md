# Coulomb-edge eigenvalue cascades for binomial Bergman multiplier Gram operators

## Finding

Let \(A^2_\alpha(\mathbb D)\) be the usual analytic weighted Bergman Hilbert space with \(\alpha>-1\), and let \(V_{m,a}=M_{z^m+a}^{*}M_{z^m+a}\) for every integer \(m\ge2\) and \(a\in\mathbb C\). Put \(c=|a|\) and \(L_c=(1-c)^2\). The following is valid simultaneously for all these parameters.

1. The Fredholm essential spectrum is exactly \(\sigma_{\mathrm{ess}}(V_{m,a})=[(1-c)^2,(1+c)^2]\). The \(m\) canonical congruence-class reducing subspaces each have this essential spectrum.
2. If \(0\le c<1\), **each** of these \(m\) reducing subspaces has infinitely many discrete eigenvalues strictly below \(L_c\); their only possible accumulation point below or at the essential band is \(L_c\). If \(0<c<1\), there is a constant \(C=C(\alpha,m,c)>0\) and \(\epsilon_0>0\) such that in every congruence class, counting eigenvalues with multiplicity,
   \[
   \#\{\lambda\in\sigma(J_r):\lambda<L_c-\epsilon\}\ge C\epsilon^{-1/2}\qquad(0<\epsilon<\epsilon_0).
   \]
3. If \(c\ge1\), the **entire spectrum** equals the essential interval, with no eigenvalues outside it: \(\sigma(V_{m,a})=[(c-1)^2,(c+1)^2]\). No claim about embedded eigenvalues is needed or made.

For \(c=0\), the discrete eigenvalues on a congruence class are explicitly the weight ratios below one. For \(c>0\), the individual half-line Jacobi blocks have simple eigenvalues outside the band, although eigenvalues in different blocks may coincide.

## Assumptions and scope

Use the normalized measure \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\). With \(e_n=z^n/\sqrt{\omega_n}\),
\[
\omega_n=\|z^n\|_{A^2_\alpha}^{2}=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)},\qquad
\omega_0=1.
\]
All spectra concern the bounded self-adjoint positive operator on this analytic Bergman space, not a harmonic-Bergman Toeplitz compression or the non-self-adjoint multiplier itself. The essential spectrum uses the Fredholm definition. A rotation and unimodular scalar remove the phase of \(a\), so it suffices to prove the assertion for real \(c\ge0\).

For each residue \(r\in\{0,\ldots,m-1\}\), let \(\mathcal H_r=\overline{\operatorname{span}}\{e_{r+jm}:j\ge0\}\), and let \(J_r=V_{m,c}|_{\mathcal H_r}\). These subspaces reduce both the multiplication shift by \(z^m\) and its Gram operator.

## Proof

**1. Exact Jacobi representation.** Writing \(W=M_{z^m}\), one has
\[
We_n=\sqrt{\frac{\omega_{n+m}}{\omega_n}}e_{n+m},\qquad
V_{m,c}=W^*W+c(W+W^*)+c^2I.
\]
Set \(\beta=\alpha+1>0\) and
\[
w_{r,j}=\sqrt{\frac{\omega_{r+(j+1)m}}{\omega_{r+jm}}}
=\left(\frac{(r+jm+1)_m}{(r+jm+\alpha+2)_m}\right)^{1/2}.
\]
The real symmetric Jacobi block \(J_r\) has diagonal \(w_{r,j}^{2}+c^2\) and off-diagonal \(cw_{r,j}\) between sites \(j\) and \(j+1\). Here \((x)_m=x(x+1)\cdots(x+m-1)\). Its weights satisfy, uniformly in the finite set of residues,
\[
w_{r,j}=1-\frac{\beta}{2j}+O(j^{-2}),\qquad
w_{r,j}^{2}=1-\frac{\beta}{j}+O(j^{-2})\quad(j\to\infty).
\]
These follow by expanding the fixed finite product; in particular \(0<w_{r,j}<1\).

**2. Essential spectral interval.** Every \(J_r\) is a compact perturbation of the free half-line Jacobi operator with constant diagonal \(1+c^2\) and off-diagonal \(c\), since the two sequences of matrix coefficients converge. The free operator is \((1+c^2)I+c(S+S^*)\) on \(\ell^2(\mathbb N_0)\), which has spectrum and Fredholm essential spectrum \([(1-c)^2,(1+c)^2]\) (for \(c=0\), the singleton \(\{1\}\)). Thus the same is the essential spectrum of each block, and of their finite direct sum.

**3. Attractive Coulomb edge for \(0<c<1\).** Conjugate \(J_r\) by the diagonal sign unitary \((-1)^j\), giving negative off-diagonals. For a nonnegative finitely supported real sequence \(y\), supported away from zero, the exact quadratic-form identity is
\[
\begin{aligned}
\langle (J_r-L_cI)y,y\rangle
={}&c\sum_{j\ge0}(y_{j+1}-y_j)^2
+\sum_{j\ge0}(w_{r,j}^2-1)y_j^2\\
&+2c\sum_{j\ge0}(1-w_{r,j})y_jy_{j+1}.
\end{aligned}
\]
The first sum includes the left edge of the finite support (the omitted \(cy_0^2\) boundary term vanishes because \(y_0=0\)). Use \(2y_jy_{j+1}\le y_j^2+y_{j+1}^2\). For all sites with \(j\ge1\), the combined site coefficient is
\[
A_{r,j}=w_{r,j}^2-1+c(1-w_{r,j})+c(1-w_{r,j-1})
=-\frac{\beta(1-c)}{j}+O(j^{-2}).
\]
There is \(N_0\), uniform across residues, such that \(A_{r,j}\le-\beta(1-c)/(4N)\) for every integer \(N\ge N_0\) and \(N\le j\le2N\).

Choose a constant \(K>0\) large enough that \(c\pi^2/K^2\le\beta(1-c)/8\). On any integer interval of length \(\ell=\lceil K\sqrt N\rceil\) contained in \([N,2N]\), take the nonnegative Dirichlet sine vector \(y_j=\sin[\pi(j-J+1)/(\ell+1)]\), with zero entries outside that interval. Its exact discrete Dirichlet energy is
\[
\sum_{j\ge0}(y_{j+1}-y_j)^2
=4\sin^2\left(\frac{\pi}{2(\ell+1)}\right)\|y\|_2^2
\le\frac{\pi^2}{(\ell+1)^2}\|y\|_2^2.
\]
Combining the estimates gives the uniform strict Rayleigh bound
\[
\langle (J_r-L_cI)y,y\rangle\le-\frac{\eta}{N}\|y\|_2^2,
\qquad \eta=\frac{\beta(1-c)}8>0.
\]
For all sufficiently large \(N\), the interval \([N,2N]\) accommodates at least \(b\sqrt N\) disjoint such supports for a fixed \(b>0\), with at least one zero site between consecutive supports. They are orthogonal, and since \(J_r\) is tridiagonal their mixed quadratic-form terms vanish. Hence their entire span has Rayleigh quotient at most \(L_c-\eta/N\). The spectral min–max principle, together with the essential-spectrum statement, proves at least \(b\sqrt N\) discrete eigenvalues strictly below this threshold, counting multiplicities. Taking \(N=\lfloor\eta/(2\epsilon)\rfloor\) for sufficiently small \(\epsilon\) yields the asserted \(C\epsilon^{-1/2}\) lower count. The same proof applies to every residue.

**4. Zero coefficient.** If \(c=0\), \(J_r\) is diagonal with entries \(w_{r,j}^2<1\), tending to one. Thus each residue has infinitely many discrete eigenvalues below \(L_0=1\). In this case they are exactly \(\omega_{r+(j+1)m}/\omega_{r+jm}\).

**5. Non-attractive regime.** If \(c\ge1\), for every \(z\in\mathbb D\) one has \(c-1\le|z^m+c|\le c+1\). Integrating the squared pointwise inequalities gives
\[
(c-1)^2 I\le V_{m,c}\le(c+1)^2 I.
\]
The full spectrum is therefore contained in the interval already filled by the essential spectrum, giving equality. Finally, for \(c>0\) each Jacobi block has nonzero off-diagonal coefficients, so its eigenvectors are determined by their first coordinate and hence all its eigenvalues are simple. This does not rule out coincidences between different residues.

## Verification

`python3 check_binomial_bergman.py` uses only the Python standard library. It checks 351 finite, exactly rational inequalities for integer weighted-Bergman exponents, several binomial degrees and coefficients, and strict monomial moment monotonicity. Its success marker is `BERGMAN_BINOMIAL_EXACT_CHECK_OK 351`. These tests only corroborate the matrix formulas and finite trial-vector signs; the infinite eigenvalue count, all real \(\alpha>-1\), and the asymptotic lower count follow from the proof above, not from enumeration.

## Relationship to prior work

Santana-Rivero and Seco (2026), arXiv:2611.18044v1, treat spectral descriptions of \(M_f^*M_f\), including degree-two Bergman polynomials. Their Theorem 1.3 gives nonexistence of point eigenvalues when the associated differential-equation leading polynomial meets the unit circle, and bounds eigenspace dimension otherwise. Their concluding Section 6 explicitly identifies the existence of one-dimensional eigenspaces as difficult, and asks about higher degree. The result here supplies an explicit infinite family of eigenvalues in all congruence sectors for the nonzero binomial class, without solving their differential equation. The essential band itself is compatible with their general essential-spectrum result, and is not asserted as novel by itself.

Monsalve-López and Seco (2025), arXiv:2501.12298v1, completely characterize the degree-one Bergman-type case and use Jacobi analysis. Their theorem is acknowledged. Reducing a higher monomial shift into residue classes produces different moment sequences; the all-residue assertion for every degree and every \(\alpha>-1\), plus the quantitative \(\epsilon^{-1/2}\) counting lower bound, is the new claim. General Jacobi oscillation criteria (Luef and Teschl) may imply the qualitative accumulation after the block reduction, but do not themselves explicitly state this Bergman binomial classification or the proved counting estimate. This relationship is a bibliographic risk, not a claim of independence from established Jacobi theory.

## Limitations

This theorem does not supply exact individual nonzero-parameter eigenvalues, sharp constants in the eigenvalue counting law, a matching upper counting estimate, or a classification of eigenvalues inside the essential interval. It is restricted to binomial analytic symbols and the standard beta-weighted Bergman spaces. It makes no claim about all degree-two polynomial symbols. No independent validation has been performed.

## References

1. J. Airán Santana-Rivero and Daniel Seco, *Another step towards spectral descriptions of cyclic functions*, arXiv:2611.18044v1 (first posted 2026-11-13), https://arxiv.org/abs/2611.18044.
2. Miguel Monsalve-López and Daniel Seco, *Towards spectral descriptions of cyclic functions*, arXiv:2501.12298v1 (2025), https://arxiv.org/html/2501.12298v1; *Annals of Functional Analysis* 16 (2025), 52, DOI:10.1007/s43034-025-00446-0.
3. Franz Luef and Gerald Teschl, *On the Finiteness of the Number of Eigenvalues of Jacobi Operators below the Essential Spectrum*, arXiv:math/0109213, https://arxiv.org/abs/math/0109213.
4. Shunhua Sun, Dechao Zheng, Changyong Zhong, *Multiplication Operators on the Bergman Space and Weighted Shifts*, *Journal of Operator Theory* 59 (2008), 435–454.
