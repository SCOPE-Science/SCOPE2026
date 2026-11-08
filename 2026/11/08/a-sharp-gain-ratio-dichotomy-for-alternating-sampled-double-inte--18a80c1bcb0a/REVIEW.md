# Scientific assessment

## Correctness — PASS

An exact zero-order-held double-integrator transition yields three scalar Jury inequalities for each individual step. For a two-step product, two inequalities are automatically strict for individually stable steps, while the last becomes the explicit polynomial \(S_r(a,b)\). For fixed product \(ab\), the polynomial decreases with the step sum, whose sharp upper bound occurs at a single-step stability boundary. Optimizing the resulting edge quadratics proves every interval of the gain-ratio classification and the stated infimum, with strictness in the open square even at the critical ratios. A rational witness demonstrates actual instability. A standalone exact-arithmetic verifier supplements the proof, not replaces it.

## Originality — PASS, with residual precedence risk

The examined sampled-data control primary literature develops general sufficient robust maximum-sampling-interval bounds or state-feedback design procedures; the double-integrator symplectic-discretization source changes its feedback design with the discrete model. Those results do not state nor directly imply the full fixed-gain two-period Schur-stability equivalence with gain-ratio thresholds \(1/2\) and \(2\). Comparison with related mathematical-record results found a two-period recurrence bound and a periodic-oscillator resolvent result, both for distinct objects and invariants. Originality is assigned narrowly to this exact classification and margin, not to the classical Jury test or exact sampled flow. Inaccessible older specialist control papers remain a specific risk.

## Value — PASS

Individually stabilizing sampling intervals are not automatically safe under alternation, even for an elementary feedback-stabilized double integrator. The classification identifies exactly when that obstruction occurs in terms of a physically interpretable dimensionless ratio and provides a reproducible rational witness. It is a sharp robust-stability boundary for a complete natural two-period family, not an arbitrary numerical example or routine restatement of single-step stability.

## Closest literature and limitations

Berberich et al., arXiv:2011.09221, and Wildhagen et al., arXiv:2103.14353, concern general aperiodic sampling guarantees and design. Kotyczka and Lefèvre (IFAC 2020) use exact double-integrator discretization for a different symplectic feedback-design purpose. Sevim and Goren-Sumer (arXiv:2212.02922) derive sufficient common-contraction criteria for nonuniformly sampled double-integrator consensus and do not give an exact if-and-only-if two-period gain-ratio boundary. The theorem concerns fixed-gain two-period held control only, not arbitrary switching, uncertain plants, noisy measurements, or complete prevalence of earlier results in specialist sources.

Self-review: passed. Independent audit: not yet performed.
