# Scientific review

## Correctness — PASS
The common-core selection lemma identifies the same \(k-1\) shared window occurrences in each middle-\(k\) rank set, so one sliding step changes a binary tag count by at most one. Every input difference decomposes into spatial single jumps; each directional response has at most \(2r+1\) changing edges. Integration across finite sorting chambers proves the universal nonlinear two-input bound. A single explicit even–odd permutation gives a middle-rank tag count changing by exactly one on all \(2r+1\) edges. Exact rank counting and reflection prove the witness for every integer radius and trimming level, and comparison with the \(n-1\) edge bound proves the minimal length. The checker independently reproduces the finite arithmetic identities and tests sample pairs.

## Originality — PASS, provisional
Pitas–Venetsanopoulos (1992, Section III-C) describes the trimmed-mean L-filter and robustness; Cai–Yang–Song (2018, Sections 3.1.1 and 3.2.2) discusses image filtering and noise/edge behavior. Neither inspected section establishes the sharp two-input path-variation factor or the minimal path length. Existing published records for three-point and all-radius running medians give the extreme-trim special case. A published cyclic five-point central trimmed-mean result gives its different-boundary special case; neither has an implication yielding this complete all-radius path formula. Bednar–Watt (1984) is a relevant, unavailable full-text risk: its indexed abstract covers algorithms and median-root behavior, not this seminorm, but full priority cannot be guaranteed.

## Value — PASS
The sharp coefficient interpolates from \(1\) for sliding averages to \(2r+1\) for medians and characterizes every intermediate trimming level. The central-common-core cancellation produces a stronger bound than summing the separate rank-filter sensitivities. The precise minimal-length threshold is relevant when selecting robust smoothers on short finite records. The result resolves a natural complete stability classification, rather than an arbitrary fixed-window example.

## Limits and closest literature
This is not one-input variation decrease, not a cyclic bound, and not a claim about arbitrary robust L-filters or adaptive trimming. Historical priority is provisional pending access to early papers. See RESULT.md for the complete analytic proof, references and reproduction instructions.

Self-review: passed. Independent audit: not yet performed.
