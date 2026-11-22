# Scientific review: nonadjacent-repeat four-letter universal cycles

## Correctness — PASS

The theorem counts precisely the four-letter windows `abac`, `abcb`, `abca` for pairwise distinct letters, not the broader square-free or three-distinct families. The word-overlap graph has \(q(q-1)\) repeated-endpoint triple vertices of degree \(q-2\) and \(q(q-1)(q-2)\) distinct-letter triple vertices of degree two. The rotation, reversal, and one-letter replacement paths prove strong connectivity for every integer \(q\ge4\). Eliminating the order-three rotation block yields an explicit pair-array Laplacian determinant. The constant, standard, symmetric zero-sum, and antisymmetric zero-sum pieces have dimensions summing to \(q(q-1)\), and their evaluated factors give the exact tree count. The BEST theorem fixes one distinguished edge, avoiding a spurious division by circle length.

A full direct-cofactor check for \(q=4\), three modular checks for \(q=5\), an independent six-point symbolic-factorization comparison modulo two primes, and constructive window checks agree with the theorem. These finite checks are corroboration, not the proof for all alphabet sizes.

## Originality — PASS, qualified

The exact previously published count for **adjacent** repeats uses the disjoint target set `aabc`, `abbc`, `abcc` and does not imply this nonadjacent-target result. The exact locally square-free count includes additional all-distinct targets for each \(q\ge4\), and its spectral formula does not specialize by substituting alphabet size or a theorem parameter to the present restriction. Its ternary count of twelve does cover the \(q=3\) boundary, so novelty is explicitly claimed only for \(q\ge4\). The original broader non-injective and restricted-word studies establish existence statements for different word sets, not the current enumerator. Detailed statement and graph comparisons are recorded in the accompanying structured audit. An unindexed equivalent restricted-window computation remains a historical-priority risk.

## Value — PASS

The three nonadjacent equality patterns form a natural, closed, proper sublanguage of ordinary four-letter square-free factors and an opposite structural class to previously counted adjacent-repeat motifs. The new all-alphabet product counts the exact number of admissible compressed circular listings and isolates the spectral effect of excluding all-distinct four-mers. It distinguishes the quaternary value \(1{,}177{,}583{,}616\) from both the adjacent-repeat and locally square-free counts. This is an exact structural enumeration rather than a routine fixed-size table entry.

## Limits

The result counts rotation classes with labeled letters, not reversal classes. No statement about longer windows or globally square-free circles is made. The all-\(q\) theorem is analytically proved, but independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
