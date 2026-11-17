---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

After each dimer deposition, m unoccupied vertices remain per side and k labels are shared. There are m^2-k available rate-one edges partitioned into counts k(k-1), 2k(m-k), (m-k)^2, proving the transform recurrence with terminal (m,k)=(1,0)/(1,1). Verified mean exactly for n=2..8 from a separately implemented rational dynamic program. Symbolically verified nonnegative F_m drift and exact waiting-time partial fraction identity in Sympy. The factorial-moment upper bound controls cumulative drift O(log n/n^2), giving E T_n=H_n^(2)-1/n+O(log n/n^2); the finite n=2 case has opposite sign and is correctly not claimed uniformly.

## originality

PASS

A same-graph published defect theorem gives the overlap-state chain and q_n asymptotics, but not physical-time Poisson Laplace transform nor a sharp negative 1/n mean-time correction. The new rate-weighted expectation proof and cancellation establish a different kinetic observable with a nontrivial sign.

## value

PASS

Saturation time is a physical-time observable intrinsic to irreversible adsorption; the sign reversal from removing edges is counterintuitive and the explicit first-order -1/n coefficient is a meaningful asymptotic kinetic comparison. Neither correctness nor code alone is used as the reason for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
