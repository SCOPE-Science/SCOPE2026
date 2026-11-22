# Self-review

**Claim assessed:** Two-type Poisson epidemic survival-probability ordering is exactly the ordering of total offspring row sums at every supercritical common scale; a strictly positive three-type matrix has a crossing between scales \(1\) and \(20\), so dimension three is minimal.

## Correctness — PASS

The parent-to-child convention is stated explicitly; it is the transpose of the underlying published reproduction-operator convention. The Poisson generating function gives the fixed-point equation. Strict positivity and supercriticality give a unique positive solution. The two-type inequalities follow from the strict increase of \(-\log(1-x)/x\), with the direction of the cross terms checked. The three-type proof uses only exact rational inequalities and the scalar Poisson mean-two survival bound, rather than treating numerical iteration as proof. The continuity step is secured by an invertible Jacobian at each positive fixed point. The extracted checker independently reproduced the rational certificates and test cases. The theorem does not assert uniqueness of the three-type crossing.

## Originality — PASS, with literature limitations

Wang and Valdano's 2026 paper (open full text, Results and Methods) provides the multitype model, epidemic probabilities, and the homogeneous-total condition. Its conclusions do not imply that the *ordinal rankings* must agree for **all** two-type positive matrices, nor do they exhibit a three-type fixed-matrix ranking change under scalar amplification. The closest search results concerning two equitable-community SIS **endemic infection levels** concern a deterministic equilibrium, not a multitype branching seed's survival probability; independent-edge SIR tree risk reversals concern finite outbreak-size statistics. Two-way cross-group branching risk bounds constrain products of transmission rates, not rank by total row offspring. Exact-priority searches did not find a statement equivalent to the paired sharp-dimension theorem; absence from search indexes is not a proof of priority. Historical textbooks and unindexed works remain plausible sources of a component of the theorem.

## Value — PASS

A practical reason to compute an introduction-site survival probability is to rank potential seed sites. The result gives a complete, model-specific classification of when a readily observed proxy—the total expected secondary infections per index case—is guaranteed to rank seed risk correctly, and an explicit *strictly positive* witness showing the threshold at three community types. It also proves that changing only the common transmissibility scale cannot reverse an ordering in two communities but can do so with three; the latter cannot be explained merely by different average contacts. Both the sharp minimum and crossover address a natural limitation in the motivating risk-estimation framework, rather than an arbitrary finite statistic.

## Remaining limitations

No claim is made for heterogeneous offspring laws, independent-edge finite SIR outbreaks, global network epidemic burden, stochastic finite population sizes, or uniqueness of the rank-crossing scale. General mathematics of nonlinear fixed points can contain related comparisons not indexed by the queries used here; independent expert literature review has not occurred. The source's supplemental overdispersion calculations were not fully inspected; the new result is explicitly restricted to its primary Poisson equation.

Self-review: passed. Independent audit: not yet performed.
