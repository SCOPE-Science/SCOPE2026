# Geodesic-needle crossing networks: exact star spectrum and a variance transition

## Finding

For \(n\ge 2\), independently sample geodesic arcs \(A_1,\ldots,A_n\) on the round unit two-sphere. Take a random length \(L\) supported on \((0,\pi)\), form the corresponding shorter great-circle arc and rotate it independently by a Haar-uniform element of \(\mathrm{SO}(3)\). Join vertices \(i,j\) when the interiors of \(A_i,A_j\) intersect. Denote the degree of vertex \(i\) by \(K_i\), and the total number of crossings by \(C_n\).

Set \(\mu=\mathbb E[L]>0\), \(\sigma^2=\operatorname{Var}(L)\), \(p=\mu^2/(2\pi^2)\) and \(\gamma=\mu^2\sigma^2/(4\pi^4)\). Then:

\[
 K_i\mid (L_i=\ell)\sim\operatorname{Bin}\left(n-1,\frac{\mu\ell}{2\pi^2}\right),
 \qquad \mathbb E C_n=\binom n2p,
\]

\[
 \operatorname{Var}C_n=\binom n2p(1-p)+6\binom n3\gamma.
\]

For every positive integer \(r\), the probability that one fixed arc intersects each of \(r\) other independently chosen arcs is exactly
\[
 s_r=\mathbb E\left[\left(\frac{\mu L}{2\pi^2}\right)^r\right].
\]
Consequently the complete limiting normalized-degree law is the distribution of \(\mu L/(2\pi^2)\), and the empirical law of \(\{K_i/(n-1):1\le i\le n\}\) converges weakly to it almost surely under a common infinite-sample coupling. If \(\sigma^2>0\),
\[
 \frac{C_n-\mathbb E C_n}{n^{3/2}}\Longrightarrow
 N\left(0,\frac{\mu^2\sigma^2}{4\pi^4}\right).
\]
If the arc length is a fixed \(\ell\in(0,\pi)\), all distinct crossing indicators are pairwise independent, and the exact variance is only \(\binom n2p(1-p)\), with \(p=\ell^2/(2\pi^2)\). No Gaussian limit on the smaller scale is asserted in the fixed-length case.

**Area-uniform endpoint specialization.** If each arc connects two independently selected area-uniform sphere points by the shorter arc, then \(L\) has density \(\frac12\sin\ell\) on \((0,\pi)\). In this case \(\mu=\pi/2\), \(\sigma^2=\pi^2/4-2\), \(p=1/8\), and
\[
 \operatorname{Var}C_n=
 \binom n2\frac7{64}
 +6\binom n3\frac{\pi^2-8}{64\pi^2}.
\]
The normalized-degree density equals \(2\pi\sin(4\pi x)\) on \((0,1/4)\), and is zero elsewhere. The star probabilities have the elementary recurrence
\[
 s_r=\frac{I_r}{2(4\pi)^r},\qquad I_0=2,\quad I_1=\pi,
 \quad I_r=\pi^r-r(r-1)I_{r-2}\quad(r\ge2).
\]

## Assumptions and scope

Only the round two-sphere, shortest arcs of length strictly less than \(\pi\), independent arcs, isotropic Haar rotations, and independent lengths with a common probability distribution are assumed. The length distribution may contain atoms. Arc endpoints and intersection events have no geometric degeneracies with positive probability. Every arc is an *edge* and a *vertex of the crossing graph* simultaneously; a crossing is a transverse intersection of two arc interiors. The theorem does not concern a complete-graph drawing whose arcs share sample endpoints.

## Proof

**1. Conditional crossing probability.** Fix a shorter arc \(A\) of length \(\ell\). The supporting great circle of an independently isotropic arc \(B\) intersects the supporting circle of \(A\) in a uniformly rotated antipodal pair. Since \(\ell<\pi\), exactly one of these two points lies in the interior of \(A\) with probability \(\ell/\pi\). Conditional on this supporting circle and on the length \(L_B=s\), the phase of the arc \(B\) is uniform on the full great circle of circumference \(2\pi\), so the probability it covers the selected point is \(s/(2\pi)\). Hence
\[
 g(\ell):=\Pr(B\cap A\ne\varnothing\mid A)=\frac{\ell\mu}{2\pi^2}.
\]
This is the critical geometric identity. Its derivation requires the two antipodal intersection points and the distinction between \(\pi\) and \(2\pi\); missing either factor would change every subsequent formula.

**2. Exact degrees, stars and variance.** Conditional on \(A_i\), all \(n-1\) crossing events with the other independent arcs are independent Bernoulli variables of common success probability \(g(L_i)\). This proves the binomial mixture. Taking expectations gives \(p=\mathbb E[g(L)]=\mu^2/(2\pi^2)\) and the star moments \(s_r=\mathbb E[g(L)^r]\). Write \(H_{ij}\) for the crossing indicator. Indicators indexed by disjoint arc pairs are independent. For distinct pairs sharing one arc, conditional independence yields
\[
\operatorname{Cov}(H_{12},H_{13})=\operatorname{Var}(g(L_1))
=\frac{\mu^2\sigma^2}{4\pi^4}=\gamma.
\]
There are \(\binom n2\) individual indicators and \(3\binom n3\) unordered pairs of distinct indicators sharing one arc; expansion of the variance (with a factor \(2\) on off-diagonal pairs) proves the displayed exact expression. If \(\sigma^2=0\), these covariances vanish. Because each distinct pair of indicators is Bernoulli with equal marginal \(p\), zero covariance is equivalent to pairwise independence.

**3. Empirical degree law.** Given arc \(A_i\), Hoeffding's binomial tail inequality gives
\[
 \Pr\left(\left|\frac{K_i}{n-1}-g(L_i)\right|>\varepsilon\right)
 \le2\exp[-2(n-1)\varepsilon^2].
\]
The union bound over all \(n\) vertices is summable in \(n\). On an infinite independent-arc coupling, Borel–Cantelli therefore gives uniform convergence of \(K_i/(n-1)-g(L_i)\) over \(1\le i\le n\) almost surely. The ordinary strong law for the independent \(g(L_i)\) proves the claimed empirical weak limit.

**4. Central limit theorem.** The bounded symmetric kernel \(h(A,B)=\mathbf1_{\{A\cap B\ne\varnothing\}}\) has first Hoeffding projection \(h_1(A)=g(L_A)-p\), of variance \(\gamma\). Its centered two-sample degenerate remainder has variance of order \(n^2\) when summed over all pairs, since cross-covariances of distinct degenerate terms vanish. Thus
\[
 C_n-\mathbb E C_n=(n-1)\sum_{i=1}^n h_1(A_i)+R_n,
 \qquad\mathbb E R_n^2=O(n^2).
\]
For \(\gamma>0\), the usual independent-summand central limit theorem and Slutsky's theorem yield the asserted normal limit on scale \(n^{3/2}\). For \(\gamma=0\), the exact variance calculation identifies the different quadratic variance order, but no distributional limit at scale \(n\) is implied.

**5. Endpoint model.** If the endpoints are independent uniform points on \(S^2\), the angle \(L\) between them has density \(\sin\ell/2\). Elementary integration gives \(\mathbb E L=\pi/2\) and \(\mathbb E L^2=(\pi^2-4)/2\). Substituting into the formulas above gives the stated variance and the change-of-variable density. Integration by parts gives the recurrence for \(I_r=\int_0^\pi \ell^r\sin\ell\,d\ell\). Conditional isotropy of each endpoint-defined arc follows from rotational invariance.

## Verification

The standalone script `verify.py` independently samples arcs from random spherical midpoints and tangents, computes great-circle intersection points, checks membership in each shorter arc, and compares the total crossing count with the exact mean and variance for both fixed length \(\pi/2\) and random endpoint lengths. It also checks the conditional degree binomial second-moment identity, the star-moment recurrence and the degree-density normalization. In the recorded execution, 20,000 independent networks of 10 arcs were generated for **each** length model. The exact analytic argument above, rather than the simulation, proves the theorem.

## Relationship to prior work

The pairwise crossing probability \(1/8\) for independent uniform endpoints is known; it was given with an antipodal-point symmetry argument in Gil Bor's January 6, 2014 MathOverflow answer. Bonamy, Mohar and Wesolek's 2020 geodesic crossing-graphon work proves general graphon convergence and the edge density \(1/8\) for related uniform spherical drawings, and treats independent random geodesic arcs in its comparison model. Those results establish important overlapping structural groundwork; the present contribution is the evaluated **full star-moment sequence**, its explicit degree measure, the exact finite-network variance, and the random-versus-fixed-length variance transition, not the edge probability or existence of the graphon limit. Lepsveridze and Solé-Pi's 2026 result treats sharp weighted crossing minimization at a prescribed edge density, not this arc-crossing network's degree/variance law. The general central-limit-theorem step is the standard first-order theory of U-statistics, not a newly invented probabilistic theorem.

## Limitations

This result concerns iid isotropic geodesic arcs with independent lengths; it does not describe random edges of one complete graph with shared endpoints, nonuniform directional distributions, antipodal arcs of length exactly \(\pi\), or crossing statistics on nonspherical manifolds. No non-Gaussian limit law for deterministic arc lengths is claimed. Source comparisons were bounded; older spherical-needle treatments could have unrecognized equivalent intermediate formulas. This is a self-review, not independent validation or a claim of established historical priority.

## References

1. Gil Bor, answer to *Probability of random geodesics on the round sphere intersecting*, MathOverflow, January 6, 2014. https://mathoverflow.net/questions/153700/probability-of-random-geodesics-on-the-round-sphere-intersecting
2. M. Bonamy, B. Mohar and A. Wesolek, *Limiting crossing numbers for geodesic drawings on the sphere*, arXiv:2008.10459 (2020). https://arxiv.org/abs/2008.10459
3. S. Lepsveridze and O. Solé-Pi, *Uniform Geodesic Drawings of Graphs*, arXiv:2605.16700 (2026). https://arxiv.org/abs/2605.16700
4. Y. Isokawa, *Buffon's short needle on the sphere*, Bulletin of the Faculty of Education, Kagoshima University, Natural Science 51 (2000), 17–36 (historical needle context; original full text not inspected).
5. W. Hoeffding, *A class of statistics with asymptotically normal distribution*, Annals of Mathematical Statistics 19 (1948), 293–325 (classical U-statistic asymptotics).
