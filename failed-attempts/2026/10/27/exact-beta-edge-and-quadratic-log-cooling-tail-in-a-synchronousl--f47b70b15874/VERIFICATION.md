---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The common-clock stationary convolution is bounded in conditional L² by the unreset OU convolution, with variance strictly inside (0,b/a) because there is a past reset almost surely. Synchronous coupling is contractive. At a fixed stationary time the particles are conditionally iid, giving the almost sure Gaussian empirical limit; conditional fourth moments give E[(M_N−V)²]=2E[V²]/N. The backwards Poisson gaps are independent exponentials, so the last age T and older pre-jump width are independent and 1−Y=e^(−aT)(1−cY′). The conditional power law remains unsaturated throughout 0<epsilon<1−c, giving exactly the claimed coefficient; the nonzero conditional slope and continuous age guarantee no atoms. For the lower end the event Y≤y forces both U≥1−y and Y′≤y/[c(1−y)], while U≥1−delta y and Y′≤(1−delta)y/c suffice. Each age-event factor is a positive multiple of y to leading order. Arbitrarily small positive y have positive CDF by packing sufficiently many jumps in a sufficiently short interval. Scaling to a fixed threshold by ratios (1−delta)/c and (1+eta)/c yields the two quadratic-log bounds with error O(log(1/y)) at each fixed ratio, and then delta,eta→0 give the coefficient. Independently, ordering n integration times in E[Y^n] separates the Poisson increments and gives n! divided by the product over j=1..n of j+beta(1−c^j), confirming the recurrence without assuming the generator. The stationary variance simplifies to the strictly positive expression in the finding and the two moment equations invert on 0<c<1, r>0. The frozen verify.py was inspected, not run. Its Monte Carlo checks are finite; its displayed finite-N loop checks positivity of the theoretical increment, not an independently sampled variance identity, and its recursion loop substitutes its own recurrence. Neither is needed for the analytical results.

## originality

FAIL

The claimed new width laws are covered by a standard exponential-functional formulation and its prior theorems. The exact upper interval, including its prefactor, and the moment recursion are immediate exact specializations of an earlier density equation. The lower coefficient is the earlier iid geometric-weight small-deviation constant, transferred by deterministic comparison on a common Poisson path and an independent suffix. Conditional iid given a common clock is itself antecedent. The same-model later catalogue overlaps corroborate equivalence but are not the basis of the earlier-coverage conclusion. The result is correct, not rejected for access or priority uncertainty.

## value

FAIL

The random collective width is a physically meaningful observable, and the two edge interpretations are clear. As an original mathematical package, however, the results are direct density and moment specializations plus an elementary comparison with the established geometric small-deviation law; their combination is not a separate new invariant. The recovery uses exact moments and adds no robustness result or new identification beyond the elementary inversion. The frozen claim does not establish an independently substantial remainder warranting repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
