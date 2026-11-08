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

# Reproducibility and scope

Run `python3 verify.py` in the directory containing the standalone checker. It uses the Python 3 standard library, prints two `*_OK` lines, and checks branch power identities exactly for rational samples as well as numerical time asymptotics at independent parameters. No downloaded papers or private tools are needed to execute the checker.

The checker validates finitely many examples and does not certify the all-parameter theorem. The universal statements are supplied by the integrations, Euler--Maclaurin argument, index shift and Gamma Fourier analysis written in RESULT.md. No independent audit or external formal proof has been performed. Publication-priority coverage remains subject to independent literature verification.
