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

The two standalone checks are `periodic_check.py` (reversible order-eight recurrence) and `gauss_check.cpp` (direct binary linear algebra on the closed-neighborhood matrix). Both were run from the delivered package sources. The periodic program enumerates \(256\) initial words and validates all six formal period classes, plus all orders \(7\le n\le400\). The C++ program compares complete affine-solution weight histograms against the theorem for every \(7\le n\le100\), directly checks every listed solution, and separately brute-forces all vertex subsets for \(7\le n\le10\).

These finite calculations establish the explicit weight table only. The extension to every integer \(n\ge7\) uses the algebraic proof that the characteristic polynomial divides \(t^{20}+1\) over \(\mathbb F_2\). The programs do not claim independent mathematical review or general-domain certification.
