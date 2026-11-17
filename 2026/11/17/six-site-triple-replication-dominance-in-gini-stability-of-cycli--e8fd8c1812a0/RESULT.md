# Six-site triple-replication dominance in Gini stability of cyclic morphological opening

## Finding

For every integer \(n\ge2\), consider the two-site flat opening on real cyclic sequences,
\[
 (O_nx)_i=\min\{x_i,\max(x_{i-1},x_{i+1})\},\qquad i\in\mathbb Z/n\mathbb Z,
\]
and the complete-graph pairwise-difference (Gini) seminorm
\[
 G_n(h)=\sum_{0\le i<j<n}|h_i-h_j|.
\]
Its exact **global two-input** Lipschitz coefficient is
\[
 \boxed{\operatorname{Lip}_{G_n}(O_n)=
 \begin{cases}
 0,&n=2,\\
 1,&n=3,\\
 4/3,&n=4,\\
 3/2,&n=5,\\
 3(n-3)/(n-1),&n\ge6.
 \end{cases}}
\]
Every positive constant is attained by arbitrarily close pairs of strictly ordered real input signals. Thus the opening is Gini-nonexpansive exactly in dimensions two and three, begins amplifying perturbations at four samples, and first makes threefold **coordinate replication strictly more amplifying than twofold replication** at six samples. For \(n\ge6\), the norm equals \(3-6/(n-1)\) and approaches the sharp but never finite-dimensional attained universal ceiling \(3\). Its Gini triple-replication dominance threshold at six samples is different from its centered-Euclidean full saturation at eight samples: the choice of variation geometry materially changes the stability threshold.

## Assumptions and scope

Signals are arbitrary vectors in \(\mathbb R^n\), with zero-based cyclic indexing and the ordinary order on \(\mathbb R\). The finite opening above is the maximum of the two adjacent pairwise erosions and may also be written \((O_nx)_i=\max\{\min(x_{i-1},x_i),\min(x_i,x_{i+1})\}\). For \(n=2\), the two neighbors coincide; the formula still applies. The seminorm \(G_n\) is unweighted, with no normalization by the number of pairs. Both the opening and the seminorm are invariant under common additive shifts in the sense \(O_n(x+c\mathbf1)=O_nx+c\mathbf1\) and \(G_n(h+c\mathbf1)=G_n(h)\). The Lipschitz coefficient is the supremum over pairs \(x,y\) with \(G_n(x-y)>0\); pairs with zero denominator have zero output-difference seminorm by translation equivariance.

## Proof

**Step 1: Exact cut reduction for any coordinate selector.** If the coordinates of \(x\) are distinct, there is a neighborhood of \(x\) on which the opening equals a fixed matrix \(Q\) with one unit entry per row: \((Qh)_i=h_{\sigma(i)}\). Put \(c_j=\#\{i:\sigma(i)=j\}\), so \(\sum_jc_j=n\). For every proper nonempty subset \(S\) of input indices, let \(s=|S|\) and \(q=\sum_{j\in S}c_j\). Then
\[
 G_n(\mathbf1_S)=s(n-s),\qquad G_n(Q\mathbf1_S)=q(n-q).
\]
For arbitrary real \(h\), sort its distinct levels and express it as a constant plus a nonnegative combination of nested superlevel indicators. The triangle inequality on the output and the exact coarea identity on the input imply
\[
 \|Q\|_{G_n\to G_n}=
 \max_{\varnothing\ne S\subsetneq\{0,\ldots,n-1\}}
 \frac{q(n-q)}{s(n-s)}.\tag{1}
\]
The reverse inequality holds because each cut vector is itself a permitted perturbation.

**Step 2: From local selectors to the global nonlinear coefficient.** For any strictly ordered base input \(x\), every direction \(h\) is realized by the pair \(x,x+\varepsilon h\) for sufficiently small \(\varepsilon>0\). Conversely, a line segment joining arbitrary inputs passes through finitely many affine selector cells, outside possible persistent tie hyperplanes. Approximate such a segment by generic segments and use continuity of the min-max map. Integrating the piecewise-constant directional derivative and applying the triangle inequality shows that the global two-input coefficient is the maximum of the selector norms in (1). No finite enumeration is assumed in this reduction.

**Step 3: Every coordinate can be copied at most three times.** The output at index \(i\) uses only input indices \(i-1,i,i+1\). Consequently \(0\le c_j\le3\) for every input coordinate, irrespective of its order or of dimension. For \(n\ge6\), fix a cut and, by replacing it with its complement, assume \(1\le s\le n/2\). Then \(q\le3s\). If \(3s\le n/2\), monotonicity of \(q(n-q)\) for \(0\le q\le n/2\) gives
\[
 \frac{q(n-q)}{s(n-s)}
 \le\frac{3(n-3s)}{n-s}
 \le\frac{3(n-3)}{n-1};\tag{2}
\]
the last inequality is equivalent to \(2n(s-1)\ge0\). If \(3s\ge n/2\), then \(n/6\le s\le n/2\) and hence \(s(n-s)\ge5n^2/36\). Since \(q(n-q)\le n^2/4\),
\[
 \frac{q(n-q)}{s(n-s)}\le\frac95
 \le\frac{3(n-3)}{n-1}\qquad(n\ge6).\tag{3}
\]
Equations (1)--(3) prove the claimed upper bound for every dimension at least six. For \(3\le n\le5\), the universal integer cut estimate \(q(n-q)\le\lfloor n^2/4\rfloor\) and \(s(n-s)\ge n-1\) gives the respective upper bounds \(1,4/3,3/2\). For \(n=2\), both output coordinates equal \(\min(x_0,x_1)\), so the output variation vanishes for every input pair.

**Step 4: Exact witnesses, including the six-site cutoff.** For \(n=3\), take \(x=(0,1,2)\) and perturb coordinate zero; the output copies that perturbation once, giving ratio one. For \(n=4\) and \(n=5\), take the strictly increasing input \(x=(0,1,\ldots,n-1)\) and perturb coordinate \(n-2\). Its selected value occurs at output indices \(n-2,n-1\), so the output difference has precisely two nonzero equal entries. These yield ratios \(2(n-2)/(n-1)\), equal respectively to \(4/3\) and \(3/2\).

For every \(n\ge6\), choose a strictly ordered input with \(x_0=0\), \(x_1=4\), \(x_{n-1}=5\), \(x_2=-2\), \(x_{n-2}=-1\), and every remaining coordinate distinct and strictly smaller than \(-3\). At outputs \(0,1,n-1\), the opening selects precisely the input coordinate \(0\). No other output can select that coordinate. Perturb \(x_0\) by \(0<\varepsilon<1\), without changing any selector. The input difference is \(\varepsilon\mathbf1_{\{0\}}\), while the output difference is \(\varepsilon\mathbf1_{\{0,1,n-1\}}\). Therefore
\[
 \frac{G_n(O_n(x+\varepsilon\mathbf1_{\{0\}})-O_nx)}
 {G_n(\varepsilon\mathbf1_{\{0\}})}
 =\frac{3(n-3)}{n-1},
\]
exactly attaining the upper bound. Letting \(\varepsilon\downarrow0\) establishes arbitrarily close attainment. For clarity, threefold coordinate replication itself can already occur at four and five sites. For example, the four-site input \((3,4,1,5)\) selects coordinate zero at three output sites; at five sites \((0,4,-2,-1,5)\) does likewise. At four sites triplication gives cut ratio \(3(4-3)/(4-1)=1\), strictly worse than the two-copy value \(4/3\); at five sites it ties the two-copy value \(3/2\). For every \(n\ge6\), however, triplication strictly exceeds the two-copy ratio because \(3(n-3)-2(n-2)=n-5>0\). This is the precise sense in which six is the sharp **dominance** threshold. The limit \(3\) as \(n\to\infty\) is a supremum over dimensions; the finite-dimensional sharp coefficient stays strictly below \(3\).

## Verification

The standalone `verify.py` performs four reproducible independent exact-rational checks using Python's standard library: all strict-order chambers and all binary input cuts for dimensions two through eight (46,232 chambers); the multiplicity-based cut inequality for dimensions six through two hundred (1,810,900 feasible cut-parameter instances); explicit attaining pairs in dimensions three through two hundred; and 4,350 randomly generated pairs with rational coordinates in dimensions two through thirty. All tests passed. They corroborate but do not replace the all-dimensional proof in Steps 1--4.

## Relationship to prior work

Maragos and Schafer's 1987 morphology papers introduce and analyze flat erosions, dilations, openings, and their connection to order-statistic and stack filters. Their relevant reported conclusions concern structural max-min and threshold representations, not the Gini seminorm of the **difference of two opened signals**. Anguelov and Rohwer's 2007 full-text study proves trend and **one-input path-total-variation** preservation for LULU-type operators on intervals, without a corresponding two-input complete-pair Gini norm. In a distinct finite-path setting, the published result *Finite-window morphology: sharp two-input variation and a boundary-weight transition* determines weighted adjacent-edge variation for individual sliding erosions and dilations, and therefore does not imply (1)--(3) for the cyclic opening and the complete-graph metric. Published exact cyclic three-point median results use cyclic adjacent-edge variation rather than Gini variation. Closely related results for the same opening under centered Euclidean variation and for cyclic running maxima under Gini variation also involve different seminorms or operators. Neither implication transfers a sharp value or its dimension cutoff to the present claim; for example centered-Euclidean saturation requires eight sites, whereas triple replication first becomes strictly Gini-norming at six. The literature comparison does not constitute a proof that no unindexed equivalent exists.

## Limitations

The theorem is restricted to a flat two-site cyclic opening on finite real scalar signals with unweighted Gini variation. It does not determine corresponding constants for larger structuring elements, weighted Gini or adjacent-edge variation, arbitrary graph neighborhoods, adaptive morphology, multichannel data, or general compositions. The 1987 technical-report full texts were inspected selectively rather than page-by-page; an equivalent unindexed result remains a historical-priority risk. This mathematical result has not undergone independent validation.

## References

1. P. Maragos and R. W. Schafer, *Morphological Filters—Part I: Their Set-Theoretic Analysis and Relations to Linear Shift-Invariant Filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing **35** (1987), 1153–1169, DOI:10.1109/TASSP.1987.1165259; technical-report full text https://drum.lib.umd.edu/bitstreams/dd491c47-619b-403b-8120-bd0b4078663d/download.
2. P. Maragos and R. W. Schafer, *Morphological Filters—Part II: Their Relations to Median, Order-Statistic, and Stack Filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing **35** (1987), 1170–1184, DOI:10.1109/TASSP.1987.1165254; technical-report full text https://drum.lib.umd.edu/bitstreams/154a294b-2b9b-4c93-871a-8c68ed6834ff/download.
3. R. Anguelov and C. Rohwer, *LULU operators for functions of continuous argument*, arXiv:0711.1944v1 (first posted 2007-11-13), https://arxiv.org/abs/0711.1944.
4. C. Gerstenberger and D. Vogel, *On the efficiency of Gini's mean difference*, arXiv:1405.5027 (first posted 2014-05-20), https://arxiv.org/abs/1405.5027.
5. *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, public mathematical record dated 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2.
6. *Sharp BV perturbation threshold for cyclic three-point medians*, public mathematical record dated 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-bv-perturbation-threshold-for-cyclic-three-point-medians--59530ef626eb.
