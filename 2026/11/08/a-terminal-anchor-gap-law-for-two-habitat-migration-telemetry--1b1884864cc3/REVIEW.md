# Self-review: terminal-anchor gap law for two-habitat migration telemetry

## Correctness — PASS

The generator and Bernoulli transition likelihood yield the precise Fisher normalization \(J_m(H)/(4\kappa^2)\). The proof handles boundaries using \(f'(0)=1>f'(u)\), all integer observation budgets \(m\ge2\), and both short and long fixed-horizon limits. The unique large-horizon short branch follows from strict local monotonicity of \(f'\). The first sharp correction and the exponentially growing equal-spacing deficit follow by Taylor expansion and the exponential tail. A standalone standard-library checker corroborates exact rational and finite likelihood computations and numerical asymptotics; the proof, not finite enumeration, establishes the infinite theorems.

## Originality — PASS within inspected evidence, provisional

Cook et al. (2007 online) motivate information-optimal stochastic observation timing. Pagendam and Ross (2011) optimize ecological GPS designs on general habitat networks. Parker et al. (2011) already give information additivity, gap-permutation invariance and nonuniform Markov observation examples; Michel (2018) already derives the optimum unconstrained fixed sampling interval for the identical symmetric chain. None of the inspected primary results states or proves the fixed-count, mandatory-terminal-observation long-horizon branch, its sharp short-gap correction or the exact exponential loss relative to equal spacing. The 2013 follow-up by Pagendam and Ross remained inaccessible in full, and historical priority has not been independently certified.

## Value — PASS

For a deployment in which first and last location readings are mandatory, regularizing every gap over a very long horizon destroys nearly all Fisher information at a fixed number of fixes. The all-budget theorem identifies the globally optimal sacrificial-gap structure, supplies sharp asymptotics and an exact finite counterexample to uniform spacing, and distinguishes a natural constrained design from familiar unconstrained constant-interval optimization. Applicability is restricted to exact two-habitat symmetric-state observation, known nominal rate and no measurement or battery dynamics.

Self-review: passed. Independent audit: not yet performed.
