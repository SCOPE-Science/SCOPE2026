# All-dimensional shattering census for discrete axis-parallel boxes

## Finding

Let \(d\geq1\), let \(n_1,\ldots,n_d\) be positive integers, and put
\[
G=\prod_{i=1}^d\{1,\ldots,n_i\},\qquad N=\prod_{i=1}^d n_i.
\]
The concept family \(\mathcal B(G)\) contains **every nonempty Cartesian box** \(\prod_i\{a_i,\ldots,b_i\}\), where \(1\leq a_i\leq b_i\leq n_i\). In particular, singleton boxes are permitted; the empty concept is *not* added.

Let \(s_m(G)\) count the unordered \(m\)-element subsets of \(G\) shattered by this family and let \(\Phi_G(z)=\sum_{m\geq0}s_m(G)z^m\). Define
\[
B=\#\{i:n_i=2\},\qquad T=\#\{i:n_i\geq3\},\qquad K=B+2T.
\]
Then \(\operatorname{VCdim}(\mathcal B(G))=K\). The complete polynomial has \(s_0=1\), \(s_1=N\) if \(K\geq1\) (otherwise \(s_1=0\)), \(s_2=\binom N2\) if \(K\geq2\) (otherwise \(s_2=0\)), and the following explicit coefficients for every \(3\leq m\leq K\).

For integers \(m\geq3\) and \(n\geq1\), set
\[
L_m(n)=\sum_{t=0}^{n-1}t^{m-1},\qquad
E_m(n)=\sum_{t=0}^{n-2}(n-t-1)t^{m-2},
\]
where an empty sum is zero. Then
\[
\boxed{\displaystyle
s_m(G)=\frac1{m!}\sum_{j=0}^m(-1)^j\binom mj
\prod_{i=1}^d\Bigl(n_i^m-2jL_m(n_i)+j(j-1)E_m(n_i)\Bigr).}
\]
All coefficients above degree \(K\) vanish. When \(K\geq3\), the maximum-degree coefficient factors:
\[
\boxed{\displaystyle s_K(G)=2^B\prod_{i:n_i\geq3}E_K(n_i).}
\]
Thus the exact probability that a uniform unordered \(m\)-point support is shattered is \(s_m(G)/\binom Nm\) whenever \(0\leq m\leq N\).

Illustrations, with the variables recording support size, are
\[
\Phi_{\{1,2,3\}^2}(z)=1+9z+36z^2+16z^3+z^4,
\]
\[
\Phi_{\{1,2\}^4}(z)=1+16z+120z^2+160z^3+16z^4,
\]
and
\[
\Phi_{\{1,2,3\}^3}(z)=1+27z+351z^2+1184z^3+821z^4+90z^5+z^6.
\]
The first two finite grids have equal VC dimension but different coefficientwise shattering profiles. The two-dimensional coefficients were already available through a path-grid convexity calculation; the new contribution is the arbitrary-dimensional coefficient formula, including all degrees up to \(K\), and its factored highest-degree count.

## Assumptions and scope

All coordinates are totally ordered finite chains; boxes are **non-wrapping**, **closed** and **nonempty**, with degenerate singleton factors allowed. No general-position assumption is imposed: ties in individual coordinates are permitted. Distinctness refers to full vectors. The statement includes singleton grids and arbitrarily unequal factor sizes. The shattering polynomial enumerates supports in the entire finite domain, not the worst-case trace growth of a fixed sample.

## Proof

**1. Private-extreme criterion.** For a support \(S\subseteq G\) containing at least three distinct points, call \(x\in S\) *privately extreme* if for some coordinate \(i\), either \(x_i<y_i\) for every \(y\in S\setminus\{x\}\), or \(x_i>y_i\) for every such \(y\). We prove:
\[
S\text{ is shattered}\quad\Longleftrightarrow\quad
\text{every }x\in S\text{ is privately extreme.}
\]
For necessity, shattering realizes the labeling that includes every point except \(x\). Any box containing \(S\setminus\{x\}\) must contain the coordinatewise bounding box of those points. Therefore the excluded \(x\) must lie strictly below its minimum or above its maximum in some coordinate.

For sufficiency, take any nonempty \(U\subseteq S\) and its smallest coordinatewise bounding box. If it contained an excluded point \(x\in S\setminus U\), then \(x\) would lie in the bounding box of \(S\setminus\{x\}\), contradicting its private extremum. This box therefore realizes precisely \(U\). To realize the empty labeling, observe that coordinate \(i\) supplies at most one privately minimal point and at most one privately maximal point, and supplies **at most one** privately extreme point when \(n_i=2\) and \(|S|\geq3\). Consequently \(|S|\leq K\). Moreover \(n_i\geq1+b_i\), where \(b_i=0,1,2\) according as \(n_i=1,2,\geq3\), whence
\[
N\geq\prod_i(1+b_i)\geq1+\sum_i b_i=1+K>|S|.
\]
There is a grid point outside \(S\); its singleton box realizes the empty labeling. This proves the equivalence, including all tied-coordinate cases.

**2. Local inclusion–exclusion.** Fix \(m\geq3\) labels and one coordinate chain of length \(n\). A specified label is a unique strict minimum in exactly \(L_m(n)\) ordered coordinate assignments and a unique strict maximum in exactly \(L_m(n)\) assignments. Two different specified labels are both privately extreme only when one is the unique minimum and the other is the unique maximum. For each orientation there are
\[
\sum_{1\leq a<b\leq n}(b-a-1)^{m-2}=E_m(n)
\]
assignments. Three different labels cannot all be privately extreme in one coordinate. Inclusion–exclusion over \(j\) specified labels thus gives exactly
\[
Q_m(n,j)=n^m-2jL_m(n)+j(j-1)E_m(n)
\]
assignments for which none of those \(j\) labels is privately extreme in that coordinate.

Across independent coordinates, the number of ordered \(m\)-tuples in which a specified group of \(j\) labels has **no private extremum anywhere** is \(\prod_iQ_m(n_i,j)\). A second inclusion–exclusion over the labels left uncovered gives the displayed numerator. Every surviving tuple necessarily has distinct full vectors, since coincident labels cannot possess private extremes. Division by \(m!\) therefore counts unordered shattered supports exactly.

**3. Degree and top coefficient.** At most \(K\) points can be privately extreme, so \(s_m=0\) for \(m>K\). To attain \(K\), assign a different support point to each coordinate's available extreme role: one privately minimal role for each binary coordinate, two (minimum and maximum) for each coordinate of length at least three. In a binary coordinate, give the designated point value \(1\) and the others value \(2\). In a longer coordinate, give designated minimum and maximum values \(1\) and \(n_i\), and give the other points value \(2\). For \(K\geq3\), this constructs \(K\) distinct privately extreme points. For \(K=1,2\), the same VC-dimension assertion follows from the singleton and pair cases below. Thus \(\operatorname{VCdim}=K\).

When \(K\geq3\), every maximum shattered support uses **all** extreme roles, with exactly one role per point. For a specified role in a binary coordinate there are precisely two possible coordinate columns (one isolated low value or one isolated high value). In a longer coordinate with specified distinct minimum and maximum roles, there are exactly \(E_K(n_i)\) columns. Assigning the \(K\) labeled points bijectively to the \(K\) roles and then forgetting labels cancels the \(K!\) bijections, yielding \(s_K=2^B\prod_{n_i\geq3}E_K(n_i)\).

**4. Empty, singleton and pair supports.** The empty support is always shattered by a nonempty concept family. A one-point support can be labeled both ways precisely when \(N\geq2\), since a singleton containing that point and a distinct singleton suffice. Every pair of distinct grid points can be captured together by its bounding box and individually by the corresponding singleton boxes; its empty labeling is realizable exactly when \(N\geq3\), by a singleton at a third grid point. If \(K\geq2\), then \(N\geq1+K\geq3\). If \(K<2\), no shattered pair is possible. These observations prove the stated low-degree terms and all boundary cases.

## Verification

The standalone file `verify_finite_boxes.py` builds nonempty interval products independently of the private-extreme proof, computes their traces on supports, and compares exhaustive counts with the formulas on 14 finite grids (48,917 nonempty support tests). Additional deterministic sampled trace tests on three larger grids cover 28,500 supports. The replayed output is recorded in `verification_output.txt` and ends with `ALL_FINITE_BOX_SHATTERING_CHECKS_PASS`. These finite tests are corroboration, not a substitute for the all-parameter proof above.

## Relationship to prior work

An earlier two-dimensional Cartesian path-grid convexity calculation already gives the entire shattering polynomial for two finite chain factors, including the empty concept. On grids with at least three points its coefficients agree with the present two-factor case; on grids with one or two points, adding the empty hypothesis changes low-degree behavior. No planar enumeration is claimed as new. The arbitrary-dimensional formula, its higher-degree terms, the binary/long-coordinate threshold, and the top-degree product are not consequences of the stated planar formula alone. The classical VC dimensions \(d\) for anchored boxes and \(2d\) for non-anchored continuous axis-parallel boxes are discussed in Gillibert–Lachmann–Müllner (2020, Introduction). That article primarily studies *periodic* boxes on a torus and derives a different, order-\(d\log d\), dimension law; its objects allow wrapping, and its statements do not enumerate shattered supports of finite non-wrapping grids. Classical proofs using extreme coordinates determine the maximum size of a shattered support, not the complete coefficientwise census in the presence of tied coordinates, binary factors and unequal chain sizes. The present formula uses a two-sided local inclusion–exclusion with a nonzero paired-extremum term; a one-sided anchored-orthant formula does not by itself count the supports in this larger concept family.

Moran–Rashtchian (2015) develop Hilbert-function bounds using shattered and strongly shattered sets in abstract Boolean set systems; those general bounds also do not imply the coordinatewise exact counts claimed here. Searches of accessible mathematical records did not identify a dominating arbitrary-dimensional full-grid coefficient formula; the related two-dimensional result is explicitly recognized above. This is a best-knowledge originality assessment, not a proof of historical priority.

## Limitations

The result concerns a finite domain with **all** nonempty non-wrapping boxes and arbitrarily selectable integer endpoints. It does not cover periodic or toroidal boxes, fixed-volume boxes, cubes constrained to equal side lengths, or continuous sampling distributions. Search-based priority assessment remains incomplete; synonymous formulations under product-order or discrete computational-geometry terminology may exist. No independent scientific audit has yet been performed.

## References

1. P. Gillibert, T. Lachmann and C. Müllner, “The VC-Dimension of Axis-Parallel Boxes on the Torus,” first arXiv version posted 2020-04-28, arXiv:2004.13861, https://arxiv.org/abs/2004.13861.
2. S. Moran and C. Rashtchian, “Shattered Sets and the Hilbert Function,” arXiv:1511.08245, first posted 2015-11-25; MFCS 2016, https://arxiv.org/abs/1511.08245.
3. Extremal Combinatorics, Section 1.3 “VC-Dimension,” examples for intervals and axis-aligned rectangles, https://extremalcombinatorics.com/notes/sec_VC.html.
