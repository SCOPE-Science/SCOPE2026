# Marked extremes of circular one-dimensional Voronoi cells

## Finding
For every integer \(n\ge3\), let \(X_1,\ldots,X_n\) be independent uniform points on a circle of circumference one, and let \(L_i\) be the arc length of the Voronoi cell of site \(X_i\). Let \(G_i^-\) and \(G_i^+\) be its clockwise-preceding and clockwise-following intersite gaps, and define the left-fraction mark \(R_i=G_i^-/(G_i^-+G_i^+)\). Put \(a_n=\log n+\log\log n\).

As \(n\to\infty\), the marked point measure
\[
\Xi_n=\sum_{i=1}^n\delta_{(X_i,\,2nL_i-a_n,\,R_i)}
\]
converges vaguely on \(\mathbb T\times\mathbb R\times[0,1]\) to a Poisson point process with intensity \(du\,e^{-x}dx\,dr\), where \(du\) and \(dr\) are uniform probability measures on the circle and on \([0,1]\), respectively. In particular, the centered largest-cell score \(2n\max_iL_i-a_n\) tends to the standard Gumbel distribution, and the location and left-fraction mark of its almost surely unique maximizing cell tend jointly to independent uniform variables, independent of the Gumbel score. For each fixed \(x\in\mathbb R\), the number \(N_n(x)=\#\{i:2nL_i>a_n+x\}\) satisfies
\[
d_{\mathrm{TV}}\bigl(\mathcal L(N_n(x)),\operatorname{Poisson}(e^{-x})\bigr)
=O_x\!\left(\frac{1+\log\log n}{\log n}\right).
\]
There is also an exact finite-sample structural identity: the left-fraction mark of a predesignated site is uniform on \([0,1]\) and independent of twice that site's Voronoi length, which has the \(\operatorname{Beta}(2,n-2)\) law.

## Assumptions and scope
All sites are independent and arclength-uniform, distances are shorter circular arc distances, and no two sites coincide (an almost sure condition). The Voronoi cell of any site is the clockwise interval between the midpoints to its two neighboring sites; hence \(2L_i=G_i^-+G_i^+\). The point-process topology is vague convergence on compact height windows, with circle coordinate modulo one. The quantitative total-variation assertion holds for each fixed real \(x\), for all sufficiently large \(n\) such that \(a_n+x>0\); it does not assert uniformity as \(x\) varies with \(n\).

## Proof
**1. Exact exponential representation and tagged law.** Choose a uniformly tagged starting site and list the circular spacings from it. This random vector has the Dirichlet \((1,\ldots,1)\) law. Equivalently, if \(E_1,\ldots,E_n\) are independent unit-rate exponentials and \(T=\sum_j E_j\), its gaps are \(G_j=E_j/T\), cyclically. The starting phase \(\theta\) is uniform and independent of the gap vector. Label the sites \(X_i=\theta+\sum_{j=1}^i E_j/T\pmod1\) for \(1\le i\le n\), so the incoming gap of \(X_i\) is \(E_i/T\) and its outgoing gap is \(E_{i+1}/T\), with cyclic indices. Write \(B_i=E_i+E_{i+1}\) and \(R_i=E_i/B_i\). Then \(2nL_i=nB_i/T\). Since two independent exponentials have gamma sum and an independent uniform ratio, \(B_i\sim\operatorname{Gamma}(2,1)\), \(R_i\sim\operatorname{Uniform}[0,1]\), and these two variables are independent. Likewise \(B_i/T\sim\operatorname{Beta}(2,n-2)\), independently of \(R_i\). Thus, for \(0\le y\le1\), the tagged exact tail is
\[
\Pr(2L_i>y)=(1-y)^{n-2}\bigl(1+(n-2)y\bigr).
\]

**2. Rare-event probabilities and overlaps.** Put \(u_n(x)=a_n+x\). For \(u>0\), direct gamma integration gives
\[
p(u):=\Pr(B_i>u)=(1+u)e^{-u}.
\]
The sequence of marked triples \((B_i,R_i,i/n)\) is one-dependent away from the circular wrap. For neighbors, integrate over their common exponential \(E_{i+1}\) to obtain the exact identity
\[
q(u):=\Pr(B_i>u,B_{i+1}>u)
=\int_0^u e^{-y-2(u-y)}dy+\int_u^\infty e^{-y}dy
=2e^{-u}-e^{-2u}.
\]
For nonneighboring indices with disjoint exponential pairs, the events are independent. At \(u=u_n(x)\), \(np(u)\to e^{-x}\), while \(nq(u)=O_x(1/\log n)\).

**3. Poisson convergence with height, shape and spatial marks.** Fix a lower height cutoff \(x_0\) and divide the cyclic index set into consecutive blocks of length \(b_n=\lfloor(\log n)^2\rfloor\), deleting one index between blocks. The probability of any exceedance among the deleted indices is \(O(1/b_n)\). Blocks of the remaining marked exponential data are independent because each uses disjoint underlying exponentials. By a union bound using the preceding probabilities, the probability that any surviving block contains two or more exceedances is at most
\[
O\bigl(nq(u_n(x_0))+nb_np(u_n(x_0))^2\bigr)=o(1).
\]
The maximum probability that a given block contributes a point is \(O(b_n/n)=o(1)\). The intensity measure summed over the blocks converges to \(du\,e^{-x}dx\,dr\): the index locations form a uniform grid, \(n\Pr(B_i>a_n+x)\to e^{-x}\), and \(R_i\) is exactly uniform and independent of \(B_i\). The law of small numbers for independent rare marked blocks therefore gives the required Poisson convergence for \((i/n,B_i-a_n,R_i)\) above any fixed cutoff \(x_0\), and hence vague convergence.

For the original Voronoi variables, \(T/n\to1\) with fluctuations \(O_{\mathbb P}(n^{-1/2})\), and \(\max_iB_i=O_{\mathbb P}(\log n)\). Therefore replacing \(B_i\) by \(nB_i/T\) changes all relevant heights by \(o_{\mathbb P}(1)\). Maximal partial-sum deviations give \(\max_i|\sum_{j<i}E_j/T-(i-1)/n|=o_{\mathbb P}(1)\). Restoring the independent uniform starting phase only rotates the limiting homogeneous Poisson process, leaving its law invariant. This completes the marked limit.

**4. Count approximation with a rate.** For \(N_n^E(x)=\sum_i\mathbf1\{B_i>u_n(x)\}\), the dependency-neighborhood Chen–Stein bound has \(b_1\le3np(u)^2\) and \(b_2\le2nq(u)\), hence
\[
d_{\mathrm{TV}}\bigl(\mathcal L(N_n^E(x)),\operatorname{Poisson}(np(u_n(x)))\bigr)=O_x(1/\log n).
\]
Moreover \(np(u_n(x))=e^{-x}[1+(\log\log n+x+1)/\log n]\). To transfer the estimate to the normalized gaps, use \(\Pr(|T/n-1|>n^{-1/3})\le n^{-1/3}\), by Chebyshev's inequality. On its complement, sandwich \(N_n(x)\) between exponential-gap exceedance counts whose thresholds differ from \(u_n(x)\) by \(O(n^{-1/3}\log n)\). The probability that the sandwich counts differ is \(O_x(n^{-1/3}\log n)\), using the gamma tail and a union bound. This proves the stated total-variation bound.

**5. Largest-cell consequences.** The limiting point process has finitely many points above each fixed height, almost surely a unique top point, and product-form intensity. Its top height has distribution \(\exp(-e^{-x})\), while its location and left-fraction mark are independent uniforms independent of that height. The continuous-mapping argument applies after truncation below a sufficiently negative cutoff and then removal of the cutoff.

## Verification
The standalone `check.py` uses exact rational identities for the finite tagged \(\operatorname{Beta}(2,n-2)\) survival law, independently integrates the two-neighbor exponential exceedance probability, and runs reproducible finite simulations of the largest-cell score and marks. It does not substitute for the coupling, blocking, and approximation arguments above. The proof requires no unprovided numerical constants or external datasets.

## Relationship to prior work
An existing exact finite-dimensional law for the entire ordered vector of circular Voronoi cell lengths determines any finite-n length statistic. For odd sample sizes this law also uniquely reconstructs the original spacings, so it implicitly determines the finite joint distribution of left/right shape fractions. Those exact finite formulas do not themselves establish the present growing-dimensional, marked extreme point-process limit, its asymptotic factorization or the quantitative count error. The present proof supplies a direct one-dependent extremal analysis. Classical spacing theory and the published Poisson/compound-Poisson treatments of circular \(m\)-spacings cover important unmarked extreme-spacing and exceedance-count behavior. In particular, Roos (1993) addresses counts and their approximation rates. Aaron, Cholaquidis and Fraiman (2014, arXiv:1411.2482) analyze maximal *empty* spacings for density-based support testing, which are not the two-consecutive-gap Voronoi cells here. Devroye, Györfi, Lugosi and Walk (2015, arXiv:1512.04267) establish distributional facts for a *typical* Voronoi cell, not the joint extreme height–location–left/right-shape process. The new assertion here is the explicit shape-marked point-process law and independence of the maximizing cell's skew, with a direct one-dependent proof and a count approximation rate. The available abstracts of older \(m\)-spacing works do not resolve every historical-priority question; see REVIEW.md.

## Limitations
The statements assume a homogeneous uniform circle and do not cover nonuniform densities, interval boundary cells, higher-dimensional Voronoi shapes, or a growing height threshold. The \(O_x\) constant depends on \(x\); optimality of its order is not claimed. The unmarked Gumbel law is related to classical extreme \(m\)-spacing results and is not claimed as novel by itself. Independent mathematical review and full historical-priority certification have not been performed.

## References
- M. Roos, “Compound Poisson approximations for the numbers of extreme spacings,” *Advances in Applied Probability* **25** (1993), 847–874, DOI: 10.2307/1427795.
- C. Aaron, A. Cholaquidis and R. Fraiman, “A Generalization of the maximal-spacings in several dimensions and a convexity test,” first arXiv posting 2014-11-10, arXiv:1411.2482, https://arxiv.org/abs/1411.2482.
- L. Devroye, L. Györfi, G. Lugosi and H. Walk, “On the measure of Voronoi cells,” first arXiv posting 2015-12-14, arXiv:1512.04267, https://arxiv.org/abs/1512.04267.
- A. D. Barbour, L. Holst and S. Janson, *Poisson Approximation*, Oxford University Press, 1992, Chapter 7 (spacings).
