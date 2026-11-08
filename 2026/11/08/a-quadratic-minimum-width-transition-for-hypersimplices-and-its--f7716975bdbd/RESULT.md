# A quadratic minimum-width transition for hypersimplices and its weighted partition formula

## Finding

For integers \(n\ge 2\) and \(1\le k\le n-1\), write
\[
\Delta_{n,k}=\operatorname{conv}\{\mathbf 1_I:I\subseteq\{1,\ldots,n\},\ |I|=k\}
=\{x\in[0,1]^n:\textstyle\sum_i x_i=k\}.
\]
Let \(s_i>0\) and put \(K_s=\operatorname{diag}(s_1,\dots,s_n)\Delta_{n,k}\), with the intrinsic Euclidean metric inherited from \(\mathbb R^n\). Define, for each nonempty proper \(S\subsetneq[n]\),
\[
A_S=\sum_{i\in S}s_i^{-2},\quad B_S=\sum_{i\notin S}s_i^{-2},\quad T=A_S+B_S,\quad m(S)=\min\{|S|,n-|S|,k,n-k\}.
\]
**Weighted theorem.** Its minimum directional width is exactly
\[
\boxed{\operatorname{width}_{\min}(K_s)=
\min_{\varnothing\ne S\subsetneq[n]}m(S)\sqrt{\frac{T}{A_SB_S}}.}
\]
Every minimizing unit normal is one of the following vectors \(\pm v^S\), and these are minimizing precisely for subsets \(S\) attaining the displayed minimum:
\[
v_i^S=\begin{cases}
\dfrac1{s_i}\sqrt{\dfrac{B_S}{A_ST}},&i\in S,\\[5pt]
-\dfrac1{s_i}\sqrt{\dfrac{A_S}{B_ST}},&i\notin S.
\end{cases}
\]
Thus all minimizing normal directions have exactly two levels after multiplication of coordinate \(i\) by \(s_i\). There are no additional minimizers, even when several subsets tie.

**Unweighted phase theorem.** Let \(q=\min\{k,n-k\}\), \(r=\lfloor n/2\rfloor\), \(t=\lceil n/2\rceil\). For the ordinary hypersimplex,
\[
\boxed{\operatorname{width}_{\min}(\Delta_{n,k})=
\min\left\{\sqrt{\frac n{n-1}},\ q\sqrt{\frac n{rt}}\right\}.}
\]
When \(n<4q^2-1\), precisely the signed intrinsic coordinate normals minimize. When \(n>4q^2-1\), precisely the signed balanced bipartition normals minimize (their positive support has size \(r\) or \(t\)). At the equality threshold \(n=4q^2-1\), both families minimize and no other directions do. For \(q=1,n=3\) the two labels describe the same directions; for every \(q\ge2\) the families at equality are distinct. The equality threshold is attained at infinitely many integer pairs, for instance \((n,k)=(15,2),(35,3),(63,4)\).

For \(q\ge2\), the number of unoriented minimizing lines is \(n\) below the threshold, \(\binom n{r}/2\) above it when \(n\) is even, \(\binom n{r}\) above it when \(n\) is odd, and \(n+\binom n{r}\) at equality. The sharp switch therefore changes the geometry and combinatorial multiplicity of all thinnest projections.

## Assumptions and scope

All coordinates use the original Euclidean embedding. Width is the separation of the two supporting hyperplanes orthogonal to a unit vector **parallel to the affine hull**, not the zero width obtained from a normal perpendicular to that affine hull. In the scaled case the direction space is \(L_s=\{v:\sum_i v_i/s_i=0\}\). The rank \(k\) is neither zero nor \(n\); those degenerate ranks yield points and are excluded. The scales are strictly positive, so the affine dimension is \(n-1\). Every theorem quantifies over all permitted integers and all positive real coordinate scales.

## Proof

**1. Symmetry and support functional.** The affine transformation \(x\mapsto\mathbf1-x\) takes \(\Delta_{n,k}\) onto \(\Delta_{n,n-k}\) and preserves widths. Set \(q=\min(k,n-k)\). For a direction \(v\in L_s\), set \(y_i=s_iv_i\). The support function of \(K_s\) is the sum of the largest \(q\) coordinates of \(y\), and the negative support is the negative of the sum of its smallest \(q\). Hence its directional width is
\[
W(y)=\sum_{i\text{ in top }q}y_i-\sum_{i\text{ in bottom }q}y_i.
\]
Also \(\sum_i s_i^{-2}y_i=0\) and \(\|v\|_2^2=\sum_i s_i^{-2}y_i^2\). The function \(W(y)\) is unchanged under adding a constant to all \(y_i\).

**2. The strict two-level extremality lemma.** Fix any ordering of the coordinates and work within its closed cone \(y_1\ge\cdots\ge y_n\), after relabelling. For \(1\le j<n\), let \(\rho_j\) be the step vector with its first \(j\) entries equal to \(1\), its remaining entries \(0\), minus its weighted mean \(A_j/T\) in all coordinates, with \(A_j=\sum_{i\le j}s_i^{-2}\). Every weighted-mean-zero vector in this cone has the unique decomposition
\[
y=\sum_{j=1}^{n-1}(y_j-y_{j+1})\rho_j,
\]
where all coefficients are nonnegative. The width functional \(W\) is linear on this cone, while \(\|y\|_{s^{-2}}=(\sum_i s_i^{-2}y_i^2)^{1/2}\) is the norm induced by the metric. Writing \(c=\min_j W(\rho_j)/\|\rho_j\|_{s^{-2}}\), the triangle inequality gives
\[
W(y)=\sum_j d_jW(\rho_j)\ge c\sum_jd_j\|\rho_j\|_{s^{-2}}
\ge c\|y\|_{s^{-2}},\qquad d_j=y_j-y_{j+1}\ge0.
\]
If at least two \(d_j\) are positive, the last triangle inequality is **strict**: two distinct step rays are not positive collinear, and the metric is positive definite. Therefore every minimizing direction is a single two-level step ray. This proves both global reduction and exhaustive equality characterization, rather than just a candidate upper bound.

**3. Evaluation of every step ray.** Let \(S\) be the indices of the higher level, \(j=|S|\). The difference of the levels equals \(1\) for the unnormalized mean-centered indicator. Its squared weighted norm is \(A_SB_S/T\). The top-minus-bottom \(q\)-sum counts the number of high coordinates gained when exchanging the top and bottom \(q\) ranks, namely
\[
m(S)=\min\{j,n-j,q\}=\min\{j,n-j,k,n-k\}.
\]
Thus the quotient of width by norm is \(m(S)\sqrt{T/(A_SB_S)}\). Normalizing the two levels gives the stated \(v^S\), which has Euclidean norm one and belongs to \(L_s\). Applying step 2 over all possible orderings and sets \(S\) proves the weighted formula and all minimizers.

**4. Unweighted minimization.** With all \(s_i=1\), the squared candidate width for a split of cardinality \(j\) is
\[
f(j)=\frac{n\min\{j,n-j,q\}^2}{j(n-j)},\qquad 1\le j\le n-1.
\]
By the symmetry \(j\leftrightarrow n-j\), it suffices to consider \(j\le n/2\). For \(1\le j\le q\), \(f(j)=nj/(n-j)\) is strictly increasing, hence the unique minimum in this range is at \(j=1\). For \(q\le j\le n/2\), \(f(j)=nq^2/[j(n-j)]\) is strictly decreasing, hence the unique minimum in this range is at the balanced integer split \(j=r\). This proves that **no intermediate split** can minimize, and the two alternatives are exactly \(n/(n-1)\) and \(q^2n/(rt)\). (The two ranges touch when \(q=r\), without introducing an additional equality class.)

**5. Exact threshold and counts.** The balanced candidate is better exactly when \(rt>q^2(n-1)\). If \(n\) is odd, \(rt=(n^2-1)/4\); the difference factors as
\[
rt-q^2(n-1)=\frac{(n-1)(n+1-4q^2)}4.
\]
If \(n\) is even, \(rt=n^2/4\). For \(q\ge2\) the quadratic \(F(n)=n^2/4-q^2(n-1)\) is negative at both \(n=2q\) and \(n=4q^2-2\), so convexity makes it negative at every intermediate admissible even integer. It is positive at \(n=4q^2\) and strictly increasing thereafter. No even integer lies between the latter two endpoints. The only integer tie therefore occurs at odd \(n=4q^2-1\). For \(q=1\) the same conclusion follows directly, including \(n=2,3\). Step 2 makes the equality classification exhaustive. Complementary higher-level sets define antipodal directions, giving the stated unoriented counts.

## Verification

The standalone `verify.py` uses exact rational arithmetic. It recomputes the weighted subset formula and every small unweighted phase, enumerates a finite grid of normal directions in dimensions two through seven, checks four nontrivial positive rational inverse-squared-scale profiles, and verifies five exact transition equalities. A successful run prints `HYPERSIMPLEX_WIDTH_CHECKS_PASSED`. These checks are finite consistency tests; the all-dimensional correctness is furnished by the five proof steps above. The weighted part can be verified directly by enumerating at most \(2^n-2\) proper subsets; it is not claimed to give a polynomial-time algorithm for arbitrary scales.

## Relationship to prior work

Martínez-Sandoval and Padrol (2019) analyze strict preservation of hypersimplex skeleta under linear projections; their Proposition 3.1 and surrounding discussion concern combinatorial face preservation, not the *metric minimum* over all unit directions. Their hypersimplex model and face structure are used as background. Har-Peled and Robson (2023) give a self-contained proof of the classical minimum width of the regular simplex, which is exactly the \(q=1\) case after accounting for edge-length normalization; that case is **not** claimed as a new result. The new all-rank result identifies a sharp quadratic \(n\)-versus-rank transition, all minimizing directions for \(q\ge2\), and a formula valid for arbitrary positive diagonal scales. Earlier equivalent derivations may exist under `uniform-matroid base`, `hypersimplex thickness`, `top-k norm`, or `order-statistic norm` terminology.

## Limitations

Historical priority is not independently certified. The theorem concerns intrinsic Euclidean width rather than lattice width, inradius, graph diameter, support-function averages, or projection-skeleton preservation. It does not claim a polynomial-time implementation of the weighted subset optimization or a full classification of other matroid base polytopes. No independent mathematical audit has been conducted.

## References

1. L. Martínez-Sandoval and A. Padrol, *The convex dimension of hypergraphs and the hypersimplicial Van Kampen-Flores Theorem*, arXiv:1909.01189, first public version 2019-09-03. https://arxiv.org/abs/1909.01189
2. S. Har-Peled and E. W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616, first public version 2023-01-06. https://arxiv.org/abs/2301.02616
3. L. Ferroni, *Valuative invariants for large classes of matroids*, Journal of the London Mathematical Society (2024), https://doi.org/10.1112/jlms.12984 (background on matroid base polytopes, not a width theorem).
