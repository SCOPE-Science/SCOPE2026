# Scientific review

## Correctness: PASS

The forced-middle lemma follows from strict increase along every arc. Mixed–mixed adjacency is impossible. Removing closed neighbourhoods of mixed vertices leaves only pure sources and pure sinks; the set of remaining vertices assigned to the middle level is precisely an independent set. This establishes the weighted formula bijectively. The stability inequality injects \(2^{|M|}\) copies of every residual independent set into the independent-set family of the whole underlying graph; strictness follows from a neighbour of a mixed vertex. The double-star tree proves the best possible universal factor and run-length enumeration proves the path formula. The all-size proof is independent of the finite checker (`VERIFY_OK 3473`).

## Originality: PASS within inspected evidence

The closest 2026 paper by Meyer and Starke addresses Datalog and the existence of homomorphisms into transitive tournaments, rather than exact solution counts. Earlier oriented-homomorphic polynomial work does handle tournament homomorphisms in a general way, and the classical directed-path obstruction already determines whether a homomorphism exists. Those do not, in inspected material, state the closed-neighbourhood independence polynomial with the weighted three-layer template and sharp half-gap. Searches of published mathematical records and accessible earlier findings found no equivalent claim. Historical priority remains uncertain, especially for older fixed-template #CSP reductions.

## Value: PASS

The result replaces a yes/no constraint-satisfaction criterion with a complete weighted counting formula, and yields an orientation-level extremal rigidity principle with a sharp stability constant. The proof identifies the mixed-vertex closed neighbourhood as the exact controlling object and produces a natural independence-polynomial reduction suitable for exact counting and parameter studies. The asymptotic double-star extremizers show the gap is not merely a loose consequence of counting.

Self-review: passed. Independent audit: not yet performed.
