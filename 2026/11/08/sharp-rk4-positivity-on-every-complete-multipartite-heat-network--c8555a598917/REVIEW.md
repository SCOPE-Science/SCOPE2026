# Scientific evaluation

## Correctness — PASS

The orthogonal projectors split all modes of the full complete multipartite Laplacian, including singleton parts. The cross-part matrix coefficient is exactly \((1-f(Nh))/N\), so a genuine cross-part pair enforces the unique cubic cutoff. The within-part coefficient has a quadratic with strictly negative discriminant and positive leading coefficient; all diagonal entries are positive by the Taylor-remainder inequality \(f(x)>0\). All nonnegative initial vectors are covered. The same-mode spectral bound follows from the known but independently reconstructed spectrum. An exact-fraction standalone script returned 96054 checks, independently confirming the formulas on finite partitions; this is not a substitute for the proof.

## Originality — PASS (with residual risk)

The full source materials inspected for Blanes–Iserles–Macnamara, the spectral Proposition 6 of Klee–Stamps, and Horváth 1998/2005 have different claim strength: general graph-Laplacian motivation, the spectrum alone, and uniform Runge–Kutta positivity/cone conditions respectively. Their statements do not imply the specific full multipartite RK4 positivity classification without additional coefficient and sign analysis. The two-state case and the previously established multipartite spectrum are explicitly excluded from novelty. Specialized unindexed earlier exact-threshold work remains possible, so publication priority is not certified.

## Value — PASS

The natural class of all complete multipartite heat networks contains both irregular stars and all complete graphs and has arbitrary partitions and dimensions. An exact dimension-independent-in-partition positivity horizon, matching spectral stability despite zero universal RK4 positivity radius, gives a useful counterpoint to standard impossibility results and supplies an exact stepsize benchmark. The abrupt loss of cross-part transitions at the boundary is structurally informative. The result is neither a finite experiment nor a routine table lookup: it requires a matrix-level nonnegativity proof not entailed by eigenvalues alone.

The guarantee does not extend to other graph families, unequal rates, RK stages or arbitrary higher-order methods.

Self-review: passed. Independent audit: not yet performed.
