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

# Reproduction and limitations

Run `python3 verify.py` using Python 3 and its standard library. The checker performs 36 exact-rational calculations of the prey-growth derivative and critical amplitude identities; it tests six exactly located positive equilibria immediately above the invasion threshold; and it iterates three critical orbits for 250,000 steps each, checking positivity and comparison with the predicted amplitudes within relative error 0.003. The latter tests are necessarily finite and cannot prove any infinite-time conclusion, global basin property, or uniqueness. The rigorous arguments for those claims appear in `RESULT.md`.

The exact map was independently matched to the original publicly posted equation (3) in Patra–Maitra, arXiv:2403.13316v1. Its 2026 journal form is behind a subscription and has not been checked line by line. No independent audit has been conducted.
