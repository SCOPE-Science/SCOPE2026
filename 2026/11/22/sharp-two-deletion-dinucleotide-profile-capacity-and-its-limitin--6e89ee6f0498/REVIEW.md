# Independent mathematical audit

## correctness

PASS

Two removed sites are either separated, an internal adjacent pair, or a boundary adjacent pair. For separated sites the changed edges add even with exactly one intervening survivor; for an internal adjacent pair the three edges are replaced by the edge joining its flanks. This establishes the local envelope for linear words of length at least four; at lengths two and three the received profile is always zero. Independently enumerating two successive run-deduplicated single-deletion descendant sets reproduced every finite maximum through 13 and all reported counts of extremizers. For each of the 64 exact boundary triples, direct deletion on a constructed interior containing two separated copies of all sixteen four-bit patterns reproduces the limiting cardinality; taking unions of the change sets over free third bits reproduces the 4-by-4 envelope, including maximum 17. The listed sharpness witnesses retain their local contexts when the displayed zero run is extended, hence 17 is attained at all lengths at least 13. For the probability proof, split disjoint interior four-blocks into two batches of floor((n-6)/8) blocks each. Conditional on the six boundary bits, the probability that any pattern is missing from either batch is at most 32(15/16)^floor((n-6)/8). On the complementary event all required changes are realized, including sums of two identical interior types, and the boundary triples are exactly uniform. The reproduced limiting multiplicities are (4,8,4,24,16,8) in the stated order. Replay: python3 /workspace/reproductions/3.py. The finite checks establish the finite tables, not the unbounded extension or limit by extrapolation. The frozen prose calls the C++ loop ordered, but it correctly uses i<j as required.

## originality

PASS

Best-of-knowledge pass for the exact two-deletion profile-image capacity and boundary-conditioned limiting law, not for overlapping substring profiles or deletion-code hashing generally. The strongest indexed alternatives change either the allowed edits or the output equivalence relation; the two-deletion hashing comparison remains access-limited.

## value

PASS

The measured object is the image of a fixed word's two-deletion ball under a standard loss-of-order profile, not a tuned finite instance. A uniform all-length bound, a first-saturation length and a distribution controlled solely by random boundary bits after interior saturation are useful distinct facts: they quantify the actual ambiguity of adjacent-pair observations. The result does not establish a deletion-correcting code size or code rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
