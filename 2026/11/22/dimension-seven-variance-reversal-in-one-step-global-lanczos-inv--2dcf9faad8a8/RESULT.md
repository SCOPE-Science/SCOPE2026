# Dimension-seven variance reversal in one-step global Lanczos inverse-trace correction

## Finding

Let \(A\in\mathbb R^{n\times n}\) be real symmetric positive definite with exactly two eigenvalues \(0<a<b\), of multiplicities \(p,q\ge1\), respectively, and set \(n=p+q\), \(\mu=(pa+qb)/n\), and \(\kappa=b/a>1\). Let \(G_s\) be the one-step full-size global Lanczos inverse-trace estimate with a Hermite-residual correction using \(s\ge1\) independent Rademacher probes, and \(T_s\) ordinary Hutchinson with the same probes and exact inverse products. For every realization,
\[
G_s-\operatorname{tr}(A^{-1})=\left(1-\frac{ab}{\mu^2}\right)\left(T_s-\operatorname{tr}(A^{-1})\right).
\]
If the ordinary variance is nonzero, the corrected-to-ordinary variance ratio is
\[
R=\left(1-\frac{ab}{\mu^2}\right)^2=\left(1-\frac{n^2\kappa}{(p+q\kappa)^2}\right)^2.
\]
The ratio is independent of the eigenvectors and probe budget in the nonzero-variance case. Diagonal \(A\) gives zero variance for both estimators, and the samplewise identity still holds. In the nonzero-variance case the correction is exact for every realization if and only if \(p>q\) and \(\kappa=(p/q)^2\).

**Sharp range of variance amplification.** At fixed multiplicities with \(p/q>3+2\sqrt2\), the correction strictly amplifies variance exactly for \(\kappa_-<\kappa<\kappa_+\), where
\[
\kappa_\pm=\left(\frac{n/\sqrt2\pm\sqrt{n^2/2-4pq}}{2q}\right)^2.
\]
In this regime the unique maximum over \(\kappa>1\) is \((p-q)^4/(16p^2q^2)\), attained at \(\kappa=p/q\). For all other integer multiplicities, \(R<1\) at every finite \(\kappa>1\), and \(\sup_{\kappa>1} R=1\) is approached as \(\kappa\to\infty\) but is not attained. In particular the value at the interior stationary contrast, when it exists, is not always a global maximum.

**Minimum dimension and Frobenius contrast.** Seven is the least dimension permitting strict variance amplification. For six eigenvalues \(1\) and one \(6\), with nonzero ordinary variance, the ratio is \(625/576>1\). Even there, the Hermite residual satisfies \(\|M\|_F^2/\|A^{-1}\|_F^2=625/2976<1\). For each \(n\ge7\), the largest possible ratio among all two-level spectra is
\[
\frac{(n-2)^4}{16(n-1)^2},
\]
attained at \(p=n-1,q=1,\kappa=n-1\) with a noncoordinate-aligned spike. In the same spike family \(\kappa=(n-1)^2\) makes the corrected estimator exact with one sign probe.

## Assumptions and scope

All arithmetic, including inverse products, is exact. Full-size global Lanczos starts at \(I_n\) and stops at one node. The \(z_j\) are real sign vectors whose entries are independent and equiprobable on \(\{-1,1\}\), independent over probes. The definitions used are
\[
T_s=\frac1s\sum_{j=1}^s z_j^{\mathsf T}A^{-1}z_j,\qquad h(x)=\frac2\mu-\frac{x}{\mu^2},\qquad M=A^{-1}-h(A),\qquad
G_s=\frac n\mu+\frac1s\sum_{j=1}^s z_j^{\mathsf T}Mz_j.
\]
The ratio refers only to matrices with positive ordinary Hutchinson variance. For every \((p,q,\kappa)\) in scope there are such matrices: start with a diagonal model and rotate a coordinate with eigenvalue \(a\) and one with eigenvalue \(b\) by \(\pi/4\), giving a nonzero off-diagonal entry of \(A^{-1}\).

## Proof

**One-node formula and samplewise reduction.** The first diagonal coefficient with normalized starting block \(I_n/\sqrt n\) is \(\langle I_n/\sqrt n,A I_n/\sqrt n\rangle_F=\mu\). For the inverse function \(f(x)=1/x\), the one-node quadrature gives \(nf(\mu)=n/\mu\). Matching value and derivative at \(\mu\) gives the stated \(h\), with \(\operatorname{tr}(h(A))=n/\mu\). The identity \(x+ab/x=a+b\) on both eigenspaces gives \(A=(a+b)I_n-abA^{-1}\), so
\[
M=\alpha A^{-1}+\beta I_n,\qquad \alpha=1-\frac{ab}{\mu^2},\qquad \beta=\frac{a+b}{\mu^2}-\frac2\mu.
\]
For every sign vector \(z\), \(z^{\mathsf T}I_nz=n\). Thus subtracting \(\operatorname{tr}(A^{-1})=n/\mu+\operatorname{tr}(M)\) from \(G_s\) cancels the identity part of the residual on each probe, which proves the scalar samplewise error formula. The estimators are unbiased since \(\mathbb E z_jz_j^{\mathsf T}=I_n\). For symmetric \(D\), \(z^{\mathsf T}Dz-\operatorname{tr}D=2\sum_{i<j}D_{ij}z_i z_j\); the summands are uncorrelated for distinct pairs. Thus \(\operatorname{Var}(T_s)=4s^{-1}\sum_{i<j}(A^{-1})_{ij}^2\), which is zero exactly when \(A^{-1}\), equivalently \(A\), is diagonal. If this variance is positive, the ratio is exactly \(\alpha^2\).

**Classification at fixed multiplicities.** Write \(H(\kappa)=n^2\kappa/(p+q\kappa)^2\), so \(\alpha=1-H\). The equation \(\alpha=0\) factors as \((\sqrt\kappa-1)(q\sqrt\kappa-p)=0\). Its nontrivial root is admissible exactly when \(p>q\). For any fixed multiplicities, \(H(1)=1\), \(H\) is positive, and \(H(\kappa)\to0\) as \(\kappa\to\infty\). Its derivative is
\[
H'(\kappa)=\frac{n^2(p-q\kappa)}{(p+q\kappa)^3}.
\]
If \(p\le q\), then \(0<H<1\) for \(\kappa>1\). If \(p>q\), its unique maximum on that domain is \(n^2/(4pq)\), at \(\kappa=p/q\). Since \(H>0\), variance amplification is equivalent to \(H>2\). Thus it is possible exactly when \(p>q\) and \(n^2>8pq\), or equivalently when \(p/q>3+2\sqrt2\). Equality at this threshold is impossible for integer multiplicities. Solving \(H=2\) gives the two stated endpoints by the quadratic formula in \(\sqrt\kappa\); both lie beyond 1 because the peak lies beyond 1, \(H(1)=1\), and \(H\) decreases to 0 beyond the peak.

On the amplifying interval, \(R=(H-1)^2\) is strictly increasing as a function of \(H\), and outside the interval \(R\le1\). Hence the unique maximum in the amplifying regime is \((n^2/(4pq)-1)^2=(p-q)^4/(16p^2q^2)\). In the nonamplifying cases \(0<H<2\) at every finite admissible contrast, so \(R<1\) everywhere while its large-contrast limit is 1. This proves the contrasting, nonattained supremum in that regime.

**Sharp dimension and examples.** For fixed \(n\), \(pq\ge n-1\), with equality at the extreme multiplicities. The order \(p=n-1,q=1\) places the maximizing point in the domain for \(n\ge7\); among amplifying choices it maximizes \(n^2/(4pq)\), and the nonamplifying choices cannot compete with its ratio. The inequality \(n^2>8(n-1)\) first holds at \(n=7\) among integers \(n\ge2\). At \(n=7,p=6,q=1,\kappa=6,a=1\), one has \(\mu=12/7\), \(\alpha=-25/24\), and the amplification interval is \((9/2,8)\). The residual eigenvalues are \(25/144\) (sixfold) and \(25/24\) (once), versus \(1\) (sixfold) and \(1/6\) (once) for the inverse. Squaring and summing gives \(\|M\|_F^2=4375/3456\) and \(\|A^{-1}\|_F^2=217/36\), proving the asserted Frobenius contrast. An explicit positive-variance witness is \(A=I_n+(\kappa-1)vv^{\mathsf T}\) with \(v=(1,\ldots,1)^{\mathsf T}/\sqrt n\); its inverse has off-diagonal entries \((\kappa^{-1}-1)/n\), giving variance \(2(n-1)(1-\kappa^{-1})^2/(sn)\). At \(\kappa=(n-1)^2\), \(\alpha=0\) by the nontrivial root above.

## Verification

The accompanying `verify.py` is a standard-library exact-rational check of the residual matrix identity and samplewise centered relation. The recorded run (`VERIFY_OK | 84 exact matrix families | 8184 exhaustive sign-vector comparisons`) covers two-level spectra in dimensions 2 through 8 at finitely many contrasts, including explicit flat-spike checks and rational checks of the thresholds and norm ratio in dimension seven. It does not certify the optimization over the continuous contrast parameter; that classification is proved analytically above.

## Relationship to prior work

Rinelli, Simunec and Vermeiren [1] introduce full-size global Lanczos with a Hermite-based stochastic error correction and give the corresponding Hutchinson variance law. The three-eigenvalue study [4, Proof, Step 4] gives the same two-level Rademacher variance ratio by off-diagonal scaling, which for signs also implies the samplewise multiplier. That identity is included here as the basis of the analysis rather than as a separate novelty claim. The contribution is the sharp two-level classification in multiplicity, contrast, and dimension, together with the exact seven-dimensional Frobenius-norm comparison. Neither generic control-variate amplification nor the Rademacher fourth-moment identity is claimed as new. Gambhir, Stathopoulos and Orginos [2] discuss variance behavior of inverse-trace spectral deflation; Chen and Hallman [3] use randomized block-Krylov deflation. Neither deflation procedure is the deterministic one-node Hermite correction considered here.

## Limitations

No claim is made for Gaussian probes, arbitrary spectra, more Lanczos nodes, approximate inverse products, floating-point stability, or runtime. The Frobenius comparison concerns a concrete reversal example, not all spectra in the amplification regime. The originality comparison is limited to inspected sources and does not determine exhaustive historical priority.

## References

1. M. Rinelli, I. Simunec, R. Vermeiren, *Global Lanczos with stochastic error correction for trace estimation of matrix functions*, arXiv:2611.18864, https://arxiv.org/abs/2611.18864.
2. H. Gambhir, A. Stathopoulos, K. Orginos, *Deflation as a Method of Variance Reduction for Estimating the Trace of a Matrix Inverse*, arXiv:1603.05988, https://arxiv.org/abs/1603.05988.
3. T. Chen, E. Hallman, *Krylov-aware stochastic trace estimation*, arXiv:2205.01736, https://arxiv.org/abs/2205.01736.
4. *A three-eigenvalue variance separation for Hermite-corrected global Lanczos*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-three-eigenvalue-variance-separation-for-hermite-corrected-glo--9b31e66832f2.
