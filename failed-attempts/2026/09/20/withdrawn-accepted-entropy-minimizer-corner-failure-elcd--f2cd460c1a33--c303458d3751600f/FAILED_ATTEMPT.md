# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/20/entropy-minimizer-corner-failure-elcd--f2cd460c1a33`  
Independent audit date: 2026-09-29 (UTC) (UTC)  
Task: `067337fc023e36d6c8907958168b28dc`

The calculations in this record are mathematically sound, but the package is not an independently validated new finding because its principal result is already present in earlier SCOPE records.

## Decisive originality issue

FAIL. The principal theorem package was already present in SCOPE two days earlier. `2026/09/18/elcd-entropy-rectangle-minimizer-gauge-dependence--f304c0de0856` gives the same closed-form rectangle minimizer, the same strict-interior counterexample family, the same affine/gauge dependence, an exact entropy-excess identity, and even a stronger identric-mean crossover analysis. `2026/09/19/entropy-gauge-corner-obstruction-elcd--8cb75d085d2d` independently repeats the same source-specific obstruction and adds a gauge-invariant diagnostic. The assigned September 20 record therefore does not establish an original finding; its benchmark-specific Configuration-3 calculation is only an illustration of already-published SCOPE results.

## Scientific-value consequence

FAIL as a separate validated finding. The mathematics remains useful, and the source-benchmark example is a concrete diagnostic, but the substantive theorem and structural objection had already been published in stronger form inside the same repository. The incremental benchmark substitution does not justify a third research record.

## Correctness retained

PASS. Direct differentiation gives the stated positive-definite Hessian, strict decrease in p, and the unique unconstrained top-edge minimizer rho0=e^{-1}p_+^{1/gamma}; clipping to [rho_-,rho_+] is therefore exact. Adding c rho shifts the stationary density by exp(-(gamma-1)c/gamma), so the normalization dependence is real. The Configuration-3 numerical values were independently recomputed: rho0=0.15567565441316625, corner entropy -0.5412116523249944, continuous minimum -0.5448647904460819, and the reported sound speeds agree. The source preprint abstract confirms entropy-minimizing interface-state selection, although its full PDF body could not be retrieved through the available web endpoint in this run.

## Relocation

Preserve the package as a failed research attempt at `failed-attempts/2026/09/20/withdrawn-accepted-entropy-minimizer-corner-failure-elcd--f2cd460c1a33--c303458d3751600f` rather than silently deleting it. Its benchmark arithmetic may remain useful as example material, but the headline exact-minimizer/gauge-obstruction theorem must not be represented as a newly validated finding.
