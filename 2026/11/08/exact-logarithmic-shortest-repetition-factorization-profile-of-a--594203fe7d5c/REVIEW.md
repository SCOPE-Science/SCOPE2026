# Scientific review

## Correctness — PASS

The digit-length formula gives runs of lengths \(2^j\). The proof treats both possible run counts of a square root (two versus at least three), including boundary truncation, and excludes every nonmonochromatic square. The period-prefix argument excludes nonmonochromatic fractional repetitions. This yields the exact shortest factorization criterion. The length lower bound and explicit witnesses cover every integer \(L\ge2\), including \(L=2,3\) and the upper endpoint \(2^{k+1}-1\) of each dyadic range. The included checker confirms 31,063 finite cases, but all quantifiers rely on the proof.

## Originality — PASS, with residual bibliographic risk

The main comparable source, Shallit and Xu, arXiv:2311.14961v2, was inspected through its results, proofs and open-problem section. Its Theorem 1 constructs automata for fixed bounded factorization width; its Thue–Morse, Fibonacci and paperfolding conclusions are bounded shortest-width examples; its Rudin–Shapiro theorem is about unbounded *longest* widths. None states or logically entails the exact logarithmic *shortest*-width envelope for this different automatic word. Search queries targeting binary-length parity, increasing runs, nonmonochromatic squares, and unbounded shortest factorization widths found no exact equivalent in the inspected records. Inoue et al. (2022) prove finite-string algorithms; only their abstract could be examined, and expanded journal coverage is not fully excluded. Results from mathematical records with superficially similar logarithmic formulas concern different invariants such as string attractors.

## Mathematical value — PASS

The paper's distinction between bounded shortest widths and unbounded longest widths motivates seeking a simple automatic sequence with unbounded *shortest* widths. The theorem supplies not merely an example but the full optimal-length profile for every factor length. The structural no-nonmonochromatic-repetition lemma explains the result and establishes a useful run-factorization principle; this is not a finite table, arbitrary parameter slice or renaming of a source result.

## Limitations and prior comparison

The theorem does not solve the unrestricted decidability problem or claim anything about regularity, minimality or uniform recurrence of the sequence. The 2024 journal version of the guiding paper and the 2022 finite-string algorithm paper were not available for full-text comparison; equivalent unindexed work may exist. Exact proof rather than numerical extrapolation supports correctness.

Self-review: passed. Independent audit: not yet performed.
