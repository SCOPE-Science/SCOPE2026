# Scientific review

## Correctness — PASS

The object is the three-vertex path, with positive position-dependent fecundity only for mutants and resident fecundity one. The absorbing first-step equations uniquely determine fixation because every nonabsorbed state reaches absorption with positive probability within two effective changes. Exact elimination gives all four rational fixation probabilities in `RESULT.md`; subtracting them gives the displayed positive-polynomial birth–death difference and the opposite-sign death–birth difference. All factors are positive on the claimed domain except the explicitly signed factor \(r-s\). Equality at \(r=s\) follows directly. A separately implemented exact rational solver verified 96 parameter/method/placement cases. Finite checks are supportive only; the analytical positivity argument proves the full quantified result.

## Originality — PASS within inspected evidence, provisional

Maciejewski–Puleo (2013, arXiv:1311.3214) examine environmental backgrounds, including a three-site line, but resident fitness also depends on background and the line example does not compare a mutant-only high-fitness center versus endpoint under both update orders. Antal–Redner–Sood (2006, arXiv:q-bio/0601031) compare the placement of the **initial mutant** at high versus low graph degree under homogeneous type fitness, not relocation of a mutant-specific habitat at a fixed uniform initial distribution. Kaveh–McAvoy–Nowak (2017, arXiv:1709.03031) study environmental fitness heterogeneity in a well-mixed Moran model and periodic cycles in Appendix B, not the proposed three-path two-rule sign theorem. De Souza–Neves (2020, arXiv:2003.05462) treat frequency-dependent type fitness on stars, not a vertex-specific mutant-only fecundity. A prior exact four-cycle habitat arrangement result addresses two high-fitness sites and only birth–death updating, and does not imply the three-path center-versus-endpoint reversal. Specific search results gave no statement logically implying the two displayed all-parameter factorization identities. Historical priority is not independently certified; specialized small-star environmental heterogeneity literature could still contain a variant.

## Value — PASS

The result is a complete sharp placement classification on the smallest connected graph with distinct center and endpoint placement orbits. It directly separates two widely used reproduction-update mechanisms under an otherwise identical fixed ecological heterogeneity and uniform mutant introduction. The death–birth center fecundity cancels mechanistically, while birth–death's global fecundity competition gives the opposite strict sign; the contrast is structural, not a routine substitution in a single update formula. It gives a minimal benchmark for checking habitat-allocation assumptions in evolutionary spatial models. It is not a prediction for empirical populations.

## Scope and historical limits

The proof concerns a single high mutant-fitness site at fixed site values, and it does not establish generality for other graphs, dynamical environments or game payoffs. The literature assessment covers specific accessible full texts and leaves the possibility of older, indirectly equivalent small-graph results. Independent validation is absent.

Self-review: passed. Independent audit: not yet performed.
