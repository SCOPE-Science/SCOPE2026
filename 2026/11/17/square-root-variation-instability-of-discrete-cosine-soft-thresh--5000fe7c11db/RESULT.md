# Square-root variation instability of discrete-cosine soft thresholding

## Finding

Fix an integer \(n\ge 2\) and a threshold \(\lambda>0\). Let \(Q\) be the real orthogonal DCT-II matrix with rows
\[
q_0(i)=n^{-1/2},\qquad
q_k(i)=\sqrt{2/n}\cos\!\left(\frac{\pi k(i+1/2)}n\right),\quad
1\le k<n,\quad 0\le i<n.
\]
Let \(\eta_\lambda(t)=\operatorname{sgn}(t)(|t|-\lambda)_+\) and define the nonlinear reconstruction
\[
T_{n,\lambda}(x)=Q^{\mathsf T}\bigl((Qx)_0,\eta_\lambda((Qx)_1),\ldots,\eta_\lambda((Qx)_{n-1})\bigr).
\]
On real \(n\)-vectors equip differences with the path-variation seminorm \(V(h)=\sum_{i=0}^{n-2}|h_{i+1}-h_i|\). Its exact two-input Lipschitz coefficient
\[
L_n=\sup_{V(x-y)>0}\frac{V(T_{n,\lambda}(x)-T_{n,\lambda}(y))}{V(x-y)}
\]
is independent of \(\lambda>0\) and satisfies
\[
\boxed{L_n=\max_{M\subseteq\{1,\ldots,n-1\}}\ \max_{1\le a<n}
\sum_{b=1}^{n-1}\left|\frac2n\sum_{k\in M}
\sin\frac{\pi ka}n\sin\frac{\pi kb}n\right|.}
\]
Every maximizing mask and step column yields a *pair of finite real data vectors attaining equality*; this is not only an infinitesimal supremum. In particular, the dimension-uniform bounds
\[
\boxed{\frac12+\frac{n-2}{2\sqrt{3n}}\ \le L_n\le\sqrt{n-1}}
\]
hold for every \(n\ge2\). Thus \(L_n=\Theta(\sqrt n)\) as \(n\to\infty\), although scalar soft thresholding is nonexpansive in the Euclidean norm.

## Assumptions and scope

Only real vectors and the stated **orthonormal DCT-II** convention are used. The constant-frequency coefficient is not thresholded. The finite path variation has \(n-1\) nonperiodic edges and no endpoint wrapping. Inputs need not be monotone or nonnegative. The result concerns two-input perturbations \(T(x)-T(y)\), not necessarily the variation of one reconstruction.

## Proof

**1. Linearized masks and global Lipschitz norm.** Each scalar \(\eta_\lambda\) is continuous and affine on the three intervals separated by \(\pm\lambda\), with derivative zero or one. Hence \(T_{n,\lambda}\) is a continuous finite-piecewise-affine map. On a region where precisely the nonconstant indices in \(M\) are active, its linear part is the orthogonal projection
\[
P_M=Q^{\mathsf T}\operatorname{diag}(1,{\bf1}_{1\in M},\ldots,{\bf1}_{n-1\in M})Q.
\]
Along any line segment, only finitely many affine regions are crossed unless a coordinate lies on a threshold hyperplane, in which case a constant affine trace applies; integrating along the segment proves the global two-input seminorm Lipschitz bound by the largest \(V\)-operator norm of \(P_M\). Each \(P_M\) preserves constants.

Conversely every mask \(M\) is realized on a nonempty open set: choose a DCT coefficient vector with coefficient \(2\lambda\) for each \(k\in M\) and zero for other nonconstant coefficients. In that neighborhood, the difference of two reconstructions equals \(P_M\) applied to their input difference. Therefore the global coefficient equals \(\max_M\|P_M\|_{V\to V}\). No derivative at a threshold is required.

**2. Exact step-response formula.** Let \(H_a(i)={\bf1}_{i\ge a}\), for \(1\le a<n\). Any \(h\in\mathbb R^n\) has the unique decomposition
\[
h=h_0{\bf1}+\sum_{a=1}^{n-1}(h_a-h_{a-1})H_a.
\]
Since \(P_M\) preserves constants, the triangle inequality shows \(\|P_M\|_{V\to V}=\max_a V(P_MH_a)\), with equality on a single step. Write \(\theta_k=\pi k/n\). For \(k\ge1\), direct geometric-series summation and a cosine difference give
\[
\langle q_k,H_a\rangle=-\sqrt{2/n}\frac{\sin(a\theta_k)}{2\sin(\theta_k/2)},\qquad
q_k(b)-q_k(b-1)=-2\sqrt{2/n}\sin(b\theta_k)\sin(\theta_k/2).
\]
Their product is \((2/n)\sin(a\theta_k)\sin(b\theta_k)\); the constant mode has zero difference. Consequently
\[
(P_MH_a)_b-(P_MH_a)_{b-1}=K_M(b,a):=\frac2n\sum_{k\in M}\sin(a\theta_k)\sin(b\theta_k)
\]
for \(1\le a,b<n\). Summing absolute values yields the exact boxed formula. The locally realized mask together with a sufficiently small nonzero step perturbation gives an *exact finite pair* attaining the maximizing column sum.

**3. Orthogonal upper bound.** The sine matrix \(U_{bk}=\sqrt{2/n}\sin(\pi bk/n)\), \(1\le b,k<n\), is orthogonal. Hence \(K_M=U\operatorname{diag}({\bf1}_M)U^{\mathsf T}\) is an orthogonal projection on \(\mathbb R^{n-1}\). Its columns have Euclidean norm at most one; Cauchy–Schwarz bounds every column absolute sum by \(\sqrt{n-1}\).

**4. Quantitative lower bound.** Choose \(M\) randomly by independent fair Bernoulli selection of each \(k=1,\ldots,n-1\). Fix any column \(a\). The diagonal entry has expectation \(1/2\), since \(K_{\{1,\ldots,n-1\}}=I\). For every \(b\ne a\), sine orthogonality gives
\[
K_M(b,a)=\frac1n\sum_{k=1}^{n-1}\varepsilon_k\sin(a\theta_k)\sin(b\theta_k)
\]
with independent symmetric signs \(\varepsilon_k\). Its variance is
\[
\sigma_{a,b}^2=\frac1{n^2}\sum_{k=1}^{n-1}\sin^2(a\theta_k)\sin^2(b\theta_k)\ge\frac1{4n}.
\]
Indeed the trigonometric sum equals \(n/4\) for \(b\ne a,n-a\), and \(3n/8\) for \(b=n-a\ne a\). This follows by expanding \(\sin^2u\sin^2v\) into cosine terms and summing roots of unity. For any Rademacher linear combination \(X\), one has \(\mathbb E X^4\le3(\mathbb E X^2)^2\); Hölder therefore gives \(\mathbb E|X|\ge\sigma/\sqrt3\). Thus each off-diagonal entry obeys \(\mathbb E|K_M(b,a)|\ge 1/(2\sqrt{3n})\), and the expected diagonal absolute value is \(1/2\). Summing \(n-2\) off-diagonal contributions yields
\[
\max_M\sum_b|K_M(b,a)|\ge\mathbb E\sum_b|K_M(b,a)|\ge\frac12+\frac{n-2}{2\sqrt{3n}}.
\]
Together with step 3 this completes the claim for every \(n\), including \(n=2\).

## Verification

The provided standalone, standard-library Python script `verify_dct_bv.py` checks, for all masks at lengths \(2\) through \(9\), the exact step-kernel identity to numerical tolerance, the finite exact-mask maximum, and both proved dimension bounds. Further tests verify orthogonal-projection upper bounds up to length \(100\) and finite perturbations inside nonlinear active-set regions. These diagnostics are not an infinite proof; steps 1–4 above supply the proof for all lengths and thresholds. Run `python3 verify_dct_bv.py`.

## Relationship to prior work

The orthogonal cosine basis and its difference-operator interpretation are classical; see Strang (1999). Classical wavelet coefficient thresholding and total-variation restoration are discussed by Durand and Froment (2003). Neither paper's inspected text states the sharp finite-mask variation norm for *DCT-II soft thresholding* or the uniform square-root upper/lower bounds proved here. The usual Euclidean nonexpansivity of coordinatewise soft thresholding is insufficient to control this path-variation seminorm uniformly in dimension. An earlier Haar soft-threshold variation result gives different logarithmic growth for the Haar basis; it does not imply the present DCT/DST finite-mask identity.

## Limitations

The optimal leading constant in \(L_n/\sqrt n\), and whether it converges, are not determined. The exact finite formula is an exponential mask maximization, not a polynomial-time algorithm. The theory does not cover DCT-I/III/IV, nonorthogonal transforms, hard thresholding, other edge weights, or two-dimensional image variation. Although searches and comparisons found no covering statement, an unindexed general unconditional-projection theorem may contain or imply parts of the asymptotic result; historical priority is not independently certified.

## References

1. G. Strang, "The Discrete Cosine Transform," *SIAM Review* **41** (1999), 135–147, DOI: 10.1137/S0036144598336745, first available online 1999-01-22. https://epubs.siam.org/doi/10.1137/S0036144598336745
2. S. Durand and J. Froment, "Reconstruction of Wavelet Coefficients Using Total Variation Minimization," *SIAM Journal on Scientific Computing* **24** (2003), 1754–1767, DOI: 10.1137/S1064827501397792, electronically published 2003-04-15. https://doi.org/10.1137/S1064827501397792
