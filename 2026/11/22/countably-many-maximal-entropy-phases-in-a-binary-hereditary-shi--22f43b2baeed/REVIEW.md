# Independent mathematical audit

## correctness

PASS

RESULT.md lines 29–44: each cyclic mask has one 1100 cluster and otherwise alternates. When periods tend to infinity, bounded windows converge either to alternation or to a translate of one isolated cluster. This also proves the list of mask orbits and least periods, and a countable invariant mask space supports ergodic probabilities only on finite orbits. Finite periods 2k with k≤n contribute at most n(n+1) words; long-period and limit words give at most n+3 cluster placements and two alternating words. The prefix discrepancy ranges from −1 to 1, so every mask word has at most floor(n/2)+1 ones; alternating windows suffice for the lower bound. Counting pairs (mask word, descendant) gives the same entropy bound for the compact extension. Over a period-2k phase the return map is a full shift on 2^k symbols with the unique uniform product maximizer. Phase conditioning loses at most log(2k) per whole word; each projected maximizer therefore retains entropy. An ergodic maximizing measure on X has an ergodic invariant lift by invariant lifting and extremality; its mask marginal is a finite orbit and the same entropy upper bound forces the product maximizer there. Frequencies on residue classes recover the phase; mixing of the return map excludes any additional cyclic factor. A finite graph edge-shift cover would have finitely many ergodic maximizers at the factor entropy (the standard finite-to-one right-resolving presentation), contradicting the list. Wu–Zhang Theorem A and equations (1),(4),(6),(7) were checked against the cited arXiv text: the strict-gap premise is excluded, and the minimal-forbidden prefix bound and generation by minimal forbidden words give h_G≤h_M≤h_top. No journal status or formal verification is inferred. The supplied verify_masks.py was read, not run; it tests finite layers, not equality or the infinite classification.

## originality

PASS

Accept the specific binary hereditary construction, with its complete list and exact cyclic periods and its explicit language estimate. Neither arbitrary hereditary nonuniqueness nor countably many maximizers at the entropy boundary by themselves are new. The equalities are an application of Wu–Zhang, not a new general forbidden-word result.

## value

PASS

This gives an economical binary hereditary witness at the known strict-gap boundary, with exactly countably many ergodic maximizing phases rather than merely nonuniqueness. The phase periods and explicit language control make the example useful for comparing combinatorial complexity with the maximizing simplex. No exact forbidden-word census or transitive example is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
