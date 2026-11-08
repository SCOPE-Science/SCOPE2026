# Scientific review of the Rule-73 image series

## Correctness — PASS

The cyclic de Bruijn graph condition is equivalent to the existence of a cyclic input, including degenerate ring lengths. Determinization by Boolean relation multiplication gives exactly one path per output word, and the actual reachable dimension is \(735\). The proposed rational series is checked through the length necessary for Cayley–Hamilton to force its recurrence globally, not extrapolated from a short numerical table. The exact integer verifier checks equality at lengths \(1\) through \(39\) and all \(735\) recurrence instances from \(40\) through \(774\). A separate exhaustive implementation confirms output counts through length \(16\).

## Originality — PASS (qualified)

Wolfram (2002) describes Rule-73 complexity and localized patterns rather than distinct indexed cyclic one-step output counts. Adamatzky and Martínez (2010) enumerate local space-time morphological patterns, not global periodic image sets; their full accessible article was examined. The Rule-73/109 color-conjugacy is incorporated, so the formula is not duplicated under an obvious alias. Searches of published research summaries, primary literature and a mathematical sequence database yielded no covering all-length formula. An interactive Elementary CA Zoo table does enumerate Garden-of-Eden counts for sampled ring sizes for all 88 elementary-rule equivalence classes, so it overlaps this invariant at finitely many values; those finite entries do not imply the proven symbolic generating function. Fukś (2003) studies block preimage sequences across iteration depth, not the cyclic distinct-image count across ring length. The arXiv preprint of Kang (2013), devoted to long-distance Rule-73 variations, could be inspected to abstract level only. The possibility of an older unindexed exact enumeration remains; the dynamic finite census is specifically acknowledged.

## Value — PASS

The result exactly measures finite-ring one-step output information for a classically studied complex elementary rule. It converts an a priori large distinct-output problem into a closed rational generating function across *all* ring sizes, rather than a handpicked finite census; its small-degree factored logarithmic derivative is a structural representation that supports further image-entropy and predecessor studies. It does not need an unproved universality hypothesis.

## Remaining scientific limitations

This is not a theorem about multiple updates, output multiplicities, or all elementary rules. Full-text access to the cited long-distance study was unavailable, and historical priority is not externally certified. All correctness checks were performed within the provided code and mathematical argument; independent reproduction remains outstanding.

Self-review: passed. Independent audit: not yet performed.
