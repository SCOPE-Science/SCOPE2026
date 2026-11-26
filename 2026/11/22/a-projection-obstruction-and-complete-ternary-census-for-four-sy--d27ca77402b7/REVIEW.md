# Independent mathematical audit

## correctness

PASS

Minimum distance three makes both two-coordinate end projections injective. If their intersection has size r, there are r codewords starting in it and r ending in it. These families are disjoint: a word belonging to both would be the shift-two splice of some codeword ending in its prefix and another codeword starting in its suffix. The witnesses need not be distinct, as required by the definition. Thus 2(2m-q²) ≤ 2r ≤ m, proving the floored bound for all q in scope, including empty codes. Independently reproduced the ternary census by enumerating partial matchings of the nine initial and nine terminal half-blocks, rejecting distance violations and updating a bit mask of all three splices of all ordered pairs, including repeated words. Injectivity and fixed initial-block order give coverage with no duplication; any rejected subset cannot extend to an admissible code. The counts at sizes 1–5 were 72, 1410, 7398, 9042, 1548; none were larger. The stated example was found. Symbol relabeling and reversal preserve both constraints (reversal interchanges the splice order and complementary shift); transforming every maximum independently and canonicalizing gave 129 orbits, all of size 12. Both frozen scripts were inspected, not executed. The independent computation is finite and does not replace the projection proof.

## originality

PASS

The classic ordinary comma-free model and the distinct prefix–suffix and error-resilient synchronization models do not cover the simultaneous aligned-distance-three condition and the resulting length-four projection bound or exact ternary census. The exact nearby ternary enumeration has length three. This is a best-of-knowledge comparison, not historical priority certification.

## value

PASS

Noiseless frame recognition together with single-substitution correction at a known frame is a natural constrained packing problem. The two-projection obstruction improves the unconstrained injective-projection bound by a constant factor, and the small ternary classification gives the exact optimum, multiplicity and lack of symmetry stabilizers. The value is the interaction between the constraints plus the complete small extremizer count, not running a search or claiming correction at an unknown frame.

The dated certificate retains the supplied scientific assessment, sources and limitations.
