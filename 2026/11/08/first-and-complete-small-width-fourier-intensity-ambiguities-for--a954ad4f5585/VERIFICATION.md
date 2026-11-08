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

# Exact finite verification

`CHECK.py` runs without nonstandard dependencies under Python 3.8 or later. Execute `python3 CHECK.py` and require exit code zero and the terminal marker `ALL_EXACT_TWO_ROW_CHECKS_PASSED`.

At each width from one through eight, the script traverses all bit pairs, keeps one exact representative per sign/central-inversion orbit, computes all nonredundant aperiodic autocorrelations using two independent integer algorithms, and groups their exact signatures. It confirms the listed singleton and double-fiber counts, the absence of larger fibers, and nonseparability for every member of the four width-six double fibers. Direct Laurent coefficient multiplication independently verifies those four pairs and the displayed example.

The checker is an exhaustive proof for the finite ranges only; it neither estimates floating-point Fourier samples nor proves any statement for widths greater than eight. Originality against all possible earlier unindexed tables and an independent mathematical audit are not certified.
