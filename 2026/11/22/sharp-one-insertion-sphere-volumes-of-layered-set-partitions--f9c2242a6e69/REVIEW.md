# Review: sharp one-insertion sphere volumes of layered set partitions

## Correctness — PASS
The proof separates outputs with and without a new block; for existing-block insertions it proves that any nonlayered output has just one noncontiguous block and that collisions are exactly pairs of singleton blocks in one adjacent chain. This yields the exact triangular-chain correction. Discrete convexity, with the mandatory extra length for each nonsingleton block, yields all fixed-length, fixed-block-count extrema and their counts. The independent `check.py` script verifies every layered input of length at most ten and checks independent reverse enumeration through length seven. The finite check is supplemental to, not a replacement for, the proof.

## Originality — PASS (qualified)
The closest related preexisting result is a general pairwise deletion-collision classification for unordered set partitions. That result supplies a structural antecedent but does not give the source-conditional insertion-sphere formula, the sharp fixed-block extrema, or the complete counts of optimal layered compositions. Sagan's 2006 pattern paper and Dahlberg et al.'s 2015 paper characterize layered partition sources, not the insertion ball. Bean, Bell and Ollson's 2026 paper uses a different insertion-encoding notion for language regularity, not unique superpartition-neighbor counts. Direct and alias searches of the available mathematical records did not find an equivalent formula; that absence is not a mathematical proof of priority. Residual risk: an unindexed result or an unrecorded direct evaluation from the earlier collision classification could cover the claim.

## Mathematical value — PASS
A one-element insertion channel on unlabeled partitions is genuinely different from ordinary labeled alphabet insertion because the block names are normalized after the insertion and distinct histories collide. The chain-length formula separates source structures with equal length and block count, while the exact extremal and optimizing-source census determines which layered sources minimize and maximize expansion. It is a natural finite-block synchronization ambiguity invariant, not an arbitrary numerical slice.

## Scientific limitations
Only layered sources and one inserted element are included. This is not an arbitrary multi-insertion code-capacity theorem. Finite enumerations are not used to justify the universal statements. The originality conclusion is qualified by potential unindexed literature and the known deletion-collision structural antecedent.

Self-review: passed. Independent audit: not yet performed.
