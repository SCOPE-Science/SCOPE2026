# Minimal first-harmonic projections on real Grassmannians: a strict rank hierarchy

## Finding

Let \(X_{n,k}\) be the compact real Grassmannian of rank-\(k\) orthogonal projectors in \(\mathbb R^n\), with invariant probability measure, where \(n\geq2\) and \(1\leq k<n\). Let \(V_{n,k}\subset C(X_{n,k};\mathbb R)\) consist of functions \(P\mapsto\operatorname{tr}(AP)\) with \(A=A^{\mathsf T}\) and \(\operatorname{tr} A=0\). Write \(T_{n,k}\) for the invariant \(L^2\)-orthogonal projector onto \(V_{n,k}\). This is a **minimum-norm projection** from \(C(X_{n,k};\mathbb R)\) onto \(V_{n,k}\), among all bounded linear projections.

Set \(D_n=(n-1)(n+2)/2\), \(P_0=\operatorname{diag}(I_k,0)\), and let \(Q\) be an invariant-uniform rank-\(k\) projector. The **exact finite-dimensional minimal projection constant** is
\[
\Lambda_{n,k}:=\|T_{n,k}\|_{C\to C}
=\frac{D_n}{k(n-k)}\mathbb E\left|n\operatorname{tr}(P_0Q)-k^2\right|.
\]
In particular \(\Lambda_{n,k}=\Lambda_{n,n-k}\). For every fixed positive integer \(k\),
\[
\lim_{n\to\infty}\frac{\Lambda_{n,k}}n
=c_k:=\frac{2s^s e^{-s}}{k\Gamma(s)},\qquad s=\frac{k^2}{2}.
\]
The constants satisfy the **strict rank hierarchy**
\[
c_1<c_2<c_3<\cdots<\frac1{\sqrt\pi},\qquad
c_1=\sqrt{\frac2{\pi e}},\qquad c_2=4e^{-2},\qquad
c_k=\frac1{\sqrt\pi}\left(1-\frac1{6k^2}+O(k^{-4})\right).
\]
For every integer rank sequence satisfying \(k_n\to\infty\) and \(k_n=o(\sqrt n)\), the constants enter the universal Gaussian window:
\[
\lim_{n\to\infty}\frac{\Lambda_{n,k_n}}n=\frac1{\sqrt\pi}.
\]
Thus the first-harmonic projection instability increases sharply with fixed rank, then reaches a common leading coefficient in the growing-sparse-rank regime.

## Assumptions and scope

All projections, functions, and measures are **real**. The invariant measure on \(X_{n,k}\) is normalized to total mass one, and the domain norm is the uniform norm. The lower-case \(k\) is a rank, not a polynomial degree. The subspace \(V_{n,k}\) omits the constants. The result covers \(n\ge2\), \(1\le k<n\) at finite dimension, and gives limiting behavior for fixed rank or \(k=o(\sqrt n)\) with \(k\to\infty\). It makes no assertion for ranks proportional to \(n\), or for \(k\) comparable to \(\sqrt n\).

## Proof

**1. Covariance and the exact projector.** Put \(P^\circ=P-kI/n\), and let \(\mathcal S_0\) denote the traceless real symmetric matrices. This is a \(D_n\)-dimensional irreducible orthogonal-conjugation module. Orthogonal invariance and \(\|P^\circ\|_F^2=k(n-k)/n\) give the exact covariance identity
\[
\int_{X_{n,k}}\operatorname{tr}(AP)\operatorname{tr}(BP)\,d\mu(P)
=\frac{k(n-k)}{nD_n}\operatorname{tr}(AB)
\quad (A,B\in\mathcal S_0).
\]
The orthogonal projection onto \(V_{n,k}\) consequently has continuous reproducing kernel
\[
K_{n,k}(P,Q)=\frac{nD_n}{k(n-k)}\left(\operatorname{tr}(PQ)-\frac{k^2}{n}\right).
\]
As every evaluation point is in one orthogonal-group orbit, \(\|T_{n,k}\|=\int|K_{n,k}(P_0,Q)|\,d\mu(Q)\), establishing the exact expectation formula. The sign of the kernel is discontinuous across its zero set, but continuous approximations give the norm as a supremum; an actual continuous norming input is not asserted. Complementing both projectors proves \(\Lambda_{n,k}=\Lambda_{n,n-k}\).

**2. Why this is the minimum over all projections.** Take any bounded projection \(R:C(X_{n,k})\to V_{n,k}\) and average its conjugates under the compact orthogonal group. The average is an equivariant projection \(\overline R\) with \(\|\overline R\|\le\|R\|\). Every equivariant map from \(C(X_{n,k})\) to \(\mathcal S_0\) has a unique finite matrix-valued representing measure. Its total variation is invariant, hence a multiple of \(\mu\). Its equivariant density at \(P_0\) is fixed under \(O(k)\times O(n-k)\), whose fixed subspace in \(\mathcal S_0\) is exactly the line \(\mathbb R(P_0-kI/n)\). Therefore the map is a scalar multiple of \(f\mapsto\int f(Q)(Q-kI/n)d\mu(Q)\), and the identity-on-\(V_{n,k}\) condition determines the scalar. Thus \(\overline R=T_{n,k}\), and \(\|T_{n,k}\|\le\|R\|\).

**3. Exact centered second moment.** Writing \(Z=n\operatorname{tr}(P_0Q)\), the preceding covariance yields
\[
\mathbb EZ=k^2,\qquad
\mathbb E(Z-k^2)^2=\frac{k^2(n-k)^2}{D_n}.
\]
These identities will supply uniform integrability; no approximate independence is assumed at finite dimension.

**4. Fixed-rank limit.** If \(U\) is Haar distributed on \(O(n)\), then \(\operatorname{tr}(P_0Q)\) equals the squared Frobenius norm of the leading \(k\times k\) block of \(U\). Jiang's Haar-orthogonal block theorem, applied with fixed \(k\), shows that \(Z\) converges in law to \(Y\sim\chi^2_{k^2}\). The exact centered second moment bounds its second moments uniformly, hence \(\mathbb E|Z-k^2|\to\mathbb E|Y-k^2|\). For \(s=k^2/2\), direct integration of the gamma density (or integration by parts at the mean) gives
\[
\mathbb E|Y-2s|=\frac{4s^se^{-s}}{\Gamma(s)}.
\]
Since \(D_n/[nk(n-k)]\to1/(2k)\), this proves the formula for \(c_k\).

**5. Strict hierarchy.** The continuous interpolation of the constants is
\[
c(s)=\sqrt2\,\frac{s^{s-1/2}e^{-s}}{\Gamma(s)},\qquad s>0.
\]
Its logarithmic derivative has the strictly positive integral representation
\[
\frac{d}{ds}\log c(s)=\log s-\frac1{2s}-\psi(s)
=\int_0^\infty e^{-st}\left(\frac12\coth\frac t2-\frac1t\right)dt>0.
\]
The final inequality holds because \(\coth u>1/u\) for all \(u>0\). Strict increase with \(s=k^2/2\) follows. Stirling's expansion for \(\Gamma(s)\) yields the displayed limit and \(k^{-2}\) correction.

**6. Growing sparse ranks.** If \(k=k_n\to\infty\) with \(k=o(\sqrt n)\), Jiang's theorem supplies total-variation approximation of the \(k\times k\) leading block of \(\sqrt nU\) by \(k^2\) independent standard normals. It follows that \(W_n=(Z-k^2)/k\) has the same weak limit as \((\chi^2_{k^2}-k^2)/k\), namely \(N(0,2)\). The exact variance identity above gives \(\mathbb EW_n^2=(n-k)^2/D_n\to2\), so the absolute first moments converge: \(\mathbb E|W_n|\to2/\sqrt\pi\). Since \(\Lambda_{n,k}/n=D_n\mathbb E|W_n|/[n(n-k)]\to\frac12(2/\sqrt\pi)\), the universal sparse-rank limit follows.

## Verification

The accompanying standalone script `check.py` tests the rank-one beta identity through independent numerical integration for twenty dimensions, checks the strict-gamma-constant hierarchy for 49 consecutive ranks, and compares the invariant-kernel norm and covariance against independent Haar-orthogonal Monte Carlo samples in four small-dimensional cases. These diagnostics do not establish the universal claims: the proof uses exact covariance, compact-group averaging, gamma/digamma identities, Jiang's published total-variation theorem, and an explicit second-moment uniform-integrability argument. For \(k=1\), \(\operatorname{tr}(P_0Q)\sim\operatorname{Beta}(1/2,(n-1)/2)\) gives the additional exact check
\[
\Lambda_{n,1}=\frac{2(n+2)}{\sqrt n\,B(1/2,(n-1)/2)}\left(1-\frac1n\right)^{(n-1)/2}.
\]

## Relationship to prior work

Jiang's 2006 theorem proves total-variation Gaussian approximation for small blocks of Haar orthogonal matrices, the asymptotic distributional input here. Defant, Galicer, Mansilla, Mastyło and Muro (first available as a 2024 preprint, published 2026) study minimal projections onto polynomial spaces on real spheres and cover the relevant sphere/rank-one harmonic setting in a broader spherical-polynomial context. Neither provides, in the inspected sections, this all-rank real Grassmannian projection constant, its strict fixed-rank hierarchy, or the \(k=o(\sqrt n)\) regime. The rank-one identity and the Gaussian-block theorem are not claimed as new. The claimed contribution is their combination with exact Grassmann covariance and minimality to give a sharp rank-profile theorem for the nontrivial rank families.

## Limitations

The asymptotic analysis leaves the transition \(k\asymp\sqrt n\) and dense ranks \(k/n\to\theta\in(0,1)\) unresolved. The theorem does not supply elementary closed forms for the finite-rank expectation at general \(k\ge2\). Source inspection and database searching cannot rule out unindexed equivalent formulas, or more general results that imply this rank-profile theorem. The finding has had self-review only; no independent audit has been performed.

## References

1. Tiefeng Jiang, “How many entries of a typical orthogonal matrix can be approximated by independent normals?”, arXiv:math/0601457, first public version 18 January 2006; *Annals of Probability* 34 (2006), 1497–1529. https://arxiv.org/abs/math/0601457
2. Andreas Defant, Daniel Galicer, Martín Mansilla, Mieczysław Mastyło and Santiago Muro, “Minimal projections onto spaces of polynomials on real Euclidean spheres”, arXiv:2405.12123, first public version 20 May 2024; *Journal of the London Mathematical Society* (2026), e70429. https://arxiv.org/abs/2405.12123
