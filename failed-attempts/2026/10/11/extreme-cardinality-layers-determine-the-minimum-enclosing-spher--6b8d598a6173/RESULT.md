# Extreme cardinality layers determine the minimum enclosing sphere of every S-hypersimplex
## Finding
Let
\[
d\ge1,
\qquad
\varnothing\ne S\subseteq\{0,1,\ldots,d\},
\]
and let
\[
\Delta(d,S)
=
\operatorname{conv}\left\{
v\in\{0,1\}^d:
\sum_{i=1}^d v_i\in S
\right\}
\tag{1}
\]
be the standard \(S\)-hypersimplex of Manecke, Sanyal, and So.

Put
\[
a=\min S,
\qquad
b=\max S,
\tag{2}
\]
and let \(h\) be the Euclidean projection of \(d/2\) onto the interval \([a,b]\):
\[
h=
\begin{cases}
b,&b<d/2,\\[1mm]
d/2,&a\le d/2\le b,\\[1mm]
a,&a>d/2.
\end{cases}
\tag{3}
\]

Then the unique minimum enclosing Euclidean sphere of \(\Delta(d,S)\) has center
\[
\boxed{
c_{d,S}=\frac{h}{d}\mathbf1
}
\tag{4}
\]
and squared radius
\[
\boxed{
R_{d,S}^2=\frac{h(d-h)}{d}.
}
\tag{5}
\]

The contact set is completely determined by the position of the cardinality interval relative to \(d/2\):
\[
\boxed{
\begin{array}{ll}
b<d/2:
&\text{exactly the vertices of Hamming weight }b,\\[1mm]
a>d/2:
&\text{exactly the vertices of Hamming weight }a,\\[1mm]
a\le d/2\le b:
&\text{every vertex of }\Delta(d,S).
\end{array}
}
\tag{6}
\]

Hence the number of contact vertices is
\[
\binom db
\quad\text{if }b<d/2,
\tag{7}
\]
\[
\binom da
\quad\text{if }a>d/2,
\tag{8}
\]
and
\[
\sum_{s\in S}\binom ds
\quad\text{if }a\le d/2\le b.
\tag{9}
\]

In particular, the minimum enclosing sphere depends only on the two extreme cardinalities
\[
\min S
\quad\text{and}\quad
\max S.
\]
All intermediate selected layers are metrically invisible to this invariant.

## Assumptions and scope
The realization is exactly the standard \(0/1\)-coordinate realization in (1), and the metric is the standard Euclidean metric on \(\mathbb R^d\).

The theorem includes lower-dimensional cases such as ordinary hypersimplices, the segment \(\Delta(d,\{0,d\})\), and the singleton cases \(S=\{0\}\) and \(S=\{d\}\). The minimum enclosing sphere is taken in the ambient Euclidean space.

No claim is made that arbitrary affine realizations of the same combinatorial type have the same radius.

## Proof
The source identifies the vertices of \(\Delta(d,S)\) with all subsets
\[
A\subseteq[d]
\]
whose cardinality lies in \(S\). Thus, for each
\[
s\in S,
\]
the Hamming-weight-\(s\) layer consists of all vectors
\[
e_A\in\{0,1\}^d
\quad\text{with}\quad
|A|=s.
\]

Fix an arbitrary candidate center
\[
z\in\mathbb R^d.
\]
Write
\[
z=t\mathbf1+w,
\qquad
\langle w,\mathbf1\rangle=0.
\tag{10}
\]
Average the squared distance from \(z\) over the complete weight-\(s\) layer. Its barycenter is
\[
\frac{s}{d}\mathbf1,
\]
and every layer vertex has squared norm \(s\). Therefore
\[
\begin{aligned}
\frac1{\binom ds}
\sum_{|A|=s}
\|e_A-z\|^2
&=
s-\frac{2s}{d}\langle\mathbf1,z\rangle+\|z\|^2\\
&=
s(1-t)^2+(d-s)t^2+\|w\|^2.
\end{aligned}
\tag{11}
\]
Define
\[
q_s(t)=s(1-t)^2+(d-s)t^2
=
dt^2+s(1-2t).
\tag{12}
\]

Since a maximum is at least an average, every enclosing ball centered at \(z\) has squared radius at least
\[
\max_{s\in S}q_s(t)+\|w\|^2.
\tag{13}
\]
Conversely, if \(w=0\), every vertex in the weight-\(s\) layer lies at exactly squared distance \(q_s(t)\) from \(t\mathbf1\). Hence the minimum enclosing problem is exactly the one-variable minimization
\[
\min_{t\in\mathbb R}\max_{s\in S}q_s(t),
\tag{14}
\]
and any nonzero \(w\) is strictly suboptimal.

For fixed \(t\), expression (12) is affine in \(s\). Therefore
\[
\max_{s\in S}q_s(t)
=
\begin{cases}
q_b(t),&t\le1/2,\\
q_a(t),&t\ge1/2.
\end{cases}
\tag{15}
\]

Suppose first that
\[
b<d/2.
\]
The quadratic \(q_b\) has its unique minimum at
\[
t=\frac bd<\frac12.
\]
On the other side of the breakpoint, the objective is at least its value at \(1/2\), namely \(d/4\), while
\[
q_b\left(\frac bd\right)
=
\frac{b(d-b)}d
<
\frac d4.
\]
Thus the unique optimum is
\[
t=\frac bd,
\]
and (4)--(5) follow with \(h=b\).

If
\[
a>d/2,
\]
the symmetric argument gives the unique optimum
\[
t=\frac ad
\]
and
\[
R^2=\frac{a(d-a)}d.
\]

Finally, suppose
\[
a\le d/2\le b.
\]
For \(t\le1/2\), the controlling quadratic \(q_b\) is nonincreasing up to \(1/2\), because its minimizer \(b/d\) lies at or to the right of \(1/2\). For \(t\ge1/2\), the controlling quadratic \(q_a\) is nondecreasing from \(1/2\), because its minimizer \(a/d\) lies at or to the left. Hence the unique optimum is
\[
t=\frac12,
\]
and every \(0/1\)-vector satisfies
\[
\left\|v-\frac12\mathbf1\right\|^2=\frac d4.
\tag{16}
\]
This proves (4)--(5) in all cases.

It remains to identify the contact sets.

When
\[
b<d/2,
\]
at the optimal value \(t=b/d\),
\[
q_b(t)-q_s(t)
=
(b-s)\left(1-\frac{2b}{d}\right)
>0
\]
for every \(s<b\). Thus exactly the weight-\(b\) layer is in contact.

When
\[
a>d/2,
\]
the analogous identity shows that exactly the weight-\(a\) layer is in contact.

When
\[
a\le d/2\le b,
\]
equation (16) shows that every vertex is in contact.

Finally, uniqueness of the center follows directly from (13): a nonzero orthogonal component \(w\) increases the lower bound strictly, while the one-variable objective in (14) has the unique minimizer found above.

## Verification
The proof is symbolic for every
\[
d\ge1
\]
and every nonempty
\[
S\subseteq\{0,1,\ldots,d\}.
\]

The source-dependent premise was checked directly in the primary full text and page image: \(\Delta(d,S)\) is the convex hull of exactly the \(0/1\)-vectors whose coordinate sums lie in \(S\), and its vertices are in bijection with subsets of \([d]\) whose cardinalities lie in \(S\).

The accompanying `verify.py` checks every nonempty \(S\) for
\[
1\le d\le8.
\]
Using exact rational arithmetic, it verifies the proposed center, radius, strict contact classification, and the one-variable lower bound on a rational test grid. These finite checks are corroborative only; the arbitrary-dimensional result is proved by (11)--(15).

## Relationship to prior work
Manecke, Sanyal, and So introduced the \(S\)-hypersimplex notation and systematically studied the vertices, edges, facets, Cayley decomposition, pulling triangulations, and monotone path polytopes of this family. Their primary full text does not state a circumradius, minimum enclosing sphere, or Euclidean center theorem.

The ordinary hypersimplex
\[
\Delta(d,\{k\})
\]
is already a single constant-weight orbit, so its centered radius is elementary. The content here is the simultaneous classification for every union of Hamming layers: the optimum is controlled only by the cardinality interval endpoints, and there is a sharp transition when that interval first meets \(d/2\).

A recent published-result computation of the one-skeleton metric for consecutive-layer \(S\)-hypersimplices concerns shortest paths in the edge graph. It does not imply the Euclidean minimum enclosing sphere, and the present theorem applies to arbitrary nonempty \(S\), not only consecutive layers.

Targeted searches under “\(S\)-hypersimplex”, “circumradius”, “minimum enclosing sphere”, “Chebyshev center”, “vertex shells”, and ordinary “hypersimplex circumradius” terminology did not locate a statement implying (4)--(9).

## Limitations
The result is realization-specific: arbitrary affine images do not preserve the Euclidean radius.

The theorem determines the minimum enclosing sphere but not the inradius, John ellipsoid, Löwner ellipsoid, or full pairwise distance distribution.

The ordinary single-layer case is classical and immediate from symmetry. The originality claim concerns the complete arbitrary-\(S\) classification, the endpoint-only dependence, and the contact-set phase transition.

Because the proof becomes short after averaging complete Hamming layers, an equivalent folklore statement may exist under coding-theoretic or Hamming-layer terminology. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Sebastian Manecke, Raman Sanyal, and Jeonghoon So, *S-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491, first public version 2018-12-18; Electronic Journal of Combinatorics 27(3) (2020), article P3.16, DOI 10.37236/8457.
