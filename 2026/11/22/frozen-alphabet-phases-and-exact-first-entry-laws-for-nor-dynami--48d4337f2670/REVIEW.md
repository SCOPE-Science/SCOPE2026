# Scientific review

## Correctness: PASS

The statement fixes the edge orientation, incoming-only Boolean NOR rule, domain \(q\ge2,d\ge1\), definition of first periodic entry, and independent Bernoulli initialization. The proof explicitly reduces the dynamics after \(d-1\) steps to loopless-complete-graph NOR, proves the exhaustive recurrent set and sharp bound, partitions initial variables into disjoint predecessor trees, and derives the cumulative time law and exact basin counts. The derivative argument for the twofold scalar recursion proves the critical-bias limit. The included program independently checks complete small examples and integer counts. Random sampling is not offered as an all-size proof.

## Originality: PASS, with residual risk

The closest accessible claims are the general directed Boolean graph-dynamics survey, a special-digraph study whose accessible extended abstract names paths/cycles/stars/arborescences, and an existing de Bruijn incoming-NOR result. The latter uses full words with repeated symbols allowed and has no one-hot frozen Kautz phases; its uniform-oscillator distribution does not imply the additional block-selective term or fixed-phase probability established here. A Kautz XOR result concerns a different linear update. Searches for Kautz NOR, equivalent prefix-tree formulas, exact entrance distributions and broader line-digraph coverage found no demonstrated implication of the complete claim. The 2013 journal version of the special-digraph study was not fully accessible; a historical equivalence there or elsewhere remains a risk.

## Value: PASS

The compared graph families are canonical bounded-degree low-diameter word networks, and removing forbidden adjacent-symbol words changes the set of nonlinear recurrent states. The exact first-entry shell and labelled-basin formulas work for every alphabet and depth, and the isolated critical-density frozen survival differs qualitatively from the almost-sure global oscillator for any fixed off-critical initialization. This is a motivated complete dynamical classification, not an arbitrary small graph table or a renaming of the NOR-tree recursion.

## Scientific limitations

The graph is directed and reads only its incoming neighbors. There is no uniformity in a bias that approaches criticality with increasing depth. Published mathematical priority is assessed under accessible-source limitations; external independent validation is pending.

Self-review: passed. Independent audit: not yet performed.
