# Scientific review

## Correctness — PASS

The theorem concerns a fully specified continuous-time, finite-state arrival-and-extinction process, not an unverified diffusion approximation. The reference process with additive missing-partner hazards is exactly realized by independent arrival and hazard clocks. Replacing only the initial extinction rate changes the probability of the first association, giving the stated constant prefactor because the sum of arrival rates is fixed. The resulting strictly concave logarithmic objective has a unique interior maximizer, with an explicitly solvable multiplier equation. Its two budget limits and the leading failure coefficient follow by controlled asymptotic expansion at fixed positive hazards. Independent exact state-equation checks confirm the closed formula in 270 heterogeneous cases; 200 numerical cases check the allocation equations and feasible comparisons. These finite checks support but do not replace the analytic proof.

## Originality — PASS within inspected evidence

Amarasekare (2004) studies deterministic patch-occupancy mutualism and dispersal; its main results and appendices describe stability and invasion rather than a finite all-partner arrival probability or fixed-rate budget. Yamauchi, Nishida and Ohgushi (2009) formulate single-partner stochastic tunneling through a diffusion model with one encounter rate and trade-offs in colony growth; the inspected model, results and discussion do not supply the multiple-partner product with an arbitrary empty-state hazard. Antunes, Deaville and Goss (first online 2005) empirically study a tripartite association, not this mathematical optimization. A reliability-theory analogy exists: system reliability allocation and exponential repair scheduling can produce related product objectives. Material inspected for that broader field was limited, so the possibility of a pre-existing abstractly equivalent allocation theorem remains a specific originality risk. Retrieved public mathematical records were also compared by statements rather than subject labels, with no direct match identified. Failed searches are not proof of novelty, and independent historical-priority verification remains necessary.

## Value — PASS

The result is a complete allocation classification for any number of required partner types, rather than a numerical optimum in an arbitrary small instance. It gives an interpretable, exact benchmark for managing multi-partner establishment bottlenecks, shows that extra initial host mortality changes success but not allocation at a fixed total encounter rate, and establishes the nontrivial budget progression from equal to square-root hazard weighting. The object is motivated by independently dispersed mutualists and documented multi-partner plant associations. It is not a field-tested ecological prescription: the essential-partner, additive-hazard, permanent-acquisition and fixed linear-budget assumptions restrict applicability, and the general reliability analogy limits priority certainty.

## Closest literature and limitations

- Amarasekare, *Spatial dynamics of mutualistic interactions* (2004), https://doi.org/10.1046/j.0021-8790.2004.00788.x — full model, conclusion, and appendices inspected; spatial population-level dynamics rather than the stated absorption problem.
- Yamauchi, Nishida and Ohgushi, *Stochastic tunneling in the colonization of mutualistic organisms* (2009), https://doi.org/10.1016/j.jtbi.2009.07.021 — full accessible paper inspected, including association model, results, and discussion; one association rate and diffusion-based establishment.
- Antunes, Deaville and Goss, *Effect of two AMF life strategies on the tripartite symbiosis...* (2005 online), https://doi.org/10.1007/s00572-005-0028-3 — abstract inspected; biological support only, not a whole-paper noncoverage determination.
- Shaked and Shanthikumar, *On the first failure time of dependent multicomponent reliability systems* (1988), https://doi.org/10.1287/moor.13.1.50 — abstract inspected; related general reliability methods but no decisive full-text implication comparison.

The finite model makes no claim about eventual persistence, dynamically coupled partner densities, nonlinear intervention costs, or arbitrary correlations among colonization clocks. General reliability literature remains a residual historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
