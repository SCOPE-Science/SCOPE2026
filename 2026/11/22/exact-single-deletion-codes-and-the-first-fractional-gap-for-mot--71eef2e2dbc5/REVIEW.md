# Scientific review

## Correctness — PASS

For every stated length and each fixed up-step count, the deletion-shadow model is checked against explicit word enumeration. The received word recovers the layer index as the maximum of its up/down counts, proving layer separation. `certificates.json` contains exact rational primal and dual assignments, satisfying all constraints and matching objectives; disjoint-shadow integer witnesses have size equal to the floor of the layer's fractional optimum. Two different complete recursive graph searches reproduce every optimal-codebook count and every capacity; the corresponding standalone programs replay successfully from the complete package. Integer and rational arithmetic excludes solver tolerance concerns. No finite experiment is treated as proof beyond length seven.

## Originality — PASS, qualified

The closest general paper is Kulkarni and Kiyavash (2012), which gives general constrained-source deletion hypergraphs, LP bounds and RLL cases, but not a Motzkin-excursion capacity census. Oste and Van der Jeugt (2015) concern Motzkin recurrence/enumeration, and Stanovnik, Moškon and Mraz (2024) concern prefix/suffix non-overlap rather than single-deletion output disjointness. The exact source constraint, deletion channel, objective, all-optimum count, and fractional integrality gap are compared as statements, not just by names. Published related records and indexed mathematical searches did not identify equivalent finite results. This is a qualified claim; absence of a search hit cannot establish historical uniqueness.

## Mathematical value — PASS

Motzkin excursions are a classical, naturally structured constrained alphabet. This complete finite classification measures the single-deletion correction cost and counts all optimal designs through the first strict objective gap for the deletion-shadow packing relaxation. The sharp \(7/15\) objective gap, together with exact optimizer populations, is a natural benchmark for constrained-source coding and LP bounds. It is not a routine substitution of a parameter in a general exact formula.

## Residual risk and scope

No lengths above seven are settled, and an unindexed earlier complete enumeration may exist. The exact arithmetic and exhaustive proofs are reproducible but have not undergone independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
