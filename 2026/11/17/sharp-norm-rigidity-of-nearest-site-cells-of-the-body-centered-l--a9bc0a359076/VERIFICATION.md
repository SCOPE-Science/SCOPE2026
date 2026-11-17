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

# Reproducibility and limitations

Run `python3 verify_norm_rigidity.py` in this directory with Python 3. The deterministic seeded reference run produces `PASS 9011 deterministic seeded geometric checks`. The checker independently enumerates lattice sites in bounded cubes (for test points strictly inside one fundamental chamber), tests both coset competitors, compares exponent-dependent decisions in dimensions one through four, and verifies strict weighted-cost agreement. It additionally uses exact rational arithmetic to demonstrate different preferred lattice cosets at \((3/10,3/10,151/1000)\) for \(p=1\) versus \(p=3\) and \(p=\infty\).

Finite enumeration is not a proof of a continuum statement or of universal behavior in arbitrary dimensions. The complete proof is the algebraic comparison, monotonicity argument, and nonvanishing Taylor coefficient in `RESULT.md`; the checker tests implementations and example instances only. No independent audit or externally certified proof has been performed. Earlier covering-density and classical Voronoi facts are used only as motivation and contextual references.
