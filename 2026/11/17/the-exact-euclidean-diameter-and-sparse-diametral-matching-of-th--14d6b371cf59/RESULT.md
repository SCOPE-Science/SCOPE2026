# The exact Euclidean diameter and sparse diametral matching of the harmonic polytope
## Finding
For an integer \(n\ge2\), write
\[
\Pi_n=\operatorname{conv}\{(p_1,\ldots,p_n):(p_1,\ldots,p_n)\text{ permutes }(1,\ldots,n)\},
\]
and, in the direct sum of two coordinate copies of \(\mathbb R^n\), put
\[
D_n=\operatorname{conv}\{(e_i,e_i):1\le i\le n\},\qquad
H_{n,n}=(\Pi_n\times\Pi_n)+D_n.
\]
Then the ordinary ambient Euclidean diameter of the harmonic polytope is
\[
\boxed{\operatorname{diam}(H_{n,n})^2=\frac{2n(n^2-1)}3+8n-4.}
\tag{1}
\]

For a coordinate permutation \(p\), define its reversal complement by
\[
p_i^{\star}=n+1-p_i\quad(1\le i\le n).
\]
Every **unordered diametral pair of points**, without restricting a priori to vertices, is exactly
\[
\boxed{\left\{(p+e_i,q+e_i),\ (p^\star+e_j,q^\star+e_j)\right\},}
\tag{2}
\]
where \(i\ne j\), \(p,q\) are arbitrary independent permutations satisfying
\[
p_i=q_i=n,\qquad p_j=q_j=1.
\tag{3}
\]
There are exactly
\[
\boxed{\frac{n(n-1)}2\bigl((n-2)!\bigr)^2}
\tag{4}
\]
unordered diametral pairs. In particular, the diameter graph on the harmonic-polytope vertices is a matching on
\[
n(n-1)\bigl((n-2)!\bigr)^2
\]
vertices, with every other polytope vertex isolated. There are no nonvertex diametral endpoints.

The circumsphere-contact vertices were classified previously: their number is \(n((n-1)!)^2\). Precisely the proportion
\[
\boxed{\frac1{n-1}}
\tag{5}
\]
of these contact vertices occur as endpoints of a diameter. Thus a vanishing proportion of outer-shell vertices participate in a longest chord as \(n\to\infty\).

## Assumptions and scope
All distances use the Euclidean norm on \(\mathbb R^n\times\mathbb R^n\) in the **standard** Ardila–Escobar realization. The harmonic polytope is a Minkowski sum as above, not the related bipermutahedron. The theorem holds for every integer \(n\ge2\), including the rank-two exceptional shape, and makes no claim of affine invariance. A diameter graph joins distinct vertices exactly when their Euclidean distance equals the diameter.

## Proof
We first establish the strict rearrangement fact: for coordinate permutations \(p,p'\) of \((1,\ldots,n)\),
\[
\|p-p'\|^2\le B_n:=\frac{n(n^2-1)}3,
\tag{6}
\]
with equality if and only if \(p'=p^\star\). Indeed,
\[
\|p-p'\|^2=2\sum_{k=1}^n k^2-2\sum_{k=1}^n p_kp'_k,
\]
and the strict rearrangement inequality says the scalar product is uniquely minimized by oppositely sorted entries. In that case the squared difference is \(\sum_{k=1}^n(2k-n-1)^2=B_n\).

By the definition of a Minkowski sum, any point of \(H_{n,n}\) is a convex combination of points \((p+e_i,q+e_i)\), with \(p,q\) coordinate permutations and \(i\) a coordinate index. Because squared Euclidean distance is convex in each argument separately, a diameter is achieved among pairs of these generating points. Fix two of them,
\[
v=(p+e_i,q+e_i),\qquad w=(p'+e_j,q'+e_j).
\]
If \(i=j\), equation (6) gives
\[
\|v-w\|^2=\|p-p'\|^2+\|q-q'\|^2\le2B_n.
\tag{7}
\]

Suppose \(i\ne j\). In the first coordinate block,
\[
\begin{aligned}
\|p+e_i-p'-e_j\|^2
&=\|p-p'\|^2+2+2\bigl((p_i-p'_i)-(p_j-p'_j)\bigr)\\
&\le B_n+2+4(n-1),
\end{aligned}
\tag{8}
\]
since every coordinate difference of two permutations lies between \(-(n-1)\) and \(n-1\). Equality in (8) holds if and only if
\[
p'=p^\star,\quad p_i=n,\quad p'_i=1,\quad p_j=1,\quad p'_j=n.
\tag{9}
\]
The same argument applies independently to the second block, replacing \(p\) with \(q\). Therefore
\[
\|v-w\|^2\le 2B_n+4+8(n-1)
=\frac{2n(n^2-1)}3+8n-4.
\tag{10}
\]
The right-hand side is strictly greater than the bound (7). Equality is possible exactly when the two blocks simultaneously satisfy (9), which is precisely (2)–(3). Such permutations exist for every \(n\ge2\), proving (1) and the complete equality characterization among generating points.

We next rule out **all nonvertex endpoints**. If \(x\) is a strict convex combination \(x=tx_1+(1-t)x_2\) of distinct points of \(H_{n,n}\), where \(0<t<1\), then for any fixed \(y\) the squared Euclidean norm is strictly convex:
\[
\|x-y\|^2=t\|x_1-y\|^2+(1-t)\|x_2-y\|^2-t(1-t)\|x_1-x_2\|^2
<\operatorname{diam}(H_{n,n})^2.
\]
Thus a diametral endpoint must be a vertex. The explicit equality candidates (2) are indeed vertices: in each, the marked coordinate has largest permutation value in both blocks, so it is exposed by a common pair of strictly increasing coordinate weights. Equivalently, they satisfy the fine-harmonic-triple vertex criterion of Ardila–Escobar, Proposition 3.6. Hence (2) is the complete equality set among all polytope points.

To count pairs, choose the ordered distinct labels \(i,j\) in \(n(n-1)\) ways and choose each of \(p,q\) with prescribed values \(n\) and \(1\) at \(i,j\), giving \(((n-2)!)^2\) independent choices. Each unordered pair is counted exactly twice, once per orientation. This proves (4). An endpoint determines its unique partner: its largest designated coordinate is \(i\), its unique common minimum is \(j\), and both complementary permutations are fixed. Thus the diameter graph is a matching. Every other vertex is isolated by the just-proved complete equality characterization.

For completeness, the outer-sphere comparison can be seen directly from the coordinate norm. Put
\[
\mu_n=\frac{n+1}2+\frac1n,
\qquad c_n=(\mu_n\mathbf1,\mu_n\mathbf1).
\]
For every generating point \((p+e_k,q+e_k)\), elementary expansion gives
\[
\|(p+e_k,q+e_k)-c_n\|^2
=\frac{n(n^2-1)}6+2-\frac2n
+2\left(p_k+q_k-(n+1)\right).
\tag{11}
\]
The unique maximal value of the last summand occurs when \(p_k=q_k=n\), and there are \(n((n-1)!)^2\) distinct such vertices. Their average is the center \(c_n\), proving that this is the minimum enclosing sphere and exactly its contact set (also established in prior work). Exactly \(n(n-1)((n-2)!)^2\) of those vertices have in addition a common coordinate \(j\ne k\) where \(p_j=q_j=1\), as characterized by (3). Dividing the latter count by the outer-shell count proves (5).

## Verification
The proof is symbolic for all integers \(n\ge2\). The self-contained `artifacts/verify_diameter.py` performs independent exact-integer vertex enumeration, direct squared-distance comparison and witness tests using only the Python standard library. Run from the package root with `python3 artifacts/verify_diameter.py`.

A successful replay reports `HARMONIC_DIAMETER_PASS exhaustive=[(2, 6, 1, 16), (3, 66, 3, 36), (4, 1200, 24, 68)] witnesses_n=2..100 random_pairs_n5=120000`. The triple for each exhaustively enumerated order records its order, true vertex count, number of unordered diametral pairs, and diameter squared. Additional explicit witnesses are checked through order 100, and 120,000 seeded pairs are checked in order 5. These finite tests corroborate but do not replace the strict rearrangement, equality and strict-convexity arguments.

## Relationship to prior work
Ardila and Escobar introduced the harmonic polytope and proved its Minkowski-sum realization, vertex description, and face numbers. Their paper does not give its Euclidean diameter or enumerate pairs at that diameter. Ardila's bipermutahedron is a related but different polytope; a Minkowski quotient and combinatorial refinement do not imply the metric formula (1).

Published work on the **same harmonic polytope** has already determined its exact radial vertex shells, minimum enclosing sphere and the count \(n((n-1)!)^2\) of sphere contacts. This prior shell theorem is explicitly credited and not claimed as new. An inradius and incenter theorem, and a local vertex-degree theorem, also exist for the same object. None of the inspected statements describes the pairwise Euclidean diameter, its exact sparse matching, or the proportion of outer-shell contacts that participate in diametral pairs. The present contribution is those diameter and matching classifications, not the already-known circumsphere or vertex formula.

Relevant searches compared the same object under “harmonic polytope”, “Minkowski sum of permutahedra with diagonal simplex”, “diameter”, “diametral pairs”, “maximum Euclidean distance”, and related expressions, including published exact-radius and local-degree work. No identified stronger result implies (1)–(4); this is not proof of absolute historical novelty.

## Limitations
The distance is the standard realization's ambient Euclidean distance, not an affine invariant. The result gives the greatest pairwise point distance and all its equality cases, not the whole pair-distance spectrum or the John/Löwner ellipsoids. The strongest originality comparison is with the primary harmonic-polytope articles and publicly available same-object results; a differently named older statement is a residual historical-priority risk. Independent scientific audit has not been performed.

## References
1. Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078, initial public preprint 2020-06-04; Selecta Mathematica 27 (2021), article 91, DOI 10.1007/s00029-021-00687-6.
2. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295, initial public preprint 2020-08-05; Combinatorial Theory 2(3) (2022).
3. *Harmonic-polytope vertices form exactly n Euclidean shells*, published mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-harmonic-polytope-vertices-form-exactly-n-euclidean-shells--f2f2da42b2f8.
4. *Exact Euclidean inradius and incenter transition of the harmonic polytope*, published mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-inradius-and-incenter-transition-of-the-harmonic--81e898ba9eb4.
5. *Simple vertices and local degree of the harmonic polytope*, published mathematical record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-simple-vertices-and-local-degree-of-the-harmonic-polytope--8017b01864fe.
