# Sharp two-wall variation law for one-sided cyclic dilation

## Finding

Fix an integer \(n\ge3\), and let the sites be \(\mathbb Z/n\mathbb Z\). For every positive real cyclic edge-weight vector \(w=(w_0,\ldots,w_{n-1})\), define
\[
 V_w(z)=\sum_{i=0}^{n-1}w_i|z_{i+1}-z_i|,
 \qquad (Dz)_i=\max\{z_i,z_{i+1}\},
\]
with subscripts modulo \(n\). The exact **two-input** variation-Lipschitz coefficient of the one-sided two-site dilation is
\[
 K_n(w)=\sup_{V_w(x-y)>0}\frac{V_w(Dx-Dy)}{V_w(x-y)}.
\]
It has the following explicit, finite, *attained* formula. Put
\[
 L_1(w)=\max\left\{1,\max_{j\in\mathbb Z/n\mathbb Z}
 \frac{w_{j-2}+w_{j-1}}{w_{j-1}+w_j},
 \max_{j\in\mathbb Z/n\mathbb Z}\frac{w_{j-2}+w_j}{w_{j-1}+w_j}\right\},
\]
and, for \(n\ge4\), put
\[
 L_2(w)=\max_{\substack{a\in\mathbb Z/n\mathbb Z\\2\le k\le n-2}}
 \frac{\max\{w_{a-1},w_a\}+\max\{w_{a+k-1},w_{a+k}\}}
 {w_a+w_{a+k}}.
\]
For \(n=3\), set \(L_2(w)=0\). Then
\[
 \boxed{K_n(w)=\max\{L_1(w),L_2(w)\}.}
\]
Every value attaining this maximum is realized by two arbitrarily close real data vectors, not merely by a formal linearization.

**Rigidity and an essential two-wall obstruction.** For every \(n\ge3\),
\[
 K_n(w)\le1\quad\Longleftrightarrow\quad w_0=\cdots=w_{n-1}.
\]
For even \(n\ge4\) and alternating weights \(w_{2j}=a\), \(w_{2j+1}=b\), \(a,b>0\), the exact constant is
\[
 \boxed{K_n(w)=\max\{a/b,b/a\}.}
\]
Already for \(n=4\) and \(w=(1,2,1,2)\), the sharp value is \(2\) although every singleton/co-singleton cut produces gain at most \(4/3\). Thus a connected arc with *two separated boundary edges* can be necessary for the sharp norm. The same result holds for the dual one-sided erosion \((Ez)_i=\min\{z_i,z_{i+1}\}\) by \(Ez=-D(-z)\).

## Assumptions and scope

All inputs are arbitrary real vectors. The variation is the **weighted sum of cyclic first differences**, not weighted data fidelity, directed edge variation, or a path with free endpoints. The filter always uses the forward pair \(\{i,i+1\}\), not all graph neighbors or a symmetric three-site neighborhood. Positive weights are essential for a finite nondegenerate seminorm quotient. The factor concerns differences between *two* outputs and two inputs; reducing each individual input's variation is a logically different property. Constants have zero variation and the dilation is translation equivariant, so zero-denominator pairs produce zero output variation.

## Proof

**1. Strict selector chambers.** Suppose \(x_i\ne x_{i+1}\) for all \(i\), and write \(\sigma_i=1\) if \(x_{i+1}>x_i\), and \(\sigma_i=0\) otherwise. In a neighborhood of \(x\), dilation agrees with the linear selector
\[
 (A_\sigma z)_i=z_{i+\sigma_i}.
\]
A strict sign pattern is realizable around the cycle if and only if it contains both signs: the cyclic differences sum to zero, and conversely if there are \(p>0\) positive and \(q>0\) negative prescribed signs, assign all positive increments the value \(q\), and all negative increments the value \(-p\). Their sum is zero and they define the required real cyclic input. The map \(D\) is continuous and piecewise affine, so splitting the segment joining any two inputs into its finitely many strict linear pieces proves that its global variation-Lipschitz constant equals the maximum of the \(V_w\)-operator norms of its realizable selectors. A selector norm is attained by sufficiently small perturbations inside its strict chamber.

**2. Coarea and connected arcs.** Fix any selector \(A_\sigma\). For a vector \(h\), subtract its minimum and use the finite layer-cake identity to write it as a nonnegative integral of superlevel-set indicators \(\mathbf1_S\). Because selectors preserve constants and \(V_w\) is subadditive,
\[
 V_w(A_\sigma h)\le\int V_w(A_\sigma\mathbf1_{\{h>t\}})\,dt,
\qquad V_w(h)=\int V_w(\mathbf1_{\{h>t\}})\,dt.
\]
Any proper nonempty subset of the cycle is a disjoint union of maximal consecutive arcs. Its indicator is the sum of their indicators, its weighted boundary variation is the sum of their weighted boundary variations, and the output variation of that sum cannot exceed the sum of their individual output variations. Hence, for each selector, a single proper cyclic arc attains its variation operator norm after maximizing over arcs.

Write a proper arc as \(S=\{a+1,\ldots,b\}\) in cyclic order, where \(b=a+k\) with \(1\le k\le n-1\). Its input variation is \(w_a+w_b\). Away from the two boundary sites \(a\) and \(b\), both possible selector inputs lie on the same side of the arc boundary, so \((A_\sigma\mathbf1_S)_i=\mathbf1_S(i)\). At the two exceptional sites, independently,
\[
 (A_\sigma\mathbf1_S)_a=\sigma_a=:u,\qquad
 (A_\sigma\mathbf1_S)_b=1-\sigma_b=:1-v.
\]
These four binary outputs are the complete list of possible arc images.

**3. Exact attainment of all boundary choices.** Given arbitrary \(a\ne b\) and any \(u,v\in\{0,1\}\), prescribe \(\sigma_a=u\), \(\sigma_b=v\). There is at least one other cycle edge because \(n\ge3\). If \(u=v\), choose another edge of opposite sign; otherwise any remaining signs will do. The construction in step 1 then produces a strict cyclic base signal \(x\) realizing the prescribed choices, including the case \(n=3\). For sufficiently small \(\varepsilon>0\), set \(y=x+\varepsilon\mathbf1_S\). Both signals remain in the same selector chamber, and
\[
 Dy-Dx=\varepsilon A_\sigma\mathbf1_S,
 \qquad V_w(y-x)=\varepsilon(w_a+w_b).
\]
Consequently every one of the four arc ratios is exactly attained by an actual pair. Together with step 2 this proves the complete cut formula
\[
 K_n(w)=\max_{\substack{a\in\mathbb Z/n\mathbb Z\\1\le k\le n-1\\u,v\in\{0,1\}}}
 \frac{V_w(H_{a,k}^{u,v})}{w_a+w_{a+k}},
\]
where \(H_{a,k}^{u,v}\) is the indicator of \(\{a+1,\ldots,a+k\}\), except that its entries at \(a\) and \(a+k\) are replaced by \(u\) and \(1-v\), respectively.

**4. Reduction to the displayed closed finite expression.** When the arc or its complement has one vertex, the output has either zero variation or its two boundary edges are, cyclically, one of \(\{j-2,j-1\}\), \(\{j-1,j\}\), or \(\{j-2,j\}\), with input boundary \(\{j-1,j\}\). The maximal ratio over these cases is precisely \(L_1(w)\). When both arc and complement have at least two vertices, the two output boundary edges independently shift from \(a\) to either \(a\) or \(a-1\), and from \(b\) to either \(b\) or \(b-1\). Hence the largest such ratio is \(L_2(w)\), with the stated range \(2\le k\le n-2\). This completes the exact formula for all dimensions, including the three-cycle.

**5. Rigidity.** If \(K_n(w)\le1\), the first family in \(L_1(w)\) forces \(w_{j-2}\le w_j\) for every \(j\). Cycling the index in steps of two forces equality in every such inequality. If \(n\) is odd, the weights are immediately constant. If \(n\) is even, they have a two-periodic form \((a,b,a,b,\ldots)\). For \(a\ne b\), choose two boundary edges of the smaller weight, separated by two steps; the \(L_2\) term gives amplification at least \(\max\{a/b,b/a\}>1\), a contradiction. Conversely, equal weights make both parts of the formula equal to one. The same reasoning and the upper bound obtained by taking the greatest neighboring-weight ratio give the exact stated two-periodic value.

## Verification

The standalone Python 3 program `verify.py` uses exact rational arithmetic and no external dependencies. It independently enumerates every realizable strict edge-sign selector and every nonempty proper binary perturbation through eight sites, checking the analytical arc formula and its reduced expression for 36 positive weight profiles. It then constructs 3,984 explicit **strict-chamber, two-input** witnesses for all boundary configurations in those profiles and checks attainment. Uniform and alternating weight assertions are checked through 15 sites and 12 sites, respectively; a four-cycle confirms the sharp separated-wall gain \(2\) against the singleton ceiling \(4/3\). These are finite tests only. All-size conclusions rely on the preceding analytical proof.

To reproduce, run `python3 verify.py` beside this file. The program prints `ALL_CYCLIC_DILATION_VARIATION_CHECKS_PASS` when its assertions succeed.

## Relationship to prior work

The full-text archival works by Anguelov--Rohwer (2007) and Anguelov--Plaskitt (2007) establish the algebra of morphological smoothing and **one-input** total-variation preservation for LULU operators, rather than a sharp **two-input** weighted cyclic variation modulus for this one-sided flat dilation. The full-text 2014 Najman--Cousty survey develops graph morphological dilation and threshold stacking but does not give this cycle-specific weighted Lipschitz constant. Cousty--Najman--Dias--Serra (2013) establishes general morphological graph operators; only its abstract was accessible in this comparison and its possible unseen overlap remains a priority risk.

The published finite-window morphology calculation concerns **truncated path windows**: it excludes periodic boundaries and its active-edge ratio formula cannot be specialized to obtain the two-boundary cyclic ratios by setting a radius. The published cyclic median result treats a **three-site rank selector** with uniform variation, rather than two-site extrema with arbitrary weights. The published tree dilation result concerns **one-input** variation and excludes cycles. All three were compared by mathematical implication using their full scientific statements. No inspected statement implies the weighted two-wall formula, the necessity of two separated walls, or the alternating-weight sharp coefficient. This is an originality assessment conditional on the consulted literature, not a claim of exhaustive historical priority.

## Limitations

The theorem treats finite real cyclic signals, positive fixed edge weights, and exactly the forward two-site max/min filter. It does not cover symmetric radius-one three-site dilation, larger neighborhoods, spatially adaptive windows, multidimensional graph morphology, or higher-order variation. The finite checker is not a substitute for the proof. Possible equivalent results in unindexed older stack-filter and morphology literature have not been excluded, and there has been no independent mathematical validation.

## References

1. R. Anguelov and C. Rohwer, *LULU operators for functions of continuous argument*, arXiv:0711.1944v1, first submitted 13 November 2007, https://arxiv.org/abs/0711.1944 . Full HTML examined, especially Sections 2 and 5.
2. R. Anguelov and I. Plaskitt, *A Class of LULU Operators on Multi-Dimensional Arrays*, arXiv:0712.2923v1, first submitted 18 December 2007, https://arxiv.org/abs/0712.2923 . Full HTML examined, especially Sections 1, 2 and 5.
3. L. Najman and J. Cousty, *A graph-based mathematical morphology reader*, arXiv:1404.7748v1, first submitted 30 April 2014, https://arxiv.org/html/1404.7748v1 . Full HTML examined, especially Section 3.
4. J. Cousty, L. Najman, F. Dias and J. Serra, *Morphological filtering on graphs*, Computer Vision and Image Understanding **117** (2013), 370--385, DOI: 10.1016/j.cviu.2012.08.016. Public abstract inspected; full text not obtained.
5. *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2 . Full RESULT.md inspected.
6. *Sharp BV perturbation threshold for cyclic three-point medians*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-bv-perturbation-threshold-for-cyclic-three-point-medians--59530ef626eb . Full RESULT.md inspected.
7. *Exact weighted-variation amplification at every radius of tree max-dilation*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-weighted-variation-amplification-at-every-radius-of-tree-m--a69cb138f1ee . Full RESULT.md inspected.
