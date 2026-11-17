# A sharp symmetry-breaking threshold for fourfold pedal returns of rectangles

## Finding

Let \(Q=[-a,a]\times[-b,b]\), with \(a\ge b>0\). Fix an interior point \(P=(x,y)\), project it perpendicularly to the four successive supporting lines of \(Q\), join the feet in their cyclic order, and repeat the construction using the same \(P\). Call a point *admissible* if all four steps have consecutive distinct vertices and no line used for projection passes through \(P\). For admissible \(P\), the fourth quadrilateral is directly similar to \(Q\), with positive scale \(\sigma(P)\).

**Theorem.** Define
\[
A=a^2,\qquad B=b^2,\qquad U=\sqrt{B(4A+B)},\qquad r_*=\sqrt{2+\sqrt5}.
\]
The maximum of \(\sigma(P)\) over all admissible interior points is
\[
\boxed{\sigma_{\max}=\begin{cases}
\dfrac{AB}{(A+B)^2},&a/b\le r_*,\\[5pt]
\dfrac{B}{2(U-B)},&a/b>r_*.
\end{cases}}
\]
For \(a/b\le r_*\), the **only** maximizing point is the center \(P=(0,0)\). For \(a/b>r_*\), the **only** maximizing points are
\[
\boxed{P_\pm=(\pm\sqrt{A-U},0).}
\]
Both points are in the interior and are admissible. The maximal area ratio after four pedal steps is \(\sigma_{\max}^2\). Thus a rectangle's optimal pedal center undergoes a sharp change from one central point to two symmetric off-center points at the exact aspect ratio \(r_*\approx2.058171027\).

## Assumptions and scope

All lengths are Euclidean and \(a,b\) are arbitrary positive real numbers with \(a\ge b\). The polygon consists of four *ordered* vertices; the lines are entire side-supporting lines, not merely segments. The same fixed interior point is used at every step. The result concerns the four-step **similarity scale**, not the area of the first pedal quadrilateral or the higher-dimensional box pedal operation. Non-admissible interior inputs are omitted from the iteration domain but are covered by the upper-bound calculation below.

## Proof

**1. Product formula and exact rectangular objective.** For an admissible quadrilateral, the four-step pedal theorem [1, Theorem 2.2, Eq. (2)] gives
\[
\sigma(x,y)=\frac{\prod_{\text{sides }\ell}\operatorname{dist}(P,\ell)}{\prod_{\text{vertices }v}|P-v|}
=\frac{(a^2-x^2)(b^2-y^2)}{R_{a-x}(y)R_{a+x}(y)},
\]
where
\[
R_h(y)=\sqrt{\bigl(h^2+(b-y)^2\bigr)\bigl(h^2+(b+y)^2\bigr)}.
\]
All denominators are positive in the open rectangle. This formula provides a positive objective on the full open rectangle even where the pedal iteration is formally inadmissible.

**2. Strict elimination of the short-axis coordinate.** Put \(t=y^2/b^2\in[0,1)\) and \(H=h^2/b^2>0\). Direct expansion gives the exact identity
\[
R_h(y)^2-(1-t)^2R_h(0)^2
=b^4 Ht\bigl[2H+6-(H+2)t\bigr]\ge0.
\]
The right side is strictly positive for \(t>0\). Moreover, whenever \(h\ge b\),
\[
R_h(y)^2-R_h(0)^2=y^2\bigl[2(h^2-b^2)+y^2\bigr]\ge0.
\]
At least one of \(a-x,a+x\) is at least \(a\ge b\). Apply the latter inequality to this factor and the former to the other factor to get, for \(y\ne0\),
\[
R_{a-x}(y)R_{a+x}(y)>(1-t)R_{a-x}(0)R_{a+x}(0).
\]
Since \(b^2-y^2=b^2(1-t)\), the objective is strictly smaller off the long central axis:
\[
\sigma(x,y)<\sigma(x,0)\quad(y\ne0).
\]

**3. One-variable maximization and equality.** Write \(s=x^2\in[0,A)\). At \(y=0\),
\[
\sigma(x,0)=f(s)=\frac{B(A-s)}{s^2+2(B-A)s+(A+B)^2}.
\]
The denominator is the positive product \(\bigl((a-x)^2+b^2\bigr)\bigl((a+x)^2+b^2\bigr)\). Differentiation gives
\[
f'(s)=\frac{B\left((s-A)^2-B(4A+B)\right)}{\left[s^2+2(B-A)s+(A+B)^2\right]^2}.
\]
Because \(s<A\), this derivative is positive exactly for \(s<A-U\) and negative for \(s>A-U\). If \(A\le U\), the unique maximizing \(s\) is \(0\). If \(A>U\), the unique maximizing \(s\) is \(A-U\), yielding two symmetric values of \(x\). The condition \(A>U\) is equivalent to \((A/B)^2>4(A/B)+1\), namely \(a/b>\sqrt{2+\sqrt5}\). Substituting the two maximizing values yields the claimed scale values. At equality \(A=U\), \(f'\) is negative for every \(s>0\), so the center remains the unique maximizer.

**4. Admissibility at every maximizing point.** In fact, every axial interior point \(P=(x,0)\) is admissible. Translate \(P\) to the origin and let \(h_+=a-x>0\) and \(h_-=a+x>0\). The first pedal quadrilateral has vertices on the axes \((0,-b),(h_+,0),(0,b),(-h_-,0)\), in cyclic order. The second has right vertices \((L_+,\pm H_+)\) and left vertices \((-L_-,\pm H_-)\), where
\[
L_\pm=\frac{h_\pm b^2}{h_\pm^2+b^2}>0,
\qquad H_\pm=\frac{b h_\pm^2}{h_\pm^2+b^2}>0.
\]
The two vertical side lines of this second quadrilateral have perpendicular feet \((L_+,0)\) and \((-L_-,0)\). Its upper supporting line has strictly positive vertical intercept, so its perpendicular foot has strictly positive ordinate; the lower foot is its reflection with strictly negative ordinate. The third quadrilateral therefore has four distinct vertices, consisting of two nonzero axial points and two nonaxial points on opposite sides of the axis. Each of its four sides joins an axial point to a nonaxial point, and consequently none passes through the origin. In the first two iterates the side lines likewise avoid the origin, and consecutive vertices are distinct. Thus each four-step construction is defined. This proves both attainability and the complete equality classification.

Finally the fourth polygon is a direct similarity of the original by [1, Theorem 2.2], and its Euclidean area ratio is \(\sigma(P)^2\).  \(\square\)

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The checker uses exact rational arithmetic to verify the key elimination identity and reduced derivative numerator on deterministic rational grids; it independently reconstructs four successive perpendicular-foot polygons with coordinate geometry, verifies the published similarity multiplier, and tests the explicit optimizing points on both sides of the threshold. Its deterministic test count is printed at completion. Finite testing is a supplementary consistency check, not an infinite-domain proof; the proof is the algebra and inequality argument above.

## Relationship to prior work

Zwierzyński [1] proves the general four-step return theorem and provides the distance-product scale formula, both used here; that source also proves maximality of the incircle center for tangential polygons. A non-square rectangle is not tangential, and [1] does not give the rectangle optimization or aspect-ratio transition proved above. Blažek and Pech [2] derive the area of a *first* pedal quadrilateral and study quadrilateral shape conditions, not the fourth-iterate optimal scale. Prior investigations of triangle pedal-area maximization [3] do not imply a nonsquare rectangle phase transition. The new content is the globally sharp rectangular optimization, its equality set, and the aspect-ratio threshold, not the general similarity theorem or the existence of a distance-product formula.

## Limitations

The theorem is restricted to rectangles and to admissible *interior* projection points. It does not optimize outside the rectangle, arbitrary quadrilaterals, general projection angles, or other pedal periods. Independent verification and a complete historical-priority certification have not been performed. The published distance-product theorem is an essential prior input, not a new lemma.

## References

1. Michał Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1 (first public date 2026-10-31), https://arxiv.org/abs/2611.01247. Theorem 2.2 and Corollary 2.3.
2. Jiří Blažek and Pavel Pech, *Pedal quadrilateral and related topics*, *Journal of Geometry* 117, article 39 (2026), https://doi.org/10.1007/s00022-026-00818-4 (publicly dated 2026-09-24).
3. P. Humenberger and M. de Villiers, *Optimising Miquel circles centre triangles and third pedal triangles*, https://doi.org/10.1080/00255572.2025.2539599 (published 2026).
