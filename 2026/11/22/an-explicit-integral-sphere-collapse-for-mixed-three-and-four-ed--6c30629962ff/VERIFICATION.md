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

# Verification and reproducibility

Run `python3 check_theta.py` in a directory containing the accompanying standalone script. It uses only Python 3 standard-library modules and enumerates complete independence complexes directly from the specified edges. The actual output of this check is in `check_output.txt`.

Each elementary pair is validated at the moment of removal by checking that its lower face has exactly one codimension-one coface, and the complete survivor family is compared to the stated crosspolytope boundary. Nine pairs of parameters with \(1\le m,q\le3\) were tested. These encompass 2,829 elementary free-face collapses and 21 independently computed signed reduced Lefschetz character checks for the pole-reversal and branch-transposition generators. The program also checks the exact closed form for the number of pairs in every tested case.

The universal result for arbitrary positive \(m,q\) is not justified by nine computations: it follows from the ordered face-pair proof in `RESULT.md`. No full automorphism matrices or explicit equivariant collapse are claimed. The computations are finite, exact integer checks, with no stochastic approximations or external packages. Independent external auditing has not been performed.
