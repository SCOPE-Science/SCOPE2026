# Review: exact explanation profiles for finite-trace persistence

## Correctness — PASS

The domain is all nonempty fixed-length binary traces for the weak-next persistence formula. A locked partial trace is consistent with a compliant completion precisely when it contains no earlier fixed one and later fixed zero. This proves the inversion-pair AXp theorem for violations. The complete list of compliant alternatives is parametrized by a cut; direct inclusion testing of the disagreement sets yields precisely the boundary/rise CXps and hence the number of descents plus one. For satisfying inputs, direct inspection of singleton and boundary-pair flips, followed by minimal hitting-set duality, gives all explanations. Padding a binary word by zero and one produces a bijection between words with a fixed descent count and subsets of its transition gaps, proving the binomial coefficients. Inversion extrema and total counts follow by elementary incidence counting. Exhaustive direct-completion enumeration, not based on the closed formulas, for all words through length eight returned `ALL_CHECKS_OK`. These finite checks are not substituted for the proof.

## Originality — PASS, with residual priority risk

Fionda--Ielo--Ricca, arXiv:2610.35169 (first submitted 2026-10-26), establishes the general explanation semantics and hitting-set duality and exhibits an exponential independent-clause example. In inspected full text it does not state this shared-proposition persistence classification. An earlier two-letter until-formula explanation classification addresses a different language and does not imply the current results. Searches for persistence/weak-next explanation spectra, inverse-pair and descent formulations, and finite-trace AXp/CXp counts did not identify a stronger covering statement. This is best-knowledge originality, not proof of priority: an older general theorem on nested minimal covers or Boolean implicants remains a possibility.

## Value — PASS

The result completely classifies a natural, single-safety-formula explanation space under the formal definitions of a recent foundational temporal-explanation paper. Unlike arbitrary temporal obligations with exponentially many contrastive explanations, one shared persistent proposition forces a linear contrastive bound for both compliant and violating traces. It supplies exact per-trace profiles, sharp extremal counts and a complete binomial distribution over inputs; these are useful as explicit test families and illustrate which structural dependence among obligations prevents exponential explanation blow-up. The result is not merely an instance of the general duality, because determining the actual minimal families and all-length spectrum requires the cut and inversion arguments.

## Limitations

Finite experiments cover lengths one through eight, not the infinite assertion. Claims are fixed-length, weak-next and single-proposition; no unrelated temporal formulas are covered. A more general prior implicant or graph-cover theorem might imply a specialization despite different terminology. Historical priority awaits external review.

Self-review: passed. Independent audit: not yet performed.
