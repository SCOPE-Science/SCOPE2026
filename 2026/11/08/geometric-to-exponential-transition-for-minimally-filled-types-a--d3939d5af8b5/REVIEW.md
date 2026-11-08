# Review of a stopped occupancy phase transition

## Correctness

**PASS.** The Poisson embedding gives the exact stopped count law with a unique maximizing Gamma clock, and the conditional binomial representation independently supports the finite integral. The extreme Gamma quantile lies more than \(\sqrt m\) above its shape, so its hazard has an elementary Mills approximation. That asymptotic, coupled with the established all-multiplicity Gumbel clock limit, gives the marked conditional Poisson mixture and exponential regime. The quantile large-deviation rate identifies the logarithmic threshold. The checker independently compares two exact-rational finite-state methods (143 assertions); it does not attempt to infer infinite truth from experiments. Risks: asymptotic uniformity is limited to fixed compact Gumbel windows, sufficient because of tightness; arbitrary sequences are treated by subsequences.

## Originality

**PASS, subject to historical priority.** Castro–Marinho and Long establish a growing-multiplicity clock law, not the terminal count of exactly-minimal types. Myers–Wilf already establish the full \(m=1\) stopped singleton law, which is expressly credited and not claimed anew. Ilienko's fixed-level extended-collection results include exponential and geometric limits for different observables and delayed times, and some fixed-threshold behavior may be deducible. The additional threshold \(m\asymp\log n\) and continuum of geometric terminal-count limits are not directly stated in these inspected sources. Search comparisons of nearby published occupancy, coupon, and point-process claims did not identify a dominating theorem, but absence from search is not proof of global novelty. Castro–Marinho's full text was intermittently inaccessible on reinspection, so its appendices remain a residual risk.

## Value

**PASS.** In repeated coupon collection, the count of types remaining exactly at the required multiplicity is the natural terminal bottleneck-size statistic. The new geometric limiting family at \(m\asymp\log n\), its explicit large-deviation parameter, and the collapse and exponential regimes on either side quantify a structural transition not determined by the distribution of total collection time. The exact finite law provides a reproducible starting point for future finite-size estimates. This is a bounded, model-specific result, not a claim about all occupancy models.

Self-review: passed. Independent audit: not yet performed.
