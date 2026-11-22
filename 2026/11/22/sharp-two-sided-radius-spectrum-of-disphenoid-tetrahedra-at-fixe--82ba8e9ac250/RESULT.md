# Sharp two-sided radius spectrum of disphenoid tetrahedra at fixed box eccentricity

## Finding

Let \(T\) be a nondegenerate Euclidean disphenoid (a tetrahedron with congruent opposite-edge pairs), with insphere radius \(r>0\) and circumsphere radius \(R>0\). Up to a rigid motion it is the convex hull of
\[
(a,b,c),\quad (a,-b,-c),\quad (-a,b,-c),\quad (-a,-b,c),\qquad a\ge b\ge c>0.
\]
The positive numbers \(a,b,c\), up to permutation, are half the side lengths of its canonical symmetry-aligned circumscribed rectangular box; their squares are uniquely recovered from the three pairs of opposite-edge lengths. Define the scale-independent box eccentricity \(E=a/c\ge1\) and roundness \(h=r/R\). **The exact attainable interval for every prescribed \(E\ge1\)** is
\[
\boxed{\frac{1}{\sqrt{5+2(E^2+E^{-2})}}\ \le h\le\ \frac{1}{E+1+E^{-1}}.}
\]
Both bounds are sharp. If \(E>1\), equality on the lower side holds exactly for the two distinct similarity classes with box semiaxes proportional to \((E,E,1)\) or \((E,1,1)\). Equality on the upper side holds exactly for the geometric-progression class \((E,\sqrt E,1)\). Every intermediate roundness occurs, and each strict interior value corresponds to **exactly two** non-similar disphenoids with that eccentricity, distinguished by their middle-axis ratios. The branches meet only at the upper extremizer. For \(E=1\), the sole configuration is the regular tetrahedron and \(h=1/3\).

Equivalently, for a fixed \(0<h\le1/3\), the complete possible eccentricity interval is \(E_{\min}(h)\le E\le E_{\max}(h)\), where
\[
B=h^{-1}-1,\qquad Q=(h^{-2}-5)/2,
\]
\[
\boxed{E_{\min}(h)=\left(\frac{Q+\sqrt{Q^2-4}}2\right)^{1/2},\qquad E_{\max}(h)=\frac{B+\sqrt{B^2-4}}2.}
\]
The two extremizers are those identified above. As \(h\uparrow1/3\), with \(\delta=1/3-h\downarrow0\), the exact extremal shape-stability window is
\[
E_{\min}(h)=1+\frac{3\sqrt3}{2}\sqrt\delta+O(\delta),\qquad
E_{\max}(h)=1+3\sqrt\delta+O(\delta),
\]
and both leading coefficients are sharp.

## Assumptions and scope

A disphenoid here is a full-dimensional tetrahedron with three pairs of opposite equal edges. Such tetrahedra have equal-area congruent triangular faces. Their standard circumscribed-box coordinate description is the four-point display above, with strictly positive coordinates. The \(a,b,c\) are intrinsic up to permutation and a common factor. The parameter \(E\) compares the largest and smallest **box semiaxes**; it is not a ratio of edge lengths or a variance of squared edges. We use intrinsic Euclidean insphere and circumsphere radii, not arbitrary chosen balls. All bounds include their equality cases and all \(E\ge1\); degenerating tetrahedra are excluded.

## Proof

**Radii.** The three squared opposite-edge-pair lengths (possibly repeated) are \(4(b^2+c^2)\), \(4(a^2+c^2)\), and \(4(a^2+b^2)\). These recover \(a^2,b^2,c^2\) uniquely up to permutation, making \(E\) intrinsic. Every vertex of the coordinate tetrahedron has squared norm \(a^2+b^2+c^2\); by the sign symmetries the origin is its circumcenter. The four supporting facet equations have sign choices from \(x/a\pm y/b\pm z/c=\pm1\), with one common normal length \(\sqrt{a^{-2}+b^{-2}+c^{-2}}\). The origin is interior, so it is the incenter, with distance \(r=(a^{-2}+b^{-2}+c^{-2})^{-1/2}\) to all four faces. Consequently,
\[
h^{-2}=(a^2+b^2+c^2)(a^{-2}+b^{-2}+c^{-2}).
\]
Put \(a=Ec\), \(b=tc\) where \(1\le t\le E\), and write \(F=h^{-2}\). Cancelling the common scale gives
\[
F(E,t)=(E^2+t^2+1)(E^{-2}+t^{-2}+1)
=E^2+E^{-2}+3+(1+E^{-2})(t^2+E^2t^{-2}).
\]

**Two exact nonnegative slack identities.** Expansion and factorization yield, identically for positive \(E,t\),
\[
\boxed{F(E,t)-(E+1+E^{-1})^2
=(1+E^{-2})(t-E/t)^2,}
\]
\[
\boxed{5+2(E^2+E^{-2})-F(E,t)
=(1+E^{-2})\frac{(t^2-1)(E^2-t^2)}{t^2}.}
\]
Since \(1\le t\le E\), both right sides are nonnegative. Taking reciprocal square roots proves both inequalities and all equality conditions. If \(E>1\), the first vanishes precisely at \(t=\sqrt E\); the second vanishes precisely at \(t=1\) or \(t=E\). At \(E=1\), all three coincide. Since \(t\mapsto F(E,t)\) is continuous, every intermediate value occurs.

**Exact two-branch classification.** For a prescribed admissible \((E,h)\), define
\[
Z=\frac{h^{-2}-(E^2+E^{-2}+3)}{1+E^{-2}}.
\]
The middle-axis squared ratio \(z=t^2\) satisfies \(z^2-Zz+E^2=0\), so
\[
t_{\pm}=\sqrt{\frac{Z\pm\sqrt{Z^2-4E^2}}2}.
\]
For a strict interior \(h\), these are two distinct values in \((1,E)\); their product is \(E\). At the upper endpoint they merge to \(\sqrt E\), while at the lower endpoint they are \(1,E\). Different sorted semiaxis triples represent different similarity classes. There are no further solutions because the equation is quadratic in \(t^2\).

**Fixed-radius inverse bounds.** Both \(L(E)=[5+2(E^2+E^{-2})]^{-1/2}\) and \(U(E)=(E+1+E^{-1})^{-1}\) are continuous and strictly decreasing from \(1/3\) to zero on \([1,\infty)\) (strictly on \((1,\infty)\)). The requirement \(L(E)\le h\le U(E)\) therefore gives \(E\ge L^{-1}(h)=E_{\min}(h)\) and \(E\le U^{-1}(h)=E_{\max}(h)\). Solving the reciprocal quadratics produces the stated radicals and preserves sharpness.

**Near-regular stability.** Write \(h=1/3-\delta\). Then \(h^{-1}-1=2+9\delta+O(\delta^2)\) and \((h^{-2}-5)/2=2+27\delta+O(\delta^2)\). For \(s\to0\), \((1+s)+(1+s)^{-1}=2+s^2+O(s^3)\) and \((1+s)^2+(1+s)^{-2}=2+4s^2+O(s^3)\). Substituting into the endpoint equations gives the two asserted, attainable coefficients.

## Verification

The standalone \(\texttt{checks/exact\_profile\_check.py}\) uses exact rational arithmetic to check both polynomial slack identities and the reciprocal symmetry over 14,652 rational parameter pairs, giving 75,261 exact assertions including boundary cases and the motivating example. Run with \(\texttt{python3 checks/exact\_profile\_check.py}\). This is finite corroboration of the factorization, **not** a proof for all real parameters. All real-parameter assertions follow from the displayed algebra, factor signs, monotonicity, and quadratic reconstruction.

For a concrete comparison, the unit-circumradius tetrahedron with coordinates \((\pm2,\pm2,\pm1)/3\) at the four even-minus sign patterns has \(E=2\) and \(h^2=2/27\). It is one of the lower-bound extremizers. The corresponding upper-bound disphenoid has box semiaxes proportional to \((2,\sqrt2,1)\), and its roundness is \(2/7\).

## Relationship to prior work

Nour (2026), Theorem 2.3 and Example 2.6, establishes the optimal center-containing ball radius for a union-of-balls construction from a simplex whose incenter and circumcenter agree. Its three-dimensional example is the lower endpoint \((2,2,1)\) here. The previously known covering formula for unit-circumradius tetrahedra is \(M(h)=1/[2\sqrt{1-h^2}]\); composing that **prior** formula with our new sharp interval yields an exact attainable covering-radius interval at fixed \(E\):
\[
\frac1{2\sqrt{1-L(E)^2}}\le M\le\frac1{2\sqrt{1-U(E)^2}}.
\]
For \(E=2\) the two endpoints are \(3\sqrt3/10\) and \(7/(6\sqrt5)\), respectively. This is a specialization of the present classification using Nour's established monotone formula, not a claim to invent that formula.

Existing investigations of disphenoid radii supply raw geometric formulas; other recent sharp geometric results treat volume at fixed in- and circumradii or roundness at fixed *edge-square variance*. Neither parameter constraint fixes the extreme box-axis ratio \(E\). The present full two-sided sharp interval, its geometric-progression upper extremizer, its two-to-one shape spectrum, and the inverse eccentricity window are the specific assessed additions.

## Limitations

This theorem is specific to disphenoids (equicentric tetrahedra in their standard characterization), not arbitrary tetrahedra or higher-dimensional simplices. Similarity classes are identified by the ordered positive circumscribed-box semiaxes; the second parameter can take two values for generic fixed \((E,h)\). The cited source describing general disphenoid radii was available only at abstract level; an inaccessible or unindexed older result could affect historical priority. This work has not received independent mathematical audit or comprehensive historical-priority certification.

## References

- Chadi Nour, *A counterexample to the strong version of the union of uniform closed balls conjecture in dimensions three and higher*, arXiv:2611.14181v1, first posted 2026-11-10. Full text: https://arxiv.cnoctave.top/pdf/2611.14181 . See Theorem 2.3, Example 2.6, Section 3.
- Harish Chandra Rajpoot, *Analytical Solution of Disphenoid (Isosceles tetrahedron)*, June 2016, DOI:10.13140/RG.2.2.25136.20485. Accessible description: https://www.researchgate.net/publication/332864882_Analytical_Solution_of_Disphenoid_Isosceles_tetrahedron .
- *Sharp radius-ratio profile at fixed edge-square anisotropy for disphenoids*, published mathematical record, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-radius-ratio-profile-at-fixed-edge-square-anisotropy-for-d--77a188e3731e .
- *Sharp volume interval for concentric bicentric tetrahedra*, published mathematical record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-volume-interval-for-concentric-bicentric-tetrahedra--3c21c1faa6d8 .
