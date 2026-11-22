# Sharp sublinear contact faces of skew Hochschild cubes

## Finding

Let \(n\ge2\) be an integer and let \(\Delta_S=\operatorname{conv}\{e_i:i\in S\}\). The standard Euclidean realization of the \((0,n)\)-Hochschild polytope of Pilaud and Poliakova is
\[
P_n=\mathbf1+Q_n,\qquad Q_n=\sum_{j=1}^{n-1}(n-j)\Delta_{\{j,j+1,\ldots,n\}}.
\]
Set
\[
T=\frac{n(n-1)}2,\qquad a_i=\binom{n-i}{2}\quad(1\le i\le n).
\]
There is exactly one integer \(k\in\{2,\ldots,n\}\) satisfying
\[
k(k-1)(k-2)<3T\le k(k^2-1).
\]
Define
\[
\lambda=\frac{T+\binom k3}{k},\qquad c_i=(\lambda-a_i)_+,
\quad b=\#\{i:a_i\le\lambda\}.
\]
The **unique** minimum enclosing Euclidean ball of \(P_n\) has center \(\mathbf1+c\), squared radius
\[
R_n^2=T^2+\sum_{j=0}^{k-1}\binom j2^2-k\lambda^2
=T^2+\frac{k(k-1)(k-2)(3k^2-6k+1)}{60}-k\lambda^2,
\]
and exactly \(2^{b-1}\) contacting vertices. Those contacts are precisely the composition vertices whose positive coordinates, after translating by \(-\mathbf1\), are confined to indices satisfying \(a_i\le\lambda\). They form the vertex set of an exposed \((b-1)\)-dimensional cubical face. Thus the number of contacts is exponentially smaller than the total \(2^{n-1}\) vertices: as \(n\to\infty\),
\[
b\sim k\sim (3/2)^{1/3}n^{2/3},\qquad
\log_2(\#\text{contacts})\sim(3/2)^{1/3}n^{2/3}.
\]
The possible endpoint tie \(a_i=\lambda\) is included in the definition of \(b\); it must not be dropped from the contact count.

## Assumptions and scope

All spaces carry the standard ambient Euclidean norm; translation by \(\mathbf1\) preserves all radii. The result concerns the specified \((0,n)\)-Hochschild realization, not an arbitrary affine image or the differently realized \((1,n)\)-Hochschild polytope. Each simplex summand is the convex hull of standard coordinate vectors with its displayed positive weight. The assertions hold for every integer \(n\ge2\), including ties in the active-set inequality. The dimension of \(P_n\) is \(n-1\), since it lies in the hyperplane with coordinate sum \(n+T\).

## Proof

**1. Composition vertices and a common quadratic sphere.** Write \(w_j=n-j\). A generic linear functional maximized on the nested suffix-simplices chooses, for each \(j\), its highest-valued coordinate in \(\{j,\ldots,n\}\). As \(j\) runs down through the indices, the winning coordinate changes only at a chosen set of cuts. Every cut set can be realized by a strict total ordering of the objective coordinates. Hence the vertices of \(Q_n\) are in bijection with the \(2^{n-1}\) compositions of \(\{1,\ldots,n\}\). For blocks \([r_{t-1}+1,r_t]\), with \(r_0=0\), the corresponding vertex \(v\) places mass \(\sum_{j=r_{t-1}+1}^{r_t}w_j\) at position \(r_t\), and zero elsewhere.

Every such vertex obeys the identity
\[
\|v\|^2+2a\mathbin{\cdot}v=T^2.
\]
Indeed, the all-singleton composition gives the identity by expanding \((\sum_jw_j)^2\). Merging adjacent blocks with masses \(A,B\) ending at \(s<t\) changes the square norm by \(2AB\) and the linear term by \(2A(a_t-a_s)=-2AB\), because \(a_s-a_t=B\). All compositions follow by merges. Thus all vertices are cospherical about \(-a\), although this preliminary sphere need not be minimal.

**2. Project the preliminary sphere center onto the weight simplex.** All points of \(Q_n\) lie in
\[
S_T=\{x\in\mathbb R^n:x_i\ge0,\ \sum_i x_i=T\}.
\]
The unique Euclidean projection of \(-a\) to \(S_T\) is \(c_i=(\lambda-a_i)_+\), where \(\lambda\) solves \(\sum_i(\lambda-a_i)_+=T\). Since the \(a_i\) are the consecutive values \(\binom{n-i}{2}\), the positive part consists of the last \(k\) coordinates. The two adjacent breakpoint conditions are exactly
\[
\binom{k-1}2<\lambda\le\binom k2,
\]
which reduce to the stated strict-left, weak-right inequality for \(k\); the strictly increasing piecewise-linear water-filling equation shows that this \(k\) is unique. Summing the last \(k\) values of \(a_i\) gives \(\binom k3\), hence the formula for \(\lambda\).

**3. The projected center belongs to the actual polytope.** The nondecreasing sequence \(c_1\le\cdots\le c_n\) has total sum \(T\). Consequently its first \(j\) coordinates have sum at most \(jT/n\), which is no greater than \(\sum_{h=1}^jw_h\) for every \(j<n\). These are sufficient and necessary feasibility conditions for distributing supply \(w_h\) from source \(h\) to destinations \(i\ge h\): for any subset of destinations, all incoming sources belong to the prefix ending at its greatest index, so the prefix bounds imply the max-flow/min-cut (Hall) inequalities. The resulting allocation expresses \(c\) as a sum of points in the weighted suffix simplices. Thus \(c\in Q_n\).

**4. A global minimum-sphere certificate.** The simplex-projection variational inequality gives
\[
(c+a)\mathbin{\cdot}(v-c)\ge0\qquad(v\in Q_n).
\]
For a vertex \(v\), the quadratic identity in step 1 implies
\[
\|v-c\|^2
=T^2+\|a\|^2-\|c+a\|^2-2(c+a)\mathbin{\cdot}(v-c)
\le T^2+\|a\|^2-\|c+a\|^2=:R_n^2.
\]
As \(c\in Q_n\), the exposed face \(\{v\in Q_n:(c+a)\cdot(v-c)=0\}\) contains \(c\). The vertices of that face all attain equality and their convex hull contains \(c\). For their convex weights \(\theta_v\), any proposed center \(z\) satisfies the exact identity
\[
\sum_v\theta_v\|v-z\|^2=R_n^2+\|z-c\|^2.
\]
Therefore no sphere centered away from \(c\) has squared radius at most \(R_n^2\); \(c\) is the unique minimum center. Taking the last \(k\) active \(a_i\) gives the displayed formula for \(R_n^2\); the finite sum of squared binomial coefficients has the displayed polynomial closed form.

**5. The exact contact face and asymptotics.** The projection identity yields \(c_i+a_i=\lambda\) where \(a_i<\lambda\), and \(c_i+a_i=a_i\) where \(a_i\ge\lambda\). Hence equality in the radius bound holds precisely when a vertex puts no positive mass at a coordinate with \(a_i>\lambda\). The eligible coordinates are a terminal string of length \(b\), and all earlier block-cut endpoints are forbidden. Cuts are free at precisely the last \(b-1\) positions, giving \(2^{b-1}\) contacts. For each eligible \(i<n\), the composition vertex with one cut at \(i\) differs from the no-cut vertex by \(\bigl(\sum_{j=1}^i w_j\bigr)(e_i-e_n)\); these \(b-1\) difference vectors are linearly independent. The exposed face therefore has dimension \(b-1\), and because \(Q_n\) is a combinatorial cube it is itself a cubical face. At most one extra coordinate can satisfy \(a_i=\lambda\), so \(k\le b\le k+1\). Finally the breakpoint inequality gives \(k^3\sim3T\sim(3/2)n^2\), proving the asymptotic statements.

## Verification

The standalone `hoch_circumsphere_check.py` uses exact rational arithmetic. It enumerates every composition vertex for all dimensions \(2\le n\le12\), checks the quadratic identity and squared-distance inequality for every vertex, counts all contacts, checks the unique active-size inequality, and verifies the center's simplex and prefix feasibility inequalities. Reproduce with `python3 hoch_circumsphere_check.py`. The expected final line is `HOCHSCHILD_SKEW_CIRCUMSPHERE_EXACT_PASS`. The exhaustive finite calculation is **not** used as an infinite-dimensional proof; the five analytic steps above establish the theorem for all integers \(n\ge2\).

## Relationship to prior work

Pilaud and Poliakova construct the \((m,n)\)-Hochschild polytopes, give their vertices and Minkowski-simplex coefficients (Definition 54, Proposition 57 and Remark 61), and identify the \(m=0\) case as a skew cube (Remark 62 and Example 63). Those are inputs, not new claims. The present result adds the standard Euclidean minimum enclosing sphere, its uniqueness certificate, exact contact face and its sublinear exponent. Published geometric results for the \(m=1\) and \(m\ge2\) Hochschild realizations address **inradii**, not this outer-sphere problem. General exact minimum-sphere results for weighted terminal simplices and two-part composition polytopes concern distinct objects; neither statement gives the all-composition nested-suffix family and its \(n^{2/3}\) contact law.

## Limitations

This result is for the particular coordinate realization in the definition, not a metric invariant of all skew cubes up to affine equivalence. The exact contact count includes possible breakpoint ties and does not require classifying when arithmetic ties occur. No exact minimum-volume enclosing ellipsoid or general \((m,n)\) with \(m>0\) is claimed. Historical priority remains provisional: public indexing may miss equivalent results, and some related records were available only through summaries. Independent validation has not been performed.

## References

- V. Pilaud and D. Poliakova, *Hochschild polytopes*, arXiv:2307.05940, first publicly posted 2023-07-12, relevant Definition 54, Proposition 57, Remarks 61–62 and Example 63. https://arxiv.org/abs/2307.05940
- Prior public research records: *The Hochschild-lattice polytope has the exact permutahedral inradius*; *Higher Hochschild polytopes have an exact permutahedral facet-shell law*. The available abstracts describe inner radii of other \((m,n)\) cases, rather than an outer sphere for \(m=0\).
