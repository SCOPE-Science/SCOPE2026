# Self-review

## Correctness — PASS

The candidate specifies a stationary symmetric two-state continuous-time Markov chain, equal conditional detection probability \(p\in(0,1)\), independent attempts, fixed count and compulsory endpoints. The no-detection probability equals a finite positive even-spin-moment sum. Every intervisit gap has its own strictly positive adjacent-spin exponential term, proving positive-definite Hessian and a unique optimum; Markov reversibility yields time reflection symmetry. The derivative at the all-coincident schedule has a strict central-index margin, which by convex KKT conditions proves a parity-dependent short-horizon clustering pattern for every fixed visit count. For five visits, direct expansion reduces the one-variable derivative to a strictly positive factor times a cubic; its unique positive root and boundary signs prove the exact threshold and global optimum. The independent `check.py` path enumeration, rational algebra checks and finite numerical grids returned 31,924 successful assertions. Grid checks alone are not an infinite proof; the convexity and cubic sign analysis are.

## Originality — PASS on the inspected comparisons

Jensen et al. (2022) and Preston et al. (2023) motivate temporal monitoring and repeated sampling but do not derive Markov optimal timing. MacKenzie and Royle (2005), and Guillera-Arroita, Ridout and Morgan (2010), study occupancy-estimator precision and survey allocations, not the exact all-visit zero-detection probability objective. The closest public exact four-survey result proves a different four-visit bifurcation and explicitly leaves arbitrary visit counts unclassified; a three-visit result allows unequal detection quality but does not establish the five-visit cubic or parity law. Relevant published-result searches for five visits, parity and aliases did not reveal dominating coverage. Standard Markov transition, convexity and exponential identities are not claimed novel. Broader survey-design or hidden-Markov scheduling results not inspected in full remain a priority risk; this is not a claim of historical uniqueness.

## Value — PASS

Sampling studies with intermittent target availability must trade repeatedly observing the same latent state against spreading observations to see state changes. The theorem identifies, for every fixed number of attempts, a sharp parity-specific *structural* regime under short horizons; for five attempts it resolves exactly when endpoint replication ceases to be optimal. The full boundary and cubic make a reusable benchmark for sample-timing algorithms and distinguish biological information gain from simply maximizing the probability of one detection. It is neither a numerical recomputation nor a routine rewording of a known four-visit special case, although empirical translation requires a different model and measurements.

## Literature and limitations

Sources: Jensen et al. (2022), DOI 10.1002/edn3.285 (first online 2022-02-23); Preston et al. (2023), DOI 10.1002/edn3.468; MacKenzie and Royle (2005), DOI 10.1111/j.1365-2664.2005.01098.x; Guillera-Arroita et al. (2010), DOI 10.1111/j.2041-210X.2010.00017.x; publicly available exact n=4 and n=3 Markov survey classification results, with links in RESULT.md. The earlier ecological study has a 2023 corrigendum about taxonomic assignment; it is used here only as monitoring motivation. Nonstationarity, false positives, correlated simultaneous replicates, minimum visit separation, field costs, and adaptive design are out of scope. The five-visit classification is not claimed for arbitrary asymmetric availability or heterogeneous detection probabilities. Independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
