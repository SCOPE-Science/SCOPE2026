# Sharp regularity-endpoint law for the recursive product of spacings

## Finding
For every fixed integer \(m\ge2\), let \(m-1\) independent observations be sampled from any fully specified continuous distribution, and transform them by its null cumulative distribution function. Write \(D=(D_1,\ldots,D_m)\) for the resulting \(m\) spacings, including the two endpoints. Thus \(D\sim\operatorname{Dirichlet}(1,\ldots,1)\). Let \(T_m\) be the *recursive product-of-spacings* (RPS) raw statistic of Eller and Shtembari, and let \(b_m=\sum_{j=2}^{m}j\log j\) be its exact minimum.

Define the positive definite rational \((m-1)\)-by-\((m-1)\) matrix \(Q_m\) below. For every fixed \(m\), as \(\varepsilon\downarrow0\),
\[
\Pr\{T_m-b_m\le\varepsilon\}
\sim C_m\varepsilon^{(m-1)/2},\qquad
C_m=\frac{(m-1)!\,\pi^{(m-1)/2}\,2^{(m-1)/2}}
{\Gamma((m+1)/2)\sqrt{\det Q_m}}.
\]
For the published bounded score \(T_m^*=b_m/T_m\), this is equivalently the exact rare-*regularity* endpoint law
\[
\Pr\{T_m^*\ge1-\eta\}\sim
C_m(b_m\eta)^{(m-1)/2}\quad(\eta\downarrow0).
\]
In particular, \(C_2=1\) (recovering the known one-observation endpoint law), and \(C_3=8\pi/\sqrt{1215}=0.721027320173\ldots\). The exponent in terms of the number \(n=m-1\) of observations is exactly \(n/2\).

For the ordinary Moran statistic on the same \(m\) spacings, the analogous leading constant is \(C_m^{\mathrm{Moran}}=(m-1)!\pi^{(m-1)/2}2^{(m-1)/2}/[\Gamma((m+1)/2)m^{m-1/2}]\). Consequently \(C_m<C_m^{\mathrm{Moran}}\) for \(m\ge3\), with \(C_3/C_3^{\mathrm{Moran}}=2/\sqrt5\); equality holds for \(m=2\). This comparison concerns equal *raw excesses above the respective minima*.

## Assumptions and scope
All sample sizes are fixed before the endpoint limit. The null cumulative distribution is continuous and fully specified (no fitted-parameter transform). The transformed spacings are almost surely positive and sum to one. All logarithms are natural. Nothing is asserted about a joint limit as \(m\to\infty\) and \(\varepsilon\to0\), about finite-threshold approximation errors, or about test power.

For each integer \(k\in\{0,\ldots,m-2\}\), let \(j=m-k\) and define the nonnegative \(j\)-by-\(m\) binomial-window matrix
\[
(B_k)_{i\ell}=\begin{cases}\binom{k}{\ell-i},&0\le\ell-i\le k,\\0,&\text{otherwise},\end{cases}
\quad 1\le i\le j,\ 1\le\ell\le m.
\]
Set \(v^{(k)}=B_kD/(\mathbf1^\mathsf TB_kD)\). Recursive adjacent sums followed by normalization produce exactly these \(v^{(k)}\): the intermediate normalization factors cancel. The raw statistic is
\[
T_m=-\sum_{k=0}^{m-2}\sum_{i=1}^{m-k}\log v_i^{(k)}.
\]
The omitted terminal length-one level contributes zero. Let \(P_j=I_j-j^{-1}\mathbf1\mathbf1^\mathsf T\), and let \(A\) be the \(m\)-by-\((m-1)\) matrix with an identity in its first \(m-1\) rows and \(-1\) in every entry of its last row. Define
\[
Q_m=m^2\sum_{k=0}^{m-2}4^{-k}
A^\mathsf T B_k^\mathsf T P_{m-k}B_kA.
\]
This is a finite, exact rational-matrix specification, with no numerical fitting or infinite cutoff.

## Proof
**1. Unique regularity minimizer.** Each \(v^{(k)}\) is a positive probability vector of length \(j=m-k\). The arithmetic-geometric mean inequality gives \(-\sum_{i=1}^j\log v_i^{(k)}\ge j\log j\). Hence \(T_m\ge b_m\). Equality at the first level \(k=0\) forces every original spacing to equal \(1/m\); at this vector every higher level is also uniform. Thus \(D_0=m^{-1}\mathbf1\) is the unique global minimizer. The first-level sum diverges at every boundary face of the simplex, so sufficiently small sublevel sets of \(T_m-b_m\) are confined to any prescribed neighborhood of \(D_0\).

**2. Exact Hessian.** Write \(D=D_0+Az\) for \(z\in\mathbb R^{m-1}\) near zero. Since \(B_k\mathbf1=2^k\mathbf1\), the denominator at \(D_0\) is \(j2^k/m\). Differentiating the normalized window vector gives
\[
v^{(k)}=j^{-1}\mathbf1+
\frac{m}{j2^k}P_jB_kAz+O(\|z\|^2).
\]
The entries of every \(v^{(k)}\) sum identically to one, so the linear term in the Taylor expansion of its negative log product vanishes, including any second-order normalization terms. Its quadratic term is
\[
\frac{j^2}{2}\left\|\frac{m}{j2^k}P_jB_kAz\right\|^2
=\frac{m^2}{2\,4^k}z^\mathsf TA^\mathsf TB_k^\mathsf TP_jB_kAz.
\]
Summing proves
\[
T_m-b_m=\tfrac12 z^\mathsf TQ_mz+O_m(\|z\|^3).
\]
The \(k=0\) summand is \(m^2A^\mathsf TA\), which is positive definite. Every other summand is positive semidefinite; hence \(Q_m\) is positive definite for all \(m\ge2\).

**3. Probability content of the ellipsoid.** In the free coordinates \(z=(D_1-1/m,\ldots,D_{m-1}-1/m)\), the Dirichlet density is the constant \((m-1)!\). By the strict quadratic minimum and confinement established in Step 1, rescaling \(z=\sqrt\varepsilon\,w\) reduces the sublevel volume, up to relative \(o(1)\), to the Euclidean ellipsoid \(w^\mathsf TQ_mw\le2\). Its volume is \(\pi^{(m-1)/2}2^{(m-1)/2}/[\Gamma((m+1)/2)\sqrt{\det Q_m}]\). Multiplication by the exact simplex density proves the first equivalent. The transformation \(T_m^*=b_m/T_m\) gives \(T_m^*\ge1-\eta\) precisely when \(T_m-b_m\le b_m\eta/(1-\eta)\), proving the second equivalent.

**4. Exact first constants and comparison.** For \(m=2\), \(Q_2=(8)\), so \(C_2=1\). For \(m=3\), direct binomial-window multiplication yields
\[
Q_3=\begin{pmatrix}45/2&45/4\\45/4&153/8\end{pmatrix},\quad
\det Q_3=1215/4,
\]
and therefore \(C_3=8\pi/\sqrt{1215}\). Keeping only the first (Moran) level produces \(Q_m^{\mathrm{Moran}}=m^2A^\mathsf TA\), whose determinant is \(m^{2m-1}\), since \(\det(A^\mathsf TA)=m\). At \(m\ge3\) the \(k=1\) summand is nonzero and positive semidefinite, making \(\det Q_m>m^{2m-1}\); at \(m=2\) there are no added levels. The claimed strict constant comparison and \(m=3\) ratio follow.

## Verification
The included standalone `checker_regular.py` exactly constructs each \(Q_m\) for \(2\le m\le10\) using rational arithmetic, checks positive principal minors and the determinant inequality, and compares direct binomial-window evaluation with the original normalized recursion. It also checks the local quadratic expansion numerically, computes \(Q_2\) and \(Q_3\) exactly, and reproduces the first constants. The run yielded 453 passed finite checks. The arbitrary-\(m\) theorem is proved by the displayed analytic argument, not inferred from these finite checks. To reproduce: `python checker_regular.py` with Python 3 and SymPy.

## Relationship to prior work
Eller and Shtembari, *A goodness-of-fit test based on a recursive product of spacings*, arXiv:2111.02252 (first posted 3 November 2021), define the recursion and \(b_m\), derive the bounded-score distribution for one observation, and use numerical calibration for larger samples. Their Section 3 does not provide this fixed-sample near-regularity endpoint equivalent or the rational Hessian determinant. Other subsequent work considers multivariate applications of spacing tests; the near-equispaced fixed-sample endpoint is distinct from large raw-score clustering tails. General quadratic small-ball analysis is classical; the claim is the explicit all-sample-size RPS Hessian and leading constant, not the small-ball principle itself.

## Limitations
The asymptotic applies only to \(T_m\) approaching its unique minimum, equivalently \(T_m^*\uparrow1\), for fixed sample size. It is NOT an asymptotic for the opposite clustering tail \(T_m^*\downarrow0\); those are separate results. The matrix determinant is an exact finite formula rather than a closed elementary product for arbitrary size. No numerical accuracy guarantee is supplied away from the endpoint. Historical priority is subject to independent review, especially because a relevant 2023 doctoral thesis was identified but its complete PDF could not be inspected.

## References
1. P. Eller and L. Shtembari, *A goodness-of-fit test based on a recursive product of spacings*, arXiv:2111.02252, first posted 3 November 2021; https://arxiv.org/abs/2111.02252 . Journal of Instrumentation 18 (2023), P03048, https://doi.org/10.1088/1748-0221/18/03/P03048 .
2. L. Shtembari and A. Caldwell, *Goodness-of-fit tests for arbitrary multivariate models*, Physical Review D 108 (2023), 123006; https://doi.org/10.1103/PhysRevD.108.123006 .
3. L. Shtembari, *On non-parametric tests for discovery and limit setting in one and multiple dimensions*, doctoral thesis, Technische Universität München (2023); https://mediatum.ub.tum.de/doc/1707763/1707763.pdf (full-text access unavailable during this comparison).
