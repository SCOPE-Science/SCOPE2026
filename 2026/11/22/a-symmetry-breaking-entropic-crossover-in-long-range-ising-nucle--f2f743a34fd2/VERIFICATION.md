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

# Reproducibility and limits

The general result is established analytically by: (1) a finite magnetization-layer gap, (2) strict interval rearrangement for distance-decreasing couplings, (3) finite reversible-network star-capacity reduction, and (4) the exact singleton hitting-time/capacity identity. All constants implicit in the limiting error may depend on the fixed chain length, exchange and field.

Run `python3 checker.py` with Python 3.11+ and no third-party packages to reproduce 2,049 finite checks. The checker enumerates small-chain logarithmic shape gaps and numerically solves finite Markov first-passage equations using arbitrary-precision Decimal arithmetic. Finite checks are evidence of local consistency only; they do not certify all chain lengths or the infinite temperature limit.

The displayed prefactor counts one uniformly selected spin-flip attempt as one time unit. Changing to independent rate-one clocks multiplies the prefactor by \(1/N\). No simultaneous thermodynamic-limit theorem or observation-noise guarantee is asserted.
