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

Run `python verify_block.py` with Python 3 and only the standard library. The exact finite-state kernel uses integer transition weights \(xv,uy,uv\), recursively aggregates rational terminal probabilities, and checks all blocked-count pairs for \(2\le n\le8\). It also checks concrete Hall obstructions, the mathematical bound over selected parameter pairs, and seeded independent event-level trials for larger networks.

On a clean replay the script prints `PASS: 280 exact rational terminal-law states; boundary and Jensen checks; seeded large-size trials`. The random number seed is embedded, so the output is reproducible. The theorem's infinite-size limit is proved by martingale/ODE convergence plus a deterministic tail-consumption bound; the finite program does not certify those general statements, nor does it constitute independent external validation. No external checker, formal proof system, or third-party audit is asserted.
