# Independent mathematical audit

## correctness

PASS

The rule is D∘σ∘K by expansion. Any active marker conflicts with markers at offsets ±1 and ±2, so all guards of active markers survive the update. A new marker could only be within these offsets of an old active marker, which still excludes it. Thus K is an involution, also for N=3,4 by the same modular guard identities (for N=1,2 the guard vanishes). Cyclic D has kernel consisting of the two constants and even-parity image by rank and telescoping. In the pair de Bruijn graph, even for short rings, overlapping triplets reconstruct the entire periodic symbol word with multiplicity of sites, so closed walks encode exactly the complementary K-images and weight is Hamming distance. I independently enumerated the 256 candidate windows with a truth table and checked reflexive zero-cost reachability by Boolean transitive closure. Reduced costs 0,1,2 occur on 40,16,72 edges respectively, and no cost-one edge has a zero-cost return. Telescoping gives 3·distance−N ≥ 0 and excludes 1, the extra obstruction for N≡2. For the witness motifs, two period-three repetitions suffice to contain all periodic windows and stabilize the windows on both sides of the defect block: a length-four crossing uses at most three symbols from either side, cannot bridge a run of length six, and the pure run contains all three phases. Checking the two defects with zero, one and two repetitions, the pure period-three word and the singleton verifies all witnesses and their weights. An additional direct check of the unfactored rule exhausted N=1..10. Private replay: python3 /workspace/branches/check_twin_certificate.py. The supplied verifier was inspected, not executed; bounded direct checks alone are not the all-length proof.

## originality

PASS

Best-of-knowledge pass for the sharp minimum over cyclic preimage twins, including the full mod-three law. The local rule, marker involution and binary difference kernel are not new. The closest inspected statements identify the rule or give other collision invariants; they do not determine this optimized positional distance.

## value

PASS

The rule is independently singled out in a classification of small-neighborhood automata. Fiber cardinality does not quantify the worst ambiguity: the formula establishes the exact least number of sites needed to distinguish colliding cyclic states, down to short rings and the stronger 3k+2 obstruction. The structural obstruction and constructive witnesses, rather than a finite table of small N, give this invariant independent use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
