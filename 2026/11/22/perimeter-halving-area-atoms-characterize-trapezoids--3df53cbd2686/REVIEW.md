# Review of Perimeter-halving area atoms characterize trapezoids

## Correctness — PASS

For the signed Euclidean cut cap, Green's formula gives the exact local identity \(B''(s)=-[u,v]\) on each fixed edge-pair interval. The only constant regimes are paired parallel edges, which are oppositely oriented under strict polygon convexity. Nonconstant quadratic branches have absolutely continuous inverse-square-root pushforwards. For a trapezoid with bases \(b>a\), the reverse triangle inequality yields the strictly interior sliding interval of exact length \(a\) on each parallel base; its cap area is \(h(a+b-c+d)/4\). Consequently the atom mass and smaller-area fraction match the stated formulas. Parallel-sided and no-parallel-sided quadrilateral cases are exhaustive. The independent `verify.py` run passed 948 exact rational and geometric comparisons. Its finite tests do not certify the infinite quantified theorem; the written analytic argument does.

## Originality — PASS, with priority risk

Harned (2021) gives the paired-parallel-edges point collapse of perimeter-bisecting **line envelopes**, and the result acknowledges this ingredient. The inspected full published geometric-dilation and halving-chord-moment results compute **length** quantities, and the open Amadtohed et al. and Grüne et al. full texts treat different line family/envelope and area-halving constraints. These outputs do not imply the new area-cut pushforward or its sharp trapezoid atom. Berele–Catoiu (2022), *Bisecting envelopes of convex polygons*, is the strongest residual risk: abstract/metadata were available, not full text, even after both OA and institutional attempts. No unconditional novelty certification is claimed.

## Mathematical value — PASS

The distribution of smaller areas cut by perimeter-halving chords is a natural alternative geometric statistic to chord length. Its discrete versus continuous decomposition exactly recognizes the presence of paired parallel edges in any convex polygon and the trapezoid class among quadrilaterals. The mass and location separately recover the shortest parallel base relative to perimeter and the normalized side-leg imbalance, while the continuous component has explicit inverse-square-root structure. These are complete classifications and sharp natural inverse facts, not arbitrary computed parameters. No global shape reconstruction or stability theorem follows.

## Scientific limitations

The continuous result assumes strictly convex polygon vertices, the one-atom closed form applies specifically to convex quadrilaterals, and a relevant inaccessible source remains a genuine originality risk. No outside mathematical audit or validation has occurred.

Self-review: passed. Independent audit: not yet performed.
