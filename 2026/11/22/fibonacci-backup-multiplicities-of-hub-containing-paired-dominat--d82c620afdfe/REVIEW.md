# Review of Fibonacci backup multiplicities of hub-containing paired domination in wheels

## Correctness — PASS

The claim is for every labelled \(W_{n+1}=K_1\vee C_n\), \(n\ge3\), and only for paired-dominating subsets containing the hub. The structural lemma proves that any proper selected rim subset must have precisely one odd-length selected path component; its \(2a+1\) vertices permit exactly \(a+1\) possible partners for the hub, and every even selected path component has a unique perfect matching. This yields the whole bivariate distribution with the matching *count* as the second exponent. Coefficient extraction gives the exact distinct-set and unique-pairing Fibonacci counts; an independent bijection using the hub's matched edge gives the witness total \(nF_n\). Both a direct recursive Python checker and an independently coded C++ subset-DP checker passed from current artifact paths. Boundaries \(n=3,4\), all-rim exceptional states, labelled rotations and matching-count normalization were explicitly checked. Finite tests supplement rather than replace the proof.

## Originality — PASS, with residual historical risk

The closest earlier exact paired-domination polynomial of a cycle (recoverable earlier claim, not reproduced) covers *hub-avoiding* sets only; this theorem expressly excludes those sets, and additionally records the nontrivial multiplicity of pairings for hub-containing selected subsets. The fully inspected wheel sections of Eakawinrujee's 2023 dissertation state the paired domination number and the optimum exchange graph, without classifying all hub-containing subsets by backup multiplicity. Inspected published results for generalized windmills have clique blades, and for circular ladders address a different graph and count witnesses by separate objects; these do not imply the wheel formula. The original Haynes–Slater definition provides only the general concept. An abstract-only 2016 paired-domination polynomial publication says some standard families were computed without naming them: its unavailable full exposition and unindexed literature remain historical risks, not evidence of novelty. Specific statement-level and alias searches in mathematical records and general literature identified no covering result.

## Value — PASS

The number of available perfect matchings is a natural fault-tolerance parameter of paired domination: two vertex sets of the same cardinality can have different numbers of admissible backup assignments. The full joint counting polynomial determines *every* multiplicity stratum, while the three sharp Fibonacci identities distinguish distinct deployments, uniquely paired deployments and all backup witnesses. They imply a limiting unique-pairing fraction \(\varphi^{-1}\) and mean backup redundancy \(\varphi\), a precise reliability phenomenon on a canonical infinite graph family. A prior all-cardinality polynomial without the multiplicity marking cannot answer these questions. The result is not a claim of a general graph algorithm or independent publication priority.

## Limitations and closest work

Labelled, hub-containing wheel deployments only; no assertion about all hub-avoiding cycle solutions or minimal-set reconfiguration. Historical uncertainty persists for the 2016 abstract-only paired-domination polynomial and unindexed literature. The analysis includes the relevant substantive sections of the 2023 dissertation and the complete publicly available related mathematical-result statements. The two verifiers test finite wheel sizes; all orders depend on the symbolic proof and matching bijection.

Self-review: passed. Independent audit: not yet performed.
