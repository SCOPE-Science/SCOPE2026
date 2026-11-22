# Scientific review — sparse threshold-graph births

## Correctness
**PASS.** The rescaled upper-endpoint weight cloud is exactly a binomial point process whose conditional mark distribution matches a rate-one Poisson process; the explicit total-variation bound follows from the Bernoulli–Poisson coupling and contraction under a deterministic path map. The order-statistic clique criterion gives the Gamma one-dependent gaps. Exact integrations count shared-endpoint edge pairs and the nontrivial component. In particular, births use an *infimum* threshold, since the strict inequality delays existence beyond equality. The companion checker passed 7,387 exact assertions on finite integrals, moments and clique thresholds. The asymptotic statements are proved analytically, not from finite tests.

## Originality
**PASS, qualified.** Checked source: Diaconis–Holmes–Janson's random threshold graph representation and dense limit theorem (2009 arXiv manuscript, Section 6.2); the fixed-threshold uniform model of Reilly–Scheinerman (2009, Sections 3 and 5). Those results establish the model and existing fixed-threshold statistics; the inspected arguments do not give the moving upper endpoint process, the joint clique birth-clock sequence, the complete active-component distribution, or the sharp marked-process coupling. Related indexed mathematical records concern finite-memory Pólya threshold graphs and unrelated sparse random networks, without implying this independent uniform-weight upper-tail result. The rare-binomial-point Poisson approximation is standard and not claimed as new. Some unindexed or less accessible historical literature might have the same consequences.

## Value
**PASS.** The moving-threshold upper endpoint is the natural sharp window for the first edge and every fixed-size clique; the theorem characterizes the *whole evolving active graph*, not just isolated probabilities. It quantifies a nonrenewal one-dependent Gamma law for clique waiting times, a non-Poisson sparse edge count, and the complete size distribution of the single nontrivial component. These describe a structured correlated-graph onset that an independent-edge approximation would miss. The finite-no-edge formula and explicit total-variation rate give reproducible controls useful in simulations of rare dense-core formation.

## Evidence and limitations
The proof applies to independent uniform weights, fixed bounded observation windows, and fixed finite sets of clique sizes. Error optimality, growing windows, and general tail laws are not established. Source comparisons support best-knowledge priority only; independent historical and mathematical evaluation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
