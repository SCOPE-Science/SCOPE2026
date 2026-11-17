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
# Reproduction and scope of checks

The main proof is analytic; it checks the exact conserved quantity, the unique periodic level, exponential passage bounds, uniform-in-passage integrated errors, bounded-time edge transfers, phase alignment, and a coupling estimate for the full log-coordinate distribution. No finite computation is treated as a proof of an infinite limiting assertion.

To reproduce finite numerical corroboration, use Python 3 with `numpy` and `scipy` and run `python check_tropical_phase.py`. The code numerically integrates logarithmic coordinates, locates the increasing return section, compares original-time periods and evaluates maximum phase error. Two coefficient triples and energies are tested; tests do not cover all positive parameters, do not certify the asymptotic error constant, and are not external validation.

The first public source date is taken from the initial arXiv submission of the underlying 2023 cubic-sphere-flow paper, not its later journal appearance. The previously published scalar period and area-sampled tail result is separately acknowledged, and neither is claimed as new.
