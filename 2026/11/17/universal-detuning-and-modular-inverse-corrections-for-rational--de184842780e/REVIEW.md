# Mathematical review

## Correctness

**PASS.** The claim is restricted to fixed coprime \(1\le k<n\), \(n\ge4\), \(a\to\infty\), and bounded detuning \(|\sigma|\le S\). There is one relevant reference visit at each of \(+1/(2n)\) and \(-1/(2n)\). The time of the negative visit is the uniquely defined residue \(t_* k\equiv-1\pmod n\). Exact logistic-tail expansions through relative order \(q=e^{-a/(2n)}\), together with uniform differentiated errors, give the return equation
\[
H_a(u,\sigma)=\sigma-2\sinh u+q\left(2\sinh(2u)-a[1+(t_*\sigma/n)e^u]\right)+O(a^2q^2).
\]
The limiting displacement is uniformly strictly decreasing, so the return has one root in the specified window. The expansion of this root and one circuit of the itinerary prove the stated \(B_j(\sigma)\) coefficient. Exact return differentiation proves the multiplier and parameter-sensitivity laws. The included high-precision checker passed 40 original-map cases; it is not used as an infinite proof.

## Originality

**PASS within inspected evidence.** Bielawski et al. [1] supply the rational periodic-orbit existence theorem. The published general-denominator result [3] *already* proves the fixed-rational half-grid correction and attraction gap. Both published three-cycle results [4,5] *already* prove the nonlinear \(\operatorname{arsinh}\) detuning shape for \(n=3\). These overlap cases are explicitly prior and not counted as new. The evaluated claim instead gives the uniform moving-parameter first exponentially small position coefficient \(B_j(\sigma)\) for **every fixed denominator \(n\ge4\)** and every coprime numerator, recording the precise modular-inverse time \(t_*\). Published source statements and full proofs were compared for equivalent claims and stronger implications; none of the inspected results states this coefficient. Broader perturbation-theory coverage is a residual priority risk.

## Mathematical value

**PASS.** Rational sigmoid maps are a natural near-rotation family whose attracting periodic points exhibit unusually large parameter sensitivity. A universal leading phase does not identify the numerator-dependent response. The modular-inverse q-coefficient gives the first resolved arithmetic fingerprint of the hopping orbit, for an entire motivated family rather than one arbitrary finite instance. The explicit four-cycle comparison distinguishes the two coprime numerators at the same detuning.

## Scope and limitations

All uniformities hold at fixed \(n,k\) and bounded detuning. The result is locally unique only; it does not classify all periodic cycles or prove global attraction for moving parameters. Numerical checks supplement the complete analytic argument. Literature searches and full-text comparisons cannot exclude an unknown equivalent general theorem. Independent audit has not occurred.

## Closest literature

[1] Bielawski et al., *Interval maps mimicking circle rotations* (arXiv:2411.01495v1, 2024-11-03), Sections 3–5.

[2] Bielawski et al., *Strange bifurcation diagrams* (arXiv:2605.19756v1, 2026-05-19).

[3] *Singular half-grid selection and exponentially weak attraction in rational EOS maps* (2026), publicly available full theorem.

[4] *An inverse-hyperbolic-sine resonance profile for a hopping period-three EOS attractor* (2026).

[5] *An inverse-hyperbolic-sine crossover law for hopping three-cycles in a sigmoid interval map* (2026).

Self-review: passed. Independent audit: not yet performed.
