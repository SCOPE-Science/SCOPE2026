# Self-review

## Correctness — PASS

The explicit statement quantifies over all nonempty pointed models with independently reflexive/transitive relations, finite nonempty sets of modal-index words (including the empty word), and all valuations. Run reduction is justified by relation idempotence, and scattered-subsequence dominance by reflexive insertion. A finite prefix trie with one label per directed edge is itself an admissible finite model: its only paths to an antichain leaf require the leaf word to embed in the demanded operator word. Thus each leaf is indispensable and the exact uniform support bound is proven, rather than inferred from finite testing. The prefix-free cylinder argument gives the sharp length-layer maximum, including the separate one-letter and empty-word cases. The standalone checker was executed successfully, reporting `VERIFY_OK cases=1469 max_q2=2 q3_d3=12 trie_worlds=22`. No proof relies on empirical extrapolation.

## Originality — PASS within inspected material

The closest direct source is van Benthem, ten Cate and Yang (2026), Section 2.4 and Proposition 2.9, establishing finite witness bounds without giving their exact least value for an independently indexed reflexive-transitive modal path conjunction. Earlier continuity and modal-operator references do not imply the antichain formula or its sharp two/three-modality threshold from their inspected statements. Two relevant statement-level research records about generalized path conditions and fixed-frame S4 word ranks address different objects or hypotheses. The main residual risk is an unindexed result on the free idempotent word monoid or on exact support width of positive modal path conjunctions; uniqueness has not been certified, and search absence alone is not evidence of novelty.

## Value — PASS

This is a motivated exact quantitative refinement of the standard strong-continuity property, turning a nonconstructive existential budget into a structural normal form with explicit extremal finite models. The two-versus-three modality transition is substantive: arbitrarily nested two-modal pure-path conjunctions need no more than two atomic witnesses, whereas a third independent modality yields an exponential worst-case rank in depth. This distinguishes alphabet dimension and nesting depth and supplies a computable exact certificate for the restricted syntax, rather than a numerical curiosity.

## Limits and source comparison

The theorem treats only finite conjunctions of existential word paths to one positive atom; the exponential bound does not apply generally to negation, universal modalities, additional Boolean nesting or interaction axioms. Primary text inspected: van Benthem et al., arXiv:2603.12171v1, especially Section 2.4, and Gouveia–Santocanale, arXiv:1704.03772, Introduction. The two closest indexed statement records are `2026/10/13/SCOPE-length-two-generalized-path-conditions-form-a-six-way-antichain--8fded11c0af7` and `2026/10/12/SCOPE-rank-graded-s4-modalities-on-finite-two-row-stable-kripke-frames--00d57ca864fb`. Neither inspected statement entails this result. Their full texts were not material-read, leaving a specific historical-priority risk. No external or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
