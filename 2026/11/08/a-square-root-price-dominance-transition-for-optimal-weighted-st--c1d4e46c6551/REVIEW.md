# Scientific review

## Correctness — PASS

The exact Rayleigh-quotient transformation identifies the graph connectivity constraint with \(\operatorname{diag}(v_i-1)+\mathbf1\mathbf1^\mathsf T/(m+1)\succeq0\). All feasible allocations with an edge below unit weight have exactly one deficient edge. An explicit rank-one Schur complement, Cauchy–Schwarz and the nonnegative-square identity close the optimization with all equality cases, uniqueness, boundaries and strictly positive optimal weights. Rescaling proves the original budget theorem; a direct conditional-expectation identity proves the exact stated Kaczmarz one-step certificate. The extracted verifier checks 1367 exact rational designs, 36225 principal minors and 12980 random competitors. Finite checks supplement, rather than substitute for, the proof. The scope excludes exact finite-time and runtime-optimal sampling statements.

## Originality — PASS (with residual priority risk)

The full accessible primary material of Ghosh–Boyd (2006), Strohmer–Vershynin (2007), Shafi–Arcak–El Ghaoui (2010), and Gower–Richtárik (2015, probability-design SDP section), together with the publicly readable 2026 Sarkar text, was compared at the level of the exact claim. A prior homogeneous-spoke-price double-star spectral-gap result and a star vertex-gain (diagonal pinning) result were also compared for implication; neither contains arbitrarily priced spoke conductances on a one-hub star. Ghosh–Boyd and Gower–Richtárik furnish broader convex spectral optimization, and Sarkar explicitly contains the general cost-normalized E-design formulation, which this finding **does not** claim to originate. None of the inspected sources states the all-price star exact optimum, its unique conductance formula, the square-root price dominance threshold, or the corresponding closed-form incidence-row probabilities. Searches of indexed published mathematical findings and comparison with closely related results on homogeneous-price double stars and vertex gains did not reveal a covering statement. Main risks: independent graph spectral-design literature not indexed by searched queries, and an equivalent example hidden in an uninspected appendix. Absence of a search hit is not proof of novelty.

## Value — PASS

This is a complete natural E-optimal design classification with arbitrary positive costs and any star size, not a mere formulation of an SDP. The sharp all-equal vs. differentiated allocation transition is operationally meaningful: heterogeneous prices do *not* require heterogeneous optimal sampling unless one square-root price dominates all the others. It gives an exact explicit optimizer and a closed-form sharp work-normalized certificate, not just a numerical prescription or one parameter example.

Self-review: passed. Independent audit: not yet performed.
