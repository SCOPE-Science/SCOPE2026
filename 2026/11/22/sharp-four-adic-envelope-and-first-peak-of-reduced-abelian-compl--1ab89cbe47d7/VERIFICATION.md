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
# Reproduction and boundaries

Run `python3 VERIFY.py` with Python 3 (standard library only). Compare the output to `VERIFY_OUTPUT.txt`. The program computes alternation-extrema tables through length \(4^9\), checks every prefix maximum and its first occurrence for \(2\le m\le9\), and checks the proposed extremal witness lengths. Independently it generates a binary-digit-parity prefix, scans all factor windows for lengths \(1\) to \(512\), and explicitly enumerates reduced Parikh vectors for lengths \(1\) to \(64\). This is a finite reproducibility check only; completeness over all positive lengths is supplied by the mathematical induction in `RESULT.md`, using established identities from arXiv:2509.16034.

The source analysis compared against the complete all-length reduced Abelian complexity formula in the September 2026 PDF, which strictly dominates a pointwise computation but does not itself state the first-maximizer four-adic theorem. A claim of absolute novelty or independent certification is not made.
