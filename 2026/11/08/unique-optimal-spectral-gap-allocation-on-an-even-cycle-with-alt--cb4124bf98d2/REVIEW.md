# Scientific review

## Correctness — PASS

Two-step rotation averaging is legitimate for the entire feasible set because \(\lambda_2\) is concave in edge rates. The Fourier block spectrum gives the exact periodic optimum and its equality condition; a complex Fiedler vector provides a dual-like Rayleigh bound against *every* independent rate allocation. Its adjacent chord vectors are noncollinear, proving uniqueness even outside the symmetric subfamily, including the four-cycle. The exact checker (`verify.py`) passed 48 rational examples and 1,872 principal-minor checks; the general theorem relies on the analytical proof, not the test count. Risks: none identified in the normalization or boundary cases; numerical checks do not substitute for external verification.

## Originality — PASS on inspected evidence

Göring--Helmberg--Wappler (public preprint 2005-09-02) covers the general unpriced embedding formulation. Sun--Boyd--Xiao--Diaconis (2006), Section 5.3, solves only equal-cost cycles and establishes two-dimensionality for arbitrary cost cycles, without this explicit alternating-price all-even-cycle optimum or its full-dimensional uniqueness. Inspected indexed literature and the available existing local claims do not contain a covering statement. Existing special four-cycle price defects are not this opposite-edge price pattern, and a discrete-time alternating-mass SLEM result has a different optimization problem. Unindexed equivalent work remains possible. The Ghosh--Boyd primary abstract, not its full paper, was inspected and is an access limitation.

## Value — PASS

This is a complete spectral-design solution for alternating manufacturing/communication prices on a natural periodic network. Its uniqueness is an actionable engineering prescription rather than a symmetry-only existence claim. The strict size-dependent behavior, particularly equal-rate optimality for \(C_4\) despite unequal prices, gives a meaningful structural boundary and quantitative large-cycle square-root allocation law.

## Limits

The result uses positive alternating edge prices, a single linear global budget, unit vertex masses and the continuous-time combinatorial-Laplacian objective. It does not claim arbitrary costs, discrete-time SLEM or independently audited correctness.

Self-review: passed. Independent audit: not yet performed.
