# Shattering polynomials of ordinary spheres in finite ultrametric spaces

## Finding

Let \((X,d)\) be any nonempty finite ultrametric space, with \(N=|X|\), and let
\[
\mathcal S(X)=\bigl\{\{y\in X:d(c,y)=r\}:c\in X,\ r\ge0,\ \{y:d(c,y)=r\}\ne\varnothing\bigr\}.
\]
These are **ordinary exact-distance spheres**: for positive radius the center is **not** added to the sphere. A support \(A\subseteq X\) is shattered when \(\{A\cap S:S\in\mathcal S(X)\}=\mathcal P(A)\). The full shattered-support polynomial is
\[
\Phi_X(z)=\sum_{A\subseteq X:\ A\text{ shattered}}z^{|A|}.
\]

Represent \((X,d)\) by its canonical reduced rooted ball hierarchy \(T\): the leaves are points of \(X\), each internal node has at least two children (its maximal proper subballs), and the root represents \(X\). For an internal node \(v\), let \(n_1(v),\ldots,n_{k(v)}(v)\) count the leaves in its distinct child subtrees, and write
\[
E_3(v)=\sum_{1\le i<j<k\le k(v)}n_i(v)n_j(v)n_k(v).
\]
The empty sum is zero. For \(N=1\), \(\Phi_X(z)=1\). For **every** \(N\ge2\), put \(r\) for the root and let \(n_1(r),n_2(r)\) be its child sizes only when \(k(r)=2\). Then
\[
\boxed{\Phi_X(z)=1+Nz+s_2(X)z^2+s_3(X)z^3},
\]
where
\[
\boxed{s_2(X)=\binom N2-\mathbf1_{\{k(r)=2\}}n_1(r)n_2(r)}
\]
and
\[
\boxed{s_3(X)=\sum_{\substack{v\text{ internal}\\v\ne r}}E_3(v)+\mathbf1_{\{k(r)\ge4\}}E_3(r)}.
\]
All higher coefficients vanish. In particular, for \(N\ge3\),
\[
\boxed{\operatorname{VCdim}(\mathcal S(X))=3\iff
k(r)\ge4\ \text{or some nonroot internal node has at least three children}.}
\]
Otherwise the dimension equals \(2\) when \(N\ge3\); it equals \(1\) when \(N=2\), and \(0\) when \(N=1\).

For the complete \(b\)-ary tree of height \(h\ge1\), the coefficients are explicit. With \(N=b^h\), for \(b=2\),
\[
s_2(X)=2\binom{N/2}{2},\qquad s_3(X)=0.
\]
For \(b\ge3\),
\[
s_2(X)=\binom N2,\qquad
s_3(X)=\binom b3\sum_{t=0}^{h-1}b^{t+3(h-t-1)}-\mathbf1_{\{b=3\}}b^{3(h-1)}.
\]
Thus a ternary ultrametric of height one has VC dimension \(2\), while every full ternary hierarchy of height at least two has dimension \(3\). Branching at least four yields dimension \(3\) already at height one. All formulas depend only on hierarchy shape, not the numerical values of the distinct distance levels.

## Assumptions and scope

The metric is finite and strictly separates distinct points. Radius zero spheres are the singleton sets; positive-radius spheres exclude their center. We include every distinct **nonempty** ordinary sphere, with any radius that occurs among point distances. The empty concept is not artificially adjoined. The root, child leaf counts, and least common ancestors belong to the **reduced** ball hierarchy: no unary vertices are retained. Repeated numerical distances in different branches cause no ambiguity, since only ancestor-chain diameters must strictly decrease. The polynomial includes the empty shattered support (constant coefficient one). No statement is made about arbitrary non-ultrametric metric spaces, centered spheres \(\{c\}\cup\{y:d(c,y)=r\}\), or fixed-radius subfamilies.

## Proof

**1. Exact sphere normal form.** Every nonempty sphere of radius zero is a singleton. Fix a positive radius \(r\) realized from a center \(c\). There is a unique internal ancestor node \(v\) on the path above the leaf \(c\) whose cluster diameter equals \(r\). The ultrametric inequality implies that the points at distance \(r\) from \(c\) are precisely the leaves in the children of \(v\) *other than* the child containing \(c\). Conversely, choosing any leaf \(c\) in that omitted child and the diameter of \(v\) realizes exactly that sibling shell. Thus \(\mathcal S(X)\) consists of the singletons and all such nonempty sibling shells. This description also proves invariance under changes of numerical distance labels preserving the hierarchy.

**2. Empty and singleton supports.** The empty support is always shattered by any nonempty concept. If \(N\ge2\), each singleton support has both required traces, witnessed by its own radius-zero sphere and the radius-zero sphere at another point. If \(N=1\), the only nonempty sphere is \(X\), so its sole singleton support is not shattered.

**3. Two-point supports.** Let \(A=\{x,y\}\), with \(x\ne y\). The two singleton traces are realized by radius-zero spheres. If \(N\ge3\), an empty trace is realized by the radius-zero sphere at a third point; for \(N=2\), the missing full trace follows from the binary-root argument below. Set \(v=\operatorname{LCA}(x,y)\). A sphere containing both points exists precisely when either some center is outside the cluster of \(v\), or the node \(v\) has a third child in which to place a center. Indeed, a shell at or above \(v\) is the only positive-radius candidate; a center in one of the two occupied children excludes that child's selected point. If \(v\ne r\), a center outside \(v\) realizes \(A\); if \(k(v)\ge3\), a center in a third child realizes \(A\). The only failure therefore occurs when \(v=r\) and \(k(r)=2\), i.e. when the two points lie in opposite root children. In all other cases \(N\ge3\), all four traces exist. Exactly \(n_1(r)n_2(r)\) cross-root pairs fail when the root is binary. This proves \(s_2\), including \(N=2\).

**4. Three-point supports.** If \(d(x,y)<d(x,z)=d(y,z)\), any sphere containing \(x,z\) also contains \(y\): if its center is \(c\) and its radius is \(R\), then \(R\ge d(x,z)>d(x,y)\), so \(d(c,y)=R\) by the strong triangle inequality. Hence the trace \(\{x,z\}\) cannot occur; no non-equilateral triple is shattered. Conversely, let \(x,y,z\) be pairwise equidistant. They lie in three distinct children of their common least ancestor \(v\). Each singleton trace is a radius-zero sphere. Each doubleton trace is realized by the positive-radius sphere centered at the omitted point, with radius \(d(x,y)\). A sphere contains all three points precisely if its center lies outside \(v\)'s cluster, or in a fourth child of \(v\). If \(v\ne r\), a center outside \(v\) exists. If \(v=r\), a fourth child exists exactly when \(k(r)\ge4\). In either successful case, a radius-zero sphere at that outside point also realizes the empty trace. Therefore the stated condition is both necessary and sufficient. Every equilateral triple has a unique common least ancestor, and the number of such triples at \(v\) is \(E_3(v)\). Summing over all permitted nodes proves \(s_3\).

**5. Four-point obstruction.** If a four-point support were shattered, all its three-point sub-supports would be shattered. Step 4 would force every triple of the four points to be equilateral, hence all six pairwise distances to be equal. They therefore lie in four distinct children of the same node \(v\). A radius-zero sphere meets these points in at most one point. A positive-radius sphere can meet them in zero, one, three, or four points: at the common distance scale, the center occupies at most one of the four child clusters and its shell omits exactly that represented child; at lower or higher scales the trace is empty, a singleton, or the entire support. In particular no two-point trace exists, contradiction. Shattering is hereditary under taking subsets, so no support of size at least four is shattered.

**6. VC classification and homogeneous specialization.** For \(N\ge3\) a shattered pair exists: choose two leaves in a root's same child when the root is binary (such a child must contain at least two leaves), or any pair when it has at least three children. Step 4 shows that a shattered triple exists exactly under the stated internal-node branching condition. Steps 2–5 give the remaining cases. In a complete \(b\)-ary tree, each internal node at depth \(t\) has \(b\) children of leaf size \(b^{h-t-1}\), and there are \(b^t\) such nodes. Summing \(E_3\) across depths and omitting the root term only for \(b=3\) gives the displayed homogeneous formula. No computational extrapolation is used in this proof.

## Verification

A dependency-free Python checker `verify_ultrametric_spheres.py` independently constructs each ordinary sphere as an exact distance-level set on the leaves, enumerates all Boolean traces on supports of sizes up to four, and compares its counts with the hierarchy formulas. It covered all \(405\) nonisomorphic reduced rooted hierarchies with at most eight leaves, a total of \(53{,}403\) nonempty support checks. It additionally tested the explicit homogeneous formulas for branching factors \(2\) through \(5\) over selected heights, including direct trace tests when tractable. A successful replay prints `ULTRAMETRIC_SPHERE_TRACES_PASS` and the exact shape-count dictionary. The proof of the all-size theorem is in Steps 1–6, not inferred from these finite checks.

## Relationship to prior work

Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès study sample compression for **balls** in graph metrics and provide general VC motivation [1]. The present range family consists instead of exact-distance ultrametric **spheres**; their ball results do not yield its support-by-support enumeration. Dovgoshey and Kostikov study tree representations of ultrametrics [2]. Their use of **centered spheres** in the positive-radius definition includes the center; these differ from ordinary spheres, and their representation results do not state the present Boolean-trace classification or polynomial. Existing results about laminar ball families likewise do not imply the sibling-shell formula without analysis of missing center branches. The assertions of priority here are limited to the comparisons actually made; an equivalent result under sibling-shell, hierarchy, or complementary-clade terminology cannot be ruled out.

## Limitations

This result applies to finite ultrametrics and their complete family of ordinary nonempty spheres, including radius zero. It is not a theorem about centered spheres, arbitrary balls, one prescribed distance, non-ultrametric metrics, or infinite structures. Historical priority has not been independently established. The supplied finite verifier is a check of bounded cases and not an infinite formal certificate. No independent scientific audit has been performed.

## References

[1] J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel and Y. Vaxès, *Sample compression schemes for balls in graphs*, first posted 2022-06-27, arXiv:2206.13254v1, https://arxiv.org/abs/2206.13254.

[2] O. Dovgoshey and A. Kostikov, *Locally finite ultrametric spaces and labeled trees*, first posted 2023-08-12, arXiv:2308.06626v1, https://arxiv.org/abs/2308.06626.
