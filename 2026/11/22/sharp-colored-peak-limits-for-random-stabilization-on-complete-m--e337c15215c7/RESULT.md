# Sharp colored-peak limits for random stabilization on complete multipartite graphs

## Finding

Let \(G=K_{a_1,\ldots,a_r}\) be a complete multipartite graph with \(r\ge3\), positive integer parts \(a_i\), total order \(N=\sum_i a_i\), and let \(k\ge2\) be fixed. Independently assign each vertex one of \(k\) equally likely initial colors; provide a recoloring palette of size at least \(\max\{k,\Delta(G)+1\}\). Under uniform random sequential activation of currently conflicting vertices and recoloring into an unused neighbor color, let \(T\) be the number of recolorings and let \(S_c\) count vertices of initial color \(c\) which never recolor. Thus \(S=\sum_{c=1}^k S_c=N-T\).

**Exact finite joint tails.** For any \(j_1,\ldots,j_k\in\mathbb Z_{\ge0}\), let \(J=\sum_c j_c\), \(C_c\) be the number of vertices initially of color \(c\), \(I=\{c:j_c>0\}\), and for \(\boldsymbol i=(i_c:c\in I)\in[r]^I\) set \(t_h(\boldsymbol i)=\sum_{c\in I:i_c=h}j_c\). Write \((a)_{\underline j}=a(a-1)\cdots(a-j+1)\), with \((a)_{\underline 0}=1\) and zero for \(j>a\). Then for \(J\le N\),

\[
\Pr(S_c\ge j_c\ \forall c)=
\Pr(C_c\ge j_c\ \forall c)\,
\frac{\displaystyle\sum_{\boldsymbol i\in[r]^I}\prod_{h=1}^r (a_h)_{\underline{t_h(\boldsymbol i)}}}{(N)_{\underline J}},
\]

where \((C_1,\ldots,C_k)\) is multinomial with parameters \(N\) and probabilities \(1/k\). The probability is zero for \(J>N\); when all \(j_c=0\) it is one. These joint tails determine the entire finite multivariate polynomial \(\mathbb E\prod_c z_c^{S_c}\) by finite differences, so in particular determine the complete distribution of \(T\).

**Quantitative asymptotic law.** Put \(p_i=a_i/N\). If \(p_i\le1-\varepsilon\) for every \(i\), with \(\varepsilon>0\), let \(G_1,\ldots,G_k\) be independent positive integer variables with

\[
\Pr(G_c=j)=\sum_{i=1}^r p_i(1-p_i)p_i^{j-1}\quad(j\ge1).
\]

Then, for all \(N\ge1\),

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(S_1,\ldots,S_k),\mathcal L(G_1,\ldots,G_k)\bigr)
 \le \min\left\{1,\frac{2k^3(1+\varepsilon^{-2})}{N}\right\}.
\]

In particular, for fixed \(r\) and \(k\), if \(a_i/N\to p_i\in(0,1)\) as \(N\to\infty\), the number \(N-T\) of unchanged vertices converges to a sum of \(k\) independent part-size mixtures of geometric variables. For balanced parts \(a_i=N/r\), the limiting probability generating function is

\[
\lim_{N\to\infty}\mathbb E[z^{N-T}]=\left(\frac{(r-1)z}{r-z}\right)^k,
\]

so for \(j\ge k\) the limiting probability is \(\binom{j-1}{k-1}((r-1)/r)^k r^{-(j-k)}\). The order \(N^{-1}\) is already sharp *within the multicolor domain*: for any named color \(c\), the event \(S_c\le1\) exceeds its geometric-mixture probability by at least \((1-\sum_i p_i^2)/(N-1)\). In particular balanced tripartite graphs have a total-variation distance of at least \(2/(3(N-1))\) for every \(k\ge2\).

## Assumptions and scope

The graph is finite, simple, and complete multipartite, with all \(r\ge3\) parts nonempty. Initial vertex colors are independent uniform labels in a fixed \(k\)-color set, and are not required to be a proper coloring. The available recoloring palette has at least \(\max\{k,\Delta(G)+1\}\) colors, possibly more than \(k\); only the initial color equalities matter for \(T\). At each step, one enabled vertex is chosen uniformly. Any choice of a color absent from its neighborhood is allowed. The color-specific counts \(S_c\) refer to the *initial* colors of unchanged vertices. The quantitative bound compares to the geometric-mixture law using the actual finite proportions \(a_i/N\), and does not require these proportions to converge. The rate lower bound applies to the stated multicolor regime; the older monochrome case is acknowledged separately rather than claimed new.

## Proof

1. **Reduction to independent random priorities.** The reduction lemma of de Panafieu–Mathieu–Gradinariu Potop-Butucaru–Tixeuil (arXiv:2611.17989v1, Lemma 1) identifies the unchanged vertices with those whose random priority is larger than the priorities of all adjacent vertices of their initial color. Every process recolors at most once. For a complete multipartite graph, the induced subgraph on any fixed initial color is itself complete multipartite, possibly with empty parts. Among its vertices ordered by decreasing priority, the unchanged vertices are *exactly* the initial consecutive run from the same part as the top vertex. Indeed every vertex of that run outranks all vertices in other parts; after the first different-part vertex, every remaining vertex has an earlier neighbor with higher priority. If the color class is empty, the run has length zero.

2. **Exact joint tails.** Conditional on all initial-color class populations being at least the specified thresholds, the ordered lists of the first \(j_c\) priorities in distinct named color classes jointly form a uniformly random injection of \(J\) ordered positions into the \(N\) labelled vertices. This follows from exchangeability of the independent initial-color assignments and random priorities, even after the class populations have been fixed. To have \(S_c\ge j_c\), all \(j_c\) sampled vertices for color \(c\) must belong to one common graph part \(i_c\). If a graph part \(h\) receives a total of \(t_h\) such positions, there are \((a_h)_{\underline {t_h}}\) ways to fill them in order with distinct vertices. Summing over part choices and dividing by \((N)_{\underline J}\) gives the displayed exact formula. For any nonnegative integer variable \(X\), the identity \(z^X=1+(z-1)\sum_{j\ge1}z^{j-1}{\bf1}_{X\ge j}\) shows that all joint tails determine the multivariate generating polynomial.

3. **Coupling and total-variation bound.** Represent a random priority order by a uniform permutation \(P_1,\ldots,P_N\) of the \(N\) vertex identities with independent uniform color marks \(D_t\in[k]\). On the same space generate independent uniform vertex identities \(U_1,U_2,\ldots\) *with replacement*, sharing the marks \(D_t\). Couple \(P_t=U_t\) whenever \(U_t\) has not been used as a value among \(P_1,\ldots,P_{t-1}\); otherwise choose \(P_t\) uniformly from the remaining unused vertices. At each step \(P_t\), conditional on the preceding permutation prefix, is uniform over unused vertices, so \(P\) is genuinely uniform.

In the with-replacement sequence, for each initial color \(c\), read only positions marked \(c\) and let \(G_c\) be the length of the first same-part run. The disjoint color subsequences are independent infinite i.i.d. samples of graph parts with probabilities \(p_i\). Their run lengths are therefore independent and satisfy \(\Pr(G_c=j)=\sum_i p_i(1-p_i)p_i^{j-1}\).

Let \(H_c\) be the index in the full infinite marked sequence of the first point at which color \(c\) has appeared in at least two *different* graph parts, and let \(H=\max_c H_c\). This is a stopping time. If no vertex identity is repeated before or at time \(H\), the without-replacement and with-replacement streams agree far enough to determine every run length, so \((S_c)_c=(G_c)_c\). If \(H>N\), such a repetition necessarily occurs. Conditional on the preceding stream, the probability that \(U_t\) repeats an earlier identity is at most \((t-1)/N\); the event \(\{H\ge t\}\) depends only on preceding positions. Therefore

\[
 \Pr\bigl(\exists t\le H:\ U_t\in\{U_1,\ldots,U_{t-1}\}\bigr)
 \le\frac{\mathbb E[H(H-1)]}{2N}.
\]

The first occurrence of mark \(c\) has a geometric waiting time with success probability \(1/k\). Conditional on its graph part, the following wait until another occurrence of mark \(c\) in a *different* part is geometric with success probability at least \(\varepsilon/k\). Since \(\mathbb E[\operatorname{Geom}(u)^2]\le2/u^2\) for the geometric law supported on positive integers, \(\mathbb E H_c^2\le4k^2(1+\varepsilon^{-2})\). As \(H^2\le\sum_c H_c^2\), the collision probability is bounded by \(2k^3(1+\varepsilon^{-2})/N\). The coupling inequality proves the claimed total-variation estimate.

4. **Limits and rate boundary.** If \(p_i\to p_i^*\in(0,1)\), then the geometric mixtures converge in distribution; the total-variation bound transfers this to \((S_c)_c\). Equal proportions \(1/r\) give the usual geometric pgf \((r-1)z/(r-z)\), whose \(k\)-fold convolution is the stated negative-binomial law. For any named color \(c\), the finite tail formula with \(j_c=2\) and all other thresholds zero gives \(\Pr(S_c\ge2)=\Pr(C_c\ge2)\sum_i a_i(a_i-1)/(N(N-1))\). Since \(\Pr(C_c\ge2)\le1\), while \(\Pr(G_c\ge2)=\sum_i p_i^2\), subtracting shows \(\Pr(S_c\le1)-\Pr(G_c\le1)\ge(1-\sum_i p_i^2)/(N-1)\). This lower bounds the joint total-variation distance, and for balanced tripartite parts the numerator equals \(2/3\), proving sharp inverse-size order in the new \(k\ge2\) domain.

## Verification

The standalone `verify.py` checks the joint-tail formula against direct enumeration of all initial named-color assignments and all priority permutations for nine independent part-size/color-count cases, including two and three initial colors. It checks 189 distinct joint-tail thresholds and verifies exact small-case rate identities. The separate `verify_dynamics.py` checks four small configurations of the actual sequential activation process against the random-priority reduction. Invoke `python verify.py` and `python verify_dynamics.py` under Python 3 with no dependencies beyond its standard library; expected final output includes `VERIFY_OK`. Exhaustive experiments confirm only the finite tested cases; the unrestricted assertions follow from the four proof steps above.

## Relationship to prior work

The initiating work, de Panafieu et al., *The Exact Stabilization Time of Self-Stabilizing Coloring* (arXiv:2611.17989v1, first public 2026-11-13), proves the random-ordering reduction, analyzes arbitrary-graph moments, and studies paths, cycles, random trees, Erdős–Rényi graphs, and bipartite Erdős–Rényi graphs. Its Proposition 9 includes a bipartite random-graph limit law and its sum over initial colors; in particular the bipartite complete-graph boundary is within that earlier coverage. The new claim concerns arbitrary \(r\ge3\) deterministic complete multipartite graphs, all their finite joint color-resolved tails, and a uniform explicit total-variation coupling bound.

Diaz-Lopez et al., *Counting peaks on graphs*, *Australasian Journal of Combinatorics* 75(2) (2019), Sections 2–3, counts prescribed peak sets of randomly ordered vertices, including joins and complete bipartite graphs. These earlier monochrome counts are acknowledged. They do not address the initial-color-resolved joint stochastic law or its quantitative many-part limit. A related mathematical research record on complete multipartite Cholesky fill has a single-priority first-run description; it concerns a different observable without independent initial-color marks or their joint convergence bound. Its accessible summary was compared, but the full repository text was not retrievable.

## Limitations

The \(N^{-1}\) rate bound has a nonoptimized multiplicative constant and requires \(\max_i p_i\le1-\varepsilon\); it does not cover a dominant part whose complement vanishes in proportion. The limiting law holds with a fixed initial-color count \(k\); growing \(k\) requires a separate analysis. The rate obstruction is a multicolor event bound, not an originality claim about the earlier monochrome literature. No independence of \(S_c\) is claimed at finite \(N\). No independence from the published priority-reduction lemma is claimed. Earlier equivalent many-color quantitative results outside the searched literature cannot be excluded without broader historical review.

## References

1. É. de Panafieu, F. Mathieu, M. Gradinariu Potop-Butucaru, and S. Tixeuil, *The Exact Stabilization Time of Self-Stabilizing Coloring: Mean, Variance, and Distribution*, arXiv:2611.17989v1 (submitted 2026-11-13), https://arxiv.org/abs/2611.17989 ; especially Lemma 1 and Proposition 9 and its proof.
2. A. Diaz-Lopez, L. Everham, P. E. Harris, E. Insko, V. Marcantonio, and M. Omar, *Counting peaks on graphs*, *Australasian Journal of Combinatorics* 75(2) (2019), 174–189; https://par.nsf.gov/servlets/purl/10130403 ; earlier arXiv:1708.08493.
3. *A first-run law and geometric near-maximal fill for complete multipartite Cholesky*, published-finding corpus record 2026/11/2/2484223143f3, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-first-run-law-and-geometric-near-maximal-fill-for-complete-mul--2484223143f3 (summary accessible; full text unavailable for comparison).
