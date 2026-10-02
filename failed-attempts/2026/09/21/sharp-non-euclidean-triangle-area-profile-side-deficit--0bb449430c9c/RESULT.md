# Sharp non-Euclidean triangle area profiles at fixed side deficit

## Result

Let a nondegenerate geodesic triangle have side lengths \(a,b,c\), perimeter
\[
p=a+b+c,
\]
and side-isoperimetric deficit
\[
Q=(a-b)^2+(b-c)^2+(c-a)^2.
\]
Write
\[
X=\frac{Q}{p^2},\qquad u=\sqrt{2X},\qquad m=\frac p6.
\]
Every nondegenerate triangle satisfies \(0\le X<1/2\), hence \(0\le u<1\).

For \(\kappa\in\{+1,-1\}\), define
\[
\tau_{+1}(t)=\tan\frac t2,
\qquad
\tau_{-1}(t)=\tanh\frac t2.
\]
Here \(\kappa=+1\) means the unit sphere and \(\kappa=-1\) the curvature \(-1\) hyperbolic plane. In the spherical case assume the triangle is the minor-arc geodesic triangle and \(p<2\pi\). Let \(A_\kappa\) denote its area.

Define
\[
U_\kappa(p,X)=4\arctan\sqrt{
\tau_\kappa(p/2)\,
\tau_\kappa\!\bigl(m(1+2u)\bigr)\,
\tau_\kappa\!\bigl(m(1-u)\bigr)^2},
\]
and, for \(0\le X<1/8\),
\[
L_\kappa(p,X)=4\arctan\sqrt{
\tau_\kappa(p/2)\,
\tau_\kappa\!\bigl(m(1-2u)\bigr)\,
\tau_\kappa\!\bigl(m(1+u)\bigr)^2}.
\]

Then the complete fixed-\((p,Q)\) area range is
\[
\boxed{L_\kappa(p,X)\le A_\kappa\le U_\kappa(p,X)}
\qquad(0\le X<1/8),
\]
while
\[
\boxed{0<A_\kappa\le U_\kappa(p,X),\qquad \inf A_\kappa=0}
\qquad(1/8\le X<1/2).
\]
Every value in the displayed interval is realized by a triangle, except that the lower value \(0\) in the second regime is only a degenerate boundary limit.

The upper extremizer is unique up to permutation and has side multiset
\[
\boxed{
\left\{\frac{p(1-u)}3,\frac{p(2+u)}6,\frac{p(2+u)}6\right\}.
}
\]
For \(0<X<1/8\), the lower extremizer is unique up to permutation and has side multiset
\[
\boxed{
\left\{\frac{p(1+u)}3,\frac{p(2-u)}6,\frac{p(2-u)}6\right\}.
}
\]
Thus the lower envelope undergoes a sharp, curvature-independent phase transition at
\[
\boxed{Q/p^2=1/8}.
\]
At the transition, the lower isosceles branch reaches the flat ratio \(2:1:1\).

The same formulas for curvature \(\pm R^{-2}\) follow by replacing each length by length divided by \(R\), applying the unit-curvature formula, and multiplying area by \(R^2\).

## Proof

Put \(s=p/2\) and introduce the triangle-inequality slacks
\[
x=s-a,\qquad y=s-b,\qquad z=s-c.
\]
For a nondegenerate triangle, \(x,y,z>0\) and
\[
x+y+z=s.
\]
Because \((a,b,c)=(y+z,z+x,x+y)\), subtracting the means gives
\[
\sum_{\rm cyc}\left(x-\frac s3\right)^2
=\sum_{\rm cyc}\left(a-\frac p3\right)^2
=\frac Q3.
\]
Hence the admissible slack triples form the intersection of the plane \(x+y+z=s\) with a sphere centered at \((s/3,s/3,s/3)\), restricted to the positive octant.

The classical spherical and hyperbolic L'Huilier-Heron formulas can be written uniformly as
\[
\boxed{
\tan^2\frac{A_\kappa}{4}
=\tau_\kappa(s)\tau_\kappa(x)\tau_\kappa(y)\tau_\kappa(z).
}
\]
In the spherical case, \(s<\pi\), so all four arguments lie in \((0,\pi)\) and the principal branch is unambiguous. Since \(\arctan\sqrt{\cdot}\) is increasing, it remains to optimize
\[
F_\kappa(x,y,z)=\sum_{cyc}\log\tau_\kappa(x)
\]
under the two moment constraints.

Let
\[
g_\kappa(t)=\log\tau_\kappa(t).
\]
Then
\[
g'_{+1}(t)=\csc t,
\qquad g'_{-1}(t)=\operatorname{csch} t.
\]
Both derivatives are strictly convex on the relevant domains, since
\[
(\csc t)''=\frac{1+\cos^2t}{\sin^3t}>0,
\qquad
(\operatorname{csch}t)''=\frac{2+\sinh^2t}{\sinh^3t}>0.
\]
At an interior constrained critical point, Lagrange multipliers give
\[
g'_\kappa(x_i)=\lambda+\mu x_i.
\]
A strictly convex function intersects an affine function in at most two points. Therefore every interior extremizer has at least two equal slacks.

Set
\[
d=\sqrt{Q/18}=m u,
\qquad m=s/3,
\qquad u=\sqrt{2Q/p^2}.
\]
The two possible two-value slack multisets are
\[
\{m(1+2u),m(1-u),m(1-u)\}
\]
and
\[
\{m(1-2u),m(1+u),m(1+u)\}.
\]
The second exists in the positive octant exactly when \(u<1/2\), i.e. \(X<1/8\).

To order these critical values, for \(0<d<m/2\) define
\[
D(d)=g(m+2d)+2g(m-d)-g(m-2d)-2g(m+d),
\]
where \(g=g_\kappa\). If \(h=g'\), then
\[
D'(d)=2\{h(m+2d)+h(m-2d)-h(m+d)-h(m-d)\}.
\]
Strict convexity of \(h\) implies that \(h(m+t)+h(m-t)\) is strictly increasing in \(t>0\). Hence \(D'(d)>0\), while \(D(0)=0\). Thus the first branch has strictly larger area than the second whenever \(Q>0\).

For \(X<1/8\), the whole moment circle lies in the positive octant, so compactness and the critical-point classification give the stated minimum and maximum. Substituting the two slack patterns into L'Huilier's formula gives \(L_\kappa\) and \(U_\kappa\). Translating back by \(a=s-x\) gives the two displayed isosceles side multisets.

At \(X=1/8\), the moment circle first touches a coordinate plane. For every \(1/8\le X<1/2\), its closure intersects a coordinate plane, giving degenerate triples with one slack zero and hence area zero. The positive part consists of symmetric open arcs whose boundary area tends to zero; the only interior critical pattern is the upper isosceles branch. Therefore its value is the global maximum, the infimum is zero, and continuity on an arc realizes every intermediate positive area.

This proves the complete profile.

## Relation to prior work

Svrtan and Veljan (Forum Geometricorum 12 (2012), 197--209) proved spherical and hyperbolic versions of several classical triangle inequalities, including explicit non-Euclidean Finsler--Hadwiger inequalities. Their Theorems 3.3 and 3.4 are one-sided inequalities obtained from Cagnolli formulas and Jensen convexity; they do not determine the complete area range at fixed perimeter and fixed Euclidean side deficit \(Q\).

Bogosel, *Optimal Finsler--Hadwiger Inequalities* (Results in Mathematics, 2025; arXiv:2508.06285), determines the sharp Euclidean Blaschke--Santaló diagram for perimeter, area and the same deficit \(Q\). In particular, the Euclidean fixed-\((p,Q)\) profile is prior work and is not claimed here. The result above supplies the analogous complete vertical profiles for curvature \(+1\) and \(-1\), using the classical non-Euclidean Heron/L'Huilier formulas.

Targeted searches through the current literature used combinations of *spherical/hyperbolic Finsler-Hadwiger*, *optimal Finsler-Hadwiger*, *fixed perimeter*, *side deficit*, *sum of squared side differences*, *triangle area*, and *Blaschke-Santaló diagram*. No located source stated the two-sided non-Euclidean profile, the universal \(Q/p^2=1/8\) lower-envelope transition, or the full interval-realization statement. Originality is therefore claimed only to the best of our knowledge.

## Limitations

- The spherical statement is restricted to minor-arc geodesic triangles with perimeter \(p<2\pi\); larger-perimeter spherical triangles require separate branch analysis.
- The hyperbolic statement is for curvature \(-1\), with other constant negative curvatures obtained by scaling.
- The deficit \(Q\) is the Euclidean quadratic dispersion of the three side lengths; no claim is made that it is the only natural non-Euclidean asymmetry measure.
- The Euclidean exact profile is prior work and is explicitly excluded from the novelty claim.
- Equivalent formulations may exist in older non-Euclidean triangle-inequality literature under different variables.

## Reproducibility

`artifacts/verify_profiles.py` parameterizes the fixed-moment slack circle and samples the claimed spherical and hyperbolic profiles. It uses only the Python standard library. The executed check returned:

`PASS: sampled spherical and hyperbolic profiles agree with the formulas.`

The numerical check is supplementary; the proof above is analytic.

## References

1. D. Svrtan and D. Veljan, "Non-Euclidean versions of some classical triangle inequalities," *Forum Geometricorum* 12 (2012), 197--209. Public record: https://www.croris.hr/crosbi/publikacija/prilog-casopis/151282
2. B. Bogosel, "Optimal Finsler-Hadwiger Inequalities," *Results in Mathematics* (2025), DOI: https://doi.org/10.1007/s00025-025-02405-6 ; arXiv: https://arxiv.org/abs/2508.06285
3. Classical spherical L'Huilier formula: https://en.wikipedia.org/wiki/Spherical_trigonometry#Area_and_spherical_excess
4. A standard statement of the hyperbolic tangent-quarter-area Heron formula appears in: https://indico.eimi.ru/event/435/attachments/282/540/2.pdf
