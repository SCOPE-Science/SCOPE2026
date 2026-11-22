# Scientific review

## Correctness — PASS

The definition is ordinary mutual visibility, tested on all selected vertex pairs, with endpoints permitted and internal selected vertices forbidden. Both graphs have 16 vertices, degree six and two common neighbors for every nonadjacent pair. The critical lemma reduces visibility failure precisely to containing one of the distinct four-vertex sets formed from a nonedge and both its common neighbors. This logical biconditional includes the empty set, singleton and all high-cardinality masks. Complete enumeration over all 65,536 masks yields the two stated polynomials. Independent C++ code tests actual shortest paths after deletion of internal selected vertices rather than using the quartets, and reproduces every coefficient. A separate explicit automorphism orbit enumeration covers all 96 and 32 optimal subsets, respectively; every possible single-vertex exchange between optima is checked. The proof is exact for these finite graphs, not a probabilistic or partial sample.

## Originality — PASS, subject to historical-priority risk

The earlier Cartesian-product result implies the rook maximum cardinality through the Zarankiewicz problem, which is credited, not claimed independently. The 2023 lower-mutual-visibility work concerns minimum sizes of maximal sets; the 2024 diameter-two paper treats scalar visibility values, with the rook case reduced to Zarankiewicz. The December 2024 and 2025 visibility-polynomial papers develop the generating-function invariant and provide other graph families, but the accessible full texts contain no calculation for this strongly regular pair. Relevant prior research records concern three-row rook graphs, lower maximal visibility, or other Shrikhande–rook graph invariants. None implies the complete ordinary visibility coefficient tables or the single-orbit maximum classification. The exact matching database/table clearance remains provisional: public computations not indexed in the searched sources could predate this work.

## Mathematical value — PASS

The two canonical nonisomorphic, cospectral strongly regular graphs share all parameters (16,6,2,2); an ordinary geodesic-visibility count that sharply differentiates their maxima (10 versus 9) and all coefficients beyond degree three is a motivated graph-invariant comparison. The exact four-vertex obstruction hypergraphs have 60 versus 36 distinct forbidden quartets, explaining the earliest coefficient difference. Determining full coefficients and all optimal symmetry classes is stronger than the known scalar rook maximum and can serve as an exact test case for graph-polynomial and extremal-visibility investigations. This is an exact natural finite classification, not an extrapolated infinite result.

## Closest sources and limits

Brešar–Yero (arXiv:2307.02951) concerns lower visibility; Cicerone–Di Stefano–Klavžar–Yero (arXiv:2401.02373), Section 2, notes the already-known equivalence of the rook maximum with the 2-by-2 Zarankiewicz problem. Bujtás–Klavžar–Tian (arXiv:2412.03066) and Tonny–Shikhi (arXiv:2507.01851) are the closest exact-polynomial literature inspected. No survey or publication-priority clearance can prove universal uniqueness; nonindexed exact computations remain a residual risk. No claim extends to other orders or strongly regular parameter sets. The source programs plus exact recorded outputs are embedded.

Self-review: passed. Independent audit: not yet performed.
