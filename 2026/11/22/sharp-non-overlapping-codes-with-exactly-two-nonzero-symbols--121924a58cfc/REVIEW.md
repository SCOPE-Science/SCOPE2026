# Review of the two-marker non-overlapping code bound

## Correctness

**PASS.** The theorem explicitly treats all integers \(q\ge2\), \(n\ge3\), exactly two nonzero positions, and *every* proper prefix–suffix length, including pairs of identical words. The upper bound distinguishes primitive cyclic necklaces with unequal intermarker gaps from the antipodal necklace class. The unique even-length obstruction follows from the half-length prefix–suffix comparison, yielding an optimal disjoint-pair count \(\lfloor(q-1)^2/4\rfloor\). The construction attains both bounds, and the no-overlap proof checks the only possible matching length. Finite exhaustive optimizations, full pairwise construction tests and necklace enumeration provide independent corroboration; all-length correctness follows from the proof, not the computations.

## Originality

**PASS against inspected evidence, with historical-priority risk.** Zakharov's February 2026 result concerns the asymptotic product of two overlap-avoiding word-set densities. Blackburn and Chee–Kiah–Purkayastha–Wang give unconstrained-alphabet code bounds and constructions; Yang–Ding enumerate and analyze restricted-overlap constructions rather than the extremal exactly-two-nonzero layer. The closest indexed binary weight-two result forbids only the final two overlap lengths and does not imply a result forbidding *all* nontrivial lengths. A separate binary fixed-weight-three code theorem treats a different layer. The present complete \((q,n)\)-parameter formula and its even-length alphabet partition obstruction were not found in those inspected statements or in targeted searches. Searches cannot prove global priority, and an unindexed equivalent may exist.

## Value

**PASS.** Sparse two-marker words are a natural controlled-weight layer for synchronization codes. The exact capacity and explicit optimum for *every* alphabet size and length expose a parity-sensitive obstruction invisible to general asymptotic bounds: odd lengths use every primitive necklace while even lengths require a balanced disjoint-alphabet cut. This solves a coherent natural extremal problem rather than recomputing one table or changing a known code's parameters.

## Reproducibility and limitations

Run `python3 verify/exhaustive.py` and `python3 verify/construct.py` from this package. The first exhaustively solves \(17\) small optimization instances; the second validates \(84\) constructions and \(35\) necklace counts. Their actual outputs are embedded alongside the scripts. No computation is presented as an exhaustive proof for all \((q,n)\). The result does not enumerate every optimum or extend to other Hamming weights. External independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
