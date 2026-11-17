# Stochastic majorization of geodesic distances on metric flowers

## Finding

Let \(m\ge2\), \(\ell_i>0\) and \(\sum_i\ell_i=L\). For the compact metric graph formed by identifying one common point on each of the \(m\) circles of circumference \(\ell_i\), take independent uniformly arclength-distributed points \(X,Y\), and put \(D_{\boldsymbol\ell}=d(X,Y)\). If the length vector \(\boldsymbol\ell\) majorizes another positive length vector \(\boldsymbol r\) of the same sum, then

\[\Pr(D_{\boldsymbol\ell}>t)\ge\Pr(D_{\boldsymbol r}>t)\quad\text{for every }t\ge0.\]

For distinct length multisets the distributions differ, with strict inequality on a nonempty interval. Hence, at fixed \(m\) and \(L\), the equilateral flower is the unique first-order stochastically minimal flower: it minimizes every increasing function of the random geodesic distance for which the expectation exists. This is a distributional strengthening of the known mean-distance extremum; no new claim about the mean extremum itself is made.

## Assumptions and scope

All petals are genuine positive-length circles; vertices are identified only at one common junction. Distances are intrinsic shortest-path distances rather than Euclidean distances in an embedding. Points are sampled from normalized one-dimensional Hausdorff (arclength) measure. The vector majorization convention is that \(\boldsymbol\ell\succcurlyeq\boldsymbol r\) means, after decreasing rearrangement, \(\sum_{i=1}^k\ell_{[i]}\ge\sum_{i=1}^k r_{[i]}\) for every \(1\le k<m\), with equal total sums. Put \(u_+=\max(u,0)\).

## Proof

**Step 1: exact tail kernels.** On one petal of circumference \(a\), the shortest distance of two independent uniform points is uniform on \([0,a/2]\). The ordered-pair arclength measure of pairs at distance greater than \(t\) is therefore \(J_c(a)=a(a-c)_+\), with \(c=2t\). On two distinct petals of circumferences \(a,b\), distances to their common junction independently have uniform distributions on \([0,a/2]\), \([0,b/2]\). Their sum is the cross-petal geodesic distance. Consequently its ordered-pair arclength tail measure (for one ordering) equals \(K_c(a,b)=4\int_0^{a/2}\int_0^{b/2}\mathbf1_{u+v>c/2}\,dv\,du\). Integration over the clipped rectangle gives

\[K_c(a,b)=ab-\frac12\left[c^2-(c-a)_+^2-(c-b)_+^2+(c-a-b)_+^2\right].\]

Accounting for both orders of distinct petals, the complete normalized tail is

\[L^2\Pr(D_{\boldsymbol\ell}>c/2)=\sum_{i=1}^{m}J_c(\ell_i)+2\sum_{1\le i<j\le m}K_c(\ell_i,\ell_j).\tag{1}\]

At a finite threshold, every function here is continuous and piecewise polynomial in the lengths.

**Step 2: derivative under unequalizing two lengths.** Fix \(c>0\), choose two distinct coordinates \(a>b>0\), and increase \(a\) by \(s\) while decreasing \(b\) by the same amount, keeping every other length constant. At differentiability points of the hinge functions, the contribution to the directional derivative from these two petals and their mutual cross-petal pairs is

\[\frac{d}{ds}[J_c(a+s)+J_c(b-s)+2K_c(a+s,b-s)]_{s=0}=c\,\mathbf1_{\{b<c<a\}}.\tag{2}\]

This follows by the three cases \(c\le b\), \(b<c<a\), \(a\le c\), using \(J_c'(x)=(2x-c)\mathbf1_{x>c}\) and the expression for \(K_c\). For a third petal of length \(d>0\), the partial derivative of its cross term with an endpoint petal of length \(x\) is

\[\partial_x K_c(x,d)=d-(c-x)_+ +(c-x-d)_+.\tag{3}\]

The right side is nondecreasing in \(x\): its slope is either zero or one at all regular points. Thus \(\partial_xK_c(a,d)\ge\partial_xK_c(b,d)\), and the cross terms involving third petals contribute a nonnegative amount to the transfer derivative. All other terms are constant. At a threshold coinciding with a hinge, the conclusion extends by continuity and absolute continuity along every transfer segment. Therefore unequalizing a pair cannot decrease the tail at any \(t\).

**Step 3: majorization and strictness.** The elementary finite-dimensional transfer characterization of majorization expresses \(\boldsymbol r\) as a finite sequence of averaging (Robin Hood) transfers from \(\boldsymbol\ell\), up to permutations. Reversing the transfers and applying Step 2 yields the asserted tail comparison for every threshold. If a reverse transfer is nontrivial, take any \(c\) strictly between the two lengths at a point of positive separation along its transfer. Equation (2) is then strictly positive, and so the comparison is strict at this \(c\); continuity gives a nonempty open threshold interval. Since strict inequalities persist when composing nonnegative comparisons, distinct multisets yield distinct distributions. Every fixed-sum positive length vector majorizes the equal vector, proving unique stochastic minimization.

**Step 4: boundaries and a caution about strictness.** If \(0\le t<\frac12\min_i\ell_i\), all hinges in (1) simplify to

\[\Pr(D_{\boldsymbol\ell}>t)=1-\frac{2t}{L}-\frac{2m(m-1)t^2}{L^2}.\]

The shape-independent initial tail shows why strict inequality at *each* positive threshold would be false. For \(t\ge L/2\), all tails vanish. The theorem includes repeated lengths, arbitrarily skewed positive length vectors, and thresholds at every piecewise-polynomial breakpoint.

## Verification

The separate exact-arithmetic program `verify.py` checks 21,420 rational majorization-threshold comparisons from independent random unequalizing transfers for \(2\le m\le8\), plus direct two-dimensional Riemann integration of the shortest-path distance predicate for three two-loop cases and an explicit strictness witness. Successful marker: `METRIC_FLOWER_STOCHASTIC_SCHUR_OK 21420`. These computations corroborate the identities but are not used to infer the inequalities at untested real values. Equations (1)–(3) and the majorization transfer argument constitute the proof for arbitrary real positive lengths and all thresholds.

## Relationship to prior work

Doyle and Graver (1982) introduced mean-distance calculations for geometric shapes and networks. Baptista, Kennedy and Mugnolo (first public preprint 2023) establish the equilateral flower as the unique **mean**-distance minimizer, and their full accessible article (Example 4.3, Lemma 4.4 and its proof) supplies the first-moment formula and pairwise averaging argument. The present theorem is not the first-moment result: it orders **every** survival threshold, which does not follow from a mean comparison. Earlier published results on inverse global distance distributions of graphs and moment comparisons likewise do not establish first-order stochastic majorization under all length transfers. The exact joint tail formula and its nonnegative derivative at every threshold are the additional mechanism.

## Limitations

The ordering is established only within the topology of bouquets of finitely many positive circles, with independent arclength-uniform endpoints and common total length; it is not asserted for arbitrary metric graphs or for nonuniform endpoint distributions. The law is not strictly ordered at all positive thresholds. Full text of Doyle–Graver's longer 1982 paper was not accessible for a complete historical-priority check; possible unindexed or indirect stronger results remain a risk. This research has not been independently audited.

## References

1. J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B 9 (1982), 177–179. Publisher reports June 1982 (specific day not verified). DOI: 10.1068/b090177.
2. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471. DOI: 10.1002/jgt.3190060410.
3. F. Chazal and J. Sun, *Gromov-Hausdorff Approximation of Metric Spaces with Linear Structure*, arXiv:1305.1172 (first submitted May 6, 2013), on reconstructing sampled metric graphs.\n4. L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952 (first posted December 8, 2023); Journal of Geometric Analysis 34 (2024), article 137. DOI: 10.1007/s12220-024-01574-0. Section 4, especially Example 4.3 and Lemma 4.4.
