---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Each part sees S-a_i active neighbors, hence becomes homogeneous unless tied; homogeneity cannot reverse to mixed. Fixed mixed parts force all r occupancies n/2. In two-periodic states all uniform parts exchange and their initial one/zero counts agree; >=2 mixed parts force n even and all half-filled, while one mixed part with r odd allows any nonconstant internal word. These disjoint cases yield the F and primitive-two P binomial sums for all r>=4,n>=1. Independent exact vertex simulation matched (r,n)=(4,2): F=18,P=54 and (5,2): F=34,P=220; finite checks only.

## originality

FAIL

FAIL: The complete October 26 2026 published theorem gives the identical periodic-state count as the constant term of (z+z^-1+B)^r plus the odd-r one-mixed correction, identical fixed counts and parity asymptotics, and additionally proves the global F^5=F^3 entry bound. A Nov 8 separate theorem refines the same counts by number of flipping vertices.

## value

PASS

PASS: Exact all-r labelled recurrent-state enumeration and sharp parity asymptotics of a natural threshold dynamical system are independently meaningful, but this mathematical classification is already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
