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

# Reproduction instructions and limits

Run `python3 verification/verify.py` with standard Python 3 from the package root. No third-party packages, external downloads or network connections are used. The script enumerates the original simplices, verifies freeness of all simplex orbits and quotient cell counts, derives the twelve oriented triangle attaching words, and checks nine eligible free-group generator eliminations leading to the final relators \(t^{-5},t^5,1\). Exact output is supplied as `verification/expected_output.txt`; successful completion ends with `PASS`.

The homotopy-preserving interpretation of presentation eliminations and the 2-cell slide are proved in `RESULT.md`. The verifier does not constitute independent validation, does not establish universal novelty, and does not attempt a homeomorphism classification.
