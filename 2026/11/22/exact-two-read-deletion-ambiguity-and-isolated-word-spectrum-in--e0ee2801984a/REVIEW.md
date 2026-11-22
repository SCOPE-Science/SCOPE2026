# Scientific review: exact two-read deletion ambiguity of `010`-free binary words

## Correctness — PASS

Cai–Kiah–Nguyen–Yaakobi, Proposition 9 (arXiv:2001.01376), establishes the alternating-interval premise for two shared one-deletion outputs. The forbidden triple rules out both opposite phases of any length-three or longer alternating interval, leaving only legal adjacent swaps. The context-language factorization proves the edge series. Exact eleven-state polynomial identities (not numerical extrapolation) prove the isolated-word generating function. Direct descendant enumeration through length 13, separate finite-state edge checks through length 17, and an independent zero-degree test through length 14 all pass. All hypotheses and the length-zero convention are explicit.

## Originality — PASS (qualified)

The full-space Type-A theorem and the published unrestricted edge census are recognized as prior and cannot be called novel. Neither gives the complete two-read zero-degree series on the induced `010`-free finite-word graph. The closest similarly constrained published three-gram census measures *circular three-gram profiles* of necklaces, not linear single-deletion read intersections. The 2012 alternating-pattern article works with a further symbol-count balance restriction and no deletion channel. Full-text comparisons are recorded in the accompanying structured review. An earlier unindexed exact computation remains a priority risk.

## Value — PASS

The isolated-word count is a natural all-length structural invariant of constrained two-read reconstruction: each counted word needs no exclusion of any other permitted source due to this reconstruction channel. The regular padded forbidden-factor characterization and rational series make this invariant constructive and exactly enumerable. The result also explains why a shortest forbidden alternating triple transforms the general nonlocal ambiguity graph into a bipartite adjacent-swap graph. This does not claim the exact optimum code size or generalize beyond the specified channel and language.

## Boundaries and reproducibility

All proofs apply to finite linear binary strings of every nonnegative length, with deletion defined only at positive length. The three complete Python scripts use standard-library integers and have no outside dependencies. The isolated-series identity is certified by explicit eleven integer polynomials. The publication-priority assessment is limited to accessible literature and mathematical records; it is not a proof of global uniqueness or historical priority.

Self-review: passed. Independent audit: not yet performed.
