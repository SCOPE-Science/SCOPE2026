# Review: dyadic Rudin–Shapiro extremal-factor localization

## Correctness — PASS
The argument uses the exact recursive signed blocks \(P_k,Q_k\), their closed prefix extrema and least attaining indices. Every dyadic-length factor straddles at most two aligned blocks. An explicit bound separates the even-to-odd block order (too small to be extremal) from the odd-to-even order, and the first eligible sign pair and the earliest prefix extrema give the four exact starting positions. The standalone integer checker tests all start positions in a sufficiently long initial segment through \(k=16\), including all claimed first witnesses; the proof alone supplies the all-\(k\) statement.

## Originality — PASS, qualified
Lü–Chen–Wen–Wu's 2016 open preprint, subsequently published in 2017, proves the maximal and minimal sums and supplies constructive factor existence; Lü–Han (2022) studies complexity and the *lengths* at which complexity-level extremes occur. Neither inspected result supplies the least *factor starting position* at a fixed dyadic length. OEIS A350774 records the older complexity values, not first occurrences. Research-record and accessible-claim comparisons found no equivalent localization law. The 2022 full text was examined through its openly accessible article reproduction, though unindexed prior first-occurrence results remain possible.

## Value — PASS
The first-observation threshold is mathematically different from the value spectrum: it asks how far a finite observed prefix must extend before an extremal Parikh class appears. The theorem supplies an exact infinite family with nontrivial parity dependence and asymmetric positive/negative witness thresholds. It does not assert a new result for the previously known extremal sums or for non-dyadic lengths.

Self-review: passed. Independent audit: not yet performed.
