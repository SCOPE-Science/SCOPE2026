# Self-review

## Correctness: PASS

The claim is an all-length constructive lower bound, not a finite-table extrapolation. The proof explicitly lists \(a+5\) distinct positional intervals crossing one cut of an eight-run binary word, identifies a two-occurrence longest border for each, and applies a proved one-character extension criterion to both existing neighbors. The exceptional \(n=13\) boundary and odd/even parity are handled separately in the parameter ranges. The standalone direct checker confirms 57 parameter instances and 1211 proposed intervals; independent complete small-instance enumeration supports, but does not replace, the general proof.

## Originality: PASS against accessible evidence

The closest primary source (Faro–Marino–Pavone, arXiv:2611.11552, especially Section 7) proves a much larger upper bound and an all-length lower construction of \(\lfloor(n-1)/2\rfloor\), not the current strict half-density construction. Umezaki et al. (arXiv:2607.02838) give a general RLE-based MCS enumeration framework, not this explicit all-length cut witness; Fischer–Köppl (arXiv:2610.38114) address output-sensitive enumeration rather than cut density. A finite length-fourteen extremal instance is already known and is excluded as a separate novelty claim. Exact aliases, maximal closed repeats, interval boundaries, and comparable constructions were searched. Risks: an equivalent unindexed construction, an implicit specialization of general valid-pair methods, and the limited independent novelty review.

## Value: PASS

The optimal constant in the local cut-density problem is explicitly open in the relevant 2026 primary paper. A finite strict-half example does not establish whether such an excess can occur at arbitrary lengths. The explicit family resolves that *persistence* question for every length from thirteen onward, using a single systematic list of border families rather than a sequence of finite optimizers. Its additive gain is small and the leading coefficient remains unchanged; those restrictions materially limit significance, but the new infinite stability assertion addresses a natural structural boundary in the original problem.

Self-review: passed. Independent audit: not yet performed.
