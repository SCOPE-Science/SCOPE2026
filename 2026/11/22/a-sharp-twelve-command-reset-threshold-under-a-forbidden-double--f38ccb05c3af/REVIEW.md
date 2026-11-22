# Self-review

## Correctness

**PASS.** The claim is finite, over exactly 65,536 pairs of total transformations of four labeled states. The 31-state image-subset/last-symbol construction is proved by a length induction; its shortest-path metric is exactly the requested constrained reset length, and its full reachable-state closure settles nonexistence. The provided deterministic checker compares this BFS method to an independent exact-length family recurrence for every transition pair, verifies all twelve positive-length bins and the infinite bin, replays a specific 12-letter reset word, and checks a unique 24-element state-conjugacy orbit. An unrestricted baseline is computed independently. Reproducibility uses no third-party dependencies.

## Originality

**PASS, with residual priority risk.** Searches of finite-state constrained synchronization, forbidden `00` input languages, and four-state reset-word thresholds, including the research database, found no statement giving the full labeled exact constrained spectrum, the 24 extremal transition tables, or the 5,424 lost ordinary synchronizers. The 2012 Kisielewicz--Kowalski--Szykuła preprint concerns *unrestricted* shortest reset words; the 2022 Volkov survey sets out regular-language constraints without this enumeration. Other accessible four-state studies concern unrestricted state complexity, adversarial games, or other reset metrics, none of which implies a numerical count for the different, letter-asymmetric language restriction. The inspected 2021 Hoffmann full-text introduction, main theorems and appendix address commutative and simple-idempotent automata or complexity classifications; no exact census of all four-state binary transformations is stated in those material sections. Other unindexed finite tables remain a priority risk.

## Mathematical value

**PASS.** A local input restriction models an actuator command that cannot be repeated consecutively. The result gives a complete first-small-scale benchmark for how such a constraint changes synchronizability and latency: 5,424 ordinarily resettable four-state devices lose all admissible reset words, and the sharp surviving worst-case latency doubles from six to twelve for a uniquely characterized family. The full finite distribution and extremal rigidity, not merely code reproducibility, are the mathematical content. It does not assert a general-state bound.

## Closest sources and boundaries

Kisielewicz--Kowalski--Szykuła (arXiv:1203.2822) supplies the unrestricted subset-BFS context, not the forbidden-factor constraint. Volkov (Russian Math. Surveys 77, section 2.2) introduces regular-language-constrained synchronization, not this census. Hoffmann (arXiv:2109.02743) treats constrained synchronization for restricted automaton classes; the relevant full-text sections, including Theorem 4.3, were read and compared against this all-table census. The exact values here apply only to four *labeled* states and two ordered input letters, and the symmetry is state relabeling only.

Self-review: passed. Independent audit: not yet performed.
