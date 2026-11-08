# Scientific assessment

## Correctness — PASS

The statement is restricted to exactly the labelled regular seven-vertex tournaments and legal reversal of directed three-cycles. A structural argument proves that a cyclic tournament and its complete reversal cannot be connected by fewer than nine moves: seven edge-disjoint directed triangles cannot cover the seven arcs of cyclic step two, and path length has the parity of the 21 reversed arcs. The upper bound, the complete eccentricity classification, and all distance counts are established by finite exhaustive constructions in two distinct programs: one tests all possible bit orientations with all-source breadth-first search; the other enumerates fixed-row-score orientations recursively and uses permutation orbit reductions. Both reconstruct exactly the same complete state space and metrics. Residual correctness risk consists of implementation or transcription defects in the finite exhaustions; the two distinct constructions and exhaustive assertions mitigate but do not eliminate it.

## Originality — PASS, qualified

Brualdi and Li introduced the interchange graph and the lower-bound conjecture, as quoted in McShine (2000), Remark 2. McShine proves general connectivity and mixing, and the more recent Coxeter interchange literature treats extensions and regular degrees; these do not imply the order-seven exact radius, all distances, and unique antipodal pairing. McKay's published tournament census gives three nonisomorphic order-seven types, not metric data. Material inspected for the relevant primary papers and secondary source identifies no equivalent complete classification; the original 1984 Brualdi–Li chapter and an inaccessible later book chapter were not fully inspectable, and hidden historical numerical tables cannot be excluded. The theorem is not presented as absolute priority certification.

## Value — PASS

The seven-vertex case is the first regular-tournament order with multiple isomorphism types, making it a natural nontrivial finite test of the Brualdi–Li conjectural sharp diameter bound. The result determines the exact transformation complexity and singles out the extremal objects and their unique opposites, rather than restating connectivity, a known state count, or a routine parameter translation. Three orbit-dependent eccentricity profiles expose metric asymmetry not visible from the regular degree or the unlabelled census. The finding is finite and self-contained; no general theorem for larger orders is claimed.

Self-review: passed. Independent audit: not yet performed.
