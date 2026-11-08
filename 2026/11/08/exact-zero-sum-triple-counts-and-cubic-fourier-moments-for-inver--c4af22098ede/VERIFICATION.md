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

# Reproducible verification and scope

Execute `python verify.py` using Python 3.8+ with its standard library. The verifier independently enumerates all \(299\) moduli \(2\le m\le300\). For each modulus it compares (i) a direct ordered unit-pair count of simultaneous zero sums, (ii) a root count for \((t^2+t+1)^2\), and (iii) the claimed local-factor product. The program exits with an assertion error on a disagreement, otherwise prints a `VERIFY_OK` line and selected examples.

The tested range is finite and no claim of exhaustive verification across infinitely many moduli is made. The unrestricted result follows from the explicit bijection, prime-power root calculations and CRT in RESULT.md. The Fourier identity follows from exact character orthogonality. No independent mathematical review has been performed.
