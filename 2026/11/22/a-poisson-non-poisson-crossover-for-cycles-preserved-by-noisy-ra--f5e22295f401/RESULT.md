# A Poisson–non-Poisson crossover for cycles preserved by noisy random mappings

## Finding
Let \(f_n:[n]\to[n]\) be uniform, and construct \(g_n\) independently at each vertex by keeping \(f_n(v)\) with probability \(\rho_n\in[0,1]\), otherwise replacing it by an independent uniform value of \([n]\). A **common directed cycle** is the same cyclically ordered list of distinct vertices under both maps. Write \(C_{n,k}\) for the number of common directed cycles of length \(k\), and put
\[
s_n=\rho_n+\frac{1-\rho_n}{n},\qquad \delta_n=-\log s_n.
\]
For any ordered list of positive integers \(k_1,\ldots,k_r\), with \(K=\sum_i k_i\), the exact factorial measure of distinct common cycles is
\[
\mathbb E\!\sum_{\substack{(\gamma_1,\ldots,\gamma_r)\\\text{ordered distinct common cycles}}}
\prod_{i=1}^r {\bf1}\{|\gamma_i|=k_i\}
=\frac{(n)_K}{n^K}\frac{s_n^K}{\prod_i k_i},
\quad (n)_K:=\prod_{j=0}^{K-1}(n-j),
\]
with value zero if \(K>n\). This identity supports a **single crossover theorem** for the point measure of common-cycle lengths:

1. If \(s_n\to s\in[0,1)\), the counts at distinct positive integer lengths converge jointly to independent \(\operatorname{Poisson}(s^k/k)\) variables, and the total number converges to \(\operatorname{Poisson}(-\log(1-s))\).
2. If \(\delta_n\to0\) and \(\delta_n\sqrt n\to\infty\), then \(\sum_k C_{n,k}\delta_{\delta_n k}\) converges vaguely on \((0,\infty)\) to a Poisson point process with intensity \(e^{-x}\,dx/x\).
3. If \(\delta_n\sqrt n\to a\in[0,\infty)\), then \(\sum_k C_{n,k}\delta_{k/\sqrt n}\) converges vaguely on \((0,\infty)\) to a point process \(\Xi_a\) whose ordered factorial moment densities are, for every \(r\ge1\),
\[
\boxed{\quad\alpha_a^{(r)}(x_1,\ldots,x_r)
=\frac{\exp[-aS-S^2/2]}{x_1\cdots x_r},\qquad S=x_1+\cdots+x_r.\quad}
\]
In particular, for any two disjoint intervals \(A,B\) of positive length contained in a compact subinterval of \((0,\infty)\),
\[
\operatorname{Cov}(\Xi_a(A),\Xi_a(B))
=\int_A\!\int_B
\frac{e^{-a(x+y)}\big(e^{-(x+y)^2/2}-e^{-(x^2+y^2)/2}\big)}{xy}\,dy\,dx<0.
\]
Thus the critical scaling is **not** Poisson: cycles in separated macroscopic size bands are strictly negatively correlated. This contrasts with independent Poisson cycle-length bands below the critical scale.

Write \(M_n=\max\{k:C_{n,k}>0\}\), with \(M_n=0\) if there is no shared cycle. In regime 2, for every \(x>0\),
\[
\Pr(\delta_n M_n\le x)\to\exp\!\left(-\int_x^\infty\frac{e^{-u}}u\,du\right).
\]
In regime 3, for each \(x>0\), \(\Pr(M_n/\sqrt n\le x)\) converges to the absolutely convergent inclusion–exclusion series
\[
F_a(x):=\sum_{r=0}^\infty\frac{(-1)^r}{r!}
\int_{(x,\infty)^r}\!\frac{e^{-aS-S^2/2}}{x_1\cdots x_r}\,dx_1\cdots dx_r,
\]
where the \(r=0\) term is one.

## Assumptions and scope
The maps act on labelled \([n]\), and independent vertex replacement uses the **same** number of vertices \(n\). A redraw may accidentally equal the original target, which is why the effective agreement probability is \(s_n\), not \(\rho_n\). Self-loops count as length-one directed cycles. Every cycle is counted once modulo cyclic rotation, and reversed orientation counts as different unless the directed edges coincide. Point-process convergence is vague on \((0,\infty)\): the covariance concerns finite counts in bands bounded away from zero. In fact \(\Xi_a\) has infinitely many points in every interval \((0,b)\), \(b>0\), almost surely. The regimes are statements about deterministic parameter sequences and integer \(n\to\infty\).

## Proof
**Exact factorial identity.** For a fixed ordered length list \((k_i)\), there are \((n)_K/\prod_i k_i\) ordered collections of vertex-disjoint oriented cycles with those lengths. A prescribed directed edge of \(f_n\) has probability \(1/n\); conditional on \(f_n\), the corresponding edge of \(g_n\) agrees with it with independent probability \(s_n\). Thus a prescribed collection is common with probability \((s_n/n)^K\). Distinct cycles in any functional digraph are automatically vertex-disjoint. This proves the stated identity, including the zero case \(K>n\).

**Point-process limits.** For bounded continuous compactly supported \(h\) on \((0,\infty)\), expand the exact multiplicative functional \(\mathbb E\prod_{\gamma}(1+h(t_n|\gamma|))\), where the product runs over common cycles. Its \(r\)-th term is
\[
\frac1{r!}\sum_{k_1,\ldots,k_r\ge1}
\frac{(n)_K}{n^K}s_n^K\prod_i\frac{h(t_n k_i)}{k_i},
\]
with \((n)_K=0\) for \(K>n\). If the support lies in \([\varepsilon,B]\), the sum of \(1/k\) over its index range is uniformly bounded; hence the whole expansion is dominated by an exponential series. If \(t_n=\delta_n\), \(\delta_n\sqrt n\to\infty\), and \(\delta_n\to0\), the sum is a Riemann sum: for \(k_i\delta_n\to x_i\), \((n)_K/n^K\to1\) and \(s_n^K=e^{-\delta_n K}\to e^{-S}\). This yields the Poisson exponential functional of intensity \(e^{-x}/x\).

If \(t_n=n^{-1/2}\), \(\delta_n\sqrt n\to a\), then for \(K/\sqrt n\to S\),
\[
\log((n)_K/n^K)=\sum_{j=0}^{K-1}\log(1-j/n)\to-S^2/2,
\qquad s_n^K\to e^{-aS}.
\]
The same dominated Riemann-sum argument gives the factorial densities \(\alpha_a^{(r)}\). Taking \(h=e^{-\varphi}-1\) for nonnegative compactly supported continuous \(\varphi\) identifies the limiting Laplace functional; uniform first-moment bounds give tightness on every compact subinterval. Such a locally finite point process exists, independently witnessed by the scaling limit of the uniform mapping's cyclic vertices (Rayleigh law), a uniform permutation of that cyclic set (Poisson–Dirichlet \((1)\) cycle proportions), and independent marks retaining a cycle of scaled size \(x\) with probability \(e^{-ax}\). The displayed factorial measures also determine the process uniquely because all compact-support exponential moments are bounded by the preceding expansion.

When \(s_n\to s<1\), the exact factorial identity for fixed lengths yields independent Poisson limits; the expected number of cycles of length above \(L\) is at most \(\sum_{k>L}s_n^k/k\), which tends uniformly to zero as \(L\to\infty\). This also gives convergence of total cycle counts.

**Dependence and extremes.** For disjoint size bands bounded away from zero, integrate the first and second factorial densities and subtract the product of their means. Since \((x+y)^2>x^2+y^2\) when \(x,y>0\), the critical covariance is strictly negative. The same kernel comparison on the square of a single band shows that the count on \((\varepsilon,b)\) has variance at most its mean, and its mean diverges as \(\log(1/\varepsilon)+O_{a,b}(1)\) when \(\varepsilon\downarrow0\). Chebyshev's inequality gives \(\Pr(\Xi_a((\varepsilon,b))\le m)\to0\) for each finite \(m\). Monotonicity in \(\varepsilon\) gives the claimed infinite count on \((0,b)\) (simultaneously for all \(b>0\) by a countable sequence decreasing to zero). There is no finite covariance assertion for such a band.

For \(x>0\), the limiting upper tails of the expected number of lengths beyond \(B>x\) are bounded by the tail integrals of \(e^{-u}/u\) or \(e^{-u^2/2}/u\). In the critical scaling use \((n)_k/n^k\le e^{-k(k-1)/(2n)}\): on an interval \([B,L]\) this bound gives the Gaussian tail integrand in the Riemann-sum limit, and on \([L,\infty)\) it is dominated uniformly for large \(n\) by \(e^{-u^2/4}\) with \(u=k/\sqrt n\). These bounds extend compact convergence to the largest-cycle event; a specified positive boundary \(x\) has no atom by absolute continuity of the first intensity. The Poisson void probability gives regime 2. In regime 3, inclusion–exclusion for the number of points above \(x\) gives \(F_a(x)\). Absolute convergence follows since \(S^2\) is at least both \((rx)^2\) and \(\sum_i x_i^2\), so the \(r\)-fold integral is at most \(e^{-(rx)^2/4}\big(\int_x^\infty e^{-au-u^2/4}\,du/u\big)^r\).

## Verification
Run `python3 verify.py` from the package directory. It enumerates all \(50{,}068\) functional maps across sizes \(n=2,\ldots,6\), conditions exactly on each map's directed-cycle counts, and checks \(115\) rational identities: single- and ordered-distinct-pair factorial expectations at every length, plus a full inclusion–exclusion void probability. It uses \(\rho=2/3\) and the correct accidental-redraw adjustment. Computations test finite algebra but do not replace the analytic limiting proof.

## Relationship to prior work
The classical random-mapping literature describes cyclic vertices, unperturbed cycle lengths, Brownian-bridge limits and the uniform permutation on the cyclic set. Aldous and Pitman (1994 and 2004), Hansen and Jaworski (2010), and Finch (2022) are relevant. The \(a=0\) critical cycle-size process and unperturbed longest-cycle law are prior. Conditional on the first map, its cycles are independently retained with probability \(s_n^k\) for a length-\(k\) cycle; accordingly the fixed critical window is an explicit size-dependent thinning of the classical cycle-size process. Equivalently, assign a cemetery target to each disagreeing outgoing edge: each ordinary vertex independently points to each ordinary target with probability \(s_n/n\) and otherwise points to the cemetery. The common cycles are exactly the cycles avoiding the cemetery. This is an independent-image mapping representation, not a new general construction of random mappings. Hansen and Jaworski's distinct trimming process deletes only **noncyclic** edges and leaves the original cycles intact. The contribution here is a single noise-scale analysis of identical directed-cycle survival, including the intermediate Poisson process, its change to critical dependence, and the corresponding extreme-cycle laws. Historical equivalent formulations may exist.

## Limitations
There is no assertion about cycles of \(g_n\) not already present in \(f_n\), or about shared periodic vertices that follow different cycle trajectories. No convergence rates or quantitative asymptotics for the total number of cycles in regimes 2 and 3 are given. The original 1994 article was not available in full for comparison; the later mathematical treatment is a source for the unthinned partition. No exhaustive historical-priority claim is made.

## References
- D. Aldous and J. Pitman, *Brownian bridge asymptotics for random mappings*, Random Structures & Algorithms **5** (1994), 487–512, https://doi.org/10.1002/rsa.3240050402.
- D. Aldous and J. Pitman, *Two recursive decompositions of Brownian bridge related to the asymptotics of random mappings*, arXiv:math/0402399, first posted 2004-02-25, https://arxiv.org/abs/math/0402399.
- J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria **94** (2010), 341–359, https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/.
- J. C. Hansen and J. Jaworski, *A cutting process for random mappings*, Random Structures & Algorithms **30** (2007), 287–306, https://doi.org/10.1002/rsa.20159.
- S. Finch, *Components and Cycles of Random Mappings*, arXiv:2205.05579 (2022), https://arxiv.org/html/2205.05579v1.
