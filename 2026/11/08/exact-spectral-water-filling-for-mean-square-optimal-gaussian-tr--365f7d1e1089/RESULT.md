# Exact spectral water-filling for mean-square-optimal Gaussian trace sampling spaces

## Finding

Let \(A\in\mathbb R^{n\times n}\) be symmetric positive semidefinite and nonzero, with eigenvalues \(\lambda_1\ge\cdots\ge\lambda_n\ge0\), and let \(1\le r<n\), \(m\ge1\). The uncorrected rank-\(r\) Gaussian trace estimator uses any real \(n\times r\) orthonormal frame \(U\), independent standard Gaussian \(\gamma^{(j)}\in\mathbb R^r\), and
\[
H_{U,m}=\frac1m\sum_{j=1}^m(\gamma^{(j)})^{\mathsf T}U^{\mathsf T}AU\gamma^{(j)}.
\]
Its target is the **uncompressed** trace \(T=\operatorname{tr}A\). Define intervals \(I_i=[\lambda_{i+n-r},\lambda_i]\) and \(c_i(t)=\min\{\lambda_i,\max\{\lambda_{i+n-r},t\}\}\), for \(i=1,\ldots,r\). There is exactly one \(\tau>0\) satisfying
\[
\sum_{i=1}^r c_i(\tau)+\frac{2\tau}{m}=T.
\]
The exact global minimum, over **all** rank-\(r\) sampling subspaces, is
\[
\boxed{\min_{U^{\mathsf T}U=I_r}\mathbb E(H_{U,m}-T)^2
=\frac{4\tau^2}{m^2}+\frac2m\sum_{i=1}^r c_i(\tau)^2.}
\]
Equality holds **if and only if** the eigenvalues of \(U^{\mathsf T}AU\), in decreasing order, are \(c_1(\tau),\ldots,c_r(\tau)\). This unique optimal *Ritz spectrum* is always realizable by a real subspace; the subspace itself need not be unique.

A principal top-\(r\) eigenspace is optimal precisely when
\[
\frac m2\sum_{j=r+1}^n\lambda_j\ \ge\ \Lambda_{\rm act},\qquad
\Lambda_{\rm act}:=\max\bigl(\{\lambda_i:1\le i\le r,\ \lambda_i>\lambda_{i+n-r}\}\cup\{0\}\bigr).
\]
Consequently, if \(A\ne0\) has rank at most \(r\), its top-\(r\) eigenspace is **strictly suboptimal for every finite** \(m\), even though it retains all nonzero eigenvectors. The gain comes from deliberate truncation bias that outweighs a reduction in Gaussian variance.

## Assumptions and scope

The estimator is exactly the Gaussian-probe compression considered for truncated Girard–Hutchinson/infHutch, with a **deterministic**, chosen \(r\)-dimensional sampling space, \(m\) independent standard real Gaussian probes, no control variate and no deterministic bias correction. We minimize squared error about \(\operatorname{tr} A\), not variance about the compression trace. The integer \(m\) counts probes (not entries or cost per operator call); \(n\ge2\), \(1\le r<n\), \(m\ge1\) are arbitrary. Neither a spectral oracle nor an efficient algorithm for learning the optimal subspace is assumed available to an actual matrix-free user; this is a sharp design benchmark, not a claimed implementable spectral-free estimator. The zero matrix has zero error for every subspace and is excluded to state \(\tau>0\).

## Proof

**1. Exact risk.** Put \(B=U^{\mathsf T}AU\), and write its decreasing nonnegative eigenvalues as \(\mu_1,\ldots,\mu_r\). Gaussian rotational invariance yields \(H_{U,m}\stackrel{d}=\sum_i\mu_i\chi_{m,i}^2/m\), where the chi-squared variables are independent with \(m\) degrees of freedom. Hence \(\mathbb EH_{U,m}=\sum_i\mu_i\) and \(\operatorname{Var}(H_{U,m})=2\sum_i\mu_i^2/m\). Thus the exact mean squared error is
\[
F(\mu)=\left(T-\sum_i\mu_i\right)^2+\frac2m\sum_i\mu_i^2. \tag{1}
\]

**2. Attainable spectra.** The Cauchy interlacing inequalities give \(\lambda_i\ge\mu_i\ge\lambda_{i+n-r}\). Conversely the *real symmetric Fan–Pall compression theorem* says that every nonincreasing \(r\)-tuple obeying these inequalities is the spectrum of \(U^{\mathsf T}AU\) for some real orthonormal \(U\). This standard converse, not a newly claimed lemma, is indispensable: a formal spectral optimum without it would not establish attainability.

**3. Convex optimization.** First minimize (1) on the larger axis-aligned box \(\prod_{i=1}^r I_i\). Its Hessian \(2\mathbf1\mathbf1^{\mathsf T}+(4/m)I_r\) is positive definite, so there is a unique box minimizer. Setting \(\tau=(m/2)(T-\sum_i\mu_i)\), the scalar first-order box conditions \(\partial_iF=(4/m)(\mu_i-\tau)\) are equivalent to \(\mu_i=c_i(\tau)\). The scalar equation in the Finding has a unique root: its left side is continuous and strictly increasing from a value at \(t=0\) below \(T\) to infinity. It is positive because \(A\ne0\), \(r<n\), and the sum of the bottom \(r\) eigenvalues is strictly smaller than \(T\).

Both endpoints of \(I_i\) are nonincreasing in \(i\), hence the clipped values \(c_i(\tau)\) are also nonincreasing. The box optimizer therefore satisfies the Fan–Pall ordering conditions and corresponds to a real compression. Since it is the unique minimizer over the larger box, it is the unique optimal Ritz spectrum over all admissible subspaces. Substituting \(T-\sum_i c_i(\tau)=2\tau/m\) into (1) proves the displayed minimum.

**4. Sharp principal-space criterion.** The top-\(r\) eigenspace has \(\mu_i=\lambda_i\). At this box corner the associated scalar equals \(\tau_{\rm top}=m\sum_{j>r}\lambda_j/2\). The box first-order conditions hold if and only if \(\tau_{\rm top}\ge\lambda_i\) for every nondegenerate interval \(I_i\). The degenerate intervals need no condition. Taking the maximum over the nondegenerate intervals gives the stated necessary-and-sufficient criterion; strict convexity makes every failed criterion imply a strict MSE gap. If \(A\ne0\) has rank \(s\le r\), then \(\lambda_s>\lambda_{s+n-r}=0\) while the omitted trace vanishes; thus the criterion fails for every finite \(m\).

**5. Exact witness.** For \(A=\operatorname{diag}(10,2,0)\), \(r=2\), \(m=3\), the equation yields \(\tau=6\), \((\mu_1,\mu_2)=(6,2)\). The explicit orthonormal columns
\[
U=\bigl[\sqrt{3/5}\,e_1+\sqrt{2/5}\,e_3,\ e_2\bigr]
\]
produce \(U^{\mathsf T}AU=\operatorname{diag}(6,2)\) and optimal MSE \(128/3\). The principal compression has MSE \(208/3\). In the minimal rank-one example \(A=\operatorname{diag}(1,0)\), \(r=1\), the optimum compression eigenvalue is \(m/(m+2)\), giving MSE \(2/(m+2)\) instead of the principal value \(2/m\), for every finite \(m\).

## Verification

The standalone `check.py` implements the scalar clipped-root solution, confirms convex first-order conditions and ordering, compares against independent numerical box-constrained optimization over 5,040 nontrivial/test parameter combinations, and checks the exact two- and three-dimensional witnesses (5,060 checks including witness instances). Run `python3 check.py` with Python 3, NumPy and SciPy. This is **finite verification only**; the all-dimensions theorem is established by the preceding proof plus the classical real Fan–Pall converse.

## Relationship to prior work

Bujanović, Grubišić, Kressner and Olić (2026), Section 3.3.1, define the truncated infHutch estimator on a fixed sampling basis and separate the compression bias from Gaussian sampling error. Their main analysis establishes operator trace-estimation bounds and convergence of truncated variants. Formula (1) uses the classical Gaussian second moment; that formula alone is not asserted as new. The present claim is the *global optimization over all deterministic rank-\(r\) sampling subspaces*, its unique clipped Ritz spectrum, and the exact condition for a principal subspace to be optimal. Standard Cauchy interlacing and its real Fan–Pall converse supply the spectral feasibility theorem, not a new eigenvalue interlacing result. The distinct Hutch++ literature deflates a dominant subspace and estimates the *complement*; because it corrects for retained trace, its unbiased deflation criterion is not the risk criterion here.

Saibaba, Alexanderian and Ipsen (2016) also analyze a **biased** projected trace estimate, but their estimator computes the compressed trace deterministically after a randomized subspace iteration; it does not independently sample Gaussian quadratic forms *within the chosen space* and does not solve the present joint truncation-bias/Gaussian-variance design problem.

## Limitations

The optimizer depends on the target spectrum and trace; without spectral information it is an oracle benchmark rather than a directly usable matrix-free selection algorithm. It minimizes mean squared error for a fixed *uncorrected, truncated* Gaussian-probe estimator, not high-probability relative error, worst-case error, or the variances of unbiased Hutch++ residual estimators. It does not optimize simultaneously over subspace dimension, number of probes, probe distribution, deterministic trace corrections or runtime cost. Real symmetric positive semidefiniteness and independent Gaussian probes are essential to this formula. No computational test can certify infinite-parameter statements. Historical priority remains contingent on unindexed equivalent design results.

## References

1. Z. Bujanović, L. Grubišić, D. Kressner and H. Olić, *Stochastic trace estimation for positive trace-class operators*, arXiv:2608.28135, first public version August 28, 2026, https://arxiv.org/abs/2608.28135 (Sections 2.2 and 3.3.1).
2. K. Fan and G. Pall, *Imbedding Conditions for Hermitian and Normal Matrices*, Canadian Journal of Mathematics 9 (1957), 298–304, https://doi.org/10.4153/CJM-1957-036-1 (classical converse interlacing).
3. J. Holbrook, N. Mudalige and R. Pereira, *Normal matrix compressions*, arXiv:1203.3908, https://arxiv.org/abs/1203.3908 (Theorem 1 restates Cauchy–Fan–Pall).
4. R. A. Meyer, C. Musco, C. Musco and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649, https://arxiv.org/abs/2010.09649 (distinct unbiased deflation model).
5. H. Avron and S. Toledo, *Randomized algorithms for estimating the trace of an implicit symmetric positive semi-definite matrix*, J. ACM 58 (2011), https://openreview.net/forum?id=F9dRCbIYJzQ (classical Gaussian-probe variance baseline).

