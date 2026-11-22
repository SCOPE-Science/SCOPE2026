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

# Verification evidence

The standalone `verify.py` enumerates distinct comparator transformations on every \(C_m^n\) for \(2\le n\le6\) and \(m=2,3\). It checks all \(n!\) transformation normal forms, their distinctness, each explicit probe-set fingerprint, and the extremal coatom equation \(c_j\circ G_j=F\). The actual output is retained as `verification_output.txt`.

The checker cannot establish the universal theorem for unbounded \(n\) and \(m\); this is established in the mathematical proof in `RESULT.md`. No external or independent audit has occurred.
