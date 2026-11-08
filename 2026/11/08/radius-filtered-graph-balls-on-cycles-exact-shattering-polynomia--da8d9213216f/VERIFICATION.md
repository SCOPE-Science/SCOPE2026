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

# Verification record

Run `python3 verify_radius_filtered_cycle_balls.py` with Python 3 and no third-party packages. It creates cycle-ball bitmasks from actual shortest-path radii and explicitly checks all Boolean traces for each support of sizes one through four, for every parameter pair \(3\le n\le20\) and \(0\le R\le\lfloor n/2\rfloor\). The verifier compares the observed shattering counts with the symbolically derived finite formulas and the individual three-point gap characterization.

Observed output: `ALL_CYCLE_BALL_SHATTERING_CHECKS_PASS 117 families 259527 supports 54318 triples`.

The proof of the universal bound and of the limiting random-triple density is symbolic; the listed finite verification does not extrapolate from a numerical sample. Independent scientific audit has not been performed. Potential prior equivalence under circular-arc range terminology remains an historical-priority limit.
