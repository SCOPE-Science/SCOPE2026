# Scientific review: exact fixed-width interval online ranks and shattering polynomials

## Correctness — PASS

For every n≥r≥1, the proof first bounds online depth by the number of distinct windows (m or m+1) and by the size r of every positive query fiber. A proven prefix-threshold lemma on blocks of at most r consecutive window starts supplies matching complete mistake trees. The null branch induction is carried out for 2^h−1 consecutive starts plus the empty concept. For static shattering, 101 is forbidden on any triple, and four binary pair labels are characterized explicitly, then counted by inclusion-exclusion. Edge cases r=1 and m=1 are included. A separate defining-recursion checker passed on 272 rank classes (n≤16) and exact trace coefficients for n≤14; enumeration corroborates but does not prove all-parameter identities.

## Originality — PASS within available comparisons

Compared the actual all-parameter null/nonnull ranks and pair coefficients, including their implication relations, with accessible prior theory on Shelah 2-rank and closure bounds and with the related cyclic-window rank. The cyclic result is not an equivalent linear-chain theorem (boundary traces differ; numerical example n=10,r=4). Exhaustive searches found no decisive published broader coverage, but historic priority may exist under banded consecutive-ones/active-window terminology; this remains an explicit unresolved risk.

Closest literature: Chase–Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566; Alon–Beimel–Moran–Stemmer, *Closure Properties for Private Classification and Online Prediction*, PMLR 125 (2020); Ghazi–Golowich–Kumar–Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, PMLR 132 (2021); Malliaris–Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569 (2021). The related cyclic-window rank statement is for a different concept class, with wraparound. Incomplete historical indexing and alternative terminology are residual originality risks.

## Mathematical value — PASS

The natural problem is point-membership identification of an equal-length sliding interval with or without a null state. The result simultaneously classifies its exact adaptive and static shattering across every ground-set size, gives a sharp power-of-two boundary at which one null hypothesis increases online rank, and exhibits an unbounded VC=1 versus Littlestone gap along n=2r. The exact null-state transition and paired shattering polynomials are structural facts not merely a numerical gain or a fixed-size census.

## Verification and limits

Running `python3 verify_windows.py` gave `WINDOW_RANK_AND_TRACE_PASS 136 n_r_pairs 272 rank_classes n_max 16 polynomial_n_max 14`. The checker computes online ranks from the definition and traces from literal membership patterns; it does not certify the unbounded theorem, which rests on the mathematical proof. No external independent audit was conducted.

Self-review: passed. Independent audit: not yet performed.
