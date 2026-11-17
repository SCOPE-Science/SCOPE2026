# Four-step pedal return and aspect-ratio inversion for prisms over bicentric polytopes

## Finding

For a prism over any convex polytope with a common centered insphere and circumsphere, repeated projection of the origin to every facet hyperplane has a **four-step homothetic return**. Its even-step prism aspect ratio is inverted after two steps. The four-step multiplier, and the sharp condition for a two-step return, are explicit:

\[
\mathcal D^4(K_h)=\Gamma K_h,\qquad
\Gamma=\frac{t^2}{(1+s^2t^2)(s^2+t^2)},\quad
s=R/a,\quad t=h/a.
\]

For regular polygonal prism bases with at least five sides, this gives a genuinely non-box family whose minimal positive homothetic return exponent is four whenever \(h\ne a\).

## Assumptions and scope

Let \(m\ge2\) and let \(B\subset\mathbb R^m\) be full-dimensional, convex and with the origin in its interior. Every facet has a supporting equation \(u\cdot x=a\), where \(\|u\|_2=1\) and the fixed \(a>0\) is independent of the facet. Every vertex \(v\) of \(B\) satisfies \(\|v\|_2=R\) for fixed \(R\ge a\). Define \(K_h=B\times[-h,h]\), with \(h>0\). Its ambient Euclidean metric is the product-coordinate Euclidean metric. Let \(B^\circ=\{y\in\mathbb R^m:\langle x,y\rangle\le1\text{ for every }x\in B\}\).

For every full-dimensional polytope containing the origin in its interior, \(\mathcal D\) is the convex hull of the perpendicular feet from \(0\) to all affine supporting hyperplanes of **facets**; no arbitrary triangulation of nonsimplicial facets is permitted. Set

\[
\rho^2=\left(\frac{R^2}{a^4}+\frac1{h^2}\right)^{-1},\qquad
s=\frac Ra,\qquad t=\frac ha.
\]

## Proof

**Step 1: first pedal and polar join.** The side-facet hyperplanes of \(K_h\) have equations \(u_F\cdot x=a\) and feet \((a u_F,0)\). The two horizontal facets have feet \((0,\pm h)\). Since \(B^\circ=\operatorname{conv}\{u_F/a\}\), the first pedal is exactly

\[
\mathcal D(K_h)=\operatorname{conv}\bigl((a^2B^\circ)\times\{0\},(0,h),(0,-h)\bigr).
\]

This is a full-dimensional double pyramid over the polar base. Every facet consists of an apex joined to a facet of \(a^2B^\circ\), and polarity identifies those base facets with vertices \(v\) of \(B\). Thus all its facet inequalities are exactly

\[
\frac{\langle v,x\rangle}{a^2}+\frac{\epsilon z}h\le1,
\quad v\in\operatorname{vert}(B),\quad \epsilon\in\{-1,1\}.
\]

**Step 2: the second pedal.** Every displayed facet normal has squared norm \(R^2/a^4+1/h^2=1/\rho^2\). Its perpendicular foot is \(\rho^2(v/a^2,\epsilon/h)\). Taking the convex hull over the independent sign choices yields the exact Cartesian product

\[
\mathcal D^2(K_h)=\frac{\rho^2}{a^2}B\times\left[-\frac{\rho^2}h,\frac{\rho^2}h\right].
\]

Write \(\alpha=\rho^2/a^2=t^2/(1+s^2t^2)\) for the base multiplier and \(\beta=\rho^2/h^2=1/(1+s^2t^2)\) for the half-height multiplier. The new base inradius is \(\alpha a\) while the new half-height is \(\beta h\). Their dimensionless ratio is

\[
\frac{\beta h}{\alpha a}=\frac1t.
\]

The second pedal is a homothety of the original prism precisely when \(\alpha=\beta\), equivalently \(t=1\). For \(t\ne1\), the base and height scale differently.

**Step 3: return after four steps.** The new base is again bicentric, with radii \(\alpha a\) and \(\alpha R\), so its circumradius-to-inradius ratio is still \(s\), and its height ratio is \(1/t\). Reapplying Step 2 gives a new base multiplier \(\alpha(1/t)=1/(s^2+t^2)\). Hence

\[
\mathcal D^4(K_h)=\alpha(t)\alpha(1/t)K_h,
\quad
\Gamma=\frac{t^2}{(1+s^2t^2)(s^2+t^2)}.
\]

Since \(s\ge1\) and \(t>0\), the denominator is strictly larger than \(t^2\), so \(0<\Gamma<1\). The facet-foot construction is positively homogeneous: \(\mathcal D(cK)=c\mathcal D(K)\) for \(c>0\). Thus \(\mathcal D^{4j+r}(K_h)=\Gamma^j\mathcal D^r(K_h)\) for integers \(j\ge0\), \(0\le r<4\).

**Step 4: primitive four-step instances.** Let \(B\) be a regular \(n\)-gon with \(n\ge5\), circumradius \(R\), inradius \(a=R\cos(\pi/n)\), and \(h\ne a\). Every even iterate is a prism with \(2n\) vertices, while every odd iterate is a bipyramid with \(n+2\) vertices. A positive homothety cannot identify an even and odd iterate. Step 2 excludes a return after two steps because \(h\ne a\); consequently four is the least positive homothetic return exponent. The base and prism dimension are unbounded: any bicentric \(m\)-polytope supplies a corresponding \((m+1)\)-dimensional example.

As an explicit nonregular higher-dimensional example, take the tetrahedral base with vertices \((A,B,C)\), \((A,-B,-C)\), \((-A,B,-C)\), and \((-A,-B,C)\), where \(A,B,C>0\) and they are not all equal. The four facets have common distance \(a=(A^{-2}+B^{-2}+C^{-2})^{-1/2}\) from the origin; every vertex has norm \(R=\sqrt{A^2+B^2+C^2}\). Any prism over this tetrahedron with \(h\ne a\) has the same exact four-step return and two-step aspect inversion. These four-dimensional prisms are not rectangular boxes.

## Verification

A standalone numerical diagnostic, `verify_pedal.py`, constructs facet planes directly from independent convex-hull computations and compares all two- and four-step vertex sets with the formulas, for a regular pentagon base and a nonregular tetrahedral disphenoid base. Both tests pass at floating-point tolerance \(2\times10^{-6}\). These tests are finite diagnostics; the unrestricted theorem rests on the preceding exact polar/normal derivation. The source date and relevant published propositions were checked against the full arXiv HTML text.

## Relationship to prior work

Zwierzyński's Proposition 4.1 identifies the known two-step return for an already bicentric polytope; Proposition 4.2 proves the four-step return for rectangular boxes. The present theorem **does not claim those cases as new**. Instead, it classifies the pedal dynamics of a right prism over an arbitrary bicentric base, for which the prism itself generally fails to be tangential and is not a rectangular box. The exact prism-to-bipyramid normal geometry gives a new aspect inversion, a sharp two-step resonance criterion, and the general four-step contraction factor. The regular-polygon examples with at least five sides and the higher-dimensional nonregular-base examples lie beyond the stated rectangular-box family. The argument uses standard convex polarity as a tool, without claiming polarity itself as new.

## Limitations

The result requires both concentric spheres for the base, and the projection reference point must be their common center lifted to the prism's midplane. It does not classify arbitrary prisms, nonconcentric sphere configurations, or other starting points. Exact four-step return is asserted as a **positive homothety**, not as uniqueness of every possible Euclidean similarity. Published priority beyond the inspected sources is provisional; an unindexed general result about iterated facet-foot transforms may cover this special geometry.

## References

1. M. Zwierzyński, "When Pedal Shapes Come Back: a Complex Story," arXiv:2611.01247v1, first submitted 2026-10-31, https://arxiv.org/html/2611.01247v1.
2. G. M. Ziegler, *Lectures on Polytopes*, Graduate Texts in Mathematics 152, Springer, 1995, Chapter 2 (standard polar face correspondence).
