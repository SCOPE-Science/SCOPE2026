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

# Verification and limits

Run `python3 verify_heisenberg_nilradical.py` and `python3 verify_transverse_slice.py` with standard Python 3 from the directory containing both files. They require no dependencies or input data. The first builds the actual degreewise polynomial quotient by equality/zero constraints, without using a symbolic Hilbert-series package; it verifies degrees through \(m+2\) for \(1\le m\le5\). The second verifies the explicit matrix equations and reduced two-branch support over prime fields of orders 2, 3 and 5.

Recorded standard output appears in `verification_heisenberg.txt` and `verification_slice.txt`. The programs check only bounded cases; the monomial-normal-form proof in RESULT.md establishes the arbitrary-\(m\), arbitrary-field assertions. The nilradical length is transverse to the free central \(a\)-coordinates. Neither program proves literature novelty or supplies independent mathematical validation.
