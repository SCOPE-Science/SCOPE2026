# Review of the right-square-pyramid random width law

## Correctness — PASS

The five-vertex support computation gives \(W=a+\max(a,h|u_z|)\) exactly. Spherical folding correctly makes \(|u_z|\) uniform on \([0,1]\), independent of a uniform first-quadrant azimuth. The CDF is obtained by integrating the explicit sublevel measure of \(\cos\phi+\sin\phi\), rather than fitting data. Both global extrema follow from monotonicity in the azimuth and one-variable branch optimization. Axial pole tangent diamonds give the lower coefficient \(1/\pi\); the oblique branch-intersection tangent triangle gives \((1+h^2)^{5/2}/[2\pi h^2(h^2-1)]\). Locally nonoverlapping spherical caps give **exact** linear upper endpoint laws. First derivatives of the competing extremal values give the two critical height crossovers; disjoint contact neighborhoods justify adding their contributions. The self-contained checker has passed 20,032 finite supplemental assertions. Risks: finite checks are not proofs; the rigorous argument relies on uniform local Taylor expansions and strict gaps away from finitely many contacts, supplied in `RESULT.md`.

## Originality — PASS, with residual historical uncertainty

The general minimum-width formula for convex pyramids, already published, **covers the bare minimum value**; that value is acknowledged rather than presented as new. The inspected complete published statement and proof do not cover the width probability distribution or critical rare-event crossover. A published complete width CDF for circular frusta is not an implication for a square-based pyramid: its transverse support is rotationally invariant while the square has an independent nonconstant azimuth. Finch's classical full text treats triangle, square, tetrahedron and cube widths but not right square pyramids. The inspected 2015 section/projection-distribution work concerns areas of hyperplane sections/projections, not line widths. An accessible prior result on the **planar shadow area** of square pyramids also has a different random observable and therefore does not cover this theorem. Direct indexed searches for aliases, support functions, width distributions, and competing height thresholds found no statement implying the combined complete CDF and the sharp two critical laws. Risks: index and web coverage are incomplete; a hidden older computation could exist. This review is not an independent priority certificate.

## Mathematical value — PASS

The family is a natural five-vertex solid with a genuine continuous shape parameter. A complete random-direction width law, including two *different* extremal height transitions, exact upper endpoint probabilities, quadratic cusp/pole lower probabilities, and moving-shape crossovers, provides more structural information than the already-known isolated minimum-width invariant. The critical mode proportions and crossovers distinguish competing geometric contact mechanisms. The value does not depend on an unproved application or generalization to arbitrary pyramids.

## Scope and limitations

The geometric claim is for right square pyramids of base side length \(2\), line projections, uniform directions, and fixed-height or fixed-crossover-parameter limits. The CDF is an exact one-dimensional integral, not an elementary closed expression. An independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
