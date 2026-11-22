# Universal \(8/\pi-1\) overdispersion of mesoscopic diagonals shared by two random triangulations

## Finding

Let \(T_n^{(1)}\) and \(T_n^{(2)}\) be independent, uniformly sampled triangulations of the same cyclically labeled convex \(n\)-gon. For a diagonal \(e\), let \(r_n(e)\) be the smaller of the two numbers of polygon vertices strictly between its endpoints along the two boundary arcs. For fixed \(0<a<b<\infty\), let
\[
 X_n(a,b)=\#\{e\in T_n^{(1)}\cap T_n^{(2)}: a\sqrt n\le r_n(e)\le b\sqrt n\}.
\]
As \(n\to\infty\),
\[
 \mathbb E X_n(a,b)\longrightarrow \Lambda_{a,b}
 =\frac1{2\pi}(a^{-2}-b^{-2}),\qquad
 \operatorname{Var}X_n(a,b)\longrightarrow
 \left(\frac8\pi-1\right)\Lambda_{a,b}.
\]
In particular, the limiting variance-to-mean ratio is the **same constant** \(8/\pi-1\approx1.5464790895\) for every fixed, nonempty mesoscopic length band. It is greater than one, despite each particular diagonal being very unlikely to occur in both triangulations.

More generally, define the locally finite random measure
\[
 \mu_n=\sum_{e\in T_n^{(1)}\cap T_n^{(2)}}\delta_{r_n(e)/\sqrt n}.
\]
For arbitrary real-valued continuous compactly supported functions \(f,g\) on \((0,\infty)\),
\[
 \lim_{n\to\infty}\mathbb E\mu_n(f)
 =\int_0^\infty\frac{f(x)}{\pi x^3}\,dx,
 \qquad
 \lim_{n\to\infty}\operatorname{Cov}(\mu_n(f),\mu_n(g))
 =\left(\frac8\pi-1\right)\int_0^\infty\frac{f(x)g(x)}{\pi x^3}\,dx.
\]
This is a first- and second-order limit, **not** a claim of convergence of the full random point measure or of its counts to a particular distribution.

## Assumptions and scope

All \(n\) vertices are fixed in strictly convex position and have a fixed cyclic order. Each of the \(C_{n-2}\) possible triangulations is chosen with equal probability, independently of the other choice. The Catalan numbers are \(C_j=(j+1)^{-1}\binom{2j}{j}\), including \(C_0=1\). A proper diagonal separates two polygonal cells and excludes polygon boundary edges. Its shorter-side index \(r_n(e)\) is between one and \(\lfloor(n-2)/2\rfloor\). For the stated asymptotics all indices lie in a fixed multiple of \(\sqrt n\), so the shorter side is unambiguous and has much fewer than half the vertices for all sufficiently large \(n\). The constants \(a,b\) do not vary with \(n\).

## Proof

**1. One- and two-diagonal probabilities.** Write \(M=n-2\) and fix a diagonal whose shorter boundary arc contains \(r\) intermediate vertices, with \(1\le r<(n-2)/2\). Cutting along that diagonal produces polygons with \(r+2\) and \(n-r\) vertices. Hence its probability of occurrence in a single uniform triangulation is
\[
 p_n(r)=\frac{C_rC_{n-r-2}}{C_{n-2}}.
\]
There are exactly \(n\) diagonals of this index, once \(2r+2<n\).

For two diagonals whose short boundary intervals are disjoint (they may meet at an endpoint), with indices \(r,s\) satisfying \(r+s+2<n\), the joint single-triangulation probability is
\[
 q_n(r,s)=\frac{C_rC_sC_{n-r-s-2}}{C_{n-2}}.
\]
If a short boundary interval of index \(s\) is properly nested inside an interval of index \(r>s\), then, setting \(d=r-s\), their joint probability is
\[
 h_n(r,s)=\frac{C_sC_dC_{n-r-2}}{C_{n-2}}.
\]
The nested short interval is obtained by shortening the two ends by nonnegative amounts totaling \(d\), giving \(d+1\) possibilities for a fixed outer interval. A pair of diagonals whose short intervals partially overlap without nesting has crossing interiors and cannot occur in a triangulation. These three classes exhaust distinct pairs on the stated length range. All corresponding probabilities are **squared** when the diagonals must occur in both independent triangulations.

**2. Exact finite factorial moment.** Take any nonempty integer interval \(I=[R,S]\cap\mathbb Z\) with \(1\le R\le S\) and \(2S+2<n\). Let \(X_{n,I}\) count diagonals of indices in \(I\) shared by both triangulations. The preceding counts give
\[
 \mathbb E X_{n,I}=n\sum_{r\in I}p_n(r)^2
\]
and, writing \((X)_2=X(X-1)\),
\[
 \begin{aligned}
 \mathbb E(X_{n,I})_2={}&n\sum_{r,s\in I}(n-r-s-1)q_n(r,s)^2\\
 &+2n\sum_{\substack{r,s\in I\\s<r}}(r-s+1)h_n(r,s)^2.
 \end{aligned}
\]
Indeed, for a fixed first short interval of index \(r\), exactly \(n-r-s-1\) cyclic placements of a second short interval of index \(s\) are disjoint; thus the ordered disjoint-pair count is \(n(n-r-s-1)\). Every nested unordered pair has a unique outer interval. The factor two in the second sum converts it to ordered pairs. This also proves the exact moment identities without a probabilistic approximation.

**3. Critical scaling and the nested contribution.** Uniformly for \(r,s\) in any fixed band of order \(\sqrt n\), Stirling's formula gives
\[
 C_r=\frac{4^r}{\sqrt\pi r^{3/2}}(1+O(r^{-1})),\qquad
 \frac{C_{n-r-2}}{C_{n-2}}=4^{-r}(1+O(r/n)).
\]
Consequently, when \(I\) comprises the integers between \(a\sqrt n\) and \(b\sqrt n\),
\[
 n\sum_{r\in I}p_n(r)^2\to\Lambda_{a,b},\qquad
 n\sum_{r,s\in I}(n-r-s-1)q_n(r,s)^2\to\Lambda_{a,b}^2.
\]
For the nested term put \(d=r-s\) and factor
\[
 h_n(r,r-d)=p_n(r)\frac{C_{r-d}C_d}{C_r}.
\]
For every fixed \(d\ge1\), uniformly over interior indices of the band, \(C_{r-d}/C_r\to4^{-d}\). Moreover, whenever both \(r\) and \(r-d\) lie in the band, the Catalan asymptotics imply the uniform bound
\[
 \frac{C_{r-d}}{C_r}\le K_{a,b}4^{-d}
\]
with a finite constant \(K_{a,b}\) independent of \(n,r,d\). Since \((d+1)C_d^2/16^d=O(d^{-2})\), dominated convergence in the difference \(d\), followed by the same Riemann sum, yields
\[
 2n\sum_{\substack{r,s\in I\\s<r}}(r-s+1)h_n(r,s)^2
 \longrightarrow 2\Lambda_{a,b}K,
 \qquad K=\sum_{d=1}^{\infty}(d+1)\frac{C_d^2}{16^d}.
\]
Terms with \(r\) within a fixed number of lattice sites of a band endpoint have vanishing total weight and do not alter this limit.

To evaluate the universal series, observe that \(C_d/4^d=(1/2)_d/(2)_d\), where \((u)_d\) denotes the rising factorial. The beta-integral identity obtained by expanding \((1-t)^{-1/2}\) term by term gives
\[
 \begin{aligned}
 1+K
 &=\sum_{d=0}^{\infty}\frac{(1/2)_d(1/2)_d}{d!(2)_d}\\
 &=\frac{2}{\pi}\int_0^1t^{-1/2}(1-t)^{1/2}(1-t)^{-1/2}\,dt
 =\frac4\pi.
 \end{aligned}
\]
Therefore \(K=4/\pi-1\). Since \(\operatorname{Var}X=\mathbb E(X)_2+\mathbb E X-(\mathbb E X)^2\), the announced variance limit equals
\[
 \Lambda_{a,b}\bigl(1+2K\bigr)=\left(\frac8\pi-1\right)\Lambda_{a,b}.
\]

**4. Weighted statement.** For compactly supported continuous \(f,g\), repeat the exact finite counts from step 2, multiplying a single diagonal of index \(r\) by \(f(r/\sqrt n)\), and an ordered pair by \(f(r/\sqrt n)g(s/\sqrt n)\). The single-diagonal term converges to \(\int f(x)g(x)/(\pi x^3)\,dx\); the disjoint-pair term converges to the product of the two first moments. In the nested term, differences \(d\) that remain fixed have \(r/\sqrt n-(r-d)/\sqrt n\to0\), so both weights converge to the same product \(f(x)g(x)\). The same summable domination yields an extra \(2K\int f(x)g(x)/(\pi x^3)\,dx\). Subtracting the product of means gives the claimed covariance. No convergence of a full point-process law is used.

## Verification

Run `python check.py` with Python 3 and its standard library. The program independently generates every triangulation of polygons with five to nine vertices, examines every ordered pair, and compares both exact rational moments with the disjoint/nested Catalan sums for all admissible consecutive integer bands. It reported **106 exact assertions passed**. It additionally checks a rigorous-tail-compatible finite approximation of the beta-integral series and prints numerical moments for growing polygon sizes. The numerical outputs for the band \([0.7,1.6]\) give variance-to-mean ratios \(1.50236531\) at \(n=2000\), \(1.52508993\) at \(n=10000\), and \(1.53496277\) at \(n=40000\), compared with the proved limit \(1.5464790895\). Exhaustive enumeration and floating-point diagnostics do not replace the analytic \(n\to\infty\) proof.

## Relationship to prior work

Classical Catalan triangulation enumeration and polygon-cutting identities are used as established inputs. Noy's 1999 survey treats the maximum length of a diagonal in one random triangulation, whereas the present statistic compares **matching diagonals in two independent triangulations** and examines the mesoscopic square-root length scale. Ralaivaosaona, Ravelomanana and Wagner (2018) develop a bivariate generating function for the **total**, unweighted number of common diagonals and for common-diagonal-free pairs; this does not report the length-resolved mesoscopic covariance or the factor \(8/\pi-1\). A published 2026 result on conditional correlation signs of two diagonals in **one** random triangulation establishes Catalan association for compatible diagonals, but not the variance law for length-restricted coincidences of two independent triangulations. These related results are credited rather than claimed as new.

## Limitations

The theorem concerns two independent **uniform** triangulations of a fixed convex polygon and indices on compact positive intervals after division by \(\sqrt n\). It does not address weighted triangulations, curved/random polygons, the largest common diagonal, a full limiting point-process distribution, or the number of all common diagonals. The analysis proves means and covariances, not a Poisson or compound-Poisson limit. Non-indexed or unexamined literature might contain an equivalent result; historical priority has not been independently validated.

## References

1. M. Noy, *Enumeration of Geometric Configurations on a Convex Polygon*, INRIA Algorithms Seminar, December 16, 1999, https://algo.inria.fr/seminars/sem99-00/noy1.html.
2. D. Ralaivaosaona, J. B. Ravelomanana, and S. Wagner, *Counting Planar Tanglegrams*, AofA 2018, DOI:10.4230/LIPIcs.AofA.2018.32, https://drops.dagstuhl.de/storage/00lipics/lipics-vol110-aofa2018/LIPIcs.AofA.2018.32/LIPIcs.AofA.2018.32.pdf.
3. *Conditional correlation signs and compatible-family association in uniform polygon triangulations*, published research record, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-conditional-correlation-signs-and-compatible-family-association--430feb7408bd/RESULT.md.
