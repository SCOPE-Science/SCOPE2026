# Scientific review

## Correctness

**PASS.** The six transition images for each fixed singleton endpoint choice range independently over all \(8^6=262{,}144\) tables. Every reachable powerset state is found by closure of exactly eight possible masks; minimization is an exact stable Myhill--Nerode partition or pair-distinguishability fixed point. The two independent programs tally identical full and trim joint spectra from the enclosed CSV, with complete finite checks and exact witness examples. The endpoint relabeling multiplicities three and six yield all \(9\cdot2^{18}\) labeled instances. No infinite extrapolation is used.

## Originality

**PASS against inspected sources, not a guarantee of historical priority.** Baburin and Cotterell (arXiv:2611.10911v1, §§2,5–7) establish general minimization/overhead context and approximation hardness, not the complete two-variable enumerative spectrum. Nicol and Frohme (TACAS 2026, §§2–5) address on-the-fly minimization and benchmarks rather than enumerating all three-state singleton-endpoint binary NFAs. Jirásková (2006) treats existence of deterministic blow-up sizes, which cannot determine our labeled counts. Semantic searches and statement-level comparisons of relevant mathematical records found no covering indexed census, but the possibility of an unindexed equivalent table remains.

## Value

**PASS.** Quantifying the gap between reachable subset construction and minimal deterministic language complexity is explicitly motivated by recent work on practical determinization and approximation hardness. The result is a complete finite classification of a natural three-state binary stratum of general nondeterministic relations, separating endpoint incidence and trimness rather than selecting an ad hoc subset. It determines a sharp five-state additive overhead even under trimness, its exact prevalence, and an eight-subset reachability boundary where at least four minimal states remain necessary.

## Scope and residual risk

This does not yield general asymptotics, a faster determinization algorithm or novelty certification against unindexed prior computations. The exposed material in the 2006 state-hierarchy paper was abstract-level only; its full text was not asserted to be ruled out. All claims are restricted to the finite domain and proof/checker specification in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
