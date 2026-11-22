# Scientific review

## Correctness — PASS

The central identity follows exactly by summing the original infectious-compartment equations. Inclusion–exclusion identifies *all* probability vectors compatible with the specified one- and two-strain history marginals. The resulting affine susceptibility formula gives a sharp interval, not a sampled bound. The two strictly interior witnesses give exact positive and negative initial logarithmic derivatives \(\pm1/54\) with all model parameters positive. A target strain in a model with at most three total strains sees at most two prior histories, so the pairwise statistics completely determine its history distribution. The optional all-order criterion follows from a two-sided Möbius-inversion/parity-trade proof. The accompanying exact-rational checker passed 4005 finite tests. Theoretical claims do not rest on numerical extrapolation.

## Originality — PASS, literature-bounded

The 2026 model paper provides the equations and a fast numerical representation; those are prior art. The 2015 review describes general information loss in model reduction but does not furnish the four-strain sharp sign reversal. The 2002 many-strain article treats a different status-based and transmission-reduction model. A related 2024 pathogen-genotype paper observes invisible third-order linkage disequilibrium; this is a real conceptual antecedent, but its statements neither compare target-strain *initial* growth under identical host prior-history marginals nor yield the exact sharp interval or minimality established here. Generic Boolean Möbius inversion is classical and explicitly not claimed as novel. Actual exact-claim searches of accessible research findings and the original local research history did not identify a covering claim. This is best-knowledge, not a proof of uniqueness or priority; other sero-epidemiological or genetic literature might contain equivalent calculations.

## Value — PASS

The first nontrivial four-strain case directly resolves a model-identifiability question relevant to low-order serological observation: exact single and pairwise co-exposure measurements can fail even to determine the sign of initial introduced-strain growth. The sharp width and fully positive, rate-certified witnesses make the limitation quantitative and robust, without depending on ad hoc high-order biological interactions. A complete necessary-and-sufficient criterion specifies exactly when a lower-order immune-history representation does suffice. This is not a claim about clinical forecasts or future epidemic persistence.

## Limitations

The result concerns admissible instantaneous states, not necessarily dynamically generated immune histories from a naive epidemic. The original history-based model, its exact source-date provenance, and accessible full text were inspected. The strongest related historical caveat is higher-order pathogen-genotype linkage-disequilibrium work, which is mathematically analogous but concerns different state variables and outputs. No independent mathematical review or exhaustive literature-priority certification has taken place.

Self-review: passed. Independent audit: not yet performed.
