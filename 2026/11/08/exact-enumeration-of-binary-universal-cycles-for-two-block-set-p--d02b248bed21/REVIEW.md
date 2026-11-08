# Scientific review: exact binary two-block partition universal-cycle count

## Correctness — PASS

The claim has one explicit domain: globally binary circular encodings, exactly two nonempty unlabeled partition blocks, and \(n\ge3\). Every binary length-\(n\) window up to complement maps bijectively to its adjacent-XOR length-\((n-1)\) word; constants correspond to the excluded all-zero pattern. Every admissible cyclic difference word has \(2^{n-2}\) one-bits, which is even, so it integrates in precisely two complementary ways. Removing or adding the unique all-zero self-loop in the directed overlap graph is a two-sided bijection. The all-order de Bruijn count is reconstructed from the directed Laplacian spectrum, matrix-tree theorem, and BEST theorem, with explicit orbit-freeness arguments. The exhaustive rooted-word tests at \(n=3,4,5\) and exact reduced-Laplacian determinant tests through difference order \(6\) agree. They supplement, and do not replace, the proof.

## Originality — PASS, with residual historical-priority risk

Higgins–Kelley–Sieben–Godbole (2015), Theorem 12 and Section 3, establish that the relevant Eulerian cycles lift and hence universal cycles exist, but the inspected full text does not state the exact number or identify these cycles with ordinary de Bruijn cycles by cyclic XOR and deletion of one zero loop. The classical binary de Bruijn count, recorded in OEIS A016031, is **not** a new integer sequence. The explicit bijection supplies the scientific comparison between the previously known existence problem and the previously known de Bruijn count. Queries for two-block partition cycles, complement representations, all-zero-window deletion, the closed numerical formula, and equivalent cyclic encodings returned no record demonstrating this exact link. The original general paper of Chung–Diaconis–Graham was verified bibliographically but its full text could not be assessed through the accessible source; an unindexed equivalent statement remains possible.

## Value — PASS

The number of globally binary shortest cycles visiting each two-block partition is a natural design-diversity invariant, distinct from proving a single cycle exists. The all-order formula gives \(\log_2 U_n=2^{n-2}-n+1\), rather than a one-off finite value, while the explicit bijection transfers constructive generation, counting, and uniform sampling from ordinary binary de Bruijn cycles. This answers a motivated exact enumeration question without claiming a new numerical de Bruijn sequence or a general result for more blocks.

## Closest literature and limitations

- Higgins, Kelley, Sieben, Godbole (2015), https://arxiv.org/abs/1502.04076 , https://doi.org/10.37236/5051 : the closest directly relevant full-text source, for existence and permutation-lifting.
- Chung, Diaconis, Graham (1992), https://doi.org/10.1016/0012-365X(92)90699-G : foundational partition-cycle framework, bibliographic access only here.
- OEIS A016031, https://oeis.org/A016031 : classical de Bruijn enumeration, not a prior attribution of the partition correspondence.

Alphabet size is fixed at two globally; rotation and bit complementation are counted as specified; reversal is not quotiented. No independent audit or historical-priority validation has been performed.

Self-review: passed. Independent audit: not yet performed.
