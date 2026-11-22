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

# Reproduction and limits

Run `python3 verify.py` with an ordinary Python 3 installation; no external packages or data files are needed. Recorded standard output appears in `verification_output.txt`. The verifier independently enumerates ternary comparison assignments for all positive ordered compositions of sizes one through seven (127 cases), tests exact integer moment recurrence against brute-force weighted compositions through size seven, and prints normalized first/second moments for sizes 10, 20, 40, 80, 140, 200. It also tests positive variance in the large finite cases.

These are **finite diagnostics** and not an exhaustive proof for arbitrary sizes. The infinite statements require the conditional renewal residue argument and the finite-order moment bounds in `RESULT.md`. The Gaussian limit and the cubic-variance asymptotic have not been independently audited.
