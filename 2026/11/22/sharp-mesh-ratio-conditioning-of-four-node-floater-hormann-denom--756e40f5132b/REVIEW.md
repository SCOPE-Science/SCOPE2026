# Scientific review

**Correctness (PASS).** The proof reduces the exact rational denominator factor to two outer-cell quadratics over a positive denominator. A single strictly decreasing critical-point polynomial proves unique cell maxima, and an explicit monotone majorant gives the sharp global envelope and equality classification. The exact expression proves the square-root asymptotic. `verify.py` passed 7,579 auxiliary tests; the proof, not sampling, establishes universality.

**Originality (PASS, qualified).** Fuda, Campagna and Hormann (2022, doi:10.1007/s00211-022-01316-w) introduced this denominator summation factor and proved a general degree-one bound quadratic in the mesh ratio. That theorem does not give the present *exact* nonuniform four-node envelope, its extremizing gap pattern, or square-root asymptotic. Themistoclakis and Van Barel (2024, doi:10.1007/s11075-024-01933-6) study different interpolation-error bounds. Relevant published four-node range and variation claims do not imply denominator term conditioning. The older de Camargo stability paper (doi:10.1007/s11075-015-0037-z) was accessible only in abstract, leaving historical priority uncertainty; no claim of exhaustive priority verification is made.

**Value (PASS).** The exact threshold-free four-node mesh-ratio law identifies the smallest case where denominator-term cancellation occurs and quantifies its sharp unavoidable growth, informing practical assessment of straightforward first-form summation and nonuniform node designs. It neither guarantees large actual rounding error nor rules out alternate stable implementations.

**Scope and limitations.** Four nodes, degree one, real interior evaluation and denominator termwise perturbations only. No general all-node, higher-degree or floating-point lower bound is claimed. Broader historical coverage remains a risk.

Self-review: passed. Independent audit: not yet performed.
