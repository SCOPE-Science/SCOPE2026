# Scientific review

## Correctness

PASS. The one-leaf projection packing bound is a direct count and the uniform rational assignment saturates it. The four-, five-, and six-leaf witness codebooks are explicitly supplied, with complete checking of every output. At seven leaves, the source/receiver incidence is constructed by both split restriction and graph deletion, checked to have 945 sources, 735 outputs and degree nine on every output. Two independent exhaustive exact-cover search implementations each rule out a covering of the 735 outputs, both visiting 2,561,709 recursive search states on the delivered data. No time cutoff is present. The proof does not assert an unverified exact seven-leaf integer maximum.

## Originality

PASS, qualified. Martin–Thatte (2012) study maximum agreement *subtree sizes*, and Vakati–Fernández-Baca (2014) study agreement *existence and compatibility* of tree profiles. Neither implies a family of 105 pairwise one-deletion-distinguishable seven-leaf trees or its impossibility. A published six-taxon quartet-tomography result addresses a different observation and cannot bound tree-deletion packing without an additional reduction. Searches of comparable descriptions, the research index and accessible existing claims disclosed no identical or stronger relevant result. There is a residual possibility of unindexed historical code-packing computations.

## Mathematical value

PASS. Tree restrictions under loss of one taxon are a natural information channel in comparative phylogenetics. The result finds the first exact, structurally motivated boundary of a standard packing relaxation, rather than merely a codebook of arbitrary size: equality holds through six taxa, but fails at seven even while the fractional solution remains uniform. The seven-leaf obstruction is finite and reproducible, and the exact value of the seven-leaf integer optimum is explicitly left open.

## Scope and remaining risks

The finite certificate is computer-exhaustive, not a conceptual all-length no-go theorem. It assumes labeled unrooted bifurcating phylogenies and exactly one missing taxon. No exhaustive literature search proves historical uniqueness, and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
