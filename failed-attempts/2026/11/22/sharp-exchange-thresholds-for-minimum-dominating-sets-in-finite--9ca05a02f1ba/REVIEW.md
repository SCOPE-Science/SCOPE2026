# Independent mathematical audit

## correctness

PASS

For a dominating set with a points and b lines, a(q+1)+b ≥ q(q+1) and a+qb ≥ q². If a+b≤2q−1 these force a=q and b=q−1. The selected points must meet at least q²+1 lines. Counting the first point's q+1 lines and at most q new lines for each later point gives exactly that number only in the collinear case: reorder any noncollinear triple first, and its third point contributes at most q−1 new lines. Thus the selected points are a whole line B, and the remaining q−1 selected vertices must be its parallel mates. Conversely these sets dominate. Two parallel base lines give intersection q−2; two intersecting base lines give intersection 1. Subtracting from the common size gives q+1 and 2q−2 respectively (one-sided replacements, not symmetric difference). Hence the reversed ordering for q=2 gives the connected K_{2,2,2} at budget 2, equality of costs gives K_12 at budget 4 for q=3, and for q≥4 each parallel class is a clique before the cross-class threshold. This proves the full phase diagram without a field assumption. An independent closed-neighborhood covering search at orders 2, 3, 4 found 6, 12, 20 optima; unordered pairs by cost were {2:12,3:3}, {4:66}, {5:30,6:160}.

## originality

FAIL

The published affine-plane optimum size and super-neatness already hold in Tang–Zhou. An independently indexed record with the same date explicitly supplies the identical family of optima. The batch-exchange phase diagram is not quoted verbatim in the inspected literature but is a direct distance readout of that family and the standard affine incidence axioms, with no new reconfiguration lemma. This is a coverage assessment, not a claim that the same-day record is earlier or that the graph was previously printed.

## value

FAIL

Batch reconfiguration is a natural question, but here the only incremental claim is a mechanically implied two-distance readout of the exact optimum family. No new obstruction, path construction, or separately useful structural invariant is needed to obtain the thresholds. The rising interval length is a comparison of the same two costs. This does not meet the standard for a distinct valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
