# Self-review

## Correctness — PASS

The claim is proved by an exact full-line geometric definition and an odd-itinerary graph argument. Every nonfixed odd orbit must traverse the perpendicular-leg edge, which projects to the right vertex. Explicit formulas \(T^{2j-1}(O)=(b^j,h(1-b^j))\) and \(T^{2j}(O)=(0,h(1-b^j))\), valid while the vertex orbit alternates, reduce the first branch change to the inequalities \(b^k\lesseqgtr d\), \(b^k\lesseqgtr c\). All ties and non-tie cases are treated. Strict branch choice plus the final perpendicular-leg projection proves local finite-time capture. Monotonicity, interlacing, and asymptotics are analytic. `CHECK.py` separately verified 20,009 supporting exact-rational assertions, not a replacement for the infinite proof.

## Originality — PASS within inspected sources

Everett's full open-access primary source, `arXiv:2408.16019`, Sections 2–4, introduces the same map and proves qualitative convergence; its isosceles-triangle bifurcation discussion does not supply the explicit high-aspect right-triangle odd-period formula or two exceptional parameter sequences. The nearest published research record, `2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`, already treats arbitrary triangle **three-cycles**; this result is not claimed. The new formula concerns all larger odd periods and shows their uniqueness and local finite capture. An accessible prior local ledger records a right-isosceles period-four result and an isosceles three/four-cycle result, neither implying high-aspect right-triangle periods. Equivalent general formulas could exist in unindexed literature; searches alone are not a proof of publication priority.

## Value — PASS

The object is a natural one-parameter family of triangles under a previously studied map. The exact complete odd-period spectrum and two distinct interlaced transitions are nontrivial structural results not determined by mere existence/convergence or a period-three census. Orthogonality forces both rigidity and finite-time capture, while the two independent tie mechanisms delete the unique orbit at isolated parameter values. This is a meaningful sharp bifurcation classification of a natural dynamical invariant, not a numerical fragment or arbitrary parameter slice.

## Scope and remaining risk

Only \(h\ge2\) and nonconstant odd least periods are classified. Even cycles, global basins, and \(h<2\) are outside scope. A nearest period-three published record was available as a searchable summary but its full proof text was not retrievable in this session; that does not prevent the decisive logical comparison because period three is outside the possible period set in this parameter domain. Alternative published formulations of the high-aspect staircase remain an acknowledged bibliographic risk.

Self-review: passed. Independent audit: not yet performed.
