---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

At alpha*=1+beta^-2 the seven interval endpoints ±1, ±beta^-1, ±beta^-2, ±beta^-3 give a full Markov partition. Direct branch-image and cell-length calculations yield the stated four-state reflection-lumped stochastic Q and invariant pi=(1,1,3-sqrt5,sqrt5-1)/4, giving r-mean=3/4. Characteristic polynomial t(t-1)(t²+beta^-2*t+beta^-4) implies three-step covariance recurrence for n>=1; initial C0,C1,C2,C3 and the geometric series give exact sigma²=sqrt5/32. Irreducible aperiodic finite-state Poisson-martingale CLT yields both stationary and normalized-Lebesgue initial laws with bounded initial bias. Independent symbolic transition/12-lag/resolvent calculations matched, but cannot themselves replace the Markov CLT.

## originality

PASS

Dajani–Sanderson introduce precisely the golden-map family, uniqueness of ACIP and 3/4 plateau; those are credited premises. In relevant sections of primary preprint we inspected, the complete three-step zero-digit covariance law, exact Green–Kubo variance and CLT at this endpoint are not supplied. A different Resultary golden fixed-point-free map computes coordinate covariance for another transformation, not the same zero-digit observable.

## value

PASS

The boundary of a maximal digit-frequency plateau is a natural singular dynamical parameter; the explicit three-lag oscillatory decay and exact variance √5/32 quantify fluctuations not determined by the mean 3/4. The exact Markov and CLT law is useful for studying digit statistics beyond first moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
