# Self-review

## Correctness — PASS

The moment-matrix row space splits orthogonally into the constant vector and centered node vector, yielding the unique minimum-norm weights and the exact identity for \(W^2\). The orthogonal decomposition into sample mean and centered node vector has Jacobian \(\sqrt m\). Rescaling the centered vector yields an exact small-ball integral. Dominated convergence under bounded continuous sampling density gives the strictly positive Pareto constant; the tail-integral formula gives the sharp necessary-and-sufficient positive-moment criterion. Conditional independence of noise establishes the unconditional mean-square threshold. Exact-rational, independent least-squares, and numerical tail diagnostics passed 9,859 assertions. No finite simulation is used as an infinite proof.

## Originality — PASS (best-knowledge, qualified)

Earlier published research claims were compared by source, aliases and statement implications, not only titles; published-finding corpus searches targeted exact affine moment fitting, random quadrature minimum-norm weights, Gram inverse singularity, small-ball tails, and measurement-noise mean-square stability. No discovered result entailed the claimed all-\(m\) Pareto constant and noise threshold. Glaubitz (2020) supplies a close **deterministic** predecessor for minimum-norm weights on fixed scattered nodes, and that known ingredient is expressly not claimed as novel. Migliorati–Nobile (2018), van den Bos et al. (2018), and more recent positive or conditioned least-squares cubature have different sampling/conditioning requirements and do not give the law for the unconditioned rule. The decisive distinction is a distributional tail/moment classification, not terminology or dimension. Residual risk: older inverse-Gram and random interpolation literature may contain an equivalent tail asymptotic not found in the bounded inspection.

## Value — PASS

This exact Pareto tail answers a natural stability question for a recognized affine moment-fitting rule and gives a sharp minimal node count for *unconditional* robustness to independent observation noise. It warns that almost-sure rank and good typical performance do not guarantee finite mean-square error. The formula has interpretable density dependence and a concrete discontinuity of integrability at sample size four. It is not presented as a general cubature accuracy or algorithm-speed claim; high-probability conditioned and positivity-preserving techniques are explicitly exempt.

## Limits and verification status

Mathematical generality is limited to one-dimensional, affine-exact, iid bounded-continuous-density abscissae and independent centered equal-variance noise. Simulation checks only finite cases; infinite claims derive analytically. Publication precedence is not independently certified.

Self-review: passed. Independent audit: not yet performed.
