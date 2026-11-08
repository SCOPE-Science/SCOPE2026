# Coordinatewise quantile formula for simplex-translate depth

## Finding
Let \(S=\operatorname{conv}\{v_0,\ldots,v_d\}\) be any full-dimensional \(d\)-simplex, \(d\ge1\), and let \(\mu\) be **any** Borel probability measure with \(\mu(S)=1\). Write \(\lambda_i(y)\) for the affine barycentric coordinates of \(y\) relative to \(S\), so that \(\sum_{i=0}^d\lambda_i(y)=1\), and set \(F_i(t)=\mu\{z:\lambda_i(z)\le t\}\). For the translate-based depth of Molchanov and Nagy,
\[
\boxed{\mathsf d_S(y;\mu)=\min_{0\le i\le d}F_i(\lambda_i(y))\quad(y\in\mathbb R^d).}
\]
In particular, all positive-depth regions are either empty, singletons, or positively homothetic copies of \(S\). For \(0<\alpha\le1\), put \(q_i(\alpha)=\inf\{t:F_i(t)\ge\alpha\}\). Then
\[
\boxed{D_\alpha^S(\mu)=\{y:\lambda_i(y)\ge q_i(\alpha)\ \forall i\},\qquad D_\alpha^S(\mu)\ne\varnothing\iff\sum_iq_i(\alpha)\le1.}
\]
The latter equivalence includes atomic measures and boundary-supported measures, with no genericity or density condition.

For \(n\ge1\) equally weighted observations in \(S\), let \(a_{i,(k)}\) be the \(k\)-th smallest value of their \(i\)-th barycentric coordinate (counting ties). The exact maximum empirical depth is
\[
\boxed{\alpha_n^*=\frac{k_*}{n},\qquad k_*=\max\{1\le k\le n:\sum_{i=0}^d a_{i,(k)}\le1\}.}
\]
Every empirical depth region, including the entire median region, is obtained from these order statistics. Once barycentric coordinates are supplied, the complete table and a deepest point are computable by sorting in \(O(nd\log n)\) comparisons and \(O(nd)\) storage. This is an exact algorithm, not a numerical approximation.

For the uniform probability measure on \(S\), the depth and its unique maximum simplify to
\[
\mathsf d_S(y;\mu)=\begin{cases}1-(1-\min_i\lambda_i(y))^d,&y\in S,\\0,&y\notin S,\end{cases}
\qquad\boxed{\alpha^*=1-\left(\frac d{d+1}\right)^d.}
\]
The unique deepest point is the barycenter. The center value tends to \(1-e^{-1}\) with increasing dimension. The general centerpoint lower bound \(1/(d+1)\) is attainable even for measures supported in the very testing simplex: take equal atoms at the centers of its \(d+1\) opposite facets. This last constant was previously available by general theory; only the explicit reduction and full depth classification are the proposed contribution.

## Assumptions and scope
The testing body is **the simplex \(S\) itself**, and the measure is supported in that same \(S\). No absolute continuity, symmetry, moment, interior-support or positive-density hypothesis is imposed. Affine barycentric coordinates are defined on all of \(\mathbb R^d\), so the pointwise formula includes query points outside \(S\). The quantile convention is the left generalized inverse of the right-continuous distribution function. All asserted depth regions have \(\alpha>0\); the formal \(\alpha=0\) region is \(\mathbb R^d\), not a simplex.

## Proof
**1. Translation thresholds.** Since \(S=\{z:\lambda_i(z)\ge0\text{ for every }i\}\), for any translation vector \(t\),
\[
 S+t=\{z:\lambda_i(z)\ge b_i\text{ for every }i\},\qquad b_i=\lambda_i(t)-\lambda_i(0),\quad\sum_i b_i=0.
\]
Conversely, every real vector \((b_0,\ldots,b_d)\) with zero sum comes from exactly one translation vector \(t\), since the linear parts of any \(d\) independent barycentric coordinates form a basis of the dual space.

**2. Upper bound for translated mass.** The defining exclusion \(y\notin S+t\) says \(b_j>\lambda_j(y)\) for at least one \(j\). Every point \(z\in S\cap(S+t)\) has \(\lambda_j(z)\ge b_j>\lambda_j(y)\). Therefore
\[
\mu(S+t)\le\max_j\mu\{z:\lambda_j(z)>\lambda_j(y)\}.
\]

**3. Matching lower bound, including atoms.** Fix \(j\), writing \(r=\lambda_j(y)\). If \(r<0\), the original simplex \(S\) itself omits \(y\) and has full mass; the right-hand cap also has mass one. If \(r\ge1\), the cap \(\{\lambda_j>r\}\) has zero mass. For \(0\le r<1\), choose \(0<\varepsilon<1-r\), put \(b_j=r+\varepsilon\) and \(b_i=-(r+\varepsilon)/d\) for \(i\ne j\). All remaining thresholds are nonpositive. Within the support \(S\), this translated simplex is **exactly** the cap \(\{z\in S:\lambda_j(z)\ge r+\varepsilon\}\), and it excludes \(y\). As \(\varepsilon\downarrow0\), the cap masses increase to \(\mu\{\lambda_j>r\}\) by continuity of measure from below. Supremizing over all excluded translates gives the exact equality
\[
 M_S(y;\mu)=\max_j\mu\{\lambda_j>\lambda_j(y)\}.
\]
Subtracting from one proves the pointwise formula, since \(1-\max_j(1-F_j)=\min_jF_j\). No boundary-null assumption is needed; the strict greater-than sign is necessary for atoms.

**4. Quantile geometry and empirical algorithm.** Every \(F_i\) is nondecreasing and right-continuous, hence \(F_i(t)\ge\alpha\iff t\ge q_i(\alpha)\) for \(0<\alpha\le1\). Barycentric coordinates sum to one, so the intersection of these \(d+1\) halfspaces is nonempty precisely when the lower thresholds sum to at most one. When the sum is \(s<1\), set \(\lambda_i(y)=q_i+(1-s)u_i\), where \(u_i\ge0\) and \(\sum_i u_i=1\); this is a positive homothet of \(S\). At \(s=1\) it is a singleton. For an empirical measure the quantiles at \(\alpha=k/n\) are exactly the sorted observations \(a_{i,(k)}\). The maximal depth lies on this finite grid and the displayed formula for \(k_*\) follows. Sorting the \(d+1\) coordinate lists yields the claimed complexity; a deepest point is constructed by assigning the remaining barycentric mass \(1-\sum_i a_{i,(k_*)}\) to any one coordinate.

**5. Uniform and sharpness cases.** For \(Z\) uniform on \(S\), the cap \(\{\lambda_i(Z)>t\}\) is a homothetic simplex of linear ratio \(1-t\), hence has mass \((1-t)^d\) for \(0\le t\le1\). Thus \(F_i(t)=1-(1-t)^d\), giving the displayed depth and quantiles. A positive-depth region becomes a singleton exactly when every barycentric coordinate equals \(1/(d+1)\), yielding the unique uniform median and its value. If \(\mu\) is uniform on the \(d+1\) facet centers (where one barycentric coordinate is zero and the others are \(1/d\)), then at levels exceeding \(1/(d+1)\) all \(d+1\) quantile thresholds equal \(1/d\) and their sum exceeds one; at the level \(1/(d+1)\) they are all zero. Thus its maximum is exactly \(1/(d+1)\).

## Verification
The standalone Python script `verify.py` uses exact rational arithmetic. It checked 15,707 assertions in dimensions one through four (in affine dimension), including every subset of small discrete samples for exact translate-exclusion feasibility, independently computed empirical depth values, the order-statistic depth regions, deepest-point construction, uniform-simplex identities and facet-center sharpness. Running `python verify.py` prints `EXACT_OK 15707`. These finite checks are supporting reproducibility tests; the proof above establishes the theorem for all dimensions, all measures and all query points.

## Relationship to prior work
Molchanov and Nagy (2026, arXiv:2610.26108) introduced and studied general translate-based depth. Their Proposition 2.2 expresses depth regions as Minkowski erosions, their Theorem 2.7 gives a translative-Helly centerpoint bound, Section 6.3 treats covariograms and a one-dimensional uniform example, and Section 7.1 gives a general empirical representation. The present result **does not** claim any of those general frameworks as new. It gives an all-measure, all-dimensional exact marginal-CDF formula under simplex support, the homothetic region/quantile classification including atoms, and an explicit sorted-order median algorithm. It is not just a bound, and it does not follow from a numerical evaluation of the existing centerpoint constant.

Schütt, Werner and Yalikun (2025, arXiv:2504.15488) introduced \(C\)-ball floating bodies and their covariogram representation, focusing on relative affine surface-area theory; their definitions are relevant antecedents but do not supply the displayed simplex/marginal formula. Small (1987) studied general set-family centrality indices; only its abstract was accessible in this comparison, so its possible specialized examples remain a historical-priority risk. Earlier work on ordinary simplicial depth concerns a different random-simplex probability and is not identical to translates of a fixed simplex.

## Limitations
The joint-support assumption \(\mu(S)=1\) is indispensable to the cap construction; the formula is not asserted for general external mass. The complexity bound assumes barycentric input and does not include preprocessing the simplex or converting Cartesian coordinates. The uniform-density corollary is not a claim of a new universal centerpoint inequality. Independent verification and a definitive historical-priority determination have not been performed.

## References
1. I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108 (first public version 2026-10-19), https://arxiv.org/abs/2610.26108 .
2. C. Schütt, E. M. Werner and D. Yalikun, *Floating bodies for ball-convex bodies*, arXiv:2504.15488 (first public version 2025-04-21), https://arxiv.org/abs/2504.15488 .
3. C. G. Small, *Measures of centrality for multivariate and directional distributions*, Canadian Journal of Statistics 15 (1987), 31–39, doi:10.2307/3314859 .
4. S. Nagy, *Simplicial depth and its median: Selected properties and limitations*, Statistical Analysis and Data Mining 16 (2023), 374–390, doi:10.1002/sam.11605 (distinct depth notion).
