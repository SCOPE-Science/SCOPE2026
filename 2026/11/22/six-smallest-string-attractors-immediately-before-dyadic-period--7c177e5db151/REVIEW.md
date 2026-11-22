# Self-review

## Correctness — PASS
The exact domain and one-based normalization are fixed. The proof has two directions: the morphic lifting lemma propagates six base pairs; a globally exhaustive finite window-mask certificate eliminates odd marked zero positions, and a parity-rigidity reverse projection halts all other pairs. The base pair list is exhaustively enumerated, all critical substitutions and singleton boundary cases are addressed, and independent direct checks at five orders agree. Residual correctness risk: a transcription error in the finite certificate or the local-to-global reduction; the accompanying full checker makes that reduction auditable.

## Originality — PASS with explicit priority risk
Schaeffer–Shallit prove minimum attractor **size** for arbitrary prefixes, not an explicit minimum **multiplicity formula** at length one less than a power of two. Banbara et al. prove exactly two attractors for full dyadic words and explicitly provide an automaton recognizing the full arbitrary-prefix relation; this automaton *implicitly covers* all specializations, but their inspected text does not state the six-pair arithmetic formula or the boundary jump and explains that interpretation is nontrivial. The new contribution is an explicit infinite-family structural classification with a general lifting lemma and an independent local proof. This is not a claim of a new decision procedure or of a first general characterization. Prior-index result summaries for greedy attractors and dyadic unique substrings do not imply the claim. Historical risk remains that someone already extracted the same six-pair formula from the general automaton.

## Value — PASS
The published paper explicitly motivates the mathematical significance of *multiplicity* of minimum attractors. The discontinuous six-to-two boundary at every dyadic scale is a natural and sharp refinement not provided by knowing only minimum cardinality, and demonstrates meaningful sensitivity to one-letter truncation. Unlike a one-off census, the classification holds for infinitely many lengths, with a proof mechanism usable in other morphic contexts. Its value does not depend on a larger classification for all prefix lengths.

## Limits
One anchored infinite family, not all arbitrary prefixes; accessible source full text for the original older theorem was limited to its abstract, whereas the closely relevant 2026 paper was inspected in full relevant sections. The 2026 paper's arbitrary-prefix automaton is a genuine known stronger decision procedure, so novelty is claimed only for the previously unstated explicit structural law, not general coverage.

Self-review: passed. Independent audit: not yet performed.
