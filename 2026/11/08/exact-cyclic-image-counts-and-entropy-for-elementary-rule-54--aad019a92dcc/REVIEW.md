# Scientific review: exact cyclic image counts for Rule 54

## Correctness — PASS

The labeled periodic predecessor/output correspondence follows from closed walks in the four-state de Bruijn graph with explicitly given Boolean edge relations. It covers even ring sizes one and two. The independently reconstructed relation monoid has 109 states, is closed under both output letters, and obeys a **full 109-coordinate vector annihilator**, not just a finite scalar numerical fit. Multiplication by the transition operator establishes the recurrence for every later index; its initial values yield the rational generating function. Direct enumeration of all inputs through ring length 18 separately reproduces every corresponding output-image count. Asymptotic claims follow by exact quartic factorization, with the other roots strictly inside the unit circle or on it as the harmless \(\pm i\) pair.

## Originality — PASS, with residual historical risk

The closest accessible original Rule-54 study, Martínez, Adamatzky and McIntosh, *Complete Characterization of Structure of Rule 54* (arXiv:1410.3096v1, first public 2014-10-12), was inspected in its HTML full text, particularly the exact local rule, de Bruijn graph, subset table and Garden-of-Eden discussion in Sections 2, 3.3, 3.4 and 4. It establishes the underlying symbolic machinery, not the same-period cyclic image-count generating function. General Garden-of-Eden and finite-state image-language methods are acknowledged as prior techniques; computing finite-period image counts requires closed-relation rather than merely path existence. A published Rule-54 phase-filtration study treats invariant dynamics within another model, not image cardinalities of one Rule-54 update. Separate counts of outputs with exactly one predecessor do not imply the full image size, which includes larger inverse fibers. Targeted searches for Rule-54 image cardinality, periodic Garden-of-Eden counts, specific initial sequence terms and the quartic growth constant found no directly covering theorem; a failed search alone is not a novelty proof. Older unindexed computations and overlooked image-language tables remain a material risk.

## Value — PASS

The exact count of one-step attainable outputs on a finite cyclic ring is a natural, previously unquantified here, information-loss invariant of a prominent nonlinear cellular automaton. The result supplies a full formula rather than an arbitrary cutoff, identifies the exact algebraic exponential rate \(\lambda=(1+\sqrt{3+2\sqrt5})/2\), gives the proportion of unreachable configurations at every size and distinguishes same-period predecessors from arbitrary bi-infinite antecedents. The compact six-term recurrence emerging from a 109-state Boolean relation closure is a structural compression. It is not an assertion about multistep dynamics or an independent audit.

## Limits and closest prior literature

The established claim concerns only indexed cyclic rings and exactly one synchronous update of Rule 54; it does not classify multiplicities of positive inverse fibers. The 2014 paper provides an explicit 16-subset diagram and minimal forbidden patterns for the corresponding infinite-language problem but no displayed same-ring image enumerator. Mathematical historical priority and the computation deserve independent checking.

Self-review: passed. Independent audit: not yet performed.
