# Orthogonal kernels of regular cross-polytopes in dimensions at least four

## Finding
For each integer \(d\ge4\), let
\[
P_d=\operatorname{conv}\{\pm e_1,\dots,\pm e_d\}
=\{x\in\mathbb R^d:\|x\|_1\le1\}.
\]
Let \(\mathcal K_d\) be the set of points \(b\in\operatorname{int}P_d\) for which the Euclidean orthogonal projection of \(b\) onto the affine hull of **every nonempty face** of \(P_d\) belongs to that face's relative interior. Then
\[
\boxed{\mathcal K_d=\{b:\|b\|_1+(d-2)\|b\|_\infty<1\}.}
\]
The closure \(K_d=\overline{\mathcal K_d}\) has complete vertex and facet descriptions:
\[
\begin{split}
V(K_d)&=\left\{\frac{s}{d-2+|\operatorname{supp}s|}:
 s\in\{-1,0,1\}^d\setminus\{0\}\right\},\\
f_0(K_d)&=3^d-1,\qquad f_{d-1}(K_d)=d\,2^d.
\end{split}
\]
Its exact Euclidean volume, and its fraction of the regular cross-polytope, are
\[
\boxed{\operatorname{vol}_d(K_d)=\frac{2^d(d-2)!}{(2d-2)!}},\qquad
\boxed{\frac{\operatorname{vol}_d(K_d)}{\operatorname{vol}_d(P_d)}
=\binom{2d-2}{d}^{-1}\sim\frac{4\sqrt{\pi d}}{4^d}.}
\]
Thus a uniformly sampled point of \(P_d\) simultaneously has valid perpendicular feet on **all faces** with the stated exact probability. In dimension four the corresponding closed kernel has \(80\) vertices, \(64\) facets, and probability \(1/15\).

## Assumptions and scope
We work with the usual Euclidean inner product in \(\mathbb R^d\), not with an \(\ell_1\) metric for perpendicularity. The ambient cross-polytope has vertices \(\pm e_i\), and both the polytope and the projections use their original Euclidean embedding. The strict relative-interior condition is essential. The closure is used only for vertex and volume calculations, since the boundary has zero \(d\)-dimensional measure.

For each nonempty subset \(S\subseteq[d]\) and \(s\in\{-1,1\}^S\), write \(F_{S,s}=\operatorname{conv}\{s_i e_i:i\in S\}\). Every nonempty proper face of \(P_d\) is exactly one such face. The case \(F=P_d\) contributes only the condition \(b\in\operatorname{int}P_d\).

## Proof
**1. Projection formula.** Fix \(F_{S,s}\), let \(m=|S|\), and put \(t=\sum_{j\in S}s_jb_j\). A point of its affine hull has coordinates zero outside \(S\) and satisfies \(\sum_{i\in S}s_ix_i=1\). Lagrange multipliers, or elementary orthogonal projection onto this hyperplane within its coordinate subspace, give
\[
 x_i=\begin{cases}
 b_i+s_i(1-t)/m,&i\in S,\\
 0,&i\notin S.
 \end{cases}
\]
The signed barycentric weights of this point in \(F_{S,s}\) are \(s_ix_i\) for \(i\in S\). Hence the projection is in \(\operatorname{relint}F_{S,s}\) precisely when
\[
1+(m-1)s_ib_i-\sum_{j\in S\setminus\{i\}}s_jb_j>0
\quad\text{for each }i\in S.\tag{1}
\]
For \(m=1\) this is the tautology \(1>0\).

**2. Reduction of all face constraints to facets.** At fixed \(S\) and distinguished \(i\), the inequalities (1) over every sign vector \(s\) are equivalent to
\[
 (m-1)|b_i|+\sum_{j\in S\setminus\{i\}}|b_j|<1.\tag{2}
\]
Every left side in (2) is bounded above by the analogous facet left side
\[
(d-1)|b_i|+\sum_{j\ne i}|b_j|
=\|b\|_1+(d-2)|b_i|,
\]
because \(m\le d\). Conversely, each such facet constraint appears in (2) when \(S=[d]\). Therefore requiring all proper-face projections to lie in the relative interiors of their faces is equivalent to
\[
\|b\|_1+(d-2)\max_i|b_i|<1.
\]
This inequality itself entails \(\|b\|_1<1\), so it also supplies the required interior condition for the full-dimensional face. This proves the kernel identity, including both directions and strict boundary exclusion.

**3. Facets of the closure.** Let \(a=d-2>0\). The closure is the intersection of the \(d2^d\) halfspaces
\[
\langle\sigma+a\sigma_je_j,x\rangle\le1,
\qquad j\in[d],\quad\sigma\in\{-1,1\}^d.\tag{3}
\]
Every indexed supporting inequality is a true facet: choose a point with signs exactly \(\sigma\), all coordinates nonzero, and \(|x_j|\) strictly larger than the other \(|x_i|\). Scale it so \(\|x\|_1+a|x_j|=1\). On a sufficiently small relative neighborhood in its supporting hyperplane, the signs and unique maximizing coordinate remain unchanged, so (3) is the only active inequality. Two different indices give different normal vectors because \(a>0\), and two different sign vectors do likewise. Hence \(f_{d-1}(K_d)=d2^d\).

**4. All vertices.** By symmetry, dissect \(K_d\) into its intersections with signed coordinate-order chambers. In the positive ordered chamber
\[
x_1\ge x_2\ge\dots\ge x_d\ge0,
\]
set \(z_j=x_j-x_{j+1}\ge0\), with \(x_{d+1}=0\). Then
\[
\|x\|_1+a\|x\|_\infty
=\sum_{j=1}^d(a+j)z_j.\tag{4}
\]
The chamber is therefore a simplex. Apart from the origin, its vertices have their first \(k\) coordinates equal to \(1/(a+k)\) and all others zero, for \(1\le k\le d\). Since a global vertex of a polytope remains a vertex of any convex chamber slice containing it, this proves that every global vertex is among the \(3^d-1\) asserted signed patterns.

Each signed pattern is indeed a global vertex. Let \(s\ne0\) have support \(S\), \(|S|=k\), and let \(v=s/(a+k)\). For every \(j\in S\), choose signs \(\sigma_i=s_i\) on \(S\) arbitrarily on its complement. The facet normal \(\sigma+a\sigma_je_j\) then satisfies \(\langle\sigma+a\sigma_je_j,v\rangle=1\). Varying signs on coordinates outside \(S\) produces \(d-k\) independent coordinate directions in the span of active normals. Varying \(j\) across \(S\) produces \(k-1\) independent differences \(a(s_je_j-s_\ell e_\ell)\) within \(S\). Any one active normal supplies the final independent direction because its dot product with \(v\) is one, whereas the previous \(d-1\) differences are orthogonal to \(v\). Thus the active normals span \(\mathbb R^d\), so \(v\) is an exposed vertex. All signed patterns give different points, proving \(f_0(K_d)=3^d-1\).

**5. Volume.** There are \(2^d d!\) signed coordinate-order chambers with mutually disjoint interiors and congruent intersections with \(K_d\). The linear map from \(z\) to \(x\) used in (4) has determinant one. The nonnegative simplex \(\sum_j(a+j)z_j\le1\) therefore has volume
\[
\frac1{d!\prod_{j=1}^d(a+j)}.
\]
Summing yields
\[
\operatorname{vol}_d(K_d)
=\frac{2^d}{\prod_{j=1}^d(d-2+j)}
=\frac{2^d(d-2)!}{(2d-2)!}.
\]
Since \(\operatorname{vol}_d(P_d)=2^d/d!\), the probability/ratio is \(d!(d-2)!/(2d-2)!=\binom{2d-2}{d}^{-1}\). Stirling's approximation gives the stated asymptotic.

## Verification
A standalone Python 3 checker in `CHECKER.py` uses exact fractions. It tested every proposed vertex against every facet inequality and verified full-rank active normals for dimensions \(d=3,4,5,6\): 1,076 vertices and 324,016 halfspace evaluations. It also checked 640 exact-rational sampled points against direct projections onto **all nonempty proper faces**, and verified 12 closed-form identities. Results: \(d=3\), 26 vertices and volume fraction \(1/4\); \(d=4\), 80 and \(1/15\); \(d=5\), 242 and \(1/56\); \(d=6\), 728 and \(1/210\). These finite checks do not prove the infinite-dimensional range; the preceding analytic argument does.

## Relationship to prior work
Pavlík's November 2026 paper introduces the orthogonal kernel and proves a three-dimensional equivalence between membership and valid orthogonally bipolar tilings; it does not compute this all-dimensional kernel for regular cross-polytopes. The companion paper establishes a distinct interval-poset realization for cubes and cross-polytopes; its \(3^d+1\) vertices refer to a different bipolar polytope and do not determine this kernel's \(3^d-1\) vertices.

The previously published regular-octahedron full-normal-locus result gives the same \(d=3\) case (volume fraction \(1/4\)). That case is **not claimed as new** here. Previously published canonical signohedron results consider \(\{\|x\|_1+\|x\|_\infty\le1\}\), including vertex/facet counts and volume. Our orthogonal-kernel family has coefficient \(d-2\), agreeing with the canonical signohedron only at \(d=3\). The combinatorial pattern alone is therefore not proposed as a wholly new type; the identification with the all-face geometric kernel and the exact dimension-linked volume law are the substantive higher-dimensional statements.

## Limitations
The result concerns only regular Euclidean cross-polytopes with \(d\ge4\), their strict kernel, and its closure. It does not establish that orthogonal cutouts form bipolar tilings in dimensions above three; that issue remains open in the cited work. It does not classify orthogonal kernels of arbitrary affine images or other polytopes. Historical-priority risk remains for alternate terminology such as full-normal loci, orthic kernels, and mixed \(\ell_1\)-\(\ell_\infty\) norm balls; published mathematical records on canonical signohedra were compared using their available summaries, not inaccessible full texts. Independent external validation is not performed.

## References
- Jan Pavlík, *Thales’s theorem in higher dimensions*, arXiv:2611.14277v1, publicly posted 10 November 2026, https://arxiv.org/html/2611.14277v1, especially Section 6 and Definition 6.1.
- Jan Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1, publicly posted 10 November 2026, https://arxiv.org/abs/2611.13896, especially Theorem 5.8, Remark 5.9, and Section 5.3.
- Published mathematical record, *The regular octahedron's full-normal locus has one-quarter volume*, 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-regular-octahedron-s-full-normal-locus-has-one-quarter-volum--596428720a97.
- Published mathematical record, *Strict isotropic deficit and logarithmic-squared limit for canonical signohedra*, 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-strict-isotropic-deficit-and-logarithmic-squared-limit-for-canon--e75d55d70549.
- Published mathematical record, *Canonical signohedra are tangential with exact radial shells*, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-canonical-signohedra-are-tangential-with-d-exact-radial-shells--c04451515c1c.
