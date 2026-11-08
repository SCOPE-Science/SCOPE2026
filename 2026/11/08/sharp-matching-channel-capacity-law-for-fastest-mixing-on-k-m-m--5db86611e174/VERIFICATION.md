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
# Verification notes

The analytic proof establishes the conclusion for every integer \(m\ge2\) and every admissible real matched-edge probability or interval. In particular, it handles the disconnected boundary \(m=2\), \(a=0\), without assuming irreducibility.

Run `python3 verify.py` using Python 3 with only the standard library. The checker constructs exact rational transition matrices for a sample of dimensions and transition parameters; verifies row sums, nonnegativity, and an entire explicit eigenbasis; checks that two derived global affine lower bounds coincide with the claimed optimum; and compares rational feasible off-matching probabilities and constrained intervals. An observed PASS establishes that those finitely many rational identities were tested, not the general theorem or publication priority. The general proof is the orbit-averaging and affine-minimax argument in `RESULT.md`.

No independent mathematical verification or publication-priority certification has been performed.
