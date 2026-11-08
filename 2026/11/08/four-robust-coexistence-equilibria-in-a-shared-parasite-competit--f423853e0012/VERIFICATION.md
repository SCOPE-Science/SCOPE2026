---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The bundled `verify.py` uses exact rational arithmetic with the Python standard library. Its five probes prove the strict bracketing inequalities and the alternating signs of the second nullcline on the first, each with certified separation exceeding \(1/1000\). This establishes four distinct positive intersections by continuity. The accompanying proof supplies the independent irreducible-conic/Bézout upper bound and transversality; the script's tests alone do not assert an infinite-domain theorem.

A separate symbolic elimination check computed four distinct real positive roots of the quartic resultant and confirmed positive paired second coordinates. Those decimal approximations are diagnostic and are not required for the exact proof.

The scope is the reduced discrete competition system with the explicit rational coefficients, including a sufficiently small open neighborhood of those coefficients. Global stability, full-model finite-fast-step coexistence, empirical likelihood, and independent validation have not been established.
