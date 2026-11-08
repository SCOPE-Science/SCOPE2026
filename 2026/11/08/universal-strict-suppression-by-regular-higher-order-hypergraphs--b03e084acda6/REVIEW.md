# Scientific review

## Correctness — PASS

The claim is a rigorous infinite-family inequality, not an inference from simulation. Each parent-edge event has probability given exactly by fitness divided by the total fitness, then by common incidence degree. Summing these events produces the claimed conditional drift. The scalar contribution \(G_{a,b}\) has zero value and slope at neutrality and strictly positive second derivative on the positive half-line whenever a hyperedge contains both types and has at least three nodes. Connectivity guarantees a mixed edge at each mixed state, so the bounded exponential mutant-count process has strict positive drift. Positive-probability monotone mutant-spreading paths rule out nonabsorbing recurrent classes. Optional stopping establishes the strict Moran comparison for both fitness directions, and direct count drift gives neutrality. The pairwise boundary follows from identically zero edgewise drift. The packaged verifier checks 8,112 exact-rational assertions, transition normalization, complete finite fixation systems and published small-size formulas. No hidden numerical bound is required.

## Originality — PASS, subject to priority uncertainty

The 2023 Liu–Masuda full model and full accessible supplementary text were inspected, including its complete/cyclic/star triple examples, formulas (20)–(41), discussion and supporting texts. Those examples do not entail a universal bound across arbitrary incidence-regular nonuniform hypergraphs or arbitrary mutant sets. The 2024 Liu–Masuda multilayer martingale method and the 2026 Sheng–McAvoy–Tian–Zhang–Fontan–Plotkin hyperedge approximation were inspected for stronger coverage. The former has coupled two-layer fitness and single-neighbor replacement, while the latter changes one focal node under death–birth/complex-contagion rules and derives weak-selection approximations. Neither yields the stated exact group-overwrite drift. The classical isothermal theorem supplies equality only for regular pairwise graphs. Mathematical-record and primary-literature searches found no statement implying the claimed all-parameter theorem. This does not prove global priority: unindexed or differently formulated stochastic-process results could exist.

## Value — PASS

Higher-order simultaneous replacement was proposed as an important mechanism for selection suppression, but the originating source relied on specific symmetric calculations and finite/empirical evidence rather than a structural theorem. A proof valid for every incidence-regular hypergraph, every initial mutant set and every positive fitness supplies a natural generalization and a clear contrasting rank-two equality boundary. It removes the need to compute an exponentially large absorbing chain to decide the sign of selection for this broad class. The scope remains biologically meaningful while excluding irregular incidence and alternative update rules.

## Closest literature and limitations

- Liu–Masuda (2023), https://arxiv.org/abs/2301.05343 : same update mechanism but selective examples, not an all-regular-network theorem.
- Lieberman–Hauert–Nowak (2005), https://doi.org/10.1038/nature03204 : equality for ordinary regular graphs.
- Liu–Masuda (2024), https://doi.org/10.1137/23M1620144 : analogous exponential submartingale on two-layer, not group-overwrite dynamics.
- Sheng et al. (2026), https://arxiv.org/abs/2605.23444 : different single-focal update and weak-selection approximate scope.

The proof does not extend automatically to irregular incidence, majority-conditioned reproduction, state-dependent fitness, or fixation times. Independent validation and independent publication-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
