# Review of exact five-label Stirling pair-deletion capacity

## Correctness — PASS

The source language and unknown whole-label-pair deletion channel are defined explicitly. The insertion construction generates the full family of \(945\) sources and \(105\) possible outputs. The checker independently regenerates all sources by exhaustive balanced-word enumeration, compares the two families, computes every distinct output set, and verifies both halves of the finite proof: \(33\) pairwise-disjoint output shadows, and \(105\) nonnegative integer shadow weights with total \(339636\) on a scale of \(10000\). It evaluates every one of the \(945\) covering inequalities exactly. Consequently any zero-error code has fewer than \(34\) members, and the explicit lower witness has \(33\). The method is a complete finite proof, not a claim based on a search program's success status. The embedded standalone checker replayed successfully.

## Originality — PASS, with a specifically identified access risk

Janson's foundational tree/Stirling permutation paper and Janson–Kuba–Panholzer establish the insertion family and tree correspondence, not a pair-erasure code capacity. Gabrys et al. study ordinary single-occurrence permutations, so their deletion-correction bounds do not supply this exact constrained-multiset capacity. Brualdi and Dahl analyze Stirling multipermutations and deletion of the **largest** adjacent pair in a structural characterization; that deterministic operation does not decide a code correcting the unknown deletion of **any** label pair. The closest inaccessible item is Sala–Gabrys–Dolecek (2014), *Deletions in Multipermutations*, DOI:10.1109/ISIT.2014.6875338: its accessible abstract gives broad coding constructions but not this 33-word special-case count. Full text could not be inspected, so the possibility of overlooked implied coverage in it is a residual priority risk. No inspected full text or located exact table implies the present 33/34 separation; lack of a database match alone has not been treated as proof of novelty.

## Mathematical value — PASS

A matched label appears twice in each Stirling permutation, so erasing it models an unknown edge contraction in a plane recursive increasing tree rather than an arbitrary pair of coordinate deletions. Exact zero-error capacity is a natural invariant for that information-loss mechanism. The explicit lower and fractional upper certificate settle the natural five-label instance sharply, improving on the mere existence of such tree encodings. The claim is restricted to one exact nontrivial finite case and does not assert a general-order formula.

## Limits and verification status

The result is finite, with a \(105\)-entry upper-bound table; its certificate is checked exhaustively. Earlier literature may contain an equivalent enumeration, especially the unavailable full 2014 multipermutation paper, and the historical priority assessment is qualified accordingly. Only a self-review was conducted; this is not independent validation or publication certification.

Self-review: passed. Independent audit: not yet performed.
