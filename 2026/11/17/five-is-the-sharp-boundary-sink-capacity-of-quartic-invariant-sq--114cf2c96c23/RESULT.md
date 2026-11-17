# Five is the sharp boundary-sink capacity of quartic invariant-square flows

## Finding

Consider the quartic planar family
\[
\dot x=(4x^2-1)f(x,y),\qquad
\dot y=(4y^2-1)g(x,y),
\]
where \(f\) and \(g\) are arbitrary real polynomials of total degree at most two. The closed square \(Q=[-1/2,1/2]^2\) is invariant.

**Theorem.** The boundary \(\partial Q\) contains at most **five distinct hyperbolic sinks** of the full planar flow, without any restriction on equilibria in the interior, and even when a boundary edge consists entirely of equilibria. The upper bound is **sharp on a nonempty open set in the full coefficient space**. More precisely, there are polynomials \(f,g\) for which \(\partial Q\) contains twelve distinct hyperbolic equilibria, exactly five sinks, six saddles and one source.

An exact-coefficient witness is
\[
\begin{split}
f(x,y)&=3600x^2-720x+3025y^2-1053,\\
g(x,y)&=5625x^2+4225y^2-1690y-1352.
\end{split}
\]
Its five boundary sinks are
\[
(u_+,-1/2),\quad(u_+,1/2),\quad(-1/2,v_+),\quad(1/2,v_+),\quad(-1/2,-1/2),
\]
where
\[
u_+=\frac1{10}+\frac{11\sqrt{11}}{120},\qquad
v_+=\frac15+\frac{3\sqrt{51}}{130}.
\]
In particular, five is a sharp upper bound for *full planar stability*, not merely stability along the invariant edges.

## Assumptions and scope

The polynomial coefficients are arbitrary real numbers; \(f,g\) have total degree \(\le2\). A hyperbolic sink is an equilibrium at which both eigenvalues of the full \(2\times2\) Jacobian have strictly negative real parts. The conclusion counts distinct equilibria lying on the four edges, including the corners, each exactly once. The theorem does not assume finite boundary equilibria, and makes no claims about interior equilibria, limit cycles, or global basins.

Along \(y=\pm1/2\), the restricted scalar flow is \(\dot x=(4x^2-1)f(x,\pm1/2)\). Along \(x=\pm1/2\), it is \(\dot y=(4y^2-1)g(\pm1/2,y)\). The factor \(4s^2-1\) is negative on the interior of each edge.

## Proof

**1. Cyclic alternation.** Suppose first that the boundary equilibrium set is finite. Each horizontal side has at most two noncorner equilibria, because the restricted \(f\) is a polynomial of degree at most two; each vertical side likewise has at most two from \(g\). Adding the four corners gives at most twelve boundary equilibria. The flow restricted to \(\partial Q\) is a continuous scalar flow around a circle with finitely many zeroes. Every full-planar hyperbolic sink attracts from both directions along this invariant circle. Between any two consecutive such sinks there must be at least one distinct zero of the oriented scalar vector field, by continuity and opposite signs near the two sinks. Consequently, if the total number of boundary equilibria is \(N\), the number \(S\) of hyperbolic sinks satisfies \(2S\le N\). When \(N\le11\), this already gives \(S\le5\).

**2. The extremal twelve-equilibrium case.** If \(N=12\), then both open horizontal sides contain exactly two roots of their quadratic restrictions and likewise for the two vertical sides. Let \(a\ne0\) be the coefficient of \(x^2\) in \(f\), and \(b\ne0\) the coefficient of \(y^2\) in \(g\). These coefficients are the same on the opposite parallel sides. Factoring each edge quadratic shows that its values at **both endpoints** have sign \(\operatorname{sgn}a\) on horizontal edges, respectively \(\operatorname{sgn}b\) on vertical edges. Since \(4s^2-1<0\) inside an edge, both horizontal edge flows point toward the **left corners** when \(a>0\), or toward the **right corners** when \(a<0\). Both vertical flows point toward the **bottom corners** when \(b>0\), or toward the **top corners** when \(b<0\). Thus exactly **one corner** is attracting along both of its incident edges, and no other corner can be a full-planar sink.

On each open edge, a quadratic with two simple roots has exactly one tangentially attracting root: the two derivatives have opposite signs, and the sign of the prefactor \(4s^2-1\) is fixed. At most four open-edge equilibria can therefore be full-planar sinks. Together with the single possible sink corner this yields \(S\le5\) also when \(N=12\). The argument does not assume that all twelve equilibria are hyperbolic: if some roots were repeated, their number of distinct roots would fall below twelve.

**3. Edges of equilibria.** If a whole edge is stationary because its restricted quadratic vanishes identically, any hyperbolic sink of the original full planar flow is structurally stable under sufficiently small changes to the coefficients, and remains on the invariant boundary: at an open-edge equilibrium the single simple tangential root persists by the implicit function theorem, while every corner stays fixed for all coefficients. Take a generic arbitrarily small coefficient perturbation eliminating every stationary edge, without removing any of the finitely many hyperbolic sinks. The finite-boundary case applies to this perturbation, proving the same bound for the original system. (The original system cannot have infinitely many hyperbolic sinks along a stationary edge, since its tangential Jacobian eigenvalue is zero there.)

**4. Sharpness and exact witness.** For the displayed quadratic pair, the two roots of \(f(x,\pm1/2)\) are
\[
 u_\pm=\frac1{10}\pm\frac{11\sqrt{11}}{120},
\]
and the two roots of \(g(\pm1/2,y)\) are
\[
 v_\pm=\frac15\pm\frac{3\sqrt{51}}{130}.
\]
All eight lie strictly inside their respective edges. Together with the four corners they give twelve distinct boundary equilibria.

At a horizontal-edge root \((u,\eta)\), \(\eta=\pm1/2\), the Jacobian is triangular with eigenvalues
\[
 \lambda_{\rm tan}=(4u^2-1)f_x(u,\eta),\qquad
 \lambda_{\rm nor}=8\eta\,g(u,\eta).
\]
At a vertical-edge root \((\xi,v)\), \(\xi=\pm1/2\), the eigenvalues are
\[
 \lambda_{\rm tan}=(4v^2-1)g_y(\xi,v),\qquad
 \lambda_{\rm nor}=8\xi\,f(\xi,v).
\]
Direct substitution gives
\[
\begin{split}
g(u_+,-1/2)&=\frac{72027}{64}+\frac{825\sqrt{11}}8>0,\\
g(u_+,1/2)&=-\frac{36133}{64}+\frac{825\sqrt{11}}8<0,\\
f(-1/2,v_+)&=\frac{277267}{676}+\frac{363\sqrt{51}}{13}>0,\\
f(1/2,v_+)&=-\frac{209453}{676}+\frac{363\sqrt{51}}{13}<0.
\end{split}
\]
The strict negative inequalities follow already from \(\sqrt{11}<4\) and \(\sqrt{51}<8\). Since \(f_x(u_+,\eta)>0\) and \(g_y(\xi,v_+)>0\), all four listed open-edge equilibria are hyperbolic sinks. At the bottom-left corner, \(f(-1/2,-1/2)=3853/4\), \(g(-1/2,-1/2)=3911/2\), and the Jacobian has eigenvalues \(-3853\) and \(-7822\), so that corner is also a hyperbolic sink. The other seven boundary equilibria have nonzero eigenvalues, and exact sign comparisons classify them as six saddles and one source. Strict inequalities, simple roots, and invariance of the same square persist under small coefficient perturbations. This proves sharpness on a nonempty open coefficient set. \(\square\)

## Verification

A self-contained Python 3 standard-library program, `check_boundary_sinks.py`, evaluates the edge-root identities in the exact quadratic fields \(\mathbb Q(\sqrt{11})\) and \(\mathbb Q(\sqrt{51})\), checks their locations, and verifies both Jacobian eigenvalue signs at each of the twelve boundary equilibria. It prints `INVARIANT_SQUARE_SHARP_FIVE_BOUNDARY_SINKS_OK` on success. The program certifies the explicit example, not the universal upper bound; the upper bound follows from the preceding argument. No numerical enumeration or floating-point root solver is used.

## Relationship to prior work

Gasull, Gouveia, and Santana introduce and study this broad invariant-square quartic family, focusing on centers, weak foci, and numbers of limit cycles **inside** the square. Grau and Szántó previously studied a constrained six-parameter invariant-square subfamily and obtained at least five interior small-amplitude limit cycles. The present statement is instead a sharp classification of the number of **hyperbolic sinks on the boundary** over the full family. The commonly indexed boundary-equilibrium census for Grau–Szántó's constrained subfamily (finite count at most eleven) does not imply this sharp five-sink upper bound for the unrestricted coefficient class, and its count concerns all boundary equilibrium types rather than full-planar sinks. General one-dimensional sign alternation is classical; the nontrivial point is the synchronized corner orientation imposed by common quadratic leading coefficients on opposite sides, and a full-coefficient open sharp realization.

## Limitations

The classification is restricted to the invariant-square family with total-degree-two factors and concerns only hyperbolic sinks on the four boundary edges. It gives neither the exact maximum number of interior sinks nor global convergence to the five boundary attractors. Other authors may have obtained equivalent boundary-stability classifications under different terminology. The explicit witness and proof have been checked in the present analysis, but independent validation has not been performed.

## References

1. A. Gasull, L. F. S. Gouveia and P. Santana, *On the limit cycles of a quartic model for evolutionary stable strategies*, arXiv:2410.15354v1, publicly available 20 October 2024. https://arxiv.org/abs/2410.15354
2. M. Grau and I. Szántó, *A Polynomial System of Degree Four with an Invariant Square Containing At Least Five Limit Cycles*, Qualitative Theory of Dynamical Systems **23** (2024), article 247. https://doi.org/10.1007/s12346-024-01106-9
