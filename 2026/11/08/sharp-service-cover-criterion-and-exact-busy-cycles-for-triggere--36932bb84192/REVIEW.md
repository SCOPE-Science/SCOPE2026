# Review of sharp service-cover and exact busy-cycle theorem

## Correctness — PASS

The deterministic theorem is supported by the isolated-cluster workload criterion, monotonicity of reflected work under adding arrivals, coincidence of first clearing times when no triggers remain pending, and induction over clearing epochs. The converse uses one failing cluster in isolation. For Poisson primaries, a violation has a positive-probability no-other-primary interval, while the successful reduction to the classical batch queue transfers the known busy-period branching transform. All quantifiers, finite-mark assumptions, the strict subcriticality requirement, the zero-length idle convention, and the scope of workload non-equivalence are explicit. The bundled exact rational finite sampler completed 711 checks; it does not stand in for the infinite proof.

## Originality — PASS (historical-priority risk)

The October 2026 motivating article's primary full text treats stationary workload and customer system-time bounds. Its Appendix C analyzes aggregate input variance, and its Section 4 addresses fixed-point workload bounds; it does not give the sharp service-cover classification and marked-Poisson busy-cycle law. The important earlier Inoue–Takine 2003 paper was inspected in its open-access PDF, including Section 2.2 and Lemma 1: it already establishes busy equivalence for a model of periodic equal-size cell trains with unit interarrival lags. This is closely related, and its proof idea foreshadows part of the present argument. Its restrictions do not imply the claimed necessary-and-sufficient condition for heterogeneous random multitrigger marks and the Poisson cycle law without a separate generalization. The classical \(M/G/1\) fixed-point and Borel identities are attributed, not claimed as novel. Actual targeted searches of prior research records and wider literature found no exact covering statement. An earlier general deterministic delayed-work theorem may exist under different terminology; independent historical-priority assessment is warranted.

## Mathematical value — PASS

The structural question is motivated by recent attempts to analyze the difficult triggered-arrival system. A sharp criterion identifies exactly which intra-cluster release schedules can be replaced by batches without changing *any* busy/idle cycle. The result handles arbitrarily many dependent stages with heterogeneous service, including delayed stages released after the primary job itself could finish. It turns a generally non-renewal triggered-input stream into a tractable regenerative busy/idle process for this particular observable, giving all busy-period laws, a mean, and a natural Borel special case. This addresses a natural performance metric rather than an arbitrary parameter slice or a routine numerical update; it does not claim exact workloads or sojourn times.

## Closest comparisons and limits

- Rahnamania–Mandjes–Ashtiani (2026), arXiv:2610.40865v1: same input architecture; workload and class-system-time stochastic bounds, not exact cycle equivalence.
- Inoue–Takine (2003), DOI 10.15807/jorsj.46.220, especially Lemma 1: genuinely anticipates busy-state equivalence for deterministic periodic equal-service cell trains; special, not the heterogeneous marked-Poisson classification.
- Classical \(M/G/1\) theory: supplies the fixed-point transform, mean and Borel law *after* the reduction; those formulas are not asserted to be original.
- Earlier exponential-delay matrix-analytic work, arXiv:2609.02320v1: accessible full text inspected (Introduction and Sections III–IV, including the workload and idle-state transforms); it does not analyze the service-cover classification or the Poisson busy-period transform. Broader historical priority remains a risk.

Self-review: passed. Independent audit: not yet performed.
