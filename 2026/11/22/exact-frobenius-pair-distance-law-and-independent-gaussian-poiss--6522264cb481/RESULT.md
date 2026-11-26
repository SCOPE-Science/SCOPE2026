# Independent Gaussian rank deficiencies and Poisson shared cells in uniform partial permutations

## Finding
Let \(\mathcal P_n\subset\mathbb R^{n\times n}\) be the convex hull of the partial permutation matrices (including the zero matrix) for an integer \(n\ge1\), endowed with its standard ambient Frobenius metric. Independently and uniformly sample vertices \(X_n,Y_n\). Put \(K_n=\sum_{ij}(X_n)_{ij}\), \(L_n=\sum_{ij}(Y_n)_{ij}\), and \(C_n=\sum_{ij}(X_n)_{ij}(Y_n)_{ij}\). Define the squared Euclidean distance \(D_n=\|X_n-Y_n\|_F^2=K_n+L_n-2C_n\).

Write \(A_{n,k}=\binom nk^2 k!\), \(M_n=\sum_{k=0}^n A_{n,k}=n!\mathsf L_n(-1)\), and \((u)_r=u(u-1)\cdots(u-r+1)\), with \((u)_0=1\). Here \(\mathsf L_n\) is the ordinary Laguerre polynomial. The following conditional-moment form of the finite squared-distance generating function is useful for deriving the joint limit; the finite law is also an immediate reweighting of the independently available colored-component census described below:
\[
\boxed{\mathbb E[z^{D_n}]=\frac1{M_n^2}\sum_{k,\ell=0}^n A_{n,k}A_{n,\ell}z^{k+\ell}
\sum_{r=0}^{\min(k,\ell)}
\frac{(k)_r(\ell)_r}{r!(n)_r^2}(z^{-2}-1)^r.}
\]
Although presented with Laurent factors, the right side simplifies to a polynomial and extends to \(z=0\). Thus it determines the exact multiplicity of every squared vertex-pair distance; the probability that \(D_n=d\) is its coefficient of \(z^d\). Its exact expectation is
\[
\mathbb E D_n=2\mu_n-\frac{2\mu_n^2}{n^2},\qquad
\mu_n=\frac{\sum_{k=0}^n kA_{n,k}}{M_n}.
\]

The main result is a *joint* limit for the two rank deficiencies and shared occupied cells. Let \(S_n=n-K_n\), \(T_n=n-L_n\). Then
\[
\boxed{\left(\frac{S_n-\sqrt n}{n^{1/4}},\frac{T_n-\sqrt n}{n^{1/4}},C_n\right)
\ \xrightarrow{\mathrm d}\ (G_1,G_2,Z),}
\]
where \(G_1,G_2\) are independent centered Gaussians of variance \(1/2\), and \(Z\) is an independent Poisson random variable of mean one. In particular,
\[
\boxed{\frac{D_n-(2n-2\sqrt n)}{n^{1/4}}\xrightarrow{\mathrm d}N(0,1),\qquad
n^{1/4}\bigl(\sqrt{D_n}-\sqrt{2n-2\sqrt n}\bigr)\xrightarrow{\mathrm d}N(0,1/8).}
\]
The exact residual \(2n-S_n-T_n-D_n=2C_n\) converges, without scaling, to \(2Z\) on the even nonnegative integers, independently of the two Gaussian limits. Equivalently, **half** the residual converges to \(\operatorname{Pois}(1)\). This joint Gaussian–Poisson decomposition is stronger than the leading Gaussian law of the distance alone.

## Assumptions and scope
Every partial permutation matrix, regardless of rank, is sampled with equal probability, including the empty partial matching. These are precisely the vertices of the doubly substochastic polytope
\[\mathcal P_n=\{X\in\mathbb R_{\ge0}^{n\times n}:\ \sum_j X_{ij}\le1,\ \sum_i X_{ij}\le1\}.\]
The metric uses the original matrix-entry coordinates and the standard Frobenius inner product, not an intrinsic random direction, a graph's one-skeleton metric, or a permutation-word metric. The exact formula holds for all integers \(n\ge1\); the asymptotic limits hold as \(n\to\infty\) through integers, with the two matrices sampled independently.

## Proof
**1. Conditional common-entry moments.** A rank-\(k\) vertex is a choice of \(k\) occupied rows, \(k\) occupied columns and a bijection, giving \(A_{n,k}\). There are \((n)_r^2\) ordered nonattacking lists of \(r\) matrix positions. Conditioned on rank \(k\), every such list occurs in a uniformly random matching with probability \((k)_r/(n)_r^2\): indeed the expected number of ordered occupied \(r\)-lists is \((k)_r\). Because the two matchings are independent given their ranks,
\[
\boxed{\mathbb E[(C_n)_r\mid K_n=k,L_n=\ell]=\frac{(k)_r(\ell)_r}{(n)_r^2},}\qquad 0\le r\le\min(k,\ell).
\]
No assumption of independence between entries of one matching is used.

**2. Entire distance polynomial and mean.** The factorial-moment identity \(\mathbb E[t^C]=\sum_r \mathbb E[(C)_r](t-1)^r/r!\) holds exactly for bounded integer \(C\). Insert \(t=z^{-2}\), multiply by \(z^{k+\ell}\), and average over independently distributed ranks with \(\Pr(K_n=k)=A_{n,k}/M_n\). This yields the stated polynomial and makes its coefficient interpretation immediate. A given matrix position belongs to a uniform vertex with probability \(\mu_n/n^2\). Independence of \(X_n,Y_n\) then gives \(\mathbb EC_n=n^2(\mu_n/n^2)^2\), which proves the mean formula.

**3. Gaussian deficits.** Reindex the matching enumeration by deficiency \(S_n=n-K_n\):
\[
\Pr(S_n=s)=\frac{\binom ns/s!}{\mathsf L_n(-1)},\qquad
\mathbb E e^{tS_n}=\frac{\mathsf L_n(-e^t)}{\mathsf L_n(-1)}.
\]
A standard Perron asymptotic for Laguerre polynomials, locally uniformly for complex \(a\) near \(1\), is
\[
 \mathsf L_n(-a)=\frac{e^{-a/2}}{2\sqrt\pi\,(an)^{1/4}}
\exp(2\sqrt{an})\bigl(1+O(n^{-1/2})\bigr).
\]
With \(t=u n^{-1/4}\), the logarithm of the centered moment generating function satisfies
\[
\log\mathbb E\exp\!\left[u\frac{S_n-\sqrt n}{n^{1/4}}\right]
=2\sqrt n(e^{t/2}-1)-t\sqrt n+o(1)
\longrightarrow u^2/4.
\]
The remaining exponential prefactor terms tend to zero. Thus \((S_n-\sqrt n)/n^{1/4}\Rightarrow N(0,1/2)\), and \(S_n/\sqrt n\to1\) in probability. Independence supplies the same joint limit for \(S_n,T_n\). The Laguerre asymptotic and this single-factor Gaussian scale are classical ingredients, not asserted as individually new.

**4. Poisson common edges independent of both deficits.** The exact conditional probability generating function is
\[
\mathbb E[t^{C_n}\mid K_n=k,L_n=\ell]
=\sum_{r=0}^{\min(k,\ell)}\frac{(k)_r(\ell)_r}{(n)_r^2}\frac{(t-1)^r}{r!}.
\]
For any fixed \(r\), its factorial ratio tends to \(1\) whenever \(k/n\to1\) and \(\ell/n\to1\). All ratios are between zero and one, so the series is uniformly bounded termwise by \(|t-1|^r/r!\). Since \(K_n/n,L_n/n\to1\) in probability, the conditional generating function at \(t=e^{iv}\), for each real \(v\), converges in probability to \(\exp(e^{iv}-1)\). It is bounded by one in modulus, so the convergence also holds in \(L^1\). Multiplying by the joint characteristic-function factor for the two normalized deficiencies and taking expectations thus gives the product of the two Gaussian characteristic functions and the Poisson characteristic function. The continuity theorem proves joint convergence with the stated independence.

**5. Transfer to the Euclidean metric.** From the exact identity \(D_n=2n-S_n-T_n-2C_n\) and \(C_n=O_{\mathsf P}(1)\), the squared-distance Gaussian result follows by Slutsky. Since \(D_n/n\to2\), rationalization (or the differentiable delta method) yields
\[
n^{1/4}(\sqrt{D_n}-\sqrt{2n-2\sqrt n})
=\frac{(D_n-2n+2\sqrt n)/n^{1/4}}
{\sqrt{D_n/n}+\sqrt{2-2/\sqrt n}}
\ \xrightarrow{\mathrm d}\ N(0,1/8).
\]
The discrete overlap is recovered *exactly* as \(C_n=(2n-S_n-T_n-D_n)/2\), proving the stated two-scale assertion.

## Verification
Run `python3 verify.py` with Python 3 and only its standard library. For orders \(1\) through \(4\), it independently enumerates every ordered pair of partial permutation matrices, compares the entire exact squared-distance histogram with the factorial-moment polynomial, and verifies all conditional factorial-moment identities for every possible rank pair. It separately checks the exact distance mean and evaluates the exact generating-function coefficient constraints for orders \(10\), \(20\), and \(40\), without enumerating all vertices in those larger orders. Successful replay prints `PARTIAL_PERMUTATION_METRIC_EXACT_PASS`. These checks do not constitute a computational proof of the infinite-dimensional limits; those follow from the factorial-moment and Laguerre arguments above.

## Relationship to prior work
Torres (2023) establishes normality and inequality descriptions for bipartite matching polytopes, and Heuer–Striker (2020) identify and count the vertices of the partial-permutation polytope. Classical Laguerre estimates give the one-vertex Gaussian limit. The exact covariance on the same uniform vertex space gives the mean squared distance. The exact product-rank limit for random partial bijections also combines two Gaussian deficiencies and a Poisson term, but counts coincidences of *omitted* intermediate labels rather than coincidences of occupied cells. For example, two full permutations have no omitted intermediate labels but may share occupied cells. For uniform full permutations, the shared-cell limit is the classical fixed-point Poisson law. The contribution here is the joint occupied-cell limit and its independence from the two Gaussian deficiencies in the unconditional all-rank vertex model, with the consequent distance fluctuation and discrete residual law.

The finite distance enumerator is **not** claimed as a distinct new invariant evaluation. The same-date record [e587fba564ca](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-finite-field-rank-spectra-for-sums-of-two-rook-matrices-an--e587fba564ca) studies the rank of the sum, which differs from its support size, but its component census already gives the full distance law by marking each component by its symmetric-difference size. Put \(t=xy\) in its bivariate exponential component series. An equal-sided path with \(k\) vertices per side has \(2k-1\) singly occupied cells, and an unequal-sided path with \(k\) vertices on the smaller side has \(2k\). A cycle with \(k\ge2\) has \(2k\); a double edge contributes zero. Its resulting distance-marked series is
\[
 \exp\!\left(x+y+t+\frac{2tz+(x+y)tz^2}{1-tz^2}+\sum_{k\ge2}\frac{t^kz^{2k}}{k}\right).
\]
Taking \((n!)^2[x^ny^n]/M_n^2\) gives the same probability generating function by a different expression. No relative priority is inferred from the two records' shared date.

## Limitations
The joint asymptotic assertion concerns independent uniform vertices of square partial-permutation polytopes, not rectangular polytopes, uniformly sampled interior points, or arbitrary bipartite graphs. The standard Laguerre asymptotic, one-vertex Gaussian fluctuation, and rook-counting identities are established ingredients. Absolute historical priority for the joint law is not asserted; in particular Allen's 2017 rook-polytope thesis was not available for full-text comparison.

## References
1. J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1, first public June 20, 2023, https://arxiv.org/abs/2306.11910; journal DOI 10.15446/recolma.v57n2.115853, primary MSC2020 52B11.
2. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901v1, first public December 17, 2020, https://arxiv.org/abs/2012.09901; especially Definition 3.1 and Proposition 3.4.
3. D. Gouyou-Beauchamps and C. Nicaud, *Random Generation Using Binomial Approximations*, DMTCS Proceedings (2010), https://dmtcs.episciences.org/2772/pdf, Section 4 on partial injections and rank enumeration.
4. G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications, 4th ed. (1975), Theorem 8.22.3, classical Laguerre Perron asymptotic.
5. *Exact three-eigenspace covariance and growing anisotropy of uniform partial-permutation vertices*, record [caa6c69c0a56](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-three-eigenspace-covariance-and-growing-anisotropy-of-unif--caa6c69c0a56).
6. *Gaussian deficiencies and Poisson overlap corrections in random rook-monoid products*, record [c5a891e46186](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-gaussian-deficiencies-and-poisson-overlap-corrections-in-random--c5a891e46186).
7. *Exact finite-field rank spectra for sums of two rook matrices and a characteristic-sensitive invertibility transition*, record [e587fba564ca](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-finite-field-rank-spectra-for-sums-of-two-rook-matrices-an--e587fba564ca), particularly Proof, steps 1–3.
