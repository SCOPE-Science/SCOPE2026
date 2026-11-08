# Rare-hub variance inflation in random greedy adsorption on clique-joined cycles

## Finding
Let \(C_n\) be the cycle on \(n\ge4\) vertices, let \(K_k\) be a clique on \(k\ge1\) vertices, and let \(G_{n,k}=K_k\vee C_n\) be their **join** (every clique vertex is adjacent to every cycle vertex). Process all vertices of \(G_{n,k}\) in a uniformly random order, accepting a vertex precisely when none of its previously accepted neighbors is adjacent to it. Let \(X_{n,k}\) be the final accepted-set size. For the path \(P_m\), let \(R_m\) be the corresponding random greedy accepted-set size and let \(f_m(z)=\mathbb E z^{R_m}\), with \(f_0(z)=f_{-1}(z)=1\).

**Exact finite law.** For every \(n\ge4\), \(k\ge1\), and complex \(z\),
\[
\mathbb E z^{X_{n,k}}=\frac{kz+n z f_{n-3}(z)}{n+k}.
\]
Consequently \(\Pr(X_{n,k}=1)=k/(n+k)\); otherwise the count has the distribution of \(1+R_{n-3}\).

Define \(\rho=(1-e^{-2})/2\) and \(\sigma^2=e^{-4}\). For any positive integer sequence \(k_n=o(n)\),
\[
\frac{X_{n,k_n}-\rho n}{\sqrt n}\ \xrightarrow{d}\ N(0,\sigma^2),
\qquad \frac{\mathbb E X_{n,k_n}}n\longrightarrow\rho.
\]
For each *fixed* integer \(k\ge1\), however,
\[
\lim_{n\to\infty}\frac{\operatorname{Var}(X_{n,k})}{n}=\sigma^2+k\rho^2,
\qquad \mathbb E X_{n,k}=\rho n-k\rho+o(1).
\]
Thus on ordinary wheel graphs (\(k=1\)) the Gaussian weak limit has variance parameter \(e^{-4}\) but the finite-size variance divided by \(n\) tends to \(e^{-4}+(1-e^{-2})^2/4\), strictly larger. Equivalently, the squared centered fluctuations are not uniformly integrable.

If \(k_n\to\infty\) while \(k_n=o(n)\), then
\[
\frac{\operatorname{Var}(X_{n,k_n})}{nk_n}\longrightarrow\rho^2,
\qquad \frac{X_{n,k_n}-\mathbb E X_{n,k_n}}{\sqrt{\operatorname{Var}(X_{n,k_n})}}\xrightarrow{\mathbb P}0.
\]
The last convergence does not contradict unit finite-sample variance: rare clique-first outcomes carry the missing second moment. Finally, if \(k_n/n\to c\in(0,\infty)\), then \(X_{n,k_n}/n\) converges in law to \(0\) with probability \(c/(1+c)\) and \(\rho\) with probability \(1/(1+c)\); if \(k_n/n\to\infty\), then \(X_{n,k_n}/n\to0\) in probability.

## Assumptions and scope
The graph is finite, simple, and unweighted. The vertex order is one uniformly random permutation, equivalent to independent continuous arrival labels. Every vertex is tested once; a rejected vertex is never reconsidered. The clique vertices form a complete graph, not an independent set. All asymptotic limits take \(n\to\infty\); \(k\) is either fixed or follows the stated integer sequence. The Gaussian statements concern weak convergence, which alone does not imply convergence of second moments.

## Proof
**1. Reduction to an exact mixture.** The earliest vertex in the random order lies in the clique with probability \(p=k/(n+k)\). If so it is accepted, and, being adjacent to every other vertex, precludes all further acceptances: \(X_{n,k}=1\). If the earliest vertex lies on the cycle, it is accepted and blocks every clique vertex, so the remainder of the algorithm is exactly random-order greedy adsorption on \(C_n\). The relative order of the cycle vertices is uniform and independent of whether the first overall vertex lies in the clique. The first cycle vertex is uniform and excludes its two cycle neighbors; the \(n-3\) unblocked cycle vertices form a path, and their relative order is uniform. The cycle output is consequently distributed as \(1+R_{n-3}\). This proves the displayed probability-generating function. A greedy independent set of \(C_n\) has at least two vertices for \(n\ge4\), so \(X=1\) occurs precisely on the clique-first event.

**2. Path law and its moment constants.** Conditioning on the first selected vertex of \(P_m\) gives, for every \(m\ge1\),
\[
 m f_m(z)=z\sum_{j=1}^{m} f_{j-2}(z)f_{m-j-1}(z),\qquad f_{-1}(z)=f_0(z)=1.
\]
The ordinary generating function \(F(t,z)=\sum_{m\ge0}f_m(z)t^m\) satisfies \(F(0,z)=1\) and
\[
 \partial_t F=z(1+tF)^2.
\]
Differentiation with respect to \(z\) at \(z=1\) (where \(F(t,1)=(1-t)^{-1}\)) yields the following **exact** generating functions for the first and second factorial moments:
\[
 A(t):=\left.\partial_z F\right|_{z=1}=\frac{1-e^{-2t}}{2(1-t)^2},
\]
\[
 B(t):=\left.\partial_z^2 F\right|_{z=1}=\frac{3t-1-4t^2e^{-2t}+(1+t)e^{-4t}}{4(1-t)^3}.
\]
These identities follow from \(A'=1/(1-t)^2+2tA/(1-t)\) and \(B'=4tA/(1-t)+2t^2A^2+2tB/(1-t)\), each with zero initial condition. Put \(a=e^{-2}\). Expanding near \(t=1\),
\[
 A(t)=\frac{\rho}{(1-t)^2}-\frac a{1-t}+O(1),
\]
\[
 B(t)=\frac{2\rho^2}{(1-t)^3}+\frac{-3+7a^2}{4(1-t)^2}+O((1-t)^{-1}).
\]
The remainders involve entire exponential functions after subtraction of these poles, so coefficient extraction gives
\[
 \mathbb E R_m=\rho(m+1)-a+o(1),\qquad \operatorname{Var}(R_m)=a^2m+O(1).
\]
In fact the constant term in the variance expansion is \(3a^2\), but it is not needed. As the random greedy cycle count equals \(1+R_{n-3}\), its mean \(\mu_n\) and variance \(v_n\) satisfy
\[
 \mu_n=\rho n+o(1),\qquad v_n=\sigma^2n+O(1).
\]
The path and cycle moment constants in this step are established in the one-dimensional adsorption literature and are not claimed as novel.

**3. Gaussian fluctuations of the path.** For completeness, set \(z=e^s\) and \(\Lambda=e^{s/2}\). The Riccati equation above has the explicit analytic solution
\[
 F(t,e^s)=\frac{1+\Lambda\tanh(\Lambda t)}{1-t+(\Lambda^{-1}-\Lambda t)\tanh(\Lambda t)}.
\]
For \(s=0\) it reduces to \((1-t)^{-1}\). In a fixed disk \(|t|<1+\epsilon\) with \(0<\epsilon<\pi/2-1\), its denominator has, at \(s=0\), just the simple zero \(t=1\), and the numerator is nonzero there. For complex \(s\) sufficiently close to zero, analytic perturbation and compactness therefore give one simple pole \(t=y(s)\) near 1 and no other pole in this disk. Its residue is analytic and nonzero. Uniform coefficient extraction on a contour outside that pole gives
\[
 \log \mathbb E e^{sR_m}=mU(s)+V(s)+O(\eta^m),\qquad U(s)=-\log y(s),
\]
for some \(\eta<1\) and analytic \(V\), uniformly for small complex \(s\). The moment calculations above identify \(U'(0)=\rho\) and \(U''(0)=\sigma^2>0\). Substituting \(s=iu/\sqrt m\), subtracting the mean, and expanding \(U\) through second order shows convergence of characteristic functions to \(\exp(-\sigma^2u^2/2)\). Hence
\[
 (R_m-\rho m)/\sqrt m\xrightarrow{d}N(0,\sigma^2).
\]
The shift by a constant and replacement of \(m\) by \(n-3\) prove the same limit for the cycle count centered at \(\rho n\).

**4. Variance and scaling regimes.** Let \(J\) be the indicator of a clique-first outcome. The reduction in step 1 gives an exact mixture with \(\Pr(J=1)=p=k/(n+k)\) and a cycle count \(Y_n\) independent of \(J\). In particular,
\[
 \mathbb E X_{n,k}=p+(1-p)\mu_n,
\qquad \operatorname{Var}(X_{n,k})=(1-p)v_n+p(1-p)(\mu_n-1)^2.
\]
For fixed \(k\), use \(p\sim k/n\), \(\mu_n\sim\rho n\), and \(v_n\sim\sigma^2n\), giving the mean shift and variance inflation. If \(k_n=o(n)\), then \(p_n\to0\), so the total-variation distance between the law of \(X_{n,k_n}\) and the law of \(Y_n\) is at most \(p_n\); the cycle Gaussian limit carries over even when \(k_n\to\infty\). If in addition \(k_n\to\infty\), the variance formula gives \(\operatorname{Var}(X_{n,k_n})\sim\rho^2nk_n\). On \(J=0\), the centered count is \(Y_n-\mu_n+p_n(\mu_n-1)\), which divided by \(\sqrt{nk_n}\) tends to zero in probability since its first term is \(O_{\mathbb P}(\sqrt n)\) and its second is \(O(k_n)\) with \(k_n=o(n)\). The exceptional event \(J=1\) itself has vanishing probability, proving convergence in probability of the standard-deviation-normalized count to zero. Finally, for \(k_n/n\to c>0\), \(p_n\to c/(1+c)\) and \(Y_n/n\to\rho\) in probability; mixing these two alternatives gives the stated atomic distribution, with the \(c=\infty\) case obtained by \(p_n\to1\).

## Verification
A standalone Python 3 checker, `verify.py`, independently enumerates full random vertex permutations on small clique-joined cycles and compares their exact rational output distributions with the mixture law. It separately generates the full path distribution through first-accepted-vertex recursion and checks rational first and second factorial moments against the displayed exponential generating-function coefficients. It verifies the large-index moment constants numerically; the infinite-dimensional normal limits and all-parameter laws are proved analytically above, not inferred from finite testing. Run `python verify.py` from the extracted package directory.

## Relationship to prior work
The one-dimensional first-arrival recurrence, the Riccati solution, density \(\rho\), and variance coefficient \(\sigma^2\) are already in Krapivsky (2020), Sections II–III and Appendix A; this finding does not claim priority for any of them. Krivelevich, Mészáros, Michaeli and Shikhelman (first public journal version December 2023) establish general greedy-MIS density and concentration results under local-limit and path-growth hypotheses, but do not state the exact clique-joined-cycle mixture or its second-moment anomaly. The new object is a cycle with a **nonzero clique of universally adjacent vertices**; in particular, it is not a one-dimensional path/ring and does not have uniformly bounded degree. An independently published exact wheel or join fluctuation statement might still exist and would supersede the corresponding claim; the literature comparison cannot establish exhaustive priority.

## Limitations
The result is specific to uniformly random vertex ordering, complete clique-to-cycle adjacency, and nearest-neighbor blocking on the cycle. It does not apply directly to random-edge greedy matching, repeated-attempt adsorption at nonuniform rates, or arbitrary high-degree hub structures. The Gaussian law is a weak limit, not a moment convergence theorem; this distinction is the principal mechanism. The proof uses the well-established one-dimensional Riccati solution rather than claiming a new expression for base-path statistics. No independent mathematical audit has been performed.

## References
1. P. L. Krapivsky, *Large Deviations in One-Dimensional Random Sequential Adsorption*, arXiv:2009.08609 (first public 2020-09-18), Phys. Rev. E 102, 062108 (2020). https://arxiv.org/abs/2009.08609
2. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015 (first published 2023-12-18). https://doi.org/10.1002/rsa.21200
3. G. Brightwell, S. Janson and M. Luczak, *The greedy independent set in a random graph with given degrees*, arXiv:1510.05560 (first public 2015-10-19), Random Structures & Algorithms 51 (2017), 565–586. https://arxiv.org/abs/1510.05560
