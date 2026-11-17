# Universal two-level normal-cone angle inversion in orthogonal regular-polygon joins

## Finding

For all integers \(p,q\ge3\), let \(P_{p,q}\subset\mathbb R^4\) be the convex hull of unit-circumradius regular \(p\)- and \(q\)-gons centered at the origin in mutually orthogonal two-planes. For a vertex \(v\), define its **normalized exterior solid angle** \(\omega(v)\) to be the surface-probability of the normal cone \(N_{P_{p,q}}(v)\cap S^3\); equivalently, the probability that a uniform spherical linear objective is uniquely maximized at \(v\).

Put \(a=\pi/p\), \(b=\pi/q\), and
\[
F(p,q)=\frac{pq}{\pi^2}\int_0^a\!\int_0^b
\frac{\cos^2u}{\cos^2u+\cos^2v}\,dv\,du.
\]
Then every vertex of the first polygon has angle \(F(p,q)/p\), and every vertex of the second has angle \((1-F(p,q))/q\). The double integral has the exact one-dimensional reduction
\[
F(p,q)=\frac{pq}{\pi^2}\int_0^{\pi/p}
\frac{\cos u}{\sqrt{1+\cos^2u}}\arctan\!\left(
\frac{\cos u\tan(\pi/q)}{\sqrt{1+\cos^2u}}\right)du.
\]
For every \(3\le p<q\), there is a strict *two-level reversal*:
\[
\boxed{\quad\frac p{p+q}<F(p,q)<\frac12,\qquad
\frac{F(p,q)}p>\frac{1-F(p,q)}q.\quad}
\]
Thus the more numerous \(q\)-gon vertices collectively win a random objective more often, although each individual \(p\)-gon vertex wins more often than each individual \(q\)-gon vertex. Equal polygon sizes give exactly one angular level, \(\omega(v)=1/(2p)\). The function \(F(p,q)\) is strictly increasing in \(p\) and strictly decreasing in \(q\), and
\[
\lim_{q\to\infty}F(p,q)
=1-\frac p{\pi\sqrt2}\arctan\left(\frac{\tan(\pi/p)}{\sqrt2}\right).
\]
For the square–pentagon configuration, the unique nine-vertex four-dimensional maximal-volume inscribed polytope, numerical evaluation of the exact integral gives \(F(4,5)\approx0.479684224565\): each of four square vertices has angle about \(0.119921056141\), and each of five pentagon vertices about \(0.104063155087\).

## Assumptions and scope

The polygons are convex regular polygons of radius exactly one, embedded in perpendicular two-planes through the origin, with all \(p+q\) vertices distinct. The ambient space and normal cones use the Euclidean inner product. All claims hold for every pair of integers \(p,q\ge3\); the strict inequalities refer to the ordered case \(p<q\). Angles are *normal-cone* spherical measures, not interior tangent-cone solid angles or ordinary planar vertex angles. Objective ties have zero spherical measure.

## Proof

**Angular and radial decomposition.** Let \(X\) be uniform on \(S^3\). The squared norm \(S\) of its projection onto the first two-plane has beta distribution \(\mathrm{Beta}(1,1)\), hence is uniform on \([0,1]\). Conditional directions within the two planes are independent and uniform on their circles, independent of \(S\). The unsigned angular distances from these directions to the nearest polygon vertex are independently \(U\sim\mathrm{Unif}[0,\pi/p]\) and \(V\sim\mathrm{Unif}[0,\pi/q]\). Consequently, the largest vertex objective in the two groups equals, respectively, \(\sqrt S\cos U\) and \(\sqrt{1-S}\cos V\). Conditional on \(U=u,V=v\), the first group wins precisely when
\[
S>\frac{\cos^2v}{\cos^2u+\cos^2v},
\]
whose conditional probability is \(\cos^2u/(\cos^2u+\cos^2v)\). Integrating yields \(F(p,q)\). Rotational symmetry within each polygon allocates its group's probability equally among its vertices, proving both angular formulas. Substitution \(t=\tan v\) gives the one-dimensional formula.

**Group ordering and limits.** Let independent \(R,T\) be uniform on \([0,1]\). The integrand can be written
\(H(\cos(\pi R/p),\cos(\pi T/q))\), where \(H(x,y)=x^2/(x^2+y^2)\) is strictly increasing in positive \(x\) and decreasing in positive \(y\). Thus \(F\) increases strictly with \(p\) and decreases strictly with \(q\). Symmetry gives \(F(q,q)=1/2\), so \(F(p,q)<1/2\) whenever \(p<q\). Sending \(q\to\infty\) sends the second cosine to one; elementary substitution \(t=\tan u\) gives the claimed limit \(F_\infty(p)\), with \(F(p,q)>F_\infty(p)\) at every finite \(q\).

**Per-vertex reversal for \(p\ge4\).** Write
\[
G(x)=\frac{\sin^2x}{2x^2(1+\cos^2x)}\quad (x>0).
\]
It is strictly increasing on \((0,\pi/4]\). Indeed, the sign of its derivative is the sign of \(h(x)=2x\cos x-\sin x(1+\cos^2x)\). Here \(h(0)=0\),
\[
h'(x)=\sin x\bigl(3\sin x\cos x-2x\bigr),
\]
and \(3\sin x\cos x-2x\) increases and then decreases on \([0,\pi/4]\), having derivative \(3\cos(2x)-2\), which changes sign once. Hence \(h\) increases then decreases; since \(h(\pi/4)=(\pi-3)/(2\sqrt2)>0\), it is positive throughout \((0,\pi/4]\). As \(G(\pi/4)=8/(3\pi^2)\), the uniform variable \(U\in[0,\pi/p]\) gives, for \(p\ge4\),
\[
\frac12-F_\infty(p)
=\mathbb E[U^2G(U)]<\frac8{3\pi^2}\frac{\pi^2}{3p^2}
=\frac8{9p^2}.
\]
For every integer \(p\ge4\), the elementary inequality \(9p^2\ge32p+16\) yields \(1/2-8/(9p^2)\ge p/(2p+1)\). Therefore, if \(q\ge p+1\),
\[
F(p,q)>F_\infty(p)>\frac p{2p+1}\ge\frac p{p+q}.
\]

**The remaining cases \(p=3\).** By Cauchy–Schwarz, for positive random variables \(A,B\),
\[
\mathbb E\left[\frac{A^2}{A^2+B^2}\right]
\ge\frac{(\mathbb EA)^2}{\mathbb E A^2+\mathbb EB^2}.
\]
Take \(A=\cos U\), \(B=\cos V\), with \(U\) uniform on \([0,\pi/3]\). Then \((\mathbb EA)^2=27/(4\pi^2)\), and \(\mathbb EA^2=1/2+3\sqrt3/(8\pi)\). The rational bounds \(3<\pi<22/7\), \(\sqrt3<7/4\) imply
\[
(\mathbb EA)^2>\frac{1323}{1936},\qquad
\mathbb EA^2<\frac{23}{32}.
\]
If \(q\ge5\), then \(\mathbb EB^2\le1\), so
\[
F(3,q)>\frac{1323/1936}{55/32}>\frac38\ge\frac3{3+q}.
\]
For \(q=4\), \(\mathbb EB^2=1/2+1/\pi<5/6\), and therefore
\[
F(3,4)>\frac{1323/1936}{149/96}>\frac37.
\]
All comparisons of rational constants follow by cross-multiplication. This completes the strict per-vertex ordering for every \(p<q\), and symmetry handles \(p=q\).

## Verification

Run `python3 check_angles.py` (Python standard library only). It evaluates the original two-dimensional integral independently of the reduced one-dimensional integral for seven parameter pairs, verifies group symmetry and the strict inequalities over a range of integer pairs, and performs a seeded angular/radial Monte Carlo check. The exact proofs above establish the universal claims; numerical tests do not certify the infinite parameter range or uniqueness of any other configurations.

## Relationship to prior work

Medgyes [1] establishes that the orthogonal square–pentagon join is the unique nine-vertex maximizer of four-dimensional inscribed volume. The maximal-volume assertion is not reproved here. Fitisone and Zhou [2] develop general higher-dimensional solid-angle computations for polyhedral cones, including hypergeometric-series methods. Here the new claim is an explicit one-dimensional formula and a strict *complete ordering* of the two normal-cone angle levels for every orthogonal join of two regular polygons. It does not assert a new general algorithm for polyhedral solid angles. Scalar laws for maximum support values, and formulas for facet measure or exterior dihedral angles, do not themselves determine which labeled vertex wins a generic linear objective.

## Limitations

The result uses unit circumradii in perpendicular planes; arbitrary unequal scale factors do not satisfy the stated universal ranking without separate analysis. The displayed decimal values are numerical approximations, not symbolic closed forms. The comparison against indexed literature cannot exclude an unindexed equivalent special-case theorem. The theorem concerns exterior normal cones, not their interior dual cones, 

## References

1. Csaba Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078, v1, publicly posted 2026-11-06, https://arxiv.org/html/2611.10078v1.
2. Allison Fitisone and Yuan Zhou, *Solid angle measure of polyhedral cones*, arXiv:2304.11102, publicly posted 2023-04-21, https://arxiv.org/abs/2304.11102.
