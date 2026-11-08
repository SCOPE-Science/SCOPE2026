# Scientific review: concentric regular-polygon overlap

## Correctness — PASS

All integer orders \(n\ge3\), positive outer apothems \(a\), and inner apothems \(0<b\le a\) are quantified. The proof identifies the unique small-polygon vertex exposed beyond each outer support line, and uses containment of all small edge midpoints in the outer incircle to prove disjointness of the resulting triangular pieces. Computing each triangle from two edge projection slopes yields the exact two-branch area formula. Differentiating its loss establishes the strict angular optimizer, and Taylor expansions establish quadratic versus linear contact orders. Polar slicing and monotonic intersection of two circular arcs establish the radial-weight inequality; the already-proved strict ordinary area gap plus pointwise radial monotonicity establishes strictness for weights positive almost everywhere on the active annulus. Endpoints, tangencies, and the equal-scale singular branch are addressed explicitly. A separately implemented convex polygon-clipping and shoelace calculation passes 7,200 deterministic comparisons (relative discrepancy below \(7\times10^{-16}\)); this numerical evidence is supplementary only.

## Originality — PASS (historical priority provisional)

Mathar (arXiv:1301.6293, first public 2013-01-26), materially inspected especially in the rotated-concentric-circumscription section, treats supporting-contact and containment of regular polygons, not the full unequal-scale intersection-area profile. Kiss–Vidnyánszky (arXiv:1402.5452) study unions of congruent regular polygons and their perimeter/area ratios, not the claimed unequal-scale overlap profile. Har-Peled–Roy (arXiv:1406.5778) study polygon overlap under translation rather than rotational scale mismatch. The published published-finding corpus records 4705952c9b28 and 9cc93a56f053 were read in their complete RESULT texts: they concern congruent polygon union coverage and expectations for random rotations, respectively, and do not imply the two-scale plateau and contact-order law. Containment alone and generic polygon clipping are prior art and are excluded from the novel contribution. Search incompleteness, older specialized studies, and general intersection machinery pose residual priority risks.

## Mathematical value — PASS

The exact scale-and-angle overlap is a natural registration functional for two familiar convex bodies. The theorem identifies a genuine global regime change: below a critical scale the rotation is irrelevant, above it there is a maximal full-containment plateau followed by a unique optimal half-side-step mismatch, and at equal scale the onset changes from quadratic to linear. The closed parameter-uniform formula, equality cases and radial-weight strengthening provide meaningful structural information not supplied by a single numerical clipping instance. No more general convex-body problem is claimed.

## Limits and sources

The proof is self-contained within `RESULT.md`; `verify.py` uses no third-party libraries. The examined primary material comprises Mathar arXiv:1301.6293v1 (§§I–III), Kiss–Vidnyánszky arXiv:1402.5452v2 (main body), Har-Peled–Roy arXiv:1406.5778v1 (main body), and the two published published-finding corpus record proofs listed above. Nonindexed priority is unresolved. Independent review is not represented.

Self-review: passed. Independent audit: not yet performed.
