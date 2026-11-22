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

# Finite and analytic verification

The standalone Python 3 checker `verify.py` uses only standard-library modules. It exhaustively checks all ordered triples of two-element sets from key pools of sizes 3 through 6, reproduces the exact three-vertex graph-triangle probability for pool sizes 3 through 7, and checks graph-triangle births against third-key hit births in every clean length-four sequence for pool sizes 3 through 5. Its seeded simulation for pool sizes 300, 1000 and 3000 is a non-certifying diagnostic and can display slow finite-size convergence.

The mathematical proof is separate from those experiments. It uses the exact three-set intersection classification; union bounds of orders \(O_b(m^{-1})\), \(O_b(m^{-1/3})\), \(O_b(m^{-2})\); a coupling to independent single-key draws with error \(O_b(m^{-1/3})\); independent Gamma third-arrival limits after Poisson splitting; a maximal inequality to remove Poisson clock randomness; and finite-time total variation via occupancy change coupling and Le Cam's binomial-to-Poisson estimate. All limiting statements hold for bounded rescaled horizons, not arbitrary increasing horizons.

The full original 2009 Yağan–Makowski zero-one-law preprint, the 2013 Arratia–Garibaldi–Kilian collision-process preprint and the 2016 Rybarczyk–Stark subgraph-Poisson preprint were compared at the scientific-statement level. This is not a complete historical-priority certification. No independent validation has been performed.
