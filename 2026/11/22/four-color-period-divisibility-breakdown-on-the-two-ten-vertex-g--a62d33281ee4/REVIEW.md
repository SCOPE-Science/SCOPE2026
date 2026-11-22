# Review of the exact four-color paired-period census

## Correctness (PASS)

The four-state update maps are defined on exactly \(4^{10}\) labelled states per graph. `compare.cpp` constructs both graphs by their generalized Petersen edges and classifies all states using successor-path decomposition. `verify_indegree.cpp` uses a Cartesian-product/Kneser-disjointness graph construction, a separate base-four local-update implementation, and indegree elimination. Their complete paired-period cells and sharp entry-time maxima coincide exactly. The finite-functional-graph lemma proves that both exhaustive computations determine genuine eventual least periods, including all transient states; the displayed individual five-cycle and consensus trajectories are replayable with `verify_witness.py`. Total-mass checks agree. The proof makes no infinite-family inference from a finite experiment.

## Originality (PASS, with historical-priority qualification)

The closest published results treat four-state GHM on the Petersen graph (marginals only), three-state joint CCA/GHM periods on the same generalized Petersen graphs, a three-color all-graph divisibility theorem, and four-color comparison on complete tripartite graphs. Their full accessible mathematical statements were compared. The known GHM marginal counts are recovered but not presented as new. Neither the three-color results nor the multipartite result implies the four-color paired populations, especially the nondivisibility cells \((1,5)\). A potentially unindexed historical finite census remains a residual risk; inability to prove exhaustive bibliographic priority is not treated as an originality proof.

## Value (PASS)

The previously published exact inter-model period-divisibility theorem is specific to three colors and might invite an invalid four-color extension. Two canonical, equally sized cubic generalized Petersen graphs give explicit failures for a macroscopic fraction of *all* initial states, not isolated accidents: \(258{,}660/4^{10}\) and \(245{,}820/4^{10}\). A full joint table further separates model-specific marginals from true cross-model behavior, making these natural finite benchmark instances for multicolor excitable dynamics.

## Scope and risks

The result does not locate the minimal counterexample graph, does not assert behavior for all cubic graphs, and does not supply a short closed-form dynamical classification beyond these finite state spaces. Some older related full text may be inaccessible. Historical priority and external independent verification remain open.

Self-review: passed. Independent audit: not yet performed.
