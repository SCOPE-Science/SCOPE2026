# Exact fractional illumination of every equiangular polygon
## Finding
Let \(P\subset\mathbb R^2\) be a convex equiangular \(n\)-gon with \(n\ge3\). Let \(i^*(P)\) denote the fractional illumination number introduced by Naszódi, and put
\[
r_n=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
Then
\[
\boxed{
i^*(P)=\frac{n}{r_n}
=
\begin{cases}
\displaystyle \frac{2n}{n-1},&n\ \text{odd},\\[6pt]
\displaystyle \frac{2n}{n-2},&n\ \text{even}.
\end{cases}}
\tag{1}
\]

Thus the fractional illumination number of an equiangular polygon is determined entirely by its normal fan and is independent of its side lengths.

For example,
\[
i^*(P_3)=3,\qquad
i^*(P_4)=4,\qquad
i^*(P_5)=\frac52,\qquad
i^*(P_6)=3,\qquad
i^*(P_8)=\frac83.
\]
The two parity branches both tend to
\[
2
\]
as \(n\to\infty\).

There is also an equality-rigidity statement. If \(\mu\) is an optimal finite-support fractional illumination, then every vertex receives exactly total weight \(1\), and every direction in the support of \(\mu\) illuminates exactly \(r_n\) vertices.

## Assumptions and scope
An equiangular convex \(n\)-gon has every interior angle equal to
\[
\alpha_n=\pi-\frac{2\pi}{n}.
\tag{2}
\]
Directions are identified with points of the unit circle.

For a vertex \(v_j\), let \(I_j\subset S^1\) be the set of directions illuminating \(P\) at \(v_j\). The tangent cone at \(v_j\) has aperture \(\alpha_n\), hence \(I_j\) is an open arc of angular length \(\alpha_n\).

Because consecutive edge directions turn by exactly
\[
\frac{2\pi}{n},
\]
the inward angle bisectors at the vertices are equally spaced by the same angle. Therefore the \(n\) arcs
\[
I_0,\ldots,I_{n-1}
\]
are congruent and equally spaced around \(S^1\).

Only this normal-fan geometry is used. No equality of side lengths, cyclicity, or central symmetry is assumed.

## Proof
Set
\[
\delta=\frac{2\pi}{n}.
\]
The centers of the illumination arcs \(I_j\) form a regular \(n\)-point set on \(S^1\), and each arc has length
\[
\alpha_n
=
\pi-\frac{2\pi}{n}
=
\left(\frac n2-1\right)\delta.
\tag{3}
\]

Define
\[
r_n=\left\lfloor\frac{n-1}{2}\right\rfloor.
\tag{4}
\]

We first determine how many vertex arcs can contain one direction. A point of \(S^1\) lies in \(I_j\) exactly when the center of \(I_j\) lies in an open arc of length \(\alpha_n\) around that point. Since the centers are \(\delta\)-spaced, an open arc of length (3) contains at most
\[
r_n
\]
centers. Indeed, if \(n\) is odd then
\[
\frac{\alpha_n}{\delta}=\frac{n-2}{2}
\]
is a half-integer, giving at most \((n-1)/2\) centers. If \(n\) is even then this ratio is the integer \((n-2)/2\), and openness of the arc excludes simultaneously taking both endpoints, again leaving at most
\[
\frac{n-2}{2}
\]
centers.

Let \(\mu\) be any finite-support fractional illumination of \(P\). Each vertex constraint gives
\[
\mu(I_j)\ge1.
\]
Summing the \(n\) inequalities,
\[
n
\le
\sum_{j=0}^{n-1}\mu(I_j).
\tag{5}
\]
If
\[
c(u)=\#\{j:u\in I_j\},
\]
then \(c(u)\le r_n\) for every direction \(u\), so
\[
\sum_{j=0}^{n-1}\mu(I_j)
=
\sum_{u\in\operatorname{supp}\mu}c(u)\mu(\{u\})
\le
r_n\mu(S^1).
\tag{6}
\]
Equations (5)--(6) prove
\[
i^*(P)\ge\frac{n}{r_n}.
\tag{7}
\]

For the matching upper bound, index vertices cyclically modulo \(n\). For every \(j\), consider the block
\[
B_j=\{j,j+1,\ldots,j+r_n-1\}.
\]
The centers of the arcs indexed by \(B_j\) span angular length
\[
(r_n-1)\delta<\alpha_n.
\]
Hence
\[
\bigcap_{\ell\in B_j}I_\ell
\]
is nonempty. Choose a direction \(u_j\) in this intersection and define
\[
\mu_0=\frac1{r_n}\sum_{j=0}^{n-1}\delta_{u_j}.
\tag{8}
\]
Each vertex index belongs to exactly \(r_n\) of the cyclic blocks \(B_j\). Thus every vertex receives total illuminating weight at least
\[
r_n\cdot\frac1{r_n}=1.
\tag{9}
\]

It remains only to check nonvertex boundary points. If \(x\) lies in the relative interior of an edge with endpoint \(v\), write
\[
x=(1-s)v+s w,
\qquad 0<s<1,
\]
where \(w\) is the other endpoint. If \(u\) illuminates \(v\), choose \(\varepsilon>0\) with
\[
v+\varepsilon u\in\operatorname{int}P.
\]
Then
\[
x+(1-s)\varepsilon u
=
(1-s)(v+\varepsilon u)+s w
\in\operatorname{int}P.
\]
So every direction illuminating \(v\) also illuminates \(x\). Consequently (9) implies that \(\mu_0\) fractionally illuminates every boundary point. Its total mass is
\[
\mu_0(S^1)=\frac{n}{r_n},
\]
which together with (7) proves (1).

Finally suppose \(\mu\) is optimal. Then equality holds throughout
\[
n
\le
\sum_j\mu(I_j)
\le
r_n\mu(S^1)
=
n.
\]
Therefore each of the \(n\) vertex inequalities is tight, and every atom of positive weight must satisfy
\[
c(u)=r_n.
\]
This proves the rigidity statement.

## Verification
The bundled `verify.py` independently checks the exact integer incidence inequalities and cyclic equal-weight construction for every
\[
3\le n\le500.
\]
It also performs an independent geometric sweep of every angular combinatorial cell for \(3\le n\le60\), confirming that no direction lies in more than \(r_n\) vertex illumination arcs.

It also verifies the special values
\[
3,\ 4,\ \frac52,\ 3,\ \frac83
\]
for \(n=3,4,5,6,8\), respectively.

The finite sweep is diagnostic only. The all-\(n\) result is the exact spacing-and-double-counting proof above.

## Relationship to prior work
Naszódi introduced fractional illumination as a fractional transversal problem. In the same paper he proved, for a regular pentagon \(P_5\),
\[
a(P_5)=2
\qquad\text{and}\qquad
i^*(P_5)\ge\frac52.
\]
The proof uses a fractional matching supported on the five vertex illumination sets. The present result shows that the lower bound is sharp and extends it from one regular pentagon to every equiangular polygon in every number of sides.

A later treatment of fractional illumination develops the subject further and proves general structural facts, including that illuminating all extreme points suffices for ordinary illumination. Its searchable full text contains no polygon or pentagon specialization.

The calculation can also be viewed as the exact fractional transversal number of a cyclic interval system. General fractional-covering theory supplies linear-programming duality, but the geometric reduction, the parity-sensitive rank
\[
r_n=\left\lfloor\frac{n-1}{2}\right\rfloor,
\]
and the resulting illumination formula are not supplied by the checked sources.

Targeted searches under fractional illumination, regular and equiangular polygons, cyclic illumination arcs, pentagons, and the two rational formula branches did not locate an implication-equivalent published evaluation.

## Limitations
The theorem uses equiangularity essentially: it forces both equal tangent-cone apertures and equally spaced arc centers. It does not give the fractional illumination number of an arbitrary polygon.

The result does not classify every optimal measure beyond the necessary equality conditions stated above.

The argument is elementary once the illumination problem is reduced to a cyclic interval system, so an unindexed observation in illumination or fractional-covering notes remains the main originality risk.

The regular-pentagon lower bound
\[
i^*(P_5)\ge\frac52
\]
is prior work and is not claimed as new.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* 4 (2009), 83--88. DOI: 10.55016/ojs/cdm.v4i2.62022.
2. L. Rotem, A. Schejter, and B. A. Slomka, *The complex Illumination problem*, *Combinatorica* 46 (2026), article 3. DOI: 10.1007/s00493-025-00195-7.
