# Scientific review of the triangular-marker antidictionary

## Correctness — PASS

The word's strictly increasing, once-only zero gaps imply that a factor containing two ones has a unique possible occurrence. Every zero-only and one-one word occurs; a putative minimal absence with three or more ones contradicts unique alignment of its two immediate proper factors (the three-one edge case forces consecutive gap values). For a two-one word, the exact left and right feasible zero margins are \(0\le\ell\le a-1\) and \(0\le r\le a+1\), yielding precisely the two parametric minimal obstructions. The language classification uses regular intersection and deterministic counter comparison. The finite-prefix cutoff follows by proving that the first length-\(N\) zero run is the last missing length-\(N\) factor. An independent finite enumerator checks all formulas and cutoffs through length 26; no finite test is treated as an infinite proof.

## Originality — PASS, with a bibliographic risk

Akagi et al. (2022, arXiv:2202.13591) study minimal absent words of finite run-length encoded strings; their explicit finite-string algorithm and five-class categorization are closely related but do not provide the full infinite triangular-marker formula, language class or exact finite-prefix stabilization. Gheorghiciuc (2005, arXiv:math/0512256) supplies a general theorem for **factor complexity** of strictly increasing-gap infinite words, which covers the corresponding factor counts, not the minimal-absent-factor language. That covered factor-complexity formula is explicitly excluded from the novelty claim. published-finding corpus searches for triangular-word antidictionaries, their aliases and the exact two families returned no covering recorded finding; accessible related entries concern finite absent subsequences, other sparse words, or unrelated complexity counts. A possible unindexed equivalent in the broader forbidden-factor literature remains a residual risk.

## Mathematical value — PASS

The minimal antidictionary is a standard language invariant used in symbolic dynamics, string indexing and compressed string algorithms. An explicit infinite forbidden-factor classification for the natural increasing-gap/triangular marker sequence gives exact length multiplicities, a nonregular yet deterministic context-free language, and a sharp quadratic finite-prefix extraction bound. These identify the exact boundary between local admissibility and globally missing factors. The result is an exact structural classification, not a numerical experiment, rebranding of the already-known factor complexity, or an arbitrary finite slice.

The scope is one specified infinite word; it does not classify all gap-increasing words and does not establish new factor-complexity bounds. The formal-language result is derived from the explicit antidictionary. Verification uses only the supplied standalone script and mathematical proof; external expert evaluation is not claimed.

Self-review: passed. Independent audit: not yet performed.
