# Exact linearized Gaussian Fourier-intensity spectra at every Hermite mode

## Finding

For each integer \(m\ge1\), the real differential of the Gaussian-weighted squared-intensity map at the normalized Fourier--Hermite mode has an explicit complete spectrum, an exactly one-dimensional phase kernel, and a sharp positive lower gain. This is a theorem about the linearized squared-intensity measurement, not about global nonlinear reconstruction.

Put \(B_{m,n}=\binom{m+n}{m}\) and \(R_m=\binom{2m}{m}\). For \(0\le n<m\) define
\[
\lambda_{m,n}^{\pm}=B_{m,n}+B_{m,2m-n}\pm\sqrt{(B_{m,n}-B_{m,2m-n})^2+4R_m\binom{2m}{n}}.
\]
The complete squared singular-value list, with **real** multiplicity, is: \(0\) (once), \(4R_m\) (once), each \(\lambda_{m,n}^{+}\) and \(\lambda_{m,n}^{-}\) (twice each, for \(0\le n<m\)), and \(2B_{m,n}\) (twice, for every \(n>2m\)). Coincident values from different branches have their multiplicities added.

The optimal lower-gain constant is the explicit finite expression
\[
\kappa_m=\min_{0\le n<m}\lambda_{m,n}^{-}\quad\text{with}\quad 0<\kappa_m<2.
\]
In particular \(\kappa_1=4-2\sqrt3\), and \(\kappa_2=13-\sqrt{145}\). A minimizing perturbation is a real linear combination of the two monomials \(e_n,e_{2m-n}\), with coefficients given by an eigenvector of the two-by-two block below. The result applies for EVERY \(m\ge1\), not just the computed examples.

## Assumptions and scope

Let \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) on \(\mathbb C\), let \(\mathcal F^2\) denote the holomorphic subspace of \(L^2(d\gamma)\), and let \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\), be its orthonormal basis. Complex \(\mathcal F^2\) is viewed as a **real** Hilbert space with real inner product \(\operatorname{Re}\langle\cdot,\cdot\rangle\).

For each integer \(m\ge1\), the real-linear operator \(L_m:\mathcal D_m\to L^2(d\gamma;\mathbb R)\) is
\[
L_mh(z)=\overline{e_m(z)}h(z)+e_m(z)\overline{h(z)}=2\operatorname{Re}(\overline{e_m(z)}h(z)),
\]
with natural domain \(\mathcal D_m=\{h\in\mathcal F^2:z^mh\in L^2(d\gamma)\}\), equivalently \(h=\sum_{n\ge0}c_ne_n\) with \(\sum_{n\ge0}B_{m,n}|c_n|^2<\infty\). It is the derivative along polynomial perturbations of \(F\mapsto|F|^2\) at \(e_m\); the latter map need not be defined into \(L^2(d\gamma)\) for arbitrary \(F\in\mathcal F^2\). The operator is closed on this domain, as seen from the orthogonal block decomposition below.

## Proof

**Step 1: Gaussian moments.** For nonnegative integers \(r,s\), polar integration gives
\[
\int_{\mathbb C}z^r\overline z^{\,s}\,d\gamma=\begin{cases}r!,&r=s,\\0,&r\ne s.\end{cases}
\]
Expand \(h=\sum_{n\ge0}c_ne_n\) first for polynomials. Squaring the real differential and applying this moment identity yields EXACTLY
\[
\|L_mh\|_{L^2(d\gamma)}^2
=2\sum_{n\ge0}B_{m,n}|c_n|^2
+2\operatorname{Re}\left(\frac{(2m)!}{m!}
\sum_{n+k=2m}\frac{c_nc_k}{\sqrt{n!k!}}\right).
\tag{1}
\]
There is no unproved oscillatory term: angular integration kills every term not satisfying \(n+k=2m\).

**Step 2: Real blocks.** For each \(0\le n<m\), set \(k=2m-n\), \(a=B_{m,n}\), \(b=B_{m,k}\), and \(d=\sqrt{R_m\binom{2m}{n}}\). On the four-real-dimensional span of \(e_n,ie_n,e_k,ie_k\), formula (1) becomes the direct sum of the two real symmetric matrices
\[
\begin{pmatrix}2a&2d\\2d&2b\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}2a&-2d\\-2d&2b\end{pmatrix}.
\]
They have the same two eigenvalues \(a+b\pm\sqrt{(a-b)^2+4d^2}=\lambda_{m,n}^{\pm}\). These each occur twice. At \(n=m\), the orthogonal real directions \(e_m,ie_m\) yield respectively \(4R_m\) and \(0\). Every \(n>2m\) is uncoupled, with eigenvalue \(2B_{m,n}\) on both \(e_n\) and \(ie_n\). This is an orthogonal direct sum of ALL real Fock coefficients, so the displayed list is complete, including the unbounded discrete tail.

**Step 3: Strict positivity and exact gain.** For \(n<m\), the product of the diagonal binomial numbers is strictly greater than the square of the cross term:
\[
B_{m,n}B_{m,2m-n}-R_m\binom{2m}{n}
=\frac{(m+n)!(3m-n)!-(2m)!^2}{(m!)^2n!(2m-n)!}>0.
\]
Strict positivity follows from strict logarithmic convexity of the factorial sequence, since \(m+n<2m<3m-n\). Both paired eigenvalues are therefore strictly positive. The only kernel vector is \(ie_m\).

The lower eigenvalue in the \(n=0\) block is less than the first diagonal entry \(2B_{m,0}=2\), because its off-diagonal entry is nonzero. Every upper-branch eigenvalue exceeds \(2\), the center positive eigenvalue is at least \(8\), and every uncoupled tail eigenvalue exceeds \(2\). Hence the precise smallest nonzero eigenvalue is \(\kappa_m\) as above, lying strictly between zero and two. Its eigenvector lies in the paired monomial span; thus the sharp inequality
\[
\|L_mh\|_{L^2(d\gamma)}^2\ge\kappa_m\,\inf_{t\in\mathbb R}\|h-it e_m\|_{\mathcal F^2}^2,
\qquad h\in\mathcal D_m,
\]
is attained by a polynomial direction. The right-hand side removes exactly the global-phase tangent.

**Step 4: Full domain.** Polynomial truncations converge in the multiplication graph norm because the domain weight is \(B_{m,n}\). Identity (1) extends by the direct-sum formula, and the block eigenvalues tend to infinity in the uncoupled tail. The resulting real operator is closed; its positive quadratic operator has the displayed pure-point spectrum (with repeated values counted).

## Verification

`python3 CHECK.py` checks exact Gaussian integral expansions from independent exponent bookkeeping, binomial block determinants, and strict factorial positivity for all \(1\le m\le16\), using only Python's standard library. The analytic argument is the proof for all integers \(m\ge1\); bounded computations do not certify untested orders. The checker carries no external input files.

## Relationship to prior work

Bertolini, de Dios Pont, Pineau, Ramos, and Taylor (2026) prove nonlinear \(L^2\) local phase retrieval stability for Gaussian-window STFTs at finite Hermite combinations; their Theorem 1.5 supplies an existential constant for the *amplitude* map and does not give the squared-intensity linearization's eigenvalues, multiplicities, or sharp gain. Their basic Fock normalization agrees with the normalization above. Bortolotto and Ramos (2026) prove a square-restricted coercivity inequality in Fock space at the constant function, a different (nonlinear) statement with non-sharp estimates. The earlier Gabor semidefinite-programming literature addresses optimization and measurement recovery rather than these exact local spectra. The same weight and monomial conventions are standard; only the stated full diagonalization and sharp spectral gain are assessed as potentially new here. Earlier equivalent uncatalogued Gaussian moment calculations may exist.

## Limitations

This is a **linear** theorem for squared-intensity observations in Gaussian \(L^2\), on the specified dense multiplication domain. It is not the complete nonlinear amplitude-phase retrieval theorem, does not imply a global Lipschitz inverse for squared intensities, does not cover polyanalytic higher-window ranges, and provides no uniform upper singular bound as degree grows. The lower gain is explicitly a finite minimum over \(m\) branches, rather than a simplified closed formula for the minimizing branch at every degree. No independent audit has been performed.

## References

1. S. Bertolini, J. de Dios Pont, B. Pineau, J. P. G. Ramos and M. A. Taylor, *L²-Stability for STFT phase retrieval*, arXiv:2605.20527v1 (first publicly submitted 2026-05-19), https://arxiv.org/abs/2605.20527 . Inspected HTML Theorems 1.3–1.5 and Section 2.1: https://arxiv.org/html/2605.20527v1 .
2. C. Bortolotto and J. P. G. Ramos, *A complex-analytic proof of square-restricted stable phase retrieval in Fock space*, arXiv:2608.26365v1 (2026-08-26), https://arxiv.org/abs/2608.26365 . Abstract inspected; full text could not be fetched through tested public HTML/PDF URLs.
3. *Gabor Phase Retrieval via Semidefinite Programming*, Foundations of Computational Mathematics, DOI:10.1007/s10208-024-09683-6 (related optimization literature; accessible excerpt inspected).
