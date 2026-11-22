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

# Reproducibility and limits
Run `python3 verify.py`; its saved output appears in `verification_output.txt` and terminates in `VERIFY_OK`. The program uses only the standard library. It directly enumerates admissible X, Y, and mutual-link bit assignments for up to four named points, calculates exact coefficients for up to two disjoint old hyperedges at six named points, and compares finite distribution correction factors at four larger values of \(n\). The exact finite coefficients validate the counting constraints; large-n regression illustrates but does not prove the asymptotic theorem. The unrestricted proof is in RESULT.md, especially the uniform hypergeometric-error expansion and tail bound. Historical novelty and the proof have not been independently audited.
