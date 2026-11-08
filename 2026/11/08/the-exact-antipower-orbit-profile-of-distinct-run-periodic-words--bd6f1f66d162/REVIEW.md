# Scientific review

## Correctness (PASS)

The unique-boundary-digram lemma proves that different length-\(m\) factors can coincide only as monochromatic factors of the same run. Exact circular distances control all possible block-index collisions, while addition by \(m\) modulo \(L\) identifies the full phase orbit; this reconstructs equations (1)–(3), the nondivisible two-block threshold, and edge cases \(m\ge L\). The independent enumerator passed 31,840 small exhaustive configurations and 1,600 seeded configurations. Finite tests are corroborative, not proofs for all parameters.

## Originality (PASS, with residual risk)

The general-purpose antipower counting algorithm of Kociumaka et al. (arXiv:1812.08101, introduction and sections 4–7 inspected) is a strong comparator; although it would enumerate any fixed finite truncation, it does not state or imply a closed structural longest-run/gcd rule without further specialization and proof. Garg (arXiv:1907.10816, abstract and main theorem proofs inspected) studies aperiodic morphic words, not these periodic run profiles; Berger–Defant (arXiv:1902.01291) addresses aperiodic recurrent words. The closest available research records on Fibonacci antipower radii and earlier Abelian three-antipower phase counts involve different sources or Parikh equivalence. An equivalent specialized formula outside indexed works remains possible.

## Value (PASS)

The motivating gap is a complete all-phase behavior description for finite-order antipowers in a simple but nontrivial periodic family. This determines infinitely many optimal guaranteed block orders simultaneously, proves a sharp gcd transition for full phase-orbit coverage, and provides the exact number of successful phases when the all-phase property fails. These statements address both universal and partial cyclic antipower behavior, beyond evaluating isolated examples.

## Limits

The classification requires unique letter runs per period; general periodic words can have repeated nonmonochromatic factors. The counting object is the set of starting phases and not the set of distinct antipower strings. Published general counting algorithms already solve fixed instances algorithmically; no independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
