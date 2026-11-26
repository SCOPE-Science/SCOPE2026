# Independent mathematical audit

## correctness

PASS

Petersen is triangle-free of diameter two and all edges extend to two-edge geodesics. An overlapping pair of auxiliary edges has exactly one common Petersen neighbor, the complementary pair of unused labels; the 30 maximal geodesics thus correspond to spanning P₃ plus a disjoint K₂ in K₅. If the unselected auxiliary graph has no isolates and contains a matching of size two, the fifth label has a neighbor on the matching and creates that forbidden triple. Otherwise its edges are pairwise intersecting, and only the full star (not a triangle) can avoid isolates on all five labels. This gives precisely star-containing transversals and the five separate six-edge complements themselves. The listed sets are minimal because no star lies in a six-edge complement and removing any edge of one such complement makes it infeasible. Inclusion-exclusion over star centers and addition of the five uncovered complements produce coefficients (5,30,80,90,45,10,1) in degrees four through ten, summing to 261. For b≤6 the branches over different stars are disjoint and have no inclusion edges between them; each truncated star branch is connected and has 1, 7, or 22 states, and a six-edge minimal complement is isolated when b=6. At b=7 two stars meet via their union of size seven, while a six-edge complement missing the v-star attaches by adding uv to complete the u-star. There are 205 states up to budget seven. The lower bound of six toggles between distinct stars is met by the union route.

## originality

FAIL

The advertised complete classification, nonpurity, and full polynomial are already covered by a distinct earlier Resultary result about dissociation in KG(n,2). The translation is exact, not analogy. Petersen is triangle-free of diameter two, so missing a maximal geodesic is exactly having a complement with an induced vertex of degree at least two. Taking complements swaps the two known maximal dissociation families at n=5 and reverses the polynomial coefficients. No earlier explicit TAR table was established, but the claimed one follows mechanically from the already classified minimal sets and their elementary inclusion relationships.

## value

FAIL

The static classification is intrinsically useful but already available under its equivalent dissociation form. The only potentially distinct remainder is the TAR profile. After the prior bases are supplied, that remainder is a direct truncated Boolean-interval count and a union path in the elementary add/delete model, not a new metric obstruction, structural lemma, or independently nonmechanical invariant. The frozen package has no surviving valuable advance at the stated scope; no repair is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
