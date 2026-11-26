# Independent mathematical audit

## correctness

PASS

The given F₃ incidences specify the cubic, 18-vertex Pappus graph (points and lines, not the point-collinearity graph). In an independent exhaustive Python check, for each of all 262,144 masks and each selected source I propagated bitset distance layers through unselected vertices only, testing selected targets as terminal vertices against their original distance shells. This checks exactly the required original geodesics. Every one-vertex extension was tested for maximality, sufficient since deleting selections preserves every surviving witness. The counts by size 0–8 are 1,18,153,762,2340,4374,4605,1998,36 (total 14,287); only sizes 6–8 have facets, in counts 63,1710,36 (total 1,809). A separate exhaustive search for adjacency- and nonadjacency-preserving bijections finds 216 automorphisms; their action gives size-6 orbits 9,54, size-7 orbits 18×2,54×1,108×3,216×6, and the sole size-8 orbit of length 36. Thus μ=8, μ⁻=6, and the complex is nonpure. The recorded checker sources and transcripts are consistent with these results. The matching 64-bit checksum (035086ad4bd0f946, frozen convention) is a cross-check, not a proof of bytewise equality. Replay independent calculation with python3 /workspace/pappus_review_check.py.

## originality

PASS

The full labeled ordinary-visibility census together with maximal-set sizes and the orbit refinement was not matched by a distinct inspected source. The exact database hit is the frozen result itself. Same-day work on the Heawood graph is a parallel enumeration for a different graph. The ordinary face polynomial has generic database functionality as a realistic priority risk, but the documentation does not display the Pappus value or establish the layered facet and orbit census.

## value

PASS

A standard small symmetric incidence graph and the established lower visibility invariant give a motivated test of the gap between worst inclusion-maximal placement and optimal placement, here 6 versus 8. The complete nonpure facet profile quantifies all maximal outcomes, while the orbit calculation shows all 36 optima are symmetry-equivalent and distinguishes the maximal outcomes of smaller sizes. These exact facts can be used in comparisons of visibility complexes on symmetric graphs even without a general-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
