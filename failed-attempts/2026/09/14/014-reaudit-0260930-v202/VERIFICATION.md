---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Fresh exact-Fraction reconstruction over all 8000 subintervals reproduced the certificate: the auxiliary cubic \(U\) is positive and increasing because its second derivative has positive minimum, the local derivative bound is valid with the increasing denominator handled by its left-end lower bound, and the worst certified interval is \(k=583\) with upper error approximately \(0.01653276192<1/50\). The denominator is \(1+b_2x^2>0\). The claimed denominator degree is actually 2, which is admissible for type \((6,3)\).

## originality

PASS

No searched source states this exact rectangular finite-type threshold or coefficients; modern rational-minimax literature provides algorithms and asymptotics rather than this certified inequality.

## value

FAIL

The record proves only that one low-degree rectangular class clears the externally chosen error cutoff \(0.02\). It does not determine the best error, a sharp transition in degree, or a structurally motivated family, and no prior mathematical motivation for precisely the \((6,3),0.02\) checkpoint is supplied. Under the stated bar, a reproducible witness to an arbitrary finite threshold is not enough by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
