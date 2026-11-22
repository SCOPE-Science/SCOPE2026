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

# Verification

The exact stationary birth–death ratio is derived directly in `RESULT.md`. The finite-difference identity is checked by `check.py` using `fractions.Fraction` arithmetic for three distinct positive rational slope pairs, five prior-mixing fractions and 23 successive infection counts per pair, plus 16 finite group sizes per parameter set. The example with rates \(1\) and \(3\) and low-rate fraction \(99/100\) is evaluated as exact rational numbers. Additional floating-point diagnostics inspect logarithmic-phase asymptotics for two rate contrasts, four phases and three rare-component scales. To replay with Python 3 standard library, run `python3 check.py` from the extracted file directory. The script exits with failure when any assertion fails and prints the total passed diagnostic count on success.

No finite computation verifies the universal quantifiers or the rare-event asymptotic. Those depend on the monotonic sign identity, a Lambert inversion, a geometrically uniform remainder estimate and an exact one-step comparison of the phase function, all proved in `RESULT.md`. The nonphysical all-infected exposure index is excluded. Scientific priority and the claims' use outside the low-import regime are explicitly limited. Independent audit: not performed.
