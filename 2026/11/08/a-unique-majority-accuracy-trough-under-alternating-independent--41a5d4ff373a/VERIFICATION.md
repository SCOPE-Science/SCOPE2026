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

# Reproduction and proof limits

The standalone file `verify.py` requires Python 3 and no third-party libraries. From the directory containing the files, run `python3 verify.py`. It prints `PASS: 840 exact rational assertions` when successful. Tests compare two independently constructed majority distributions, exact trinomial walk transitions, the increment identity, and strict finite-index neighboring-probability ratio growth.

The theorem is not inferred from the 840 checks. Its all-index proof is in `RESULT.md` and depends on a coupling identity, a Fourier integral with positive symbol, a strict reweighting-variance identity, a square-root limit, and the law of large numbers/central limit theorem. The full domain includes arbitrary real parameters in the stated open intervals, not only the rational test grid. Historical-priority examination is distinct from mathematical correctness; an inaccessible earlier full text remains a residual originality risk. Independent audit or external validation has not been performed.
