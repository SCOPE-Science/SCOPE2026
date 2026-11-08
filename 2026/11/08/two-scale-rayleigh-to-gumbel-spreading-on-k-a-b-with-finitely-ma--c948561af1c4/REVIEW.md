# Scientific review: two-scale push–pull broadcasting on \(K_{a,b}\)

## Correctness — PASS
The vertex-clock process splits exactly into independent edge clocks of rate \(1/a+1/b\). First-step counting gives a two-dimensional increasing continuous-time Markov chain. On the early \(b^{-1/2}\) scale its generator tends to a well-defined piecewise-deterministic Markov process with bounded finite hub jumps and deterministic drift between jumps. A direct independent-hazard argument gives the finite first-extra-hub law and the Rayleigh limit. After the last hub is informed, independent per-leaf clocks of rate \(1+a/b\) give the Gumbel law; because the hub activation time is \(o_{\mathbb P}(1)\) and the number of susceptible leaves is \(b-o_{\mathbb P}(b)\), the terminal law is asymptotically independent of the early trajectory. The standalone rational labeled-state and transient-killed-generator checks passed, but are not being mistaken for an infinite proof.

## Originality — PASS, with priority risk
The most relevant earlier sources are Acan et al. (2014, asynchronous push–pull and stars), Pourmiri–Mans (2020, dynamic-network bounds and cut rates), Aalto–Leskelä (2014, early/final asymptotic independence in a many-transmitter homogeneous mixing model), and Doerr–Kostrygin (2023, synchronous protocols on fully connected networks). The shared exponential-edge representation and generic Gumbel extreme-value fact are established background. The fixed-\(a\) activated-hub PDMP, its joint limit with independent terminal completion, and the explicit all-parameter first-extra-hub law are not consequences of the inspected theorems, whose underlying regimes or conclusions differ. A further unnoticed first-passage-percolation specialization remains possible, so historical priority is not independently certified.

## Value — PASS
Two physically distinct broadcast phases become rigorously decoupled: a random hub-discovery cascade in vanishing physical time, then the slowest of nearly \(b\) remaining leaf discoveries. The result gives a complete fixed-hub-count asymptotic description, with a nontrivial random early process and an explicit Rayleigh boundary case, rather than only a logarithmic runtime bound. It is relevant to heterogeneous contact networks and provides a benchmark for multiscale epidemic approximations.

## Limitations
Only the fixed-\(a\) unweighted graph and one-hub starting condition are proved. The result does not assert a general epidemic theorem for arbitrary networks, a growing-hub limit, or convergence of expectations. Source coverage and historical priority are subject to independent review.

Self-review: passed. Independent audit: not yet performed.
