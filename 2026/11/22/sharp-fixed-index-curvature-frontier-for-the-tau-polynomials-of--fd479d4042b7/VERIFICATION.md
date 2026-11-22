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

# Verification notes

The standalone `verify.py` uses exact `fractions.Fraction` arithmetic to check the squared exponential curvature ratio \(\Lambda_{d,j}^2\) and its predicted strict sign for all specified finite parameter pairs. The script is self-contained and has no external data dependencies. It is run from the extracted embedded file of this finding and prints `VERIFY_OK` only when all exact comparisons pass.

The unrestricted proof is analytic. Its critical inputs are (i) finite-difference inversion of chromatic polynomial evaluations, (ii) the published high-girth Tutte growth theorem of Bencs–Csikvári, (iii) strict increase of the growth base, and (iv) the explicit formula for the derivative relative to \(1/[2(d-1)]\). The finite test does not verify or replace the published limit theorem and cannot infer an infinite parameter claim from enumeration.

No effective girth threshold or global coefficient unimodality is asserted. Independent audit: not performed.
