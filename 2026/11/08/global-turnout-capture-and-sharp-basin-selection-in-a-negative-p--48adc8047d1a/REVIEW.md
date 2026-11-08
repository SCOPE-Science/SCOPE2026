# Scientific assessment

## Correctness — PASS

The domain is the entire closed electoral simplex, with the zero state separated from nonzero initial turnout. The proof first gives finite capture of the full-turnout edge using the uniform inequality \(s_{t+1}\ge2s_t\) on every under-mobilized step. It then derives a one-dimensional *exact* amplitude map from the individual's surplus-maximization rule, including saturation whenever the formal equality cut leaves the ideological interval. Strict concavity of \(H\) gives a unique interior amplitude threshold and excludes all extra periodic orbits. An expansion inequality gives finite polarization capture and a bounded-distortion argument gives the logarithmic escape-time asymptotic. The relative-share contraction identity gives a uniform small-turnout parity basin; the two states with 80:20 committed composition have rigorously opposite outcomes. The radical example is an exact factorization, not an inference from decimals. The standard-library checker independently reconstructs the microscopic rule by quadrature and verifies representative identities. Numerical tests are supporting diagnostics only, not proofs of the universal statements.

## Originality — PASS, with specified uncertainty

Fontanari's first-public October 2026 model and its November 2026 version already identify the coexistence wedge and an implicit nonsaturated period-two orbit (arXiv:2610.25210v2, Sec. 3.2, Eq. 19). These facts are not claimed original. The primary full text provides stability classifications and selected basin pictures, but not a proof that *all* nonzero initial states enter full turnout by a uniform finite-time bound, nor a global threshold classification for every state in this wedge, nor a finite-time saturated absorption law and logarithmic threshold-escape time. The separate Krueger–Szwabiński–Weron 2017 q-voter model uses a double-clique update mechanism and does not cover the present ideological-threshold map. Searches for direct equivalents and stronger results returned no covering statement; standard concave-map arguments are acknowledged as methodological background. Unindexed equivalents and analyses not located remain residual risks.

## Mathematical value — PASS

Local bistability alone does not determine which polling initial conditions converge to parity and which alternate between unanimous extremes. An exact complete basin theorem answers that natural dynamical question, including the positive-abstention interior rather than just the one-dimensional full-turnout edge. It identifies the pre-existing unstable cycle as the *global* threshold, supplies a finite activation guarantee and finite-time polarized absorption, quantifies critical slowing near the boundary, and exhibits an exact turnout-induced reversal at fixed committed composition. The endpoint issue matters because un-clipped indifference roots cease to exist for sufficiently asymmetric drives when \(\gamma>2\). The result does not assert empirical voting predictions, an outcome for asymmetric parameters, or novelty of classical one-dimensional comparison techniques.

## Scope and independent review

The proof applies only to the symmetric, deterministic, uniformly distributed ideological-threshold mechanism under the explicitly stated endpoint-saturated choice rule and the strict parameter wedge. No finite-electorate stochastic, noisy, or data-fitting claim is made. Prior equivalences outside the inspected literature remain possible.

Self-review: passed. Independent audit: not yet performed.
