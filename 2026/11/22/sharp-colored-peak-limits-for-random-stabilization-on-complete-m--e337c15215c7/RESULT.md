# Sharp colored-peak limits for random stabilization on complete multipartite graphs

## Finding

Let \(G=K_{a_1,\ldots,a_r}\) have \(r\ge3\) nonempty parts and \(N=\sum_i a_i\) vertices. Assign the vertices independent uniform initial colors from \([k]\), \(k\ge2\). Use a palette of size at least \(\max\{k,\Delta(G)+1\}\). At every step select a conflicting vertex uniformly and recolor it with any color absent from its neighborhood. Let \(S_c\) be the number of vertices of initial color \(c\) never selected, and write \(p_i=a_i/N\). If \(\max_i p_i\le1-\varepsilon\), compare \(S=(S_1,\ldots,S_k)\) to a vector \(G_*=(G_1,\ldots,G_k)\) of independent variables with
\[
\Pr(G_c=j)=\sum_i p_i(1-p_i)p_i^{j-1},\qquad j=1,2,\ldots.
\]
Then
\[
\frac{1-\sum_i p_i^2}{N-1}\ \le\ d_{\rm TV}(\mathcal L(S),\mathcal L(G_*))\ \le\ \min\!\left\{1,\frac{2k^3(1+\varepsilon^{-2})}{N}\right\}.
\]
The lower bound is witnessed by \(S_c\le1\) versus \(G_c\le1\) for any named color \(c\). In particular, with fixed \(k\) and \(\varepsilon>0\), the inverse-size order is sharp uniformly in the admissible part profiles, since \(1-\sum_i p_i^2\ge\varepsilon\). For balanced tripartite graphs the lower bound is \(2/[3(N-1)]\).

## Assumptions and scope

The graph is finite, simple, and complete multipartite with all parts nonempty. Recoloring choices may depend on past colors, provided the chosen color is absent from the activated vertex's neighborhood. The comparison uses the actual finite part proportions, not asymptotically prescribed proportions. For fixed \(k,r\) and \(p_i\to p_i^*\in(0,1)\), the comparison recovers the known weak limit of independent geometric mixtures, with weights and parameters determined by \(p_i^*\). The number of recolorings is \(N-\sum_c S_c\). For balanced parts, the limiting pgf of \(\sum_c S_c\) on \(|z|\le1\) is \(((r-1)z/(r-z))^k\). These limit statements are included to interpret the quantitative estimate.

## Proof

**Priority model.** Recoloring a conflicting vertex creates no new conflict edge and erases its incident conflict edges. Thus each vertex is selected at most once, and the dynamics depend only on the initial conflict graph and the order of selections. Process an independent uniform vertex permutation, selecting a vertex only if it still has a conflict when reached. The next live vertex is uniform among the vertices still live because the unrevealed permutation is uniform and vertices already skipped cannot become live. A vertex survives exactly when its permutation label exceeds every neighbor's in its initial conflict graph: an earlier conflicting neighbor would have selected while the vertex was still unprocessed, whereas a later conflicting neighbor forces this vertex to select. Equivalently, read the order from highest label down. In each color the survivors are exactly the initial run of vertices from the part of the first vertex of that color. Indeed, all run members precede every opposite-part vertex of that color, and any vertex after the run has an earlier same-color neighbor. An absent color gives a run of length zero.

**Upper bound.** Couple a uniformly random permutation \(P_1,\ldots,P_N\) of the vertex identities to an infinite i.i.d. uniform sequence of identities \(U_t\). At step \(t\le N\) set \(P_t=U_t\) if \(U_t\) is unused in \(P\); otherwise draw uniformly from the unused entries. This is uniform over the remaining entries at each step. Independently put i.i.d. uniform color marks \(D_t\in[k]\) on the positions, using the same marks for the two streams. In the i.i.d. stream the part subsequences for different colors are independent i.i.d. samples of the finite proportions. To see the independence, condition on the entire mark sequence: those subsequences use pairwise disjoint coordinates and their laws do not depend on the mark sequence, almost surely. Their initial part-run lengths have the displayed law of \(G_*\).

Let \(H_c\) be the first position where two vertices marked \(c\) have come from different parts in the i.i.d. stream, and \(H=\max_c H_c\). With no repeated identity at times \(1,\ldots,H\), we have \(H\le N\) and the two streams agree far enough to determine all initial runs. The event \(H\ge t\) is determined by the first \(t-1\) positions, and the conditional probability of drawing an earlier identity at time \(t\) is at most \((t-1)/N\). The chance of a repeat up through \(H\) is thus at most \(\mathbb E[H(H-1)]/(2N)\). The time to the first mark \(c\) is geometric with success probability \(1/k\); conditional on its part \(i\), the additional wait to a different part of color \(c\) is geometric with success probability \((1-p_i)/k\ge\varepsilon/k\). For a positive-support geometric variable with success probability \(u\), its second moment is \((2-u)/u^2\le2/u^2\). Applying \((x+y)^2\le2x^2+2y^2\) gives \(\mathbb E H_c^2\le4k^2(1+\varepsilon^{-2})\). Since \(H^2\le\sum_c H_c^2\), the coupling inequality gives the upper bound.

**Lower bound.** If \(C_c\) is the population of initial color \(c\), the event \(S_c\ge2\) requires \(C_c\ge2\) and the first two vertices of that color in priority order to be from the same part. Conditioned on \(C_c\ge2\), the ordered pair is uniform among distinct vertex pairs by exchangeability. Thus
\[
\Pr(S_c\ge2)=\Pr(C_c\ge2)\frac{\sum_i a_i(a_i-1)}{N(N-1)},
\qquad \Pr(G_c\ge2)=\sum_i p_i^2.
\]
Omitting the prefactor at most one in the first expression gives a difference of at least \((1-\sum_i p_i^2)/(N-1)\) on the complementary event, as claimed.

## Exact finite law used for comparison

An unconditional representation of the known conditional run law is useful for finite checks. For thresholds \(j_c\ge0\), set \(J=\sum_c j_c\), \(I=\{c:j_c>0\}\), and for \((i_c:c\in I)\in[r]^I\) put \(t_h=\sum_{c\in I:i_c=h}j_c\). If \(J\le N\), the joint tail is
\[
\Pr(S_c\ge j_c\text{ for all }c)=\Pr(C_c\ge j_c\text{ for all }c)\,
\frac{\displaystyle\sum_{(i_c)\in[r]^I}\prod_{h=1}^r(a_h)_{\underline{t_h}}}{(N)_{\underline J}}.
\]
Here the counts \((C_c)_{c=1}^k\) are multinomial with uniform probabilities, and \((a)_{\underline j}\) is the falling factorial, taken as zero if \(j>a\). The tail is zero for \(J>N\) and one when \(J=0\). Given eligible color populations, the combined priority prefixes are uniform ordered injections into the \(N\) vertices by exchangeability, and the numerator counts those injections whose prefix for each active color lies in the specified part. This gives the displayed equivalent evaluation of the joint law without conditioning on all part-by-color counts.

## Relationship to prior work and limitations

De Panafieu, Mathieu, Gradinariu Potop-Butucaru and Tixeuil, *The Exact Stabilization Time of Self-Stabilizing Coloring: Mean, Variance, and Distribution*, [arXiv:2611.17989v1](https://arxiv.org/abs/2611.17989v1), give the random-priority reduction (Lemma 1) and the bipartite limit with independent colors in the limit (Proposition 9). Diaz-Lopez et al., [*Counting peaks on graphs*](https://arxiv.org/abs/1708.08493), treat monochrome peak-set enumeration. The [multipartite colored-priority run law](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-multipartite-random-priority-peaks-exact-colored-run-laws-and-a--cd7af7620aee/RESULT.md) gives the exact conditional product law of the runs given part-by-color counts. Averaging that law gives the same unconditional distribution, and that record also gives the fixed-palette geometric-mixture limit. The shared catalogue date does not establish which derivation came first. The [multipartite Cholesky first-run result](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-first-run-law-and-geometric-near-maximal-fill-for-complete-mul--2484223143f3/RESULT.md) concerns a different observable with the same unmarked ordering statistic.

The contribution here is the explicit sharp-order joint total-variation estimate relative to the finite profiles, not a priority claim for the run law or the weak limit. The multiplicative constant is not optimized. The estimate with a fixed non-dominance margin does not describe profiles with one part exhausting the graph. No general growing-palette limit is asserted.

## Verification

The frozen `verify.py` and `verify_dynamics.py` are bounded checks of the finite distribution and its representation by priorities. They do not certify the uniform total-variation upper bound, which follows from the stopping-time proof above. No finite check or literature comparison establishes global priority.
