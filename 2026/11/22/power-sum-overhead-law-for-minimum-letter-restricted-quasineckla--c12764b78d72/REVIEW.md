# Scientific review

## Correctness (C): PASS

The exact coefficient formula follows from a bijective initial maximal-zero-run and successor decomposition; every word is counted once by its unique initial run and first successor. Burnside's lemma supplies the independent necklace formula, and isolating initial zero-run length one gives the limit. The \(L\ge2\) terms have polynomial order at most \(m^{r-2}\) for fixed \(r\), while nontrivial rotational terms are exponentially small for \(s\ge2\). The independent exhaustive and arithmetic comparisons passed (see the verification files). There is no unproved analytic interchange, only formal coefficient extraction and fixed-parameter asymptotics.

## Originality (O): PASS against inspected evidence

The 2026 Gabrić–Sawada primary text (https://arxiv.org/abs/2607.05324), read at its definition, univariate counting recurrence, global injection, and bounded-weight sections, does not give an exact count conditional on the number of minimum letters or the resulting nonbinary power-sum overhead. Its constant-overhead statement is unrestricted and not applicable inside a fixed-zero-count slice because its injection changes the content. Published binary quasinecklace fixed-content results cover the alphabet-size-two specialization, so novelty is claimed only for \(s\ge2\). Earlier binary colexicographic pseudonecklace algorithms likewise do not imply the nonbinary successor-order weighting. Actual external searches and record comparisons are detailed in the structured audit.

Residual risks: a nonindexed enumeration could exist, and the conditional enumerator is a close relative of the primary paper's run decomposition. The distinctive claim is the exact nonbinary refined coefficient formula and sharp power-sum limit, not the known global generation algorithm.

## Value (V): PASS

The fixed-minimum-count slice is a natural workload restriction for colexicographic necklace generators. The formula establishes precisely how much filtering overhead depends on alphabet size and prescribed rare-letter multiplicity, including a counterpoint to the global constant bound: for any fixed nonbinary alphabet the worst asymptotic content-slice overhead is unbounded as the minimum-symbol count grows. It also gives all exact finite-length counts and a closed form for the first nontrivial two-zero family, enabling reproducible benchmark targets. This is an infinite parametric structural law, rather than a small arbitrary instance.

## Scientific limits

Only a specified count of the minimum letter is fixed, not an entire nonzero Parikh profile. The ratio takes consecutive limits, first the number of nonzeros and then the fixed zero count; no uniform joint-limit claim is made. Historical priority is not guaranteed by search. Exhaustive tests are independent checks of finite instances and not a substitute for the proof.

Self-review: passed. Independent audit: not yet performed.
