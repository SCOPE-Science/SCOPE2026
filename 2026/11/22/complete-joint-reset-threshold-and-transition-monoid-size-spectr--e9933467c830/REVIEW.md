# Scientific review

## Correctness: PASS

The statement quantifies over all \(256^2=65{,}536\) ordered generator pairs and includes the identity transformation in monoid cardinality. Reachability of every generated map follows inductively from transformation-composition BFS; shortest paths to constant maps give the reset threshold. An independent subset-image search gives the same reset threshold and recomputes the transformation closure separately, matching all 179 reported cells. The two 48-element extremal orbits are reproduced by explicit conjugacy-and-letter-swap actions. Finite searches are exhaustive over the precisely stated finite universe rather than being used to infer anything at larger state count.

## Originality: PASS relative to checked evidence

Szykuła's 2026 synchronization survey motivates the reset-length coordinate but supplies no monoid-size–reset-length joint table. East–Egri-Nagy–Mitchell (2017) enumerate transformation semigroups by size and rank but not by specified two generators and their shortest constant-product length. Kisielewicz–Kowalski–Szykuła (2016) establish reset-length bounds and experimental facts without this joint count. Gonze et al. (2017) study full-transition-monoid reset bounds and not the two-generator four-state spectrum. Indexed closely related small-automaton findings address adversarial synchronization or synchronizing-word language state complexity, which are distinct invariants. The classical extremal reset bound nine is acknowledged as known; the new statement is the complete 179-cell joint spectrum and the two monoid-size extremal orbits. Residual risk: unindexed exhaustive datasets or generator-specific classifications may contain an equivalent tabulation.

## Mathematical value: PASS

Reset threshold measures the shortest control sequence collapsing all states; monoid size measures the diversity of possible transformation behaviors. Their joint distribution is not derivable from either marginal alone. The sharp loss of 31 possible monoid elements when the reset threshold rises from eight to nine, and the division of the slowest machines into exactly two algebraically distinct symmetry orbits, provide a natural complete small-state boundary with uses for testing hypotheses connecting synchronization delay and transformation-semigroup complexity. The scope is explicitly small and finite, with no exaggerated asymptotic conclusions.

## Limits

Classification concerns all complete ordered two-letter four-state automata, not larger automata, nondeterministic devices, or partial transitions. Novelty is assessed against examined accessible literature and indexed publications, not certified universally.

Self-review: passed. Independent audit: not yet performed.
