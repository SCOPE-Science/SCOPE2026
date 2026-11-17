# Scientific review

## Correctness

**PASS.** The general prime-two contradiction uses only simplex invariance, the linear inactive-reservoir equation, and nondecreasing incidence; it covers boundary points and arbitrary positive round length. The original competing-risk incidence is increasing and has strictly decreasing incidence per adopter, giving one positive equilibrium exactly above the previously published threshold. The exact planar Jacobian obeys all three strict Schur--Jury inequalities there, while the residual primed coordinate has a strictly contracting transverse multiplier. The rational witness has exact two-way identities, not just floating-point approximations. Standalone reproducibility checks passed; they are not treated as proofs.

## Originality

**PASS within inspected evidence.** The 2026 motivating paper derives the map, invasion multiplier, and equilibrium parametrization, but its one-stage stability discussion is observational rather than an all-parameter theorem and it contains no primitive-two exclusion proof. A 2021 stochastic/discrete-SIR paper proves extinction, persistence, and partial global-stability results for a different exponential-escape recurrence. A 2014 Euler-style SIR paper gives flip bifurcations for a differently normalized update. Previous publicly indexed related results on Euler SIR and probability-admissible SIS concern different maps. Related existing local threshold results for the same competing-risk map do not imply global prime-two exclusion or stability at arbitrarily large contact rates. Residual risk: the no-two-cycle argument may be an instance of a more general unindexed monotone-incidence or compartmental-map theorem.

## Mathematical value

**PASS.** The motivating paper reports one-stage stability numerically and contrasts it with chaos in two-stage contagion. An exact, all-step-size obstruction to the first nontrivial periodic locking, together with unconditional local endemic stability and a probability-admissible sharpness example, gives a structural explanation unavailable from finite parameter scans. It separates positivity and monotone incidence from the Euler-map mechanisms known to create flip cycles; the conclusion is not a claim of global supercritical attraction or complete dynamical classification.

## Remaining scientific limitations

The proof excludes only primitive two-cycles; higher-period cycles, nonperiodic recurrent sets, and supercritical global basins remain open for this statement. Historical priority is best-knowledge rather than certified uniqueness. The smooth negative example alters the incidence law and does not assert a counterexample to the original exponential family.

Self-review: passed. Independent audit: not yet performed.
