# Scientific review: unordered count-only occupancy identification

## Correctness — PASS

The theorem covers exactly the parameter space \(0<\psi,\pi,p,r<1\) under stationary two-state availability and the specified no-false-positive conditional detector. Exact subset-product moments imply the four displayed binomial-moment formulas. Their scale-free invariants have a strictly positive derivative in the nuisance shape coordinate and strictly negative two-dimensional Jacobian, with a connected admissible level curve; this proves **global**, not only generic or local, uniqueness. Back-substitution recovers all four physical probabilities. A separate exact-rational pair produces the same entire three-visit total-count distribution, proving sharpness. The standalone checker independently enumerates Markov paths and gives 4,768 supplementary assertions; those tests are not substituted for the proof. The zero- and unit-memory boundaries are excluded and stated as nonidentifiable.

## Originality — PASS on inspected evidence, with residual priority risk

The nearest ecological source, Goldstein et al. (2024; DOI 10.1111/2041-210X.14359), motivates autocorrelated survey availability and was read in full. Hines et al. (2014; DOI 10.1111/2041-210X.12186) address correlated replicated occupancy with time-resolved survey data; Cole (2019; DOI 10.1007/s40300-019-00156-3) addresses identification of hidden Markov processes with ordered histories. An identified published mathematical finding for **three anonymous counts at known-occupied sites** has no independent structural-occupancy parameter; its result cannot imply identification of an additional unknown occupancy probability. The present theorem concerns only the **distribution of a total count per site**, identifies all four unknowns, gives a global inverse for positive memory, and establishes the sharp number of occasions. Broad literature and research-record searches located no explicit equivalent statement. General Markov-binomial mixture or algebraic-statistics literature may contain an equivalent specialization; the 2010 original clustered-occupancy article was not fully accessible. Novelty judgment is conditional on inspected evidence, not a claim of exhaustive priority verification.

## Mathematical and applied value — PASS

Discarding within-site time order is a consequential data reduction for camera-trap and repeated ecological detection studies. The result gives a natural, sharp boundary: a three-visit anonymized count histogram admits distinct ecological mechanisms, while four visits distinguish occupancy, conditional availability, persistence, and detector efficiency over a nontrivial open parameter domain. The exact feasibility test is useful for checking whether an observed idealized distribution could arise from this model. This is a structural survey-design and interpretation theorem, not a trivial extra moment for the known-occupied three-parameter case: the unknown structural-zero component changes the identifiable parameter set and creates a new minimum-design obstruction. It does not imply reliable finite-sample estimation or an optimal field survey.

## Closest literature and remaining limits

Relevant sources are Goldstein et al. (2024), Hines et al. (2010, 2014), Cole (2019), and Schönhuth (2011/2013). Source assessment distinguishes complete open full text from abstract-only evidence in the structured audit. Broader historical priority and empirical suitability of the model remain unresolved. Independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
