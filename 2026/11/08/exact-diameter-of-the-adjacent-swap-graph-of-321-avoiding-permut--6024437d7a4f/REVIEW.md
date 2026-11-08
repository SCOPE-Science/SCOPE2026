# Review of the adjacent-swap diameter theorem

## Correctness — PASS

The quantified theorem is for all \(n\geq1\) with precisely the adjacent-position exchanges that preserve \(321\) avoidance. A descending adjacent exchange removes one inversion without introducing any, giving a legal path to the identity and an inversion-sum upper bound. The left-to-right-maxima partition provides two increasing subsequences, bounding inversions by \(\lfloor n^2/4\rfloor\), with a **unique** maximizer at even order. This sharpens the two-vertex upper bound by one when \(n\) is even. A first-crossing argument for the middle letter forces the large/small pairs to reverse twice and gives an exactly matching lower bound. All key cases (including \(n=1\) and \(n=2\)) were checked. The finite programs independently confirm the formula through order eight and confirm the extremal paths at orders nine and ten, but the infinite assertion is established only by the written proof.

## Originality — PASS (qualified)

The Catalan enumeration, inversion statistics and equivalence to fully commutative type-A elements are known: Reifegerste (2002), Biagioli–Jouhet–Nadeau (2014), and Chen–Mei–Wang (2015). The 2007 Gray-code work of Dukes–Flanagan–Mansour–Vajnovszki measures Hamming changes/uses rotations, not the induced adjacent-swap graph metric. Ehrenborg–Kitaev–Steingrímsson use window-overlap edges for their graph of pattern avoiders. Existing nearby mathematical records about the full permutahedron, related pattern-avoidance enumerations, or different reconfiguration structures do not entail this exact induced-graph diameter. A geometric equivalence or unindexed earlier calculation remains a priority risk; novelty is not asserted from the absence of a database hit alone.

## Value — PASS

This exact all-order diameter quantifies the transformation cost of the elementary adjacent-swap move on a canonical Catalan family. The restricted graph is connected but is not generally isometric to the full permutahedron (the two order-three endpoints require four rather than two swaps), so the answer is not an ambient Kendall-diameter corollary. The two-step obstruction—large and small letters must cross twice—is a reusable structural mechanism for path restrictions. The odd-order extremal-pair uniqueness further sharpens the metric theorem. No claim is made for arbitrary forbidden patterns or alternative moves.

## Remaining limitations

Potential old formulations in weak-order or fully commutative terminology may subsume the result and warrant specialist priority review. An independent scholarly audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
