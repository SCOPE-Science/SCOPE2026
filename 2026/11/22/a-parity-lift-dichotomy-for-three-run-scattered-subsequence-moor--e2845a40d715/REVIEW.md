# Review: A parity-lift dichotomy for three-run scattered-subsequence Moore counters

## Correctness (C): PASS

The theorem supplies an exact all-parameter proof. The binary Lucas period has precisely \(2^{1+\lfloor\log_2 a\rfloor}\) phases. A phase-preserving group action generates every middle-run counter vector. Explicit same-base opposite-output witnesses establish the independent final parity coordinate except at the odd-initial-run/single-middle-symbol boundary. At that boundary an exact combinatorial congruence eliminates the coordinate. Finally, specified suffixes distinguish every accessible state. Neither extrapolation from finite testing nor an external certification is used in the proof.

Two independent standard-library verification programs reproduce the predicted finite orbits and the two witness regimes. `check_prefix_automata.py` checks 66 orbit sizes, 20 Moore minimizations and 65,520 direct word-count cases. `check_phase_witnesses.py` checks 4,914 symbolic-family witnesses, 40 complete suffix signatures and 877,440 instances of the parity invariant. Every test reports PASS; their range is finite.

## Originality (O): PASS, with priority risk

The closest fully inspected published result is the exact modulo-\(m\) Moore count for the pattern \(010\), which covers precisely the \(a=b=1\) specialization. An existing full formula for two-run \(0^a1^b\) does not imply whether the new terminal zero is an independent state coordinate. The published \(0011\) result is likewise two-run. The inspected 2026 binary Parikh-class paper studies universality and subsequence-containment probabilities; the 2024 generalized-Parikh-matrix article and 2010 formal-power-series paper give representations and algebra, not this minimal-state index.

Searches included full-family parity counters, the aliases *binomial coefficients of words*, *scattered pattern counts*, *Moore state complexity*, phase stabilizers, and relevant small patterns. published-finding corpus claim searches and accessible prior records did not produce a full three-run classification. No absolute priority claim follows from absence of search results. The 2011 trie-automaton paper could be read only through its abstract despite full-text retrieval attempts; its possible stronger content remains a meaningful unresolved risk rather than being declared noncovering.

## Value (V): PASS

This solves an all-length, all-positive-parameter exact deterministic-memory problem for a natural first three-run family. It distinguishes a genuine output-fiber obstruction from the otherwise universal factor-of-two lift and proves the sharp arithmetic condition \(b=1\) with odd \(a\). The family has exponential naive prefix-counter size, whereas the minimal state count grows essentially linearly in \(a\) for fixed \(b\). This classification and its phase-action mechanism have value independent of any conjectured broader theorem.

## Limitations

The theorem is for parity and binary words; no statement is made for other moduli, separate residue acceptors, or arbitrary patterns. The 2011 historical paper remains incompletely inspected and no priority certification or independent mathematical validation is claimed.

Self-review: passed. Independent audit: not yet performed.
