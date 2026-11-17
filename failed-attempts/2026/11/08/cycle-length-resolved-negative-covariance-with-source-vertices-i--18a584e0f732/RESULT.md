# Cycle-length-resolved negative covariance with source vertices in a uniform random mapping

## Finding
Let \(f:[n]\to[n]\) be selected uniformly from the \(n^n\) maps, \(n\ge2\). Write \(Z_n\) for the number of vertices with zero indegree in the functional digraph, and \(K_{n,j}\) for the number of directed cycles with exactly \(j\) vertices. Put
\[
b_{m,j}=\begin{cases}(m)_j/m^j,&1\le j\le m,\\0,&j>m,\end{cases}\qquad (m)_j=m(m-1)\cdots(m-j+1).
\]
Then for every integer \(1\le j\le n\),
\[
\operatorname{Cov}(Z_n,K_{n,j})=\frac{n}{j}\left(1-\frac1n\right)^n\bigl(b_{n-1,j}-b_{n,j}\bigr).
\]
This covariance is exactly zero for \(j=1\), and strictly negative for all \(2\le j\le n\). For each fixed \(x>0\) and every integer sequence \(j_n/\sqrt n\to x\), the entire mesoscopic profile satisfies
\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Cov}(Z_n,K_{n,j_n})
=-\frac{x}{2e}\exp(-x^2/2).
\]
In particular, for the number \(H_n=\sum_{j=1}^n K_{n,j}\) of functional-graph components and the number \(C_n=\sum_{j=1}^n jK_{n,j}\) of cyclic vertices,
\[
\lim_{n\to\infty}\operatorname{Cov}(Z_n,H_n)=-\frac1{2e},\qquad
\lim_{n\to\infty}\frac{\operatorname{Cov}(Z_n,C_n)}{\sqrt n}=-\frac{\sqrt{\pi/8}}e.
\]

A stronger finite identity explains the law. For \(0\le\ell\le n-1\) and any bounded real-valued \(\Phi\) depending only on the vector of cycle-length counts, with \((Z_n)_0=1\),
\[
\mathbb E\big[(Z_n)_\ell\Phi(\mathbf K_n)\big]
=(n)_\ell\left(\frac{n-\ell}{n}\right)^n
\mathbb E\big[\Phi(\mathbf K_{n-\ell})\big].
\]
On the right, the cycle vector for a map on \(n-\ell\) vertices is extended by zero in the longer cycle-length coordinates. This covers mixed factorial moments of source-vertex count against any cycle-length statistic, not just the reported covariance.

## Assumptions and scope
All random maps are equiprobable, and images of distinct inputs are independently uniform on \([n]\). Directed self-loops count as cycles of length one. A vertex is a *source vertex* when its indegree (number of preimages under \(f\)) is zero. Every weak component of a functional graph contains precisely one directed cycle, so \(H_n\) is the number of components. The formulas are exact for every \(n\ge2\); limits require \(n\to\infty\) as stated. The positivity parameter \(x\) in the mesoscopic statement is fixed and strictly positive.

## Proof
**1. Removing designated source vertices.** Fix an ordered \(\ell\)-tuple of distinct vertices \(U\), with \(0\le\ell\le n-1\). The event that every vertex in \(U\) has indegree zero says every one of the \(n\) independent map images avoids \(U\). It has probability \(((n-\ell)/n)^n\). Conditional on this event, images are independent uniform choices from \(B=[n]\setminus U\). Therefore the restriction \(f|_B:B\to B\) is a uniform map of size \(n-\ell\). Every directed cycle lies entirely within \(B\), since nothing maps into \(U\), and its cycle vector is exactly that of \(f|_B\). Summing over the \((n)_\ell\) ordered choices of \(U\) proves the factorial identity.

**2. Exact covariance.** For each unordered \(j\)-element subset of the \(m\) vertices, there are exactly \((j-1)!\) distinct directed \(j\)-cycles supported on it. Each cycle requires \(j\) prescribed map images and has probability \(m^{-j}\). Summing over the \(\binom mj\) subsets yields
\[\mathbb E K_{m,j}=\frac{(m)_j}{j m^j}=b_{m,j}/j.\]
The factorial identity with \(\ell=1\) and \(\Phi=K_{n,j}\) gives
\[
\mathbb E[Z_nK_{n,j}]=n\left(1-\frac1n\right)^n\frac{b_{n-1,j}}j,
\quad
\mathbb E Z_n=n\left(1-\frac1n\right)^n.
\]
Subtract their product with \(\mathbb E K_{n,j}=b_{n,j}/j\). The claimed covariance formula follows. For \(j=1\), \(b_{m,1}=1\) for every \(m\ge1\). For \(2\le j\le n-1\), the product \(b_{m,j}=\prod_{r=1}^{j-1}(1-r/m)\) strictly increases with \(m\ge j\); for \(j=n\), \(b_{n-1,n}=0<b_{n,n}\). Thus the sign statements are strict in their stated ranges.

**3. Mesoscopic limit.** Let \(j/\sqrt n\to x>0\). Directly from the logarithm of the product,
\[b_{n,j}=\exp\bigl(-j(j-1)/(2n)+O(j^3/n^2)\bigr)\to e^{-x^2/2}.\]
For \(j<n\),
\[
\frac{b_{n-1,j}}{b_{n,j}}=
\prod_{r=1}^{j-1}\left(1-\frac{r}{(n-1)(n-r)}\right).
\]
The sum of the small subtractions is \(j(j-1)/(2n(n-1))+o(1/n)\); their squared sum is \(o(1/n)\). It follows that
\[
n(b_{n,j}-b_{n-1,j})\to \frac{x^2}{2}e^{-x^2/2}.
\]
Combine with \((1-1/n)^n\to e^{-1}\) and \(j/\sqrt n\to x\) in the exact formula to obtain the claimed profile.

**4. Summation and domination.** For \(2\le j\le n\), the telescoping difference of the two finite products yields the bound
\[
0\le b_{n,j}-b_{n-1,j}
\le \frac{j(j-1)}{2n(n-1)}
\exp\left(-\frac{(j-1)(j-2)}{2n}\right).
\]
Indeed each factorwise difference equals \(r/[n(n-1)]\), and each resulting product of \(j-2\) remaining factors is at most the exponential of minus the sum of the smallest \(j-2\) indices divided by \(n\). This supplies a Gaussian-tail majorant on the scale \(j/\sqrt n\), sufficient for dominated Riemann-sum passage in both sums (the endpoint \(j=1\) contributes zero). Consequently
\[
\begin{aligned}
\lim_{n\to\infty}\sum_j\operatorname{Cov}(Z_n,K_{n,j})
&=-\frac1{2e}\int_0^\infty x e^{-x^2/2}\,dx=-\frac1{2e},\\
\lim_{n\to\infty}\frac1{\sqrt n}\sum_jj\operatorname{Cov}(Z_n,K_{n,j})
&=-\frac1{2e}\int_0^\infty x^2e^{-x^2/2}\,dx=-\frac{\sqrt{\pi/8}}e.
\end{aligned}
\]
The finite sums may be interchanged with covariance because they contain finitely many integrable random variables. This completes all claims.

## Verification
Run \(\texttt{python verify.py}\) using Python's standard library. It independently enumerates all \(873{,}611\) mappings across \(n=2,\ldots,7\), reconstructs directed cycles by visiting function iterates, and compares exact rational expectations, pairwise covariances, the second factorial-moment identity, signs, and aggregate covariances with the formulas. It also computes finite-size asymptotic diagnostics at increasing \(n\). The enumeration is a finite check; the proof above establishes the infinite-domain assertions. The file and its outputs are not third-party certificates.

## Relationship to prior work
Soria's November 10, 1996 seminar describes the symbolic decomposition of random mappings into rooted-tree cycles and gives separate generating functions for leaves, total cycles, and other image statistics; it does not in the inspected text state this exact length-indexed mixed covariance or its mesoscopic correction. Pitman's June 15, 1998 treatment gives a multinomial law for degrees of rooted labelled forests; it is related to the source-vertex mechanism, not a complete cycle-length mixed covariance result. Hansen and Jaworski (first publicly posted March 22, 2006) develop indegree-driven random mapping models and distributions of cyclic-point counts and component counts, but their inspected text does not provide this signed cycle-length covariance profile. General generating functions can in principle encode mixed moments; the claimed contribution is the evaluated finite-sample sign law, the factorial contraction for the joint cycle vector, and the explicit mesoscopic kernel with two summed limits.

## Limitations
No claim of independence between source vertices and fixed-point count follows from their zero covariance. The asymptotic profile addresses individual cycle lengths of order \(\sqrt n\), not a joint process convergence theorem. Earlier broad work by Flajolet–Odlyzko on mapping statistics and Drmota–Soria on image/preimage counts was identified, but the full texts could not be inspected. Historical implicit coverage through general multivariate generating functions is a remaining originality risk; this document does not certify priority or independent validation. Numerical calculations only check finite cases and convergence diagnostics.

## References
- M. Soria, *Distribution of Image Points in Random Mappings*, Algorithms Seminar, November 10, 1996, https://algo.inria.fr/seminars/sem96-97/soria.html (inspected online text, including generating-function table and leaves section).
- J. Pitman, *The multinomial distribution on rooted labeled forests*, University of California, Berkeley, Technical Report 499, June 15, 1998, https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/499.pdf (inspected introductory and forest-distribution material).
- J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529, first posted March 22, 2006, https://arxiv.org/abs/math/0603529 (inspected introduction and model/results sections).
- P. Flajolet and A. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989 proceedings (1990), https://doi.org/10.1007/3-540-46885-4_34 (bibliographic/abstract comparison only).
- M. Drmota and M. Soria, *Images and Preimages in Random Mappings*, SIAM Journal on Discrete Mathematics (1997), https://doi.org/10.1137/S0895480194268421 (bibliographic/abstract comparison only).
