# Scientific review

## Correctness — PASS
The resolvent factorization follows from nilpotency of the Jordan shear. A closed two-by-two singular-value formula reduces the optimization to the product of normalized durations. The logarithmic derivative excludes every interior minimum; the strictly monotone endpoint ratio gives the unique crossover, exact shear threshold and boundary ties. These arguments cover every nonnegative duration pair, not a finite grid. `verify.py` replays exact symbolic identities and 7,272 supplementary direct singular-value comparisons. The physically dissipative but nonnormal example is reproduced.

## Originality — PASS, with residual priority risk
Reuter's 2019 primary paper analyzes transient growth of matrix exponentials and powers on Jordan subspaces rather than optimizing products of time-varying backward-Euler resolvents. Layton–Pei–Trenchea (2021) use one backward-Euler solve inside a different filtered variable-step scheme. The published affine-Jordan pencil theorem has a different fixed-coefficient-sum feasible family. Related normal-oscillator timestep allocations do not imply an induced-norm theorem for a defective nonnormal generator. The older optimal-stepsize work by Lindberg was available at abstract level only, and unpublished or unindexed exact equivalents remain possible. The source-specific implication comparisons and actual queries are recorded in `AUDIT.json`; no failed search is treated as novelty proof.

## Value — PASS
The two-stage Jordan shear is the minimal nonnormal fixed-horizon damping-allocation problem. Its sharp equal-versus-single-stage law, exact switching threshold and golden-ratio horizon give a natural complete classification. The reversal already occurs for a generator whose symmetric part is nonpositive, so it is not merely a restatement of continuous transient growth. The result addresses numerical damping, not integration-error minimization, broad matrices or solver cost.

## Limits and follow-up
Zero-length stages are admitted. An active single-step optimum becomes an unattained infimum if both step lengths must be strictly positive. The proof and checker are self-contained apart from stated numerical/symbolic Python dependencies. Independent mathematical and publication-priority validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
