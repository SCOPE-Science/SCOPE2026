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

# Reproducible verification

Run `python3 check.py` from the extracted file directory. This script uses only Python's standard library, exhaustively enumerates the \(\binom{a+b}{a}\) interleavings for each \(1\le a,b\le8\), recomputes their gap sums and defect sums, and checks the extrema and complete equality classes. For \(a+b\le7\), it additionally enumerates every assignment of the three possible new-to-old relations at every insertion gap and checks all transitivity triples directly. It also tests the balanced-chain gap through 99 elements per shore.

The captured output is in `check_output.txt`. None of the finite checks is presented as a proof for arbitrary lengths; the arbitrary-length verification is the complete algebra in `RESULT.md`. No formal proof assistant or independent human audit is claimed.
