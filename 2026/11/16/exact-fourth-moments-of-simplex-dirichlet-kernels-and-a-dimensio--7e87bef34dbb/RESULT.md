# Exact fourth moments of simplex Dirichlet kernels and a dimension-dependent energy gap

## Finding

For every positive integer \(d\) and nonnegative integer \(n\), let
\[
\Lambda_{d,n}=\left\{k\in\mathbb Z_{\ge0}^d:\sum_{j=1}^d k_j\le n\right\},\qquad D_{d,n}(x)=\sum_{k\in\Lambda_{d,n}}e^{i k\cdot x}.
\]
Define \(A_d(-1)=0\) and, for every integer \(t\ge0\),
\[
A_d(t)=\sum_{\substack{p,q\ge0\\p+q\le d}}
\frac{d!}{p!\,q!\,(d-p-q)!}\binom{t}{p}\binom{t}{q},
\]
with the usual convention that a binomial coefficient is zero when its lower index exceeds its upper index. Then the **exact fourth-power norm in every dimension and at every cutoff** is
\[
\boxed{\|D_{d,n}\|_{L^4(\mathbb T^d)}^4=
\sum_{t=0}^{n}\big(A_d(t)-A_d(t-1)\big)
\binom{n-t+d}{d}^{\!2}.}
\]
In particular, for the standard triangular Fourier cutoff in two dimensions,
\[
\boxed{\|D_{2,n}\|_4^4=
\frac{(n+1)(n+2)(n^2+2n+2)(n^2+4n+5)}{20}.}
\]
For fixed dimension, the exact leading coefficient and its normalization by the number of active characters are
\[
\boxed{\lim_{n\to\infty}\frac{\|D_{d,n}\|_4^4}{n^{3d}}=
\frac{((2d)!)^2}{(d!)^4(3d)!}},\qquad
\boxed{R_d=\lim_{n\to\infty}\frac{\|D_{d,n}\|_4^4}{|\Lambda_{d,n}|^3}=
\frac{((2d)!)^2}{d!(3d)!}.}
\]
The high-dimensional profile is
\[
\boxed{R_d\sim\frac{2}{\sqrt3}\left(\frac{16}{27}\right)^d.}
\]
For comparison, for the integer box \(B_{d,n}=\{0,1,\ldots,n\}^d\), its analogous normalized fourth-moment ratio tends to \((2/3)^d\), giving the explicit iterated-limit contrast
\[
\boxed{\frac{R_d}{(2/3)^d}\sim\frac2{\sqrt3}\left(\frac89\right)^d.}
\]

## Assumptions and scope

The torus \(\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d\) carries **probability** Haar measure. The coefficients of the Dirichlet polynomial are all exactly one. The fourth norm means the integral of the fourth absolute power, not the fourth power of an operator norm. All identities hold at cutoff \(n=0\); the asymptotics concern first \(n\to\infty\) with \(d\) fixed, and then \(d\to\infty\). This does not assert simultaneous uniformity when dimension grows with cutoff. The class considered is the standard lattice simplex, not arbitrary sloped or translated rational simplices.

## Proof

**1. Additive energy and correlations.** The character orthogonality relation on probability Haar measure gives
\[
\|D_{d,n}\|_4^4=\#\{(a,b,c,e)\in\Lambda_{d,n}^{4}:a+b=c+e\}
=\sum_{h\in\mathbb Z^d} r(h)^2,
\]
where \(r(h)=\#\{a\in\Lambda_{d,n}:a+h\in\Lambda_{d,n}\}\). No approximation has been taken here.

**2. The intersection lemma.** For a difference \(h\in\mathbb Z^d\) put
\[
P(h)=\sum_j\max(h_j,0),\quad Q(h)=\sum_j\max(-h_j,0),\quad T(h)=\max(P(h),Q(h)).
\]
Writing \(a_j=\max(-h_j,0)+y_j\), with all \(y_j\ge0\), the requirements \(a,a+h\in\Lambda_{d,n}\) become simultaneously \(\sum y_j\le n-Q(h)\) and \(\sum y_j\le n-P(h)\). Thus
\[
r(h)=\begin{cases}\displaystyle\binom{n-T(h)+d}{d},&T(h)\le n,\\[4pt]0,&T(h)>n.\end{cases}
\]
This identity determines the exact covariogram of the integer simplex, rather than merely its leading volume.

**3. Exact shell count.** Fix \(t\ge0\). A vector with exactly \(p\) strictly positive and \(q\) strictly negative coordinates has \(d!/(p!q!(d-p-q)!)\) choices of coordinate signs. Its positive-coordinate magnitudes can be chosen with sum at most \(t\) in \(\binom tp\) ways; independently, the absolute values of the negative coordinates contribute \(\binom tq\) choices. Therefore \(A_d(t)=\#\{h:T(h)\le t\}\) exactly. Taking the difference of consecutive cumulative counts gives the number of shifts with \(T(h)=t\). Substituting the intersection lemma proves the displayed finite-sum formula.

**4. Two-dimensional closed product.** Directly from the binomial sum, \(A_2(t)=3t^2+3t+1\) for \(t\ge0\). Consequently, the zero shell has size one and shell \(t\ge1\) has size \(6t\), so
\[
\|D_{2,n}\|_4^4=\binom{n+2}{2}^{\!2}+6\sum_{t=1}^{n}t\binom{n-t+2}{2}^{\!2}.
\]
Summing the polynomial using the standard sums of powers (or expanding and telescoping finite differences) gives exactly
\[
\frac{(n+1)(n+2)(n^2+2n+2)(n^2+4n+5)}{20}.
\]
For \(n=2\) the answer is \(102\); this already-known six-character case is **not** asserted to be new.

**5. Leading coefficient in general dimension.** The highest-degree part of \(A_d(t)\) arises from pairs \(p+q=d\), and Vandermonde's identity yields
\[
[t^d]A_d(t)=\frac1{d!}\sum_{p=0}^d\binom dp^2
=\frac1{d!}\binom{2d}{d}.
\]
Hence
\[
A_d(t)-A_d(t-1)=\frac{\binom{2d}{d}}{(d-1)!}t^{d-1}+O_d(t^{d-2}),
\]
where for \(d=1\) the remainder can be taken identically zero. The exact sum of Step 3 is a Riemann sum, and therefore
\[
\lim_{n\to\infty}n^{-3d}\|D_{d,n}\|_4^4
=\frac{\binom{2d}{d}}{(d-1)!(d!)^2}
\int_0^1 u^{d-1}(1-u)^{2d}\,du.
\]
The beta integral equals \((d-1)!(2d)!/(3d)!\), proving the first factorial coefficient. Finally \(|\Lambda_{d,n}|=\binom{n+d}{d}\sim n^d/d!\), which yields \(R_d\).

**6. Comparison with boxes and large dimension.** For \(B_{d,n}\), each coordinate contributes the one-dimensional difference-correlation sum
\[
(n+1)^2+2\sum_{j=1}^{n}j^2=\frac{(n+1)(2(n+1)^2+1)}3.
\]
Their product is the box fourth moment. Dividing by \(|B_{d,n}|^3=(n+1)^{3d}\) and letting \(n\to\infty\) gives \((2/3)^d\). Finally Stirling's factorial formula, applied to \(R_d=((2d)!)^2/[d!(3d)!]\), gives \(R_d\sim2(16/27)^d/\sqrt3\) and hence the stated relative rate \((8/9)^d\). These steps are valid as iterated limits, not claimed uniformly in two indices.

## Verification

The accompanying `simplex_fourier_checker.py` separately computes finite additive energy by enumerating all pairs, computes the shell count via the explicit binomial formula, and tests equality at multiple \(d,n\). It also checks the two-dimensional polynomial and several exact normalized constants. The program uses standard Python only, has no outside dependencies, and prints a single PASS result when all tests complete. These finite tests are supplemental consistency checks, **not** an infinite proof; the all-parameter statements follow from the arguments above. An algebraic expansion of the two-dimensional finite sum was also checked symbolically.

## Relationship to prior work

Nursultanov, Tikhonov and Weisz (2026), Section 3, give general order-of-growth and weighted Fourier bounds for Dirichlet kernels over classes that include convex polyhedra. Their statements are estimates, not the exact finite simplex fourth moment or its evaluated dimension-dependent leading constant. Marshall Ash's 2010 triangular-kernel paper, Theorem 1, proves the appropriate \(L^p\)-growth order for triangles without this exact fourth-power polynomial. De Dios Pont, Greenfeld, Ivanisvili and Madrid (2023) develop general additive-energy inequalities for discrete cubes; their objects and statements differ from the exact energy of the standard lattice simplex.

A previous six-term triangular Fourier-aperture calculation includes the special case \(d=2,n=2\), whose exact fourth moment is \(102\). That finite case and the general character-orthogonality mechanism are not claimed as novel. The assessed contribution is the **simultaneous exact all-dimensional finite formula, evaluated all-dimensional leading coefficient, and the dimension-dependent asymptotic gap relative to boxes**. Literature searches did not locate those assertions in the inspected sources, but absence of a match is not proof of first discovery.

## Limitations

The proof addresses fixed-unit coefficients and the standard integer simplex. It does not give sharp norms for arbitrary coefficient arrays on the same frequency region. The factorial asymptotics do not address joint growth of dimension and cutoff. Unexamined older discrete-convolution, multivariate B-spline or covariogram formulae might yield an equivalent result; independent expert literature checking remains appropriate.

## References

- E. Nursultanov, S. Tikhonov and F. Weisz, *Pitt’s Inequalities and Bounds for Dirichlet Kernels*, Journal of Fourier Analysis and Applications 32, article 56 (2026), DOI: https://doi.org/10.1007/s00041-026-10263-1 (first publicly verified May 13, 2026).
- J. Marshall Ash, *Triangular Dirichlet Kernels and Growth of \(L^p\) Lebesgue Constants*, Journal of Fourier Analysis and Applications 16, 1053–1069 (2010), https://doi.org/10.1007/s00041-009-9115-8 ; author-hosted text: https://condor.depaul.edu/mash/YudinLp.pdf.
- J. de Dios Pont, R. Greenfeld, P. Ivanisvili and J. Madrid, *Additive Energies on Discrete Cubes*, Discrete Analysis (2023), https://arxiv.org/abs/2112.09352.
- Related six-frequency triangular aperture calculation: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
