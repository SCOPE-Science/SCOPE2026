# Self-review

## Correctness: PASS

Every deleted embedding corresponds to a nondecreasing vector of original period indices. Cumulative deleted-symbol counts are nondecreasing integers from \(0\) to \(q\), giving a bijection with deleted embeddings and an explicit decomposition of the remainder into cyclic period rotations. Distinct nonzero phases are identifiable blockwise; only the codes \(0\) and \(q\) collide, yielding exactly \(r+1\) embeddings of the unchanged word and one embedding for all other outputs. This proves \(\binom{r+q}{q}-r\), including \(r=0\). Independently organized executable checks matched the theorem in 36 and 25 tested parameter instances.

## Originality: PASS against inspected evidence

The 2026 Adamson–Fleischmann–Huch article introduces the complement-scattered-factor operation and a general algorithm, leaving special exact formulas as a research direction. The existing binomial-tail theorem covers \(q=2\), explicitly not claimed here. A cyclic permutation host theorem on embedding multiplicities concerns the positional multiplicities of *survivors*, while a circular necklace deletion theorem identifies all rotations and permits arbitrary deletion masks. Their full statements do not imply the present prescribed-deletion, linear-output phase language or all-parameter count. Actual targeted database queries and full-text comparisons are recorded in `AUDIT.json`; an unindexed equivalent in shuffle literature remains possible.

## Value: PASS

This solves the all-length complementary-subsequence language and enumeration problem on a natural family of nonbinary periodic words. The structural phase-rigidity and single exceptional fiber explain the exact reduction from embeddings to distinct outputs, and the formula is a sharp polynomial of degree \(q\), useful as a tractable benchmark for constrained shuffle and deletion channels.

## Limitations

The statement is restricted to repeated distinct-letter permutations with exactly one in-order period removed, not arbitrary source words or multiple deleted periods. The finite programs support the proof but cannot establish global uniqueness. Priority checks were material but not exhaustive.

Self-review: passed. Independent audit: not yet performed.
