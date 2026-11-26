# A logarithmic mean and a finite Poisson-corner limit for distance-three pairs in random interval graphs

## Finding

For every integer \(n\ge2\), independently sample \(n\) closed intervals \(I_i=[L_i,R_i]\) by sorting two independent uniform points in \([0,1]\), and join two vertices exactly when their intervals intersect. Let \(T_n\) be the number of unordered pairs of **disjoint** sampled intervals for which **no third sampled interval meets both**. Such a pair has graph distance at least three (or is disconnected). Then

\[
\mathbb E T_n=4n(n-1)\int_{\substack{r,s>0\\r+s<1}}rs(1-2rs)^{n-2}\,dr\,ds
=4n(n-1)\sum_{j=0}^{n-2}\binom{n-2}{j}(-2)^j\frac{((j+1)!)^2}{(2j+4)!}.
\]

Writing \(\gamma\) for Euler's constant, the exact leading and constant terms are

\[
\mathbb E T_n=\log n+\gamma+\log 2-1+o(1).
\]

Nevertheless \(T_n\) converges weakly to a finite almost surely, integer-valued random variable \(T_\infty\) with **infinite expectation**. Its law is given explicitly by three independent Poisson point processes: \(\mathcal L\) and \(\mathcal R\) on \((0,\infty)\), each with intensity \(2t\,dt\), and \(\mathcal B\) on \((0,\infty)^2\) with intensity \(2\,dx\,dy\). Put

\[
T_\infty=\sum_{r\in\mathcal L}\sum_{s\in\mathcal R}
 \mathbf 1\{\mathcal B((0,r]\times(0,s])=0\}.
\]

Then

\[
T_n\Rightarrow T_\infty<\infty\ \text{almost surely},\qquad
\mathbb E T_\infty=\infty,\qquad
\frac{T_n}{\log n}\xrightarrow{\mathbb P}0.
\]

For orientation, \(\Pr(T_\infty=0)=2/3\), agreeing with the *previously known* exact probability that there exists a sampled interval that meets every other one. With probability tending to one, the entire random intersection graph has diameter at most three, so on that event \(T_n\) counts exactly the pairs at graph distance three. Thus the genuine distance-three count has the same weak limit, but the displayed finite-mean formula and additive constant are for \(T_n\), not for the genuine distance-three count. All conclusions remain valid for any **common atomless endpoint law**, by a common probability-integral transform.

## Assumptions and scope

The intervals have independent endpoint pairs, and the two coordinates within each pair are independent and identically distributed from one common atomless distribution; the graph is their undirected intersection graph. The actual derivation uses uniform coordinates, which lose no order information. An empty family of connecting third intervals is a genuine condition: pairs with no length-two graph path are counted even if graph components differ. The diameter assertion removes this possible ambiguity asymptotically, not for every finite sample. The weak limit is for the unscaled integer count, not for its expectation.

## Proof

**1. The exact finite mean.** For two specified intervals with the first lying entirely to the left of the second, let \(r\) be the first interval's right endpoint and let \(s\) be the distance of the second interval's left endpoint from one. Their separate densities are \(2r\) and \(2s\), and disjointness is \(r+s<1\). A third interval intersects both precisely when its smaller endpoint is at most \(r\) and its larger endpoint is at least \(1-s\). Since the raw endpoints are independent uniform points and the two extremal segments are disjoint, that probability is exactly \(2rs\). The \(n-2\) remaining intervals independently avoid this event, yielding the first integral after multiplying by the two orientations and \(\binom n2\) unordered choices. Binomial expansion and the triangular beta integral

\[
\int_{r+s<1}r^{j+1}s^{j+1}\,dr\,ds=\frac{((j+1)!)^2}{(2j+4)!}
\]

give the displayed finite sum.

**2. The sharp mean asymptotic.** Integrate in \(s\) first and define \(u(r)=2r(1-r)\). Direct beta integration yields the exact one-dimensional representation

\[
\mathbb E T_n=\int_0^1\frac{1-(1-u(r))^{n-1}[1+(n-1)u(r)]}{r}\,dr.
\]

We claim the difference between this integral and

\[
J_n=\int_0^1\frac{1-(1+2nr)e^{-2nr}}r\,dr
\]

tends to zero. On \(r\ge1/2\), both numerators tend to one at every fixed \(r<1\) and are bounded by one, so dominated convergence applies to their difference. On \(0<r\le1/2\), set \(x=nr\). For every bounded \(x\), the actual numerator tends to \(1-(1+2x)e^{-2x}\), uniformly on compact sets. Both it and its comparison are \(O(x^2)\) for \(0<x\le1\). For \(x\ge1\), the actual missing mass is bounded by \((1+2x)e^{-x/2}\) for all sufficiently large \(n\), since \(nr\le nu(r)\le2nr\); the comparator has a smaller exponential tail. Thus the differences divided by \(x\) are uniformly integrable and the claim follows. A standard exponential-integral identity, or elementary differentiation and the defining integral of \(\gamma\), now gives

\[
J_n=\log(2n)+\gamma-1+E_1(2n)+e^{-2n}
=\log n+\gamma+\log2-1+o(1),
\]

where \(E_1(z)=\int_z^\infty e^{-t}/t\,dt\). In particular the expectation grows logarithmically, even though the counts are tight as proved below.

**3. Three independent extreme-corner processes.** Under uniform coordinates, the joint density of a sampled ordered endpoint pair \((L,R)\) on \(0<L<R<1\) is two. In the scale \(\sqrt n\), form the process of all \(\sqrt n R_i\) for intervals near the left corner, the process of all \(\sqrt n(1-L_i)\) near the right corner, and the process of all pairs \((\sqrt n L_i,\sqrt n(1-R_i))\) near the spanning corner. On every fixed compact range, the three corresponding regions of the original endpoint triangle are disjoint once \(n\) is large. Their probabilities, multiplied by \(n\), converge to \(2r\,dr\), \(2s\,ds\), and \(2\,dx\,dy\), respectively. The elementary multinomial-to-independent-Poisson limit (or its Laplace functional) therefore gives joint vague convergence to \((\mathcal L,\mathcal R,\mathcal B)\).

A left-corner interval having \(r=\sqrt n R_i\) and a right-corner interval having \(s=\sqrt n(1-L_j)\) are disjoint for all sufficiently large \(n\) when \(r,s\) lie in a fixed compact set. A third interval bridges their gap exactly when its spanning-corner coordinates \((x,y)\) satisfy \(x\le r\), \(y\le s\). Hence the count restricted to \(\alpha\le r,s\le K\) converges in law to the corresponding finite sum over the limiting Poisson clouds. The boundary equalities have probability zero.

**4. Removing the truncation.** For every \(\alpha>0\), the probability that *any* left-corner or right-corner point has scaled coordinate smaller than \(\alpha\) is at most \(2\alpha^2\), by the expected counts. After excluding this event, the expected number of unbridged pairs with \(r,s\ge\alpha\) and \(\max(r,s)>K\) is, for \(n\ge4\), at most

\[
4\iint_{\substack{r,s\ge\alpha\\\max(r,s)>K}}rs e^{-rs}\,dr\,ds.
\]

Indeed the finite-sample joint pair density yields the same integral with \((1-2rs/n)^{n-2}\) and domain \(r+s<\sqrt n\), and \((1-2rs/n)^{n-2}\le e^{-rs}\). For fixed \(\alpha>0\), the integrand is integrable on \([\alpha,\infty)^2\), and its tail vanishes as \(K\to\infty\). The analogous Poisson expectation is bounded by \(4\iint rs e^{-2rs}\,dr\,ds\) over the same truncated domain and vanishes as well. Taking \(\alpha\downarrow0\) after \(K\to\infty\), the converging-together lemma proves \(T_n\Rightarrow T_\infty\), and these bounds also imply \(T_\infty<\infty\) almost surely.

**5. Infinite limiting mean and zero probability.** Campbell's identity and independent rectangle-void probabilities give

\[
\mathbb E T_\infty=4\int_0^\infty\int_0^\infty rs e^{-2rs}\,ds\,dr=\infty,
\]

because integrating in \(s\) leaves a positive multiple of \(\int_0^\infty dr/r\). For the zero event, let \(R_*\) and \(S_*\) be the smallest points of \(\mathcal L\) and \(\mathcal R\). Both have survival function \(e^{-t^2}\). There exists a pair \((r,s)\) with an empty spanning rectangle if and only if the minimal rectangle \((0,R_*]\times(0,S_*]\) is empty: every pair's rectangle contains that minimum rectangle, and the minimum pair itself is present. Thus

\[
\Pr(T_\infty>0)=\mathbb E[e^{-2R_*S_*}]
=4\int_0^\infty\int_0^\infty rs e^{-(r+s)^2}\,dr\,ds=\frac13.
\]

Therefore \(\Pr(T_\infty=0)=2/3\). Weak convergence to a finite random variable also proves \(T_n/\log n\to0\) in probability, despite the divergent mean.

**6. Recovering genuine graph distances.** Let \(\delta_n=n^{-3/4}\). A union bound shows that the probability of some sampled interval having \(R_i\le\delta_n\) or \(L_i\ge1-\delta_n\) is at most \(2n\delta_n^2=o(1)\). The chance that no interval spans from a left endpoint below \(\delta_n\) to a right endpoint above \(1/2\) is \((1-\delta_n)^n=o(1)\); symmetrically there is a right-anchored interval spanning \(1/2\). On the intersection of these high-probability events, every interval wholly to the left of \(1/2\) meets the left-anchored interval, every interval wholly to the right meets the right-anchored interval, and every interval containing \(1/2\) meets both. The two anchored intervals meet each other (or are the same interval). Every pair of vertices is consequently connected by a path of length at most three, and precisely the unbridged disjoint pairs are at distance three. This establishes the graph interpretation without assuming finite-sample connectivity.

The high-probability equality does not transfer the additive mean constant. Write \(D_{3,n}\) for the number of pairs at graph distance exactly three and \(N_n\) for the number of isolated intervals with \(R_i<1/n\). Each such interval gives \(n-1\) pairs in \(T_n\) but not in \(D_{3,n}\); an unordered pair can be counted at most twice. Thus \(T_n-D_{3,n}\ge(n-1)N_n/2\). Conditional on such a short right endpoint, another interval can intersect it only if its left endpoint is below \(1/n\), an event of probability at most \(2/n\). Independence of the other intervals gives \(\mathbb E N_n\ge n^{-1}(1-2/n)^{n-1}\) for \(n\ge3\). Consequently \(\liminf_{n\to\infty}\mathbb E(T_n-D_{3,n})\ge e^{-2}/2>0\).

## Verification

Run `python3 CHECK.py` from the same directory. This enumerates all \((2n-1)!!\) order-matching configurations of the \(2n\) endpoints for every \(n\in\{2,3,4,5,6\}\), calculates the distance-three obstruction count directly, and independently compares its exact rational mean with the derived finite sum. It also checks in every configuration that no obstructed pair is equivalent to existence of a universal interval and verifies the exact already-known two-thirds probability. All 11,478 exact assertions passed. A separate numerical quadrature check at \(n=10,100,1000,10000,100000\) converged to the stated asymptotic constant; these finite computations do not prove the weak limit or infinite-mean assertion, which rest on Steps 2–5.

## Relationship to prior work

The classic interval graph model and the exact two-thirds probability of at least one universal interval are established background, not claimed discoveries. Diaconis–Holmes–Janson (2011) treat interval graph limits and clique-scale questions; Iliopoulos (2015) discusses maximal cliques and universal intervals and the random interval graph model. The related *A randomly clipped Poisson field of universal random intervals* derives the same compact-window corner processes before clipping at the two extremal endpoints. The clipped law resolves the existence and number of bridges for the single extremal pair. The all-pair obstruction count needs the corner processes without this clipping, and control of pairs outside compact windows. The related *Two-vertex domination and diameter laws for random interval graphs* gives a stronger quantitative diameter bound; the high-probability diameter conclusion is not new. The contribution is the exact obstruction-count mean with its constant and the finite-but-infinite-mean weak limit. The 1990 primary paper remains a historical-priority limitation where its full contents were not assessed.

## Limitations

No quantitative total-variation convergence rate or closed-form mass function for positive values of \(T_\infty\) is claimed. The probability-integral-transform extension requires a common atomless marginal for *all* endpoints; dependent endpoints or nonidentical endpoint laws are not covered. The graph-distance interpretation holds with probability tending to one, not for every sample. The weak limit does not permit passing expectations to the limit: the failure of uniform integrability is an essential part of the finding. Originality has only a best-knowledge primary-literature comparison, without an independent exhaustive priority audit.

## References

- P. Diaconis, S. Holmes and S. Janson, *Interval Graph Limits* (arXiv first posted 2011-02-14), https://arxiv.org/abs/1102.2841 .
- D. Iliopoulos, *Random Interval Graphs* (arXiv first posted 2015-07-22), https://arxiv.org/abs/1507.06275 .
- J. Justicz, E. R. Scheinerman and P. Winkler, *Random Intervals*, *American Mathematical Monthly* 97 (1990), DOI: https://doi.org/10.1080/00029890.1990.11995679 . The available abstract and secondary discussions, but not its complete text, were inspected.
- *A randomly clipped Poisson field of universal random intervals*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-randomly-clipped-poisson-field-of-universal-random-intervals--d692eb283908/RESULT.md .
- *Two-vertex domination and diameter laws for random interval graphs*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-two-vertex-domination-and-diameter-laws-for-random-interval-grap--0083d38128b4/RESULT.md .
