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

The exact-arithmetic finite certificate is contained in `checker.py`. Invoke `python3 checker.py` in the same directory. It independently checks 18,564 possible six-active-hyperplane systems with rational elimination, reports 4,704 nonsingular systems and exactly 31 feasible distinct polytope vertices, including the two nonintegral cyclic vertices. It also evaluates 14 fourfold sums, checks the interpolation formulas and directly counts all six-variable grid solutions for levels 0–3. The expected terminal marker is `LUKASIEWICZ_THREE_WORLD_EXACT_CHECKS_OK`.

The general mathematical assertion for every positive integer granularity rests on the rational Ehrhart quasipolynomial theorem and seven exact interpolation values per parity, not on treating finite computational observations as an infinite proof. The exact vertex-enumeration code is intended as a reproducible certificate for a finite critical lemma. No independent mathematical audit is asserted.
