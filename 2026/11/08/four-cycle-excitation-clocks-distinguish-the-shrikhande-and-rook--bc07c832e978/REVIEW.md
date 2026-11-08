# Scientific review

## Correctness — PASS

For both explicitly defined 16-vertex graphs, the transition is a deterministic map on exactly \(3^{16}=43,046,721\) states. A full indegree-peeling cycle census and an independent direct-path enumeration yield identical complete \((T,P)\) tables, with 19 and 21 nonempty classes. Both reproduce the counts of primitive four-cycles (98 on the rook graph, six on Shrikhande), primitive three-cycles (3,987,936 and 4,109,384), and sharp entry-time bounds (eight and nine). Full graph automorphisms, not a chosen proper subgroup, are applied to every four-cycle. Local-neighborhood fingerprints give a group-size upper bound matching the explicitly enumerated affine/permutation automorphisms. The included replay checker checks the reconstructed outputs and the entire census; its reproducible result is `VERIFICATION_OK`. This is an exhaustive *finite* claim, not extrapolation to other graphs.

## Originality — PASS, subject to stated residual risk

The 2016 Gravner–Lyu–Sivakoff primary paper defines the same update and characterizes finite-graph synchronization and asymptotic excitation through the circulation of the initial coloring, but does not report the labelled temporal class counts, the 98-vs-6 four-cycle contrast or the graph-automorphism orbit partitions. Brouwer–Haemers record the same graph pair, spectra and switching constructions, but not the three-color Greenberg–Hastings dynamics. An accessible published record concerning independence complexes of these two graphs has a different invariant; a published period-four census for a complete-multipartite **parity** rule uses a different map. Within this record, earlier complete finite censuses of the same excitable rule concern different graphs (Petersen, Clebsch and others), while a strongly-regular graph wave classification uses a different reversible two-level linear map. A direct implication of those claims giving the exact present pairwise census was not found. Failure to find a result is not a uniqueness proof; an unindexed historical specialization remains a risk.

## Mathematical value — PASS

The Shrikhande/rook pair is canonical because its nonisomorphic members have identical strongly regular parameters and ordinary spectra. Their nonlinear excitable dynamics is distinguished by an exact conjugacy-invariant number (six versus 98 primitive four-cycles). The two different 4-cycle symmetry partitions (one type versus three) and their firing profiles provide a stronger structural comparison, and the complete labelled transient census is a reusable finite test case for coupled excitable automata. This is a motivated complete finite classification, not a parameter-substitution exercise.

## Limits and nearby literature

The general covering-space/circulation framework does not itself supply these 40 exact entry-period cells; the result adds an exhaustive graph-specific computation rather than contradicting that theory. The 1978 model, 2016 general theory, and standard cospectral-pair construction are acknowledged prior art. The historical-priority uncertainty and absence of independent audit remain explicit. The result does not extend beyond the two graphs and this exact three-color synchronous rule.

Self-review: passed. Independent audit: not yet performed.
