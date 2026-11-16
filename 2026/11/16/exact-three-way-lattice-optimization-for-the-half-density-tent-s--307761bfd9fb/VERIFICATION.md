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

# Verification and reproducibility

The complete analytic proof is in `RESULT.md`. With Python 3's standard library, run `python3 CHECK.py` from the extracted package. It tests the exact rational identities at the condition-number optimum, samples the unnormalized direct Zak transform at all phases \(0\), \(\pi/2\), and \(\pi\) across ten half-density rectangular lattices in the asserted range, checks that sampled multipliers lie in the claimed sharp bounds, and checks the analytic optimizer objectives on a rational mesh. The test output states the executed finite check count.

The decisive nonstandard step is the exact two-fiber formula with Zak period \(L=1/b\) and half-period translation \(a=L/2\), derived explicitly from the support \([0,2]\); this is independently illustrated by direct finite Zak sums. The quadratic envelope calculations and derivative sign analysis provide the infinite parameter proof. No finite mesh establishes a universal inequality by itself. No independent audit has been carried out. Full-text literature access limits and quantitative publication-priority risks are documented in `REVIEW.md` and `AUDIT.json`.
