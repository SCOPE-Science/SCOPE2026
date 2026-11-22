# Dimension-seven variance reversal in one-step global Lanczos inverse-trace correction

## Finding
Let \(A\in\mathbb R^{n\times n}\) be real symmetric positive definite with exactly two distinct eigenvalues \(0<a<b\), with multiplicities \(p\) and \(q\) respectively, \(n=p+q\ge2\). Put \(\mu=(pa+qb)/n\). Consider the one-step full-size global Lanczos approximation to \(\operatorname{tr}(A^{-1})\), corrected with \(s\ge1\) independent Rademacher Hutchinson probes. Compare it with ordinary Hutchinson using the same probes and exact inverse products. Their **centered errors agree samplewise up to the exact scalar**
\[
G_s-\operatorname{tr}(A^{-1})=\left(1-\frac{ab}{\mu^2}\right)\bigl(T_s-\operatorname{tr}(A^{-1})\bigr).
\]
Thus, whenever the ordinary Hutchinson variance is nonzero, the corrected-to-ordinary variance ratio is
\[
R=\left(1-\frac{ab}{\mu^2}\right)^2.
\]
This ratio is independent of the probe budget and eigenvectors; the samplewise identity also holds when both variances vanish.

Write \(\kappa=b/a>1\). When ordinary Hutchinson has nonzero variance, the correction eliminates its random error for every probe realization precisely when \(p>q\) and \(\kappa=(p/q)^2\). Degenerate matrices with diagonal \(A^{-1}\) have zero sign-probe variance in both estimators at any contrast. **Strict variance amplification** is possible for some \(\kappa>1\) precisely when
\[
\frac pq>3+2\sqrt2.
\]
For those multiplicities, amplification occurs exactly for \(\kappa_-<\kappa<\kappa_+\), with
\[
\kappa_\pm=\left(\frac{n/\sqrt2\pm\sqrt{n^2/2-4pq}}{2q}\right)^2.
\]
The maximum variance ratio at fixed multiplicities is
\[
\frac{(p-q)^4}{16p^2q^2},\qquad\text{attained at }\kappa=p/q.
\]
Consequently **seven is the smallest dimension** permitting variance amplification: for \(n\le6\) the correction never has greater Rademacher variance than ordinary Hutchinson, whereas in dimension seven the spectrum with six eigenvalues \(1\) and one eigenvalue \(6\) has the exact variance ratio \(625/576>1\). At the dimension-seven reversal example, the correction residual has *smaller total Frobenius norm* despite greater sign-probe variance: \(\|M\|_F^2/\|A^{-1}\|_F^2=625/2976<1\). This separates ordinary matrix approximation quality from the off-diagonal statistic that controls Rademacher variance.

Among all two-level spectra of order \(n\ge7\), the largest possible ratio is
\[
\frac{(n-2)^4}{16(n-1)^2},
\]
attained with \(p=n-1\), \(q=1\), \(\kappa=n-1\) and a noncoordinate-aligned spike. In the same single-spike family, \(\kappa=(n-1)^2\) makes the corrected estimator exact with one sign probe.

## Assumptions and scope
The inverse products, Lanczos step, Hermite residual and quadratic forms are evaluated in exact arithmetic. The full-size global Lanczos process starts with \(B=I_n\), and is stopped at one node. The test vectors \(z_1,\ldots,z_s\) have independent equiprobable entries in \(\{-1,+1\}\), independent across probes. The comparison uses the same vectors for both estimators. Set
\[
T_s=\frac1s\sum_{j=1}^s z_j^{\mathsf T}A^{-1}z_j,
\quad h(x)=\frac2\mu-\frac{x}{\mu^2},\quad M=A^{-1}-h(A),
\quad G_s=\frac n\mu+\frac1s\sum_{j=1}^s z_j^{\mathsf T}Mz_j.
\]
The formula for \(G_s\) is the one-step global Lanczos--Hermite Hutchinson correction. A diagonal \(A\) has zero Rademacher variance for both procedures; in that case \(R\) is undefined and no ratio is claimed. The scalar identity remains valid for every \(A\) under the stated assumptions.

## Proof
**Lanczos node and interpolant.** With normalized full-size starting block \(I_n/\sqrt n\), the first global Lanczos diagonal coefficient is \(\langle I_n/\sqrt n,A I_n/\sqrt n\rangle_F=\operatorname{tr}(A)/n=\mu\). The one-node Gaussian quadrature gives \(n f(\mu)=n/\mu\) for \(f(x)=1/x\). Hermite interpolation at that one node imposes \(h(\mu)=f(\mu)\) and \(h'(\mu)=f'(\mu)\), hence \(h(x)=2/\mu-x/\mu^2\).

**Two-level minimal polynomial.** On each eigenspace \(x\in\{a,b\}\), \(x+(ab)/x=a+b\). Functional calculus gives
\[
A=(a+b)I_n-abA^{-1}.
\]
Consequently
\[
M=A^{-1}-\frac2\mu I_n+\frac A{\mu^2}
=\alpha A^{-1}+\beta I_n,
\quad \alpha=1-\frac{ab}{\mu^2},\quad \beta=\frac{a+b}{\mu^2}-\frac2\mu.
\]
Every sign vector has \(z^{\mathsf T}I_nz=n\), and exact Gaussian-quadrature polynomial exactness gives \(\operatorname{tr}(h(A))=n/\mu\). Therefore the random part of \(G_s\) is exactly \(\alpha\) times that of \(T_s\), proving the centered identity. In particular \(\operatorname{Var}(G_s)=\alpha^2\operatorname{Var}(T_s)\), without a distributional approximation.

**Phase classification.** Scale \(a=1\), so
\[
\alpha(\kappa)=1-\frac{n^2\kappa}{(p+q\kappa)^2}.
\]
Solving \(\alpha=0\) is equivalent to \((\sqrt\kappa-1)(q\sqrt\kappa-p)=0\). The nontrivial root is admissible exactly when \(p>q\). For \(p>q\), the positive function \(n^2\kappa/(p+q\kappa)^2\) has a unique maximum on \(\kappa>1\) at \(\kappa=p/q\), with value \(n^2/(4pq)\). For \(p\le q\), this function decreases on \(\kappa>1\), so \(0<\alpha<1\) and amplification is impossible. In the \(p>q\) case, \(\alpha\) takes its minimum \(1-n^2/(4pq)=-(p-q)^2/(4pq)\) there. As \(\kappa>1\) implies \(\alpha<1\), amplification \(\alpha^2>1\) is equivalent to \(\alpha<-1\), i.e. \(n^2>8pq\) with the maximizing point in the domain. This is exactly \(p/q>3+2\sqrt2\). Solving \(\alpha=-1\) as a quadratic in \(\sqrt\kappa\) gives the two stated endpoints and their interval; both exceed one when the strict condition holds.

**Sharp dimension and examples.** For a fixed \(n\), \(pq\ge n-1\) with equality at multiplicities \((n-1,1)\); the maximum negative \(\alpha\) is realized by the latter ordering. Since \(n^2>8(n-1)\) first holds at \(n=7\), the minimum dimension follows, and the maximum ratio for \(n\ge7\) is \([1-n^2/(4(n-1))]^2=(n-2)^4/[16(n-1)^2]\). At \(n=7,\ p=6,\ q=1,\kappa=6\), \(\mu=12/7\) and \(\alpha=-25/24\). The amplification interval is exactly \((9/2,8)\). In this example the residual eigenvalues are \(25/144\) (sixfold) and \(25/24\) (once), while the inverse eigenvalues are \(1\) (sixfold) and \(1/6\) (once). Thus \(\|M\|_F^2=4375/3456\), \(\|A^{-1}\|_F^2=217/36\), and their ratio is \(625/2976\). At \(\kappa=36\), \(\mu=6\), \(\alpha=0\).

To witness positive ordinary variance, choose \(A=I_n+(\kappa-1)vv^{\mathsf T}\) with \(v=(1,\ldots,1)^{\mathsf T}/\sqrt n\). Its inverse is \(I_n+(\kappa^{-1}-1)vv^{\mathsf T}\), whose off-diagonal part is nonzero for \(n\ge2\) and \(\kappa>1\). Direct Rademacher fourth moments give
\[
\operatorname{Var}(T_s)=\frac{2(n-1)}{sn}(1-\kappa^{-1})^2>0.
\]
These choices establish attainment of the variance ratios rather than only formal extrema.

## Verification
The accompanying standalone `verify.py` implements rational-arithmetic matrix products and exact exhaustive enumeration of sign vectors. It compares the actual one-step Hermite residual against the scalar matrix identity for rotated two-level spectra with each \(2\le n\le8\), every \(1\le p<n\), and two positive integer contrasts; it separately checks flat single-spike matrices at four contrasts and verifies the seventh-dimensional algebraic boundaries. The run reports `VERIFY_OK | 84 exact matrix families | 8184 exhaustive sign-vector comparisons`. All finite computations corroborate the algebraic proof; they do not establish it for arbitrary dimension.

## Relationship to prior work
Rinelli, Simunec and Vermeiren introduce full-size global Lanczos with a Hermite-based stochastic error correction and give the corresponding Hutchinson variance law. Their general construction supplies the correction being evaluated; the present two-eigenvalue samplewise reduction and sharp multiplicity/dimension classification are not stated in the examined text. Gambhir, Stathopoulos and Orginos discuss variance behavior of inverse-trace spectral deflation; spectral deflation is not the same as the one-node deterministic Hermite correction. Chen and Hallman's Krylov-aware estimator uses randomized block-Krylov deflation rather than the deterministic full-size one-node correction. The general Rademacher fourth-moment identity is classical and is not claimed as new. This theorem is a specific, exactly characterized risk boundary for the recent correction, not a claim that variance amplification was previously unknown in control-variate estimation generally.

## Limitations
No claim is made for Gaussian probes: \(z^{\mathsf T}Iz\) is then random, and the samplewise scalar identity need not hold. No claim is made for matrices with more than two eigenvalues, additional Lanczos nodes, approximate matrix-function evaluations, algorithmic wall-clock cost, floating-point stability, or relative-error confidence bounds. When the ordinary Rademacher variance vanishes, the ratio is undefined. Novelty is based on inspected sources and searchable records, not an exhaustive historical priority proof. Independent mathematical validation has not been performed.

## References
1. M. Rinelli, I. Simunec, R. Vermeiren, *Global Lanczos with stochastic error correction for trace estimation of matrix functions*, arXiv:2611.18864, original submission 2026-11-13, https://arxiv.org/abs/2611.18864.
2. H. Gambhir, A. Stathopoulos, K. Orginos, *Deflation as a Method of Variance Reduction for Estimating the Trace of a Matrix Inverse*, arXiv:1603.05988, https://arxiv.org/abs/1603.05988.
3. T. Chen, E. Hallman, *Krylov-aware stochastic trace estimation*, arXiv:2205.01736, https://arxiv.org/abs/2205.01736.
4. L. Wu, J. Laeuchli, V. Kalantzis, A. Stathopoulos, E. Gallopoulos, *Estimating the Trace of the Matrix Inverse by Interpolating from the Diagonal of an Approximate Inverse*, arXiv:1507.07227, https://arxiv.org/abs/1507.07227.
