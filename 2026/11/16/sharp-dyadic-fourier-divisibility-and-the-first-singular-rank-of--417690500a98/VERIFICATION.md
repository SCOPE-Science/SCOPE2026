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

# Reproducible checks

Run `python3 pg_basis_fourier_check.py` from the directory containing the standalone script. No dependencies beyond Python 3 are needed.

The checker enumerates every unordered rank-four basis and all its \(32768\) Walsh frequencies, comparing the complete integer histogram with the recorded nine-level certificate. It also enumerates all \(83328\) rank-five bases and directly evaluates both the exact-zero nine-point frequency and a basis-sized frequency with two-adic valuation five. The former is separately evaluated through the analytic extension-count identity. The rank-dependent valuation minimum is also tested for ranks 1–64; these finite checks are supplementary to the general proof.

Expected terminal marker: `PG_BINARY_BASE_FOURIER_PASS`.

Limits: No exhaustive search of the \(2^{31}\) rank-five frequencies is asserted. The single explicit zero suffices for singularity. No exhaustive historical-priority or independent review is claimed.
