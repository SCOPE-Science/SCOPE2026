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

Execute `python3 verify_clock.py` in the extracted package directory. The finite program tests 7,729 exact modular assertions for 1,024 starting residues and numerous horizon/threshold pairs, checks the dyadic-block geometric residual distribution below the finite precision bound, checks the exact maximum-level CDF, and checks two-time divisibility intersections for several lags. These checks were executed successfully.

The infinite identities are proved by the Haar measure of residue cylinders and the original geometric first-return formula from Albers–Lander–Westermann, Section 5. The finite checker truncates valuations at its declared precision. It does not demonstrate the formulas beyond finite residue depths or validate the independent geometric construction; those are mathematical premises/proof steps, not algorithmic certificates.

An independent mathematical audit has not been performed.
