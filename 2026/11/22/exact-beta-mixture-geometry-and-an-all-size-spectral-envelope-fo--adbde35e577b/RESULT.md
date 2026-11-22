# Exact beta-mixture geometry and an all-size spectral envelope for harmonic descent occupations

## Finding

For the harmonic descent chain, fix an integer \(k\ge2\), and let \(a(n,k)\) be its probability of ever visiting state \(k\) when started from \(n\ge k\). There is a **single explicit probability measure** \(\mu_k\) on \((0,1]\) such that for every integer \(m\ge0\),

\[
a(k+m,k)=\int_{(0,1]}x^m\,\mu_k(dx).
\]

The measure has a positive atom at \(1\) and a strictly positive density throughout \((0,1)\); in particular the occupation sequence is a **strict Hausdorff moment sequence**, not merely a decreasing sequence. It has strictly alternating finite differences of every positive order, every finite Hankel moment matrix is positive definite, and consecutive occupation probabilities are strictly log-convex.

The same representation gives a **nonasymptotic spectral envelope simultaneously for every pair of integers \(n\ge k\ge2\)**. Put \(m=n-k\), define \(H_j=\sum_{i=1}^j i^{-1}\), and let \(\xi_1\in(1,2)\) be the unique solution of \(\psi(1-\xi_1)=-\gamma\), numerically \(\xi_1=1.567353753101655\ldots\). Set

\[
a(k)=\frac{H_{k-1}}{(k-1)\zeta(2)},\qquad R_{k,m}=\frac{\Gamma(k+m)\Gamma(k+\xi_1)}{\Gamma(k)\Gamma(k+m+\xi_1)},
\]

and \(w_{k,1}=H_{k-1}/[(k-1+\xi_1)\psi'(1-\xi_1)]\). Then

\[
\boxed{\quad w_{k,1}R_{k,m}\ \le\ a(k+m,k)-a(k)\ \le\ [1-a(k)]R_{k,m}.\quad}
\]

Both inequalities are strict for \(m>0\); at \(m=0\), the upper one is equality. For every fixed \(k\ge2\) the exponent \(\xi_1\) is optimal because the ratio of the middle quantity to \(w_{k,1}R_{k,m}\) tends to \(1\) as \(m\to\infty\). The fixed-\(k\) leading asymptotic itself is already in the motivating literature; the claims here are the **exact global positive-mixture law, its strict all-order shape, and the all-size finite inequality**.

## Assumptions and scope

Define a discrete-time Markov chain on \(\{1,2,\ldots\}\) by

\[
\Pr(X_{t+1}=i\mid X_t=j)=\frac{1}{(j-i)H_{j-1}}\quad(1\le i<j),\qquad \Pr(X_{t+1}=1\mid X_t=1)=1.
\]

Its path strictly decreases until absorption at \(1\). For integers \(n\ge k\ge2\), define \(a(n,k)=\Pr_n(\exists t\ge0:X_t=k)\). We make no claim for \(k=1\), where \(a(n,1)=1\) is a degenerate constant sequence. All formulas are exact at finite indices and require no asymptotic relation between \(k\) and \(n\).

Let \(\psi=\Gamma'/\Gamma\), and let \(\gamma\) denote Euler's constant. As established by Berg and Durán, put \(\xi_0=0\), and for each integer \(j\ge1\) let \(\xi_j\in(j,j+1)\) be the unique root of \(\psi(1-\xi_j)=-\gamma\). Define \(\alpha_j=1/\psi'(1-\xi_j)>0\), including \(\alpha_0=1/\zeta(2)\). The weights

\[
w_{k,j}=\frac{H_{k-1}\alpha_j}{k-1+\xi_j},\qquad j\ge0,
\]

are strictly positive and sum to one. Define \(\operatorname{Beta}(k,0)=\delta_1\); for \(\xi>0\), \(\operatorname{Beta}(k,\xi)\) is the usual probability law with density \(x^{k-1}(1-x)^{\xi-1}/B(k,\xi)\) on \((0,1)\). The representing measure is the explicit mixture

\[
\boxed{\quad\mu_k=\sum_{j=0}^{\infty}w_{k,j}\,\operatorname{Beta}(k,\xi_j).\quad}
\]

Its atom is \(\mu_k(\{1\})=w_{k,0}=a(k)\); the remaining measure has positive density on every nonempty open subinterval of \((0,1)\). This gives the scope and uniqueness of the measure by the determinate Hausdorff moment problem.

## Proof

**1. The two published input identities.** The exact finite-difference identity for the harmonic descent occupation probabilities (Aldous–Janson–Li; as displayed in Svihla's proof) reads, with \(m=n-k\),

\[
a(n,k)=H_{k-1}\binom{n-1}{k-1}\sum_{h=0}^{m}(-1)^h\binom{m}{h}\frac1{H_{k+h-1}}.\tag{1}
\]

Berg and Durán proved the positive Hausdorff spectral expansion

\[
\frac1{H_{r+1}}=\sum_{j=0}^{\infty}\frac{\alpha_j}{r+1+\xi_j},\qquad r\ge0,\tag{2}
\]

with the strict positivity, locations and normalization of the \(\xi_j,\alpha_j\) specified above. Their representing density is \(\sum_j\alpha_jx^{\xi_j}\) on \((0,1)\). Both (1) and (2) are explicitly identified as existing inputs, not results newly claimed here.

**2. Positive spectral decomposition.** Because the sum in (1) is finite and each of its constituent expansions (2) converges, we may interchange its finite sum with the sum over \(j\). The beta-integral identity, valid for any \(b>0\) and nonnegative integer \(m\), is

\[
\sum_{h=0}^m(-1)^h\binom mh\frac1{b+h}
=\int_0^1t^{b-1}(1-t)^m\,dt
=\frac{\Gamma(b)\Gamma(m+1)}{\Gamma(b+m+1)}.\tag{3}
\]

Substituting \(b=k-1+\xi_j\) and using \(\binom{n-1}{k-1}=\Gamma(n)/[\Gamma(k)\Gamma(m+1)]\) gives the **convergent identity for each finite \(n\)**

\[
a(n,k)=\sum_{j=0}^{\infty}
\frac{H_{k-1}\alpha_j\Gamma(n)\Gamma(k-1+\xi_j)}
{\Gamma(k)\Gamma(n+\xi_j)}.\tag{4}
\]

Every summand in (4) is positive. With \(m=0\), (2) at \(r=k-2\) gives \(\sum_j w_{k,j}=H_{k-1}/H_{k-1}=1\). Using \(\Gamma(z+1)=z\Gamma(z)\) turns (4) into

\[
a(k+m,k)=\sum_{j=0}^{\infty}w_{k,j}
\frac{\Gamma(k+m)\Gamma(k+\xi_j)}{\Gamma(k)\Gamma(k+m+\xi_j)}.\tag{5}
\]

The quotient in (5) is the \(m\)-th moment of \(\operatorname{Beta}(k,\xi_j)\), with value one for \(j=0\). Hence (5) proves the stated mixture formula. No asymptotic interchange has occurred.

**3. Strict shape and spectral limit.** The \(j=0\) contribution in (5) equals \(w_{k,0}=H_{k-1}/[(k-1)\zeta(2)]\), using \(\psi'(1)=\zeta(2)\). Since the remaining beta laws are supported inside \((0,1)\), dominated convergence in (5) proves \(\lim_{n\to\infty}a(n,k)=w_{k,0}=a(k)\). For every \(r\ge1\), integer \(m\ge0\) and the forward difference \(\Delta b_m=b_{m+1}-b_m\),

\[
(-1)^r\Delta^r a(k+m,k)
=\int_{(0,1]}x^m(1-x)^r\mu_k(dx)>0.\tag{6}
\]

Strictness follows because the component \(\operatorname{Beta}(k,\xi_1)\) has strictly positive weight and a positive density on \((0,1)\). More strongly, for any integer \(d\ge0\) and nonzero vector \((c_0,\ldots,c_d)\),

\[
\sum_{i,j=0}^d c_ic_j a(k+i+j,k)
=\int_{(0,1]}\left(\sum_{i=0}^d c_ix^i\right)^2\mu_k(dx)>0.\tag{7}
\]

A nonzero polynomial cannot vanish on an interval; therefore all these Hankel matrices are positive definite. Their size-two principal minors yield strict log-convexity.

**4. Sharp finite-index comparison.** After removing the \(j=0\) atom, the nonnegative error is

\[
\delta_{k,m}:=a(k+m,k)-a(k)
=\sum_{j=1}^{\infty}w_{k,j}R_{k,m}(\xi_j),
\qquad
R_{k,m}(\xi)=\prod_{\ell=k}^{k+m-1}\frac\ell{\ell+\xi}.\tag{8}
\]

The empty product is one. For \(m>0\), \(R_{k,m}(\xi)\) is strictly decreasing in \(\xi>0\). Since \(0<\xi_1<\xi_2<\cdots\), isolating the first positive term proves the lower bound and replacing all remaining factors by \(R_{k,m}(\xi_1)\) proves the upper bound; strictness follows from \(w_{k,2}>0\). Also \(\sum_{j\ge1}w_{k,j}=1-a(k)\). For fixed \(k\), every ratio \(R_{k,m}(\xi_j)/R_{k,m}(\xi_1)\) with \(j\ge2\) tends to zero as \(m\to\infty\) and is bounded by one. Dominated convergence over the finite-mass weight sequence yields \(\delta_{k,m}/[w_{k,1}R_{k,m}(\xi_1)]\to1\). Finally \(R_{k,m}(\xi_1)\sim\Gamma(k+\xi_1)\Gamma(k)^{-1}(k+m)^{-\xi_1}\), which proves optimality of the decay exponent for every fixed \(k\). The previously published fixed-\(k\) asymptotic constant agrees with this calculation.

## Verification

Run the included standalone standard-library diagnostic with `python3 verify.py`. It reconstructs the chain's rational occupation probabilities independently via first-step recursion and the exact alternating-binomial formula, checks both agree, then checks strict alternating differences through order eight, strict two-by-two Hankel determinants, and strict three-by-three Hankel determinants. Its reported run passed **4,416 exact rational assertions**, for \(2\le k\le13\) and \(n\le46\). The finite tests are diagnostics, not a proof of (4), (6), (7), or the all-index bounds; those are analytically proved above from the cited positive representation.

## Relationship to prior work

Aldous, Janson and Li identified the limiting occupation probabilities. Brandenberger, Chin and Mossel established strict first-order decrease and power-law convergence; these properties are **not** new claims. Svihla (October 2026) displayed formula (1) and used Rice-integral residues to obtain an asymptotic spectral expansion and its leading constant, but did not supply the all-finite-index positive Beta-mixture law, complete monotonicity, Hankel definiteness, or the explicit all-\(n,k\) two-sided envelope. Berg and Durán (2005) established the positive moment representation (2) for reciprocal harmonic numbers, but did not consider this descent chain. Iksanov (2024) represented the chain by regenerative compositions to derive the limiting occupation law; that construction does not give the stated beta-mixture or all-order finite-index inequalities. The result here is the exact structural transfer between these known identities and its strict consequences, not a claim of independent rediscovery of either input.

## Limitations

The statement concerns this specific harmonic descent transition kernel and target integers \(k\ge2\). The bounds are not asserted to have optimal finite-\(m\) coefficients; “sharp exponent” refers to fixed-\(k\) power-law order, not best constants for every index. The exact mixture uses an infinite countable spectral family of digamma roots, not an elementary closed-form density. No result about arbitrary beta-splitting parameters, absorption-time distributions, or other Markov chains is claimed. The bibliographic comparison cannot exclude an unlocated earlier equivalent finite-index representation.

## References

1. Sean P. Svihla, *Exact Asymptotics for the Harmonic Descent Chain and Extended Convergence Bounds for Recursive Statistics*, arXiv:2611.00347v1, first public October 30, 2026, https://arxiv.org/html/2611.00347v1 .
2. Christian Berg and Antonio J. Durán, *Some Transformations of Hausdorff Moment Sequences and Harmonic Numbers*, Canadian Journal of Mathematics 57 (2005), 941–960, especially formula (1.2), https://doi.org/10.4153/CJM-2005-036-8 .
3. Anna Brandenberger, Byron Chin and Elchanan Mossel, *Asymptotics for the harmonic descent chain and applications to critical beta-splitting trees*, arXiv:2505.24821, https://arxiv.org/pdf/2505.24821 .
4. David J. Aldous, Svante Janson and Xiaodan Li, *The Harmonic Descent Chain*, Electronic Communications in Probability 29 (2024), article 77, arXiv:2405.05102, https://arxiv.org/pdf/2405.05102 .
5. Alexander Iksanov, *A comment on “The harmonic descent chain” by D. J. Aldous, S. Janson and X. Li*, arXiv:2412.06826, https://arxiv.org/pdf/2412.06826 .
