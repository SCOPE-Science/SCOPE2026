# Self-review

## Correctness — PASS
The run-one obstruction follows from the exact three-image-set transition invariant \(Q,S,T\). The run-two construction is established by the stated block maps on \(S\) and an induction on the surviving integer interval; all indices and the boundary \(n=3\) are included. A self-contained exact-integer verifier directly tests every block and witness for \(3\le n\le100\) and independently exhausts all reachable no-\(aa\) images for \(3\le n\le15\). Those finite checks are not used as an infinite proof. The witness length is not represented as an optimum.

## Originality — PASS, qualified
A published-finding corpus meaning search on cyclic synchronization, local rotation-run restrictions, and the explicit block words, plus the 2019 regular-constraint and 2021 simple-idempotent primary papers, found no verified statement covering both the **uniform sharp threshold two** and its explicit bounded-run witness. Hoffmann's polynomial-time decision theorem is more general with respect to automata and constraint representations, but it does not state this specialized sharp boundary or the block dynamics; a general decision algorithm is not an identical all-parameter theorem and construction. The closest mathematical-records on Černý reset lengths, letter counts, subsequences and early rank compression have different conclusions; none forces avoidance of a contiguous triple rotation. An unpublished or differently named equivalent, or a non-explicit corollary of general procedures, remains a priority risk. The 2021 paper was read materially at its theorem and proof sections, not judged by snippets alone.

## Value — PASS
A regular constraint that forbids \(aa\) destroys synchronization for the entire extremal Černý family, but relaxing it just enough to permit \(aab\) restores synchronization for every size. The explicit conversion to a predecessor-collapse control system explains **why** this phase boundary occurs and yields a quadratic-size legal command sequence, not merely a finite instance or a rephrasing of the standard reset length. This is useful for constrained command scheduling, synchronizing automata and constructive complexity analysis. The exact constrained shortest length is left open rather than claimed.

## Closest literature and limitations
Primary: Hoffmann (2021), arXiv:2109.02743v1, especially Section 4, Theorem 4.3, and its appendix. Fernau et al. (2019), MFCS 2019 regular-constraint framework. Mathematically close published records: `2026/11/8/SCOPE-uniform-weighted-reset-optimality-in-the-ern-automata--6527a70965c4`; `2026/10/13/SCOPE-a-mandatory-reset-subsequence-and-exact-one-step-multiplicity-fo--8a725fd1702c`; `2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3`. These do not supply the asserted no-\(aaa\) reset construction. Historical exhaustiveness is not claimed, and independent audit remains pending.

Self-review: passed. Independent audit: not yet performed.
