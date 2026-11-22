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

# Reproducibility and boundaries

The provided `verify.py` uses Python's standard library only. Run `python verify.py` from the extracted file directory. `verification_output.txt` contains the actual captured output from the execution used for finite validation.

Checks: all partial Brauer diagrams for \(n=1,2,3,4\) against every unit permutation with both direct diagram multiplication and label invariance; all conjugacy-class representatives for \(n=5\) by direct diagram invariance; the cycle-type recovery algorithm for representatives through \(n=6\); and the independent identity-unit rank count using involution numbers through \(n=6\). The checker verifies the rank-polynomial and its rigidity reconstruction on the tested inputs. It does not inspect arbitrary degree and does not prove an all-\(n\) statement; that follows from the matching-orbit proof in `RESULT.md`.

The work has not undergone an independent mathematical audit.
