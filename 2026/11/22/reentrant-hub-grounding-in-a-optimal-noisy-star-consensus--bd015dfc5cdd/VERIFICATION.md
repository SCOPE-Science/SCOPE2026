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

Run `python3 verify_star_gain.py` using Python 3 with its standard library. The checker constructs the pinned matrices independently using exact fraction-valued Gauss–Jordan elimination, verifies the inverse trace and derivative formulas, checks both endpoint identities, tests cubic-root sign regimes, and computes scalar minimizers by bisection while comparing sampled feasible competitors. The actual run printed `VERIFY_OK: 15472 exact-rational and numerical assertions`.

The formal proof is the calculation in `RESULT.md`: positive definiteness, strict convexity on the full simplex, leaf-symmetry enforcement, arrowhead inverse trace, endpoint derivative identities, and the cubic positive-root argument. Numerical root sampling cannot certify every real budget or every integer degree; the proof handles these quantified claims. The source comparison supports originality only relative to inspected published material; it does not constitute an independent literature-priority certification.
