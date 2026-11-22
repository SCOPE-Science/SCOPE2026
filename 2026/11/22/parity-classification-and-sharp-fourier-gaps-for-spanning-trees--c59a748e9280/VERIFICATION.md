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

Run `python3 verify_theta_spectrum.py` in the directory containing this file and the program. The program uses only the Python 3 standard library. It constructs each small graph explicitly, enumerates candidate tree edge subsets and checks cycles/connectivity, transforms the full incidence indicator by an exact integer Walsh–Hadamard transform, and compares all multipliers, compressed multiplicities, Parseval sums, ranks, spectral maxima and sharp positive gaps. The observed final line was `THETA_GENERALIZED_SPECTRUM_PASS 106 cases; all exact FWHT entries; ranks and sharp gaps`. The independent graph enumerator does not use the claimed deleted-edge classification.

The proof of the unrestricted theorem is mathematical and is written in `RESULT.md`; finite verification does not constitute an exhaustive all-length certificate. Literature-priority verification is bounded. No external mathematical audit has been performed.
