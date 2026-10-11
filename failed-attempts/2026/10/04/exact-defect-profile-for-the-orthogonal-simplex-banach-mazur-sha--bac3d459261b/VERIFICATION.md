---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Starting from the source exact formula and writing n=s(q+x), r=sx gives E^2=1-x(1-x)/(q+x). With alpha=sqrt(2)-1 and alpha^2=1-2alpha, direct symbolic expansion gives E^2-2alpha=((x-alpha)^2+(q-1)alpha^2)/(q+x). Equality is impossible for finite integer data; q>=2 has a uniform positive gap, while q=1 converges exactly when x approaches alpha. Standard continued-fraction convergents yield the stated O(s^-4) squared-gap bound. The packaged symbolic checker independently reproduces the identity.

## originality

FAIL

The primary v2 preprint was inspected at Theorem 1.3 and Remark 4.5. Remark 4.5 already gives the exact orthogonal-simplex distance formula d_BM^2=ns-r(s-r) and immediately records the lower factor sqrt(2(sqrt(2)-1))*sqrt(ns). After x=r/s, the submitted defect identity is an elementary completion of the square in that source formula; nonattainment, q=1 near-extremality, and continued-fraction witnesses are routine consequences. Under the required implication standard, this is covered even though the source does not spell out the completed square or iff sequence statement.

## value

PASS

Identifying the exact unattained sharpness factor and all asymptotic parameter regimes for a canonical near-sharp family is a natural stability question. The rejection is because that refinement is already mechanically implied by the source’s exact formula, not because the quantity is unmotivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
