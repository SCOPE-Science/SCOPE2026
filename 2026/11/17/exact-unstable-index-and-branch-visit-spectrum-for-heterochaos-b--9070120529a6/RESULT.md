# Exact unstable-index and branch-visit spectrum for heterochaos baker maps

## Finding

Fix an integer \(M\ge2\), a real \(0<a<1/M\), and an integer \(n\ge1\). For the two-dimensional generalized heterochaos baker map below, let \(A_{n,m}\) and \(B_{n,m}\) count regular points fixed by the \(n\)-th iterate, with precisely \(m\) visits to the center-expanding base strip, whose respective unstable dimensions are one and two. Least period is **not** required to be \(n\). The exact joint count is

\[
A_{n,m}=\begin{cases}\binom{n}{m}(M^{n-m}-2M^m),&0\le m<n/2,\\0,&m\ge n/2,\end{cases}
\qquad
B_{n,m}=\begin{cases}\binom{n}{m}(M^m-2M^{n-m})-\mathbf 1_{\{m=n\}}(M^n-2),&n/2<m\le n,\\0,&m\le n/2.\end{cases}
\]

In particular the numbers \(N_1(n)=\sum_m A_{n,m}\), \(N_2(n)=\sum_m B_{n,m}\) satisfy the **exact signed imbalance**

\[N_1(n)-N_2(n)=M^n-2.\]

Both are asymptotic to \((M+1)^n\). If a point is selected uniformly from the index-one or index-two regular fixed points, then its visit count \(K_{1,n}\), respectively \(K_{2,n}\), satisfies

\[
\frac{K_{1,n}-n/(M+1)}{\sqrt{nM}/(M+1)}\;\Rightarrow\;N(0,1),
\qquad
\frac{K_{2,n}-nM/(M+1)}{\sqrt{nM}/(M+1)}\;\Rightarrow\;N(0,1).
\]

The theorem is independent of \(a\) throughout the indicated open interval.

## Assumptions and scope

Let \(u,v\in[0,1]\), write \(d\in\{0,\dots,M-1\}\), and define \(F_a(u,v)=(T_a(u),S(u,v))\) with

\[
T_a(u)=\begin{cases}(u-da)/a,&da\le u<(d+1)a,\\(u-Ma)/(1-Ma),&Ma\le u\le1,\end{cases}
\]

\[
S(u,v)=\begin{cases}(v+d)/M,&da\le u<(d+1)a,\\Mv-j,&Ma\le u\le1,\ j/M\le v<(j+1)/M.
\end{cases}
\]

On the last center strip include \(v=1\) in the natural last closed interval. A **regular** period-\(n\) point has \(F_a^n(u,v)=(u,v)\) and at each of its first \(n\) iterates lies in the two-dimensional *interior* of exactly one specified branch rectangle. In particular, branch boundaries and outer-square boundary points are excluded. The center multiplier over an \(n\)-itinerary with \(m\) beta visits is \(M^{2m-n}\); the base multiplier exceeds one. Thus regular \(m<n/2\) points have unstable index one and regular \(m>n/2\) points have unstable index two. Neutral \(2m=n\) points, which may occur in entire line segments, are explicitly excluded.

## Proof

**1. Base itineraries.** The \(M\) alpha branches and single beta base branch all map bijectively and increasingly onto \([0,1]\), except for the one-sided convention at endpoints. Each length-\(n\) word over \(M\) alpha labels and beta specifies a strict expanding affine return map on a base cylinder. Its inverse is a strict contraction of the unit interval and fixes a unique base point. Except for the all-beta word, fixed base points with a beta and an alpha lie strictly inside their cylinders; the all-beta base fixed point is \(u=1\), excluded. A pure-alpha word with every label \(0\) has \(u=0\) and therefore contributes no regular point; its center fixed point is also an excluded endpoint. All other pure-alpha words have an interior base fixed point, although the all-\(M-1\) center word has the excluded center endpoint \(v=1\). More generally an endpoint base fixed point of a branch word must be an orbit of a partition boundary; the expanding full-branch property forces it to map onto \(0\) or \(1\), so periodic endpoint bases reduce to these pure boundary words. Consequently the center count on all mixed base words is independent of \(a\).

**2. Cancellation of inverse center branches.** Define \(P_d(v)=(v+d)/M\) and \(E(v)=Mv-\lfloor Mv\rfloor\) on non-\(M\)-adic interior points. Every \(P_d\) satisfies \(E\circ P_d=\mathrm{id}\). A cyclic binary word in the letters alpha and beta can be cyclically cut and reduced by deleting adjacent alpha-then-beta pairs until only \(|n-2m|\) letters of the majority type remain. On regular periodic points, rotation to this cut is a bijection (apply an appropriate iterate), and each deleted pair has its beta digit forced by the preceding alpha label. Recovering the deleted pairs gives a bijection between regular periodic center points of the original word and of the reduced center map. This statement is also valid in the two pure-type cases without deletion. An elementary way to select the cut is to choose a cyclic prefix of minimum height in the \(+1\) alpha, \(-1\) beta walk (or reverse the signs if beta predominates), then successively cancel all minority steps with preceding opposite steps.

**3. More alpha steps.** Let \(c=n-m>m\) and \(r=c-m\). After cancellation, the center return is a composition of \(r\) maps \(P_d\), hence has exactly one fixed point in \([0,1]\) for every choice of the \(c\) alpha labels. It is regular precisely when this point is neither endpoint \(0\) nor \(1\): in these affine systems an \(M\)-adic rational on a periodic orbit eventually hits the center partition boundary. Endpoint fixed points occur exactly when all \(r\) surviving alpha digits are zero, or all \(M-1\). The \(m\) deleted alpha labels are unconstrained, giving exactly \(2M^m\) inadmissible assignments among the \(M^c\). Thus a fixed arrangement of \(m\) beta locations gives \(M^c-2M^m\) index-one points. There are \(\binom nm\) such arrangements.

**4. More beta steps.** When \(m>c\), cancellation leaves \(E^{m-c}\). Its non-\(M\)-adic fixed points are the \(M^{m-c}-2\) rational numbers \(j/(M^{m-c}-1)\) for \(1\le j\le M^{m-c}-2\). They remain regular when reinserting the \(c\) alpha maps (each alpha digit is freely chosen). This gives \(M^c(M^{m-c}-2)=M^m-2M^c\) for each beta-location arrangement, but the all-beta base word has \(u=1\) and contributes no regular planar point. Subtract its \(M^n-2\) center solutions when \(m=n\). In the balanced case the net center derivative is one and there are no hyperbolic points. This proves both finite histograms.

**5. Imbalance and normal laws.** The beta-dominant *uncorrected* histogram is exactly the alpha-dominant histogram reflected under \(m\mapsto n-m\); the all-beta correction therefore proves \(N_1-N_2=M^n-2\). Comparing alpha counts with \(\binom nm M^{n-m}\) and beta counts with \(\binom nm M^m\), and bounding the neglected/subtracted half-binomial sums by \(O_M((2\sqrt M)^n)\), gives

\[
N_1(n)=(M+1)^n+O_M((2\sqrt M)^n),\qquad
N_2(n)=(M+1)^n-M^n+2+O_M((2\sqrt M)^n).
\]

Since \(2\sqrt M<M+1\) for \(M>1\), both normalized visit-count distributions differ in total variation by an exponentially decaying amount from the binomial laws with parameters \(1/(M+1)\) and \(M/(M+1)\), respectively. The classical binomial central limit theorem proves the displayed Gaussian limits.

## Verification

The self-contained `CHECK.py` performs exact rational piecewise-affine iteration of the center branches for all base alphabet words in the ranges \(M=2,\ n\le8\), \(M=3,\ n\le5\), and \(M=4,\ n\le4\). It independently counts each regular center fixed point by its affine return branch and compares the counts to the derived binomial formula. It additionally applies the all-beta base exclusion and verifies the signed imbalance for each tested pair. Run `python3 CHECK.py`. The output is `HETEROCHAOS_INDEX_HISTOGRAM_OK`. These are finite diagnostics, not proof of the universal theorem.

## Relationship to prior work

Saiki–Takahasi–Yorke introduced the heterochaos baker example and proved coexistence and density of distinct unstable-index periodic points. Saiki–Takahasi–Yamamoto–Yorke define the generalized \(M\)-branch map, its regular periodic-point sets and unstable indices, and study the two maximal-entropy measures. Takahasi later proved distributional convergence of unstable-index periodic points to maximal-entropy measures, and subsequently proved large-deviation results for Dyck periodic points. Those results motivate periodic-index statistics but do not explicitly present the **parameter-independent exact joint histogram by beta visit number with the planar base-boundary subtraction** proved here. The two existing neutral-fiber records in the mathematical findings database concern the zero central exponent \(2m=n\), which is outside the hyperbolic scope of this theorem. The stated weak/CLT consequences are subordinate to the precise finite histogram and must not be presented as overturning existing periodic equidistribution.

## Limitations

Counts are of *regular fixed points of an iterate*, not only primitive-period points or cyclic orbits. Partition boundaries and all neutral fixed fibers are intentionally omitted. No corresponding histogram is proved for the three-dimensional extension. Prior published Dyck symbolic counts may encode parts of the formulas indirectly, and a complete publication-priority check remains necessary. No independent validation has been performed.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *Piecewise-linear maps with heterogeneous chaos*, arXiv:1811.01009v1 (first public 2018-11-02); Nonlinearity **34** (2021), 5744–5761.
2. Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836v2 (2024); especially §§1.1, 2.1–2.3, 3.4–3.5.
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261v1 (2024); Proceedings of the American Mathematical Society (2026).
4. H. Takahasi, *Large deviation principles for periodic points of the Dyck shift*, arXiv:2503.14164v1 (2025).
