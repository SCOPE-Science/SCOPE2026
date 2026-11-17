# Exact solid angles and a strict balance law for multipartite signed order cones

## Finding
Fix integers \(r\geq3\) and \(a_1,\ldots,a_r\geq1\), with \(n=\sum_{i=1}^r a_i\). Partition \([n]\) into classes \(A_i\) of these sizes. Define the full-dimensional cone and its signed order polytope by
\[
K_{\mathbf a}=\{x\in\mathbb R^n:x_u+x_v\geq0\text{ whenever }u\in A_i,\ v\in A_j,\ i\ne j\},\qquad O_{\mathbf a}=K_{\mathbf a}\cap[-1,1]^n.
\]
Let \(\omega(\mathbf a)\) be the normalized spherical solid angle of \(K_{\mathbf a}\), equivalently the probability that a standard Gaussian vector lies in this cone. For \(1\leq a<n\), write
\[
F_n(a)=\frac{\sum_{j=0}^{a-1}\binom nj}{\binom na}.
\]
**Exact angle and volume:**
\[
\boxed{\omega(\mathbf a)=2^{-n}\left(1+\sum_{i=1}^r F_n(a_i)\right),\qquad
\operatorname{Vol}_n(O_{\mathbf a})=1+\sum_{i=1}^r F_n(a_i).}
\]
The probability formula holds unchanged for any collection of independent, identically distributed, continuous random coordinates whose law is symmetric about zero; only its Gaussian specialization is a Euclidean solid angle.

**Sharp majorization law:** for fixed \(n\geq r\geq3\), the displayed angle and volume are strictly Schur-convex in the positive integer part sizes. Thus the unique minimum up to permutation is the balanced vector with entries differing by at most one, and the unique maximum is \((n-r+1,1,\ldots,1)\). If \(n=rb+s\), \(0\leq s<r\), their exact volumes are
\[
\boxed{V_{\min}=1+(r-s)F_n(b)+sF_n(b+1),\qquad
V_{\max}=1+F_n(n-r+1)+\frac{r-1}{n}.}
\]
A genuine balancing transfer strictly decreases the volume; a genuine transfer toward a more unequal vector strictly increases it.

**Sharp fixed-class asymptotics:** for every fixed \(r\geq3\), as \(n\to\infty\) through arbitrary integers with balanced part sizes,
\[
\boxed{V_{\min}\longrightarrow\frac{2(r-1)}{r-2},\qquad
V_{\max}\sim\frac{2^n(r-1)!}{n^{r-1}}.}
\]
Consequently the minimum solid angle decays as \(2^{-n}\) times a finite nonzero constant, while the maximum solid angle is polynomially small, asymptotic to \((r-1)!/n^{r-1}\). These are different geometric regimes of the same fixed-class family.

## Assumptions and scope
The root set \(\{e_u+e_v:u,v\text{ in different classes}\}\) is a signed poset in the type-\(B\) sense: its positive root closure introduces no new root, since its generators have two positive coordinates and a missing same-class pair cannot be generated without introducing other positive coordinates. In particular, these are legitimate signed order cones of the kind studied by Beck and Hlavacek. The metric is the ordinary orthonormal-coordinate Euclidean metric on \(\mathbb R^n\); the angle is the spherical probability in the full \(n\)-dimensional ambient space, not an angle in a quotient or a normal cone of a different polytope. Volumes are ordinary \(n\)-dimensional Lebesgue volumes, without lattice normalization. All boundary hyperplanes have Gaussian and Lebesgue measure zero.

For vectors with positive integer entries and fixed length and sum, \(\mathbf a\) *strictly majorizes* \(\mathbf b\) when the decreasing rearrangements differ and every leading partial sum for \(\mathbf a\) is at least the corresponding one for \(\mathbf b\). If only one unordered composition is available, the equality of the minimum and maximum is the unavoidable degenerate case.

## Proof
**1. Distribution-free reduction.** Let \(X_1,\ldots,X_n\) be independent with one common continuous symmetric law, and let \(E\) denote all cross-class inequalities \(X_u+X_v\geq0\). All-positive sign patterns satisfy \(E\). If negative coordinates occur in two different classes, a cross-class sum is negative, so \(E\) fails. Thus every other satisfying sign pattern has exactly \(k\geq1\) negative coordinates in one specified class \(A_i\), no negative coordinates outside \(A_i\), and arbitrary positive coordinates in the rest of \(A_i\).

Write \(b=n-a_i\). Conditional on such a sign pattern, the \(k\) magnitudes at negative coordinates and the \(b\) magnitudes outside \(A_i\) are independent and identically distributed without ties. The inequalities hold exactly if all \(k\) negative-coordinate magnitudes are smaller than all \(b\) outside magnitudes. By uniformity of the order of these \(k+b\) magnitudes, this event has probability \(1/\binom{b+k}{k}\). There are \(\binom{a_i}{k}\) choices of the negative-coordinate set in \(A_i\); each fixed sign pattern has probability \(2^{-n}\). Hence
\[
\Pr(E)=2^{-n}\left[1+\sum_{i=1}^r\sum_{k=1}^{a_i}\frac{\binom{a_i}{k}}{\binom{n-a_i+k}{k}}\right].
\]
The exact factorial identity
\[
\frac{\binom a k}{\binom{n-a+k}k}=\frac{\binom n{a-k}}{\binom na}
\]
converts the inner sum into \(F_n(a_i)\), proving the angle formula upon specializing to standard Gaussian coordinates.

**2. Euclidean volume.** Independent uniform coordinates on \([-1,1]\) also satisfy the symmetry, continuity, and exchangeability hypotheses of Step 1. Their joint density is constant \(2^{-n}\) on the cube, so their probability of belonging to \(K_{\mathbf a}\) is \(2^{-n}\operatorname{Vol}_n(O_{\mathbf a})\). Comparing this with the same distribution-free formula for Gaussian coordinates proves the volume identity. It is essential here that the root constraints consist of pair sums; a generic polyhedral cone does not have equal Gaussian and uniform-cube probabilities.

**3. Strict convexity in class size.** For fixed \(n\), set
\[
G_{n,k}(t)=\prod_{j=0}^{k-1}\frac{t-j}{n-t+j+1}\quad(k-1\leq t\leq n-1),
\]
and extend it by zero for \(0\leq t\leq k-1\). Each factor in the product is nonnegative, increasing, and convex on \([k-1,n-1]\), with positive derivative and second derivative, because
\[
\frac{d}{dt}\frac{t-j}{n-t+j+1}=\frac{n+1}{(n-t+j+1)^2},\qquad
\frac{d^2}{dt^2}\frac{t-j}{n-t+j+1}=\frac{2(n+1)}{(n-t+j+1)^3}.
\]
Products of nonnegative increasing convex twice-differentiable functions are convex; extending by zero is convex here since the right derivative at the join is nonnegative. At integer \(a\in[1,n-1]\), the identity \(F_n(a)=\sum_{k=1}^{n-1}G_{n,k}(a)\) follows from the factorial formula in Step 1, including the zero terms for \(k>a\). The \(k=1\) term \(G_{n,1}(t)=t/(n+1-t)\) is strictly convex. Therefore \(F_n\) is strictly convex at the relevant consecutive integers: for every \(1\leq a\leq n-3\),
\[
F_n(a+2)-2F_n(a+1)+F_n(a)>0.
\]
If one unit is transferred from a smaller positive part to a part already at least as large, strict convexity strictly increases \(\sum_i F_n(a_i)\). The transfer characterization of integer majorization proves strict Schur-convexity and both equality classifications. Substituting the balanced and extremal profiles gives the exact bound formulas.

**4. Asymptotics.** Suppose \(a/n\to\alpha\in(0,1/2)\). Then, for every fixed \(k\geq1\),
\[
\frac{\binom n{a-k}}{\binom na}\longrightarrow\left(\frac{\alpha}{1-\alpha}\right)^k.
\]
The ratio of consecutive terms in the backwards binomial tail is bounded by \(a/(n-a+1)\), uniformly eventually smaller than one. Dominated convergence for the geometric majorant gives \(F_n(a)\to\alpha/(1-2\alpha)\). Every class in a balanced fixed-\(r\) vector has proportion approaching \(1/r<1/2\), so its volume tends to \(1+r/(r-2)=2(r-1)/(r-2)\).

For the maximal profile let \(a=n-r+1\). By binomial symmetry,
\[
F_n(a)=\frac{2^n-\sum_{j=0}^{r-1}\binom nj}{\binom n{r-1}}.
\]
For fixed \(r\), the removed tail is polynomial in \(n\), while \(\binom n{r-1}\sim n^{r-1}/(r-1)!\). Thus \(1+F_n(a)+(r-1)/n\sim2^n(r-1)!/n^{r-1}\). Dividing both bounds by \(2^n\) gives the stated sharp angle asymptotics.

## Verification
The standalone standard-library script `verify.py` enumerates sign patterns and strict absolute-value ranks independently of the binomial-tail calculation. In particular it tests whether \(\pm1,\ldots,\pm n\), with distinct absolute ranks, obey every cross-class inequality, and compares the resulting exact rational probabilities against the theorem. It also tests the strict discrete convexity inequality and the majorization ordering in finite dimensions. The packaged execution prints `SIGNED_MULTIPARTITE_ANGLE_PASS`. Exact finite enumeration is corroboration; the proof for arbitrary class sizes is Steps 1–4.

For example, the positive-tripartite-root cones with class sizes \((2,2,2)\) and \((1,1,4)\) in dimension six have normalized angles \(3/80\) and \(31/480\), respectively. Their signed order polytopes have volumes \(12/5\) and \(62/15\), respectively. The exact formulas, not any illustrative decimal approximations, define these values.

## Relationship to prior work
Beck and Hlavacek [1] define signed order cones and signed order polytopes, and establish general type-\(B\) chamber triangulations and Jordan–Hölder enumeration. Their general result allows a signed-order volume to be counted by chambers; it does not state an evaluated complete-multipartite root-cone volume, its distribution-free formula, strict part-size majorization, or the sharp fixed-class extremal asymptotics. Godland and Kabluchko [2] evaluate conic intrinsic volumes of individual classical Weyl chambers; this is compatible with, but does not calculate, the angles of the present unions of many type-\(B\) chambers.

For two classes, changing the sign of every coordinate in one class changes \(x_u+x_v\geq0\) into a classical two-level order-cone inequality \(x_u\geq y_v\). Its well-known solid angle is \(1/\binom np\), so the bipartite boundary case is not claimed as new here. For \(r\geq3\), the graph contains triangles, preventing a single coordinate sign change from converting all positive pair constraints into difference constraints. The new result concerns exactly this non-bipartite type-\(B\) regime.

The previously recorded exact volume and imbalance result for a two-level **signed chain** polytope concerns simultaneous inequalities \(|x_i+y_j|\leq1\) on a bounded body, not the one-sided positive-root cone here. A previously recorded volume-majorization result for complete-multipartite **Lipschitz dual balls** concerns difference bounds \(|x_u-x_v|\) and anchored \((n-1)\)-dimensional volume, rather than this positive-root cone and its full-dimensional cube section. These are close methodological comparators, but neither statement logically yields the present exact formula or the fixed-class balance law merely by substituting the same part sizes.

## Limitations
The claim is for unit coefficients, complete multipartite cross-class **positive** roots, at least three nonempty parts, and ordinary Euclidean coordinates. It is not a result for arbitrary signed posets, mixed-sign edges, arbitrary weighted roots, or all conic intrinsic volumes. The distribution-free statement requires identical independent continuous symmetric coordinates; without spherical symmetry, that probability is not itself a Euclidean angle. The strict part-size comparison requires a genuine majorization change. The asymptotics keep the number of parts fixed. The existence of a differently named earlier closed evaluation remains a bibliographic risk; independent review is not claimed.

## References
[1] M. Beck and M. Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409v1, first publicly posted 2023-11-08, Sections 1–4, https://arxiv.org/abs/2311.04409.

[2] T. Godland and Z. Kabluchko, *Conic intrinsic volumes of Weyl chambers*, V. M. S. T. A. 9 (2022), 357–375, https://www.vmsta.org/journal/VMSTA/article/245/read.

[3] *Exact volume and strict imbalance law for two-level signed-chain polytopes*, publicly accessible mathematical research record (2026), compared at the level of defining inequalities and full theorem.

[4] *Strict majorization of volumes of multipartite Lipschitz dual balls*, publicly accessible mathematical research record (2026), compared at the level of defining inequalities and full theorem.
