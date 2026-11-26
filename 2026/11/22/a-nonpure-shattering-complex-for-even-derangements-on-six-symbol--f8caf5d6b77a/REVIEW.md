# Independent mathematical audit

## correctness

PASS

There are 90 derangements of type (4,2) and 40 of type (3,3), the only even derangement types at n=6. The full trace forces a matching, so enumeration through size five plus heredity covers all candidates. A fresh exact reproduction checked matching counts (1,30,315,1420,2715,1854) and even-family face counts (1,30,315,1420,1140,0). Sorting the inclusion test by size leaves exactly 360 triple and 1140 quadruple facets. Conjugacy preserves the family, and the orbits of the five stated representatives are disjoint and cover those facets, of sizes 360 for the triple and 360,360,240,180 for the four quadruples in the manuscript's representative order. Deletion boundaries over F2 are exact, with augmented ranks (1,29,286,750). Rank-nullity gives 1420−286−750=384 and 1140−750=390 in dimensions 2 and 3, and vanishing in all other reduced degrees, consistent with Euler characteristic −6. Independent replay: python3 /tmp/opencode/ordinal5_even_derangements_audit.py. The supplied programs were inspected, not executed; the broken-space reference URL and duplicated word in the bibliography discussion are editorial, not mathematical discrepancies.

## originality

PASS

Within the inspected evidence, the substantive finite contribution is the exact parity-sensitive top stratum and the resulting facet/orbit and mod-two topology, not the ordinary derangement count, the unrestricted shattering polynomial, or VC dimension alone. The closely matching all-order record already includes the same six-symbol polynomial but expressly credits this finite treatment as the source of that case; it does not give the facet or homology census. No independently preceding source was identified for the combined finite claim.

## value

PASS

Even derangements form a canonical restriction of a well-studied incidence concept class. At six symbols it has the same VC dimension as the unrestricted class but loses 1575 top faces and gains 360 lower-dimensional facets: these differences are invisible to dimension. A researcher studying parity-constrained matching complexes can use the exact simultaneous-label orbit decomposition and boundary ranks, particularly the two consecutive nonzero homology groups. This is a useful finite baseline and not a claim of an all-order homotopy type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
