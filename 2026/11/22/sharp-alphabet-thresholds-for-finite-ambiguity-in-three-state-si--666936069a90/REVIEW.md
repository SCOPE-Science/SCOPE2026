# Review of the three-state finite-ambiguity alphabet threshold

## Correctness — PASS
The exact domain is trim three-state, adjacent-only singleton-SCC chain NFAs. Three explicit obstruction configurations each create arbitrarily many accepting runs on pumpable words. Consequently every eligible alphabet embeds into one of two concrete 23-type alphabets. The supplied six-coordinate lists give closed integer-matrix sets of 48 elements each, rigorously bounding every word's accepting-run count by four. All 1024 ordered two-letter transition pairs are exhausted and sharp unary, binary, and ternary examples are checked with independent 3-by-3 and six-coordinate implementations. Matrix closure, rather than merely checking words up to a length, establishes the all-word quantifier. Critical packages: `verify.py`, `verify.cpp`, `matrices_X.csv`, `matrices_Y.csv`. No nonstandard external lemma is necessary for the main mathematical proof.

## Originality — PASS, with residual risk
Weber–Seidl (1991, Section 5 and Table 1) already give the three-letter four-path lower bound and the general IDA theory. Kiefer et al. (2026, Sections 2–5) establish the finite-ambiguity framework and an upper bound of twelve for three-state singleton-component chain automata. Neither inspected text gives the matching sharp bound four for all finite alphabets, the binary maximum three, nor the first-alphabet transition. Literature and relevant indexed research were searched by formulation and implication, not just title; an equivalent unindexed calculation or thesis remains possible. The new claim is the full exact three-state threshold, not the previously published four-run construction in isolation.

## Value — PASS
The recent improvement of the maximal finite ambiguity problem makes exact small-state baselines mathematically natural. The theorem closes an actual nontrivial gap between the previously published lower four and upper twelve at three states, identifies a strict binary-versus-ternary boundary, and provides a complete two-maximal-alphabet structural classification. The exact finite semigroup witness is usable in other small-component ambiguity analyses. This is not asserted to solve the general state-count asymptotics.

## Limitations
The result excludes skip edges, different initial/final conventions, and four or more states. The computer-assisted closure proofs require checking the supplied finite matrix lists, all included and reproducible. Remaining originality uncertainty principally concerns unindexed literature, including theses or unpublished enumerations. The displayed result is not externally validated.

Self-review: passed. Independent audit: not yet performed.
