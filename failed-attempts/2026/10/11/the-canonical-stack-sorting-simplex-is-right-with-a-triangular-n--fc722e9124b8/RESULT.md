# The canonical stack-sorting simplex is right, with a triangular-number minimum-sphere transition
## Finding
Let
\[
n\ge3,
\qquad
\tau_n=23\cdots n1,
\]
and let
\[
\Delta_n
=
\operatorname{conv}
\{\tau_n,s(\tau_n),\ldots,s^{n-1}(\tau_n)\}
\subset\mathbb R^n
\tag{1}
\]
be the stack-sorting simplex in its standard permutation-coordinate realization.

Index the vertices as
\[
v_1=(1,2,\ldots,n)
\tag{2}
\]
and
\[
v_k=(2,3,\ldots,k,1,k+1,\ldots,n),
\qquad
2\le k\le n.
\tag{3}
\]
Put
\[
d_k=v_k-v_1.
\tag{4}
\]

Then
\[
\boxed{
d_k\cdot d_\ell=0
\quad
(2\le k<\ell\le n)
}
\tag{5}
\]
and
\[
\boxed{
\|d_k\|^2=k(k-1).
}
\tag{6}
\]
Hence \(\Delta_n\) is a right \((n-1)\)-simplex at the identity vertex \(v_1\), with mutually perpendicular incident edge lengths
\[
\sqrt{2},\sqrt{6},\sqrt{12},\ldots,\sqrt{n(n-1)}.
\]

Its Euclidean inradius is
\[
\boxed{
r_n
=
\left(
\sum_{k=2}^n\frac1{\sqrt{k(k-1)}}
+
\sqrt{\frac{n-1}{n}}
\right)^{-1}.
}
\tag{7}
\]
The incenter is unique and equals
\[
\boxed{
c_{\mathrm{in}}
=
v_1+
r_n
\sum_{k=2}^n
\frac{d_k}{\sqrt{k(k-1)}}.
}
\tag{8}
\]

There is also a unique sphere through all \(n\) vertices. Its center is
\[
c_{\mathrm{all}}
=
v_1+\frac12\sum_{k=2}^n d_k
\tag{9}
\]
and its squared radius is
\[
\boxed{
C_n^2
=
\frac{n(n^2-1)}{12}.
}
\tag{10}
\]
For \(n\ge4\), this all-vertex sphere is strictly larger than the true minimum enclosing sphere.

To describe the minimum enclosing sphere, let \(q=q_n\) be the unique integer satisfying
\[
q(q-1)<2n\le q(q+1),
\tag{11}
\]
and put
\[
m=n-q+1,
\qquad
\mu=\frac{n(m-1)(q-2)}q.
\tag{12}
\]
For
\[
m\le k\le n,
\]
define
\[
\lambda_k
=
\frac12
\left(
1-\frac{\mu}{k(k-1)}
\right).
\tag{13}
\]
Then
\[
\lambda_k>0,
\qquad
\sum_{k=m}^n\lambda_k=1.
\tag{14}
\]

The unique minimum-enclosing center is
\[
\boxed{
c_{\min}
=
\sum_{k=m}^n\lambda_k v_k,
}
\tag{15}
\]
and the squared minimum-enclosing radius is
\[
\boxed{
R_n^2
=
\frac14
\left(
\sum_{k=m}^n k(k-1)
-
\mu(q-2)
\right).
}
\tag{16}
\]

The contact set is exactly
\[
\{v_m,v_{m+1},\ldots,v_n\},
\tag{17}
\]
except when
\[
2n=q(q+1),
\tag{18}
\]
in which case \(v_{m-1}\) is one additional contact. Thus the contact number is normally \(q_n\), and it jumps to \(q_n+1\) exactly when
\[
n=\frac{q_n(q_n+1)}2
\]
is triangular.

Since
\[
q_n
=
\left\lceil
\frac{\sqrt{1+8n}-1}{2}
\right\rceil,
\tag{19}
\]
the minimum sphere is certified by only on the order of \(\sqrt{2n}\) tail vertices, even though the simplex has \(n\) vertices.

## Assumptions and scope
The metric is the Euclidean metric inherited from the standard embedding of permutations as vectors in \(\mathbb R^n\).

The simplex lies in the affine hyperplane
\[
x_1+\cdots+x_n=\frac{n(n+1)}2.
\]
All balls and facet distances are intrinsic to that affine hull.

The theorem is stated for \(n\ge3\). The case \(n=2\) is the segment joining \(12\) and \(21\), with minimum-enclosing radius \(1/\sqrt2\).

The term “all-vertex sphere” in (9)--(10) means the unique sphere through every simplex vertex. It is deliberately distinguished from the minimum enclosing sphere.

## Proof
The published iteration formula for \(\tau_n\) gives exactly the vertices (2)--(3). Therefore, for \(k\ge2\),
\[
d_k
=
\sum_{j=1}^{k-1}e_j-(k-1)e_k.
\tag{20}
\]
Hence
\[
\|d_k\|^2
=
(k-1)+(k-1)^2
=
k(k-1).
\]
If \(2\le k<\ell\le n\), then \(d_\ell\) has coordinate \(1\) in each of the first \(\ell-1\) positions, except at position \(\ell\). Thus
\[
d_k\cdot d_\ell
=
(k-1)-(k-1)
=
0.
\]
This proves (5)--(6).

Write
\[
L_k=\sqrt{k(k-1)}
\]
and
\[
u_k=\frac{d_k}{L_k}.
\]
The vectors \(u_2,\ldots,u_n\) form an orthonormal basis for the translation space of the simplex. In these coordinates,
\[
\Delta_n
=
\left\{
v_1+\sum_{k=2}^n t_k u_k:
t_k\ge0,\quad
\sum_{k=2}^n\frac{t_k}{L_k}\le1
\right\}.
\tag{21}
\]

The coordinate facets have distances \(t_k\). The remaining facet has normal
\[
\left(\frac1{L_2},\ldots,\frac1{L_n}\right)
\]
in the \(u\)-coordinates, of norm
\[
\left(
\sum_{k=2}^n\frac1{k(k-1)}
\right)^{1/2}
=
\sqrt{\frac{n-1}{n}}.
\tag{22}
\]
If a radius-\(\rho\) ball centered at \(t\) lies in the simplex, then
\[
t_k\ge\rho
\]
for every \(k\), and the sloping facet gives
\[
1-\sum_{k=2}^n\frac{t_k}{L_k}
\ge
\rho\sqrt{\frac{n-1}{n}}.
\]
Therefore
\[
1
\ge
\rho
\left(
\sum_{k=2}^n\frac1{L_k}
+
\sqrt{\frac{n-1}{n}}
\right).
\tag{23}
\]
Equality is attained by setting every \(t_k=r_n\), proving (7)--(8). Equality in (23) also forces every \(t_k=r_n\), so the incenter is unique.

Because the \(d_k\) are orthogonal, the point in (9) satisfies
\[
\|v_k-c_{\mathrm{all}}\|^2
=
\frac14\sum_{j=2}^n\|d_j\|^2
\]
for every \(k\), including \(k=1\). Since
\[
\sum_{k=2}^n k(k-1)
=
\frac{n(n^2-1)}3,
\tag{24}
\]
equation (10) follows.

It remains to solve the minimum-enclosing problem.

Let \(q,m,\mu\) be as in (11)--(12). The inequalities in (11) are equivalent to
\[
(m-1)(m-2)\le\mu<m(m-1).
\tag{25}
\]
Also
\[
\sum_{k=m}^n\frac1{k(k-1)}
=
\frac1{m-1}-\frac1n
=
\frac{q}{n(m-1)}.
\tag{26}
\]
Equations (12)--(13) therefore give
\[
\lambda_k>0
\]
and
\[
\sum_{k=m}^n\lambda_k
=
\frac q2
-
\frac{\mu}{2}
\sum_{k=m}^n\frac1{k(k-1)}
=
1.
\]
Thus (15) is a convex combination of \(v_m,\ldots,v_n\).

Translate by \(v_1\), and write
\[
c'_{\min}=c_{\min}-v_1
=
\sum_{k=m}^n\lambda_k d_k.
\]
For every active index \(k\),
\[
\begin{aligned}
\|d_k-c'_{\min}\|^2
&=
\|c'_{\min}\|^2
+
k(k-1)
-
2\lambda_k k(k-1)\\
&=
\|c'_{\min}\|^2+\mu.
\end{aligned}
\tag{27}
\]
So all active vertices lie on one sphere.

For an inactive vertex \(v_j\), with \(2\le j<m\), orthogonality gives
\[
\|d_j-c'_{\min}\|^2
=
\|c'_{\min}\|^2+j(j-1)
\le
\|c'_{\min}\|^2+\mu
\tag{28}
\]
by (25). The identity vertex \(v_1\) is also inside because its squared distance is simply \(\|c'_{\min}\|^2\).

The center itself is the convex combination in (15). Hence, for any point \(y\) in the affine hull,
\[
\sum_{k=m}^n
\lambda_k\|v_k-y\|^2
=
R_n^2+\|y-c_{\min}\|^2.
\tag{29}
\]
Some active vertex is therefore at distance at least the square root of the right side. Since the ball centered at \(c_{\min}\) already contains every vertex by (27)--(28), it is the unique minimum enclosing ball.

To compute its radius, use
\[
R_n^2
=
\|c'_{\min}\|^2+\mu.
\]
Substituting (13), orthogonality, and (26) yields
\[
R_n^2
=
\frac14
\left(
\sum_{k=m}^n k(k-1)-\mu(q-2)
\right),
\]
which is (16).

Finally, an inactive vertex can be a contact only when
\[
j(j-1)=\mu.
\]
Since these values strictly increase with \(j\), only \(j=m-1\) can qualify. Equality in the left side of (25) is equivalent to
\[
q(q+1)=2n.
\]
For \(n=3\), this extra predecessor is \(v_1\). This proves the contact classification.

For \(n\ge4\), \(\mu>0\), so \(v_1\) is strictly inside the minimum sphere. The all-vertex sphere (9) therefore cannot be minimum, proving the stated strict distinction.

## Verification
The proof is symbolic for every \(n\ge3\).

The source-dependent ingredient is the exact iteration formula for \(\tau_n\), which was checked in the primary full text. The source also proves that these points form an \((n-1)\)-simplex and that \(\Delta_n\) is integrally equivalent to a lecture-hall simplex.

A later full paper on stack-sorting simplex geometry was also inspected. It proves that all stack-sorting polytopes are simplices, computes relative volumes for \(Ln1\) simplices, and studies lattice points. Its full text contains no occurrence of “orthogonal”, “inradius”, “circumradius”, or “sphere” in the sense of this theorem.

The accompanying `verify.py` checks \(3\le n\le100\). It verifies the edge orthogonality and lengths, the telescoping normal norm, the inradius tangencies, the all-vertex sphere, the rational minimum-sphere weights, every active and inactive distance inequality, the triangular-number contact transition, and strict separation between the all-vertex sphere and the minimum sphere for \(n\ge4\).

## Relationship to prior work
Lee, Mitchell, and Vindas-Meléndez introduced these stack-sorting simplices and singled out \(\tau_n=23\cdots n1\). They prove the explicit iterate formula, simplex structure, hollowness, and integral equivalence with the lecture-hall simplex. Integral equivalence is not a Euclidean isometry, so it does not determine any of the metric formulas above.

Ake, Lewis, Louie, and Vindas-Meléndez later proved that every stack-sorting polytope is a simplex and that all \(Ln1\) stack-sorting simplices have relative volume \(1\). Their paper likewise does not identify the mutually perpendicular edge basis of \(\Delta_n\), an inradius, or a minimum enclosing sphere.

General right-simplex formulas become applicable only after (5)--(6) are recognized. The minimum-enclosing theorem here also uses the special arithmetic progression of squared edge lengths
\[
k(k-1),
\]
which produces the exact threshold
\[
q(q-1)<2n\le q(q+1)
\]
and the triangular contact jump.

Targeted published-result searches under “stack-sorting simplex”, “right simplex”, “orthogonal edges”, “inradius”, “minimum enclosing sphere”, and “triangular contact” did not locate a statement implying the theorem.

## Limitations
The result concerns the distinguished source family \(\tau_n=23\cdots n1\), not every stack-sorting simplex.

The formulas depend on the standard permutation-coordinate Euclidean realization. They are not invariants of the source's integral-equivalence class.

The all-vertex circumsphere should not be confused with the minimum enclosing sphere: they agree for the right triangle \(n=3\), but differ from \(n=4\) onward.

A general treatment of right simplices can reproduce the optimization once the orthogonal edge spectrum is known. The object-specific contributions are the orthogonality theorem, the exact edge spectrum, and the resulting closed triangular-number contact law.

## References
1. Eon Lee, Carson Mitchell, and Andrés R. Vindas-Meléndez, *Stack-sorting simplices: geometry and lattice-point enumeration*, arXiv:2308.16457, first public version 2023-08-31.
2. Cameron Ake, Spencer F. Lewis, Amanda Louie, and Andrés R. Vindas-Meléndez, *On the geometry of stack-sorting simplices*, arXiv:2508.00219, first public version 2025-07-31; *American Journal of Combinatorics* 4 (2025), 52--68, DOI 10.63151/amjc.v4i.35.
