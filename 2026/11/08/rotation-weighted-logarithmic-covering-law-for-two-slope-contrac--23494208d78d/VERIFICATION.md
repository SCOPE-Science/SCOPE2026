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
# Verification of the logarithmic covering law

The complete mathematical proof is given in RESULT.md, with fixed hypotheses, universal quantifiers over all admitted lengths, and an exact comparison of word products, atom diameters, and pairwise atom separation. The two-sided covering sandwich supplies the bounded additive remainder rather than merely an asymptotic dimension.

The reproducible standard-library checker `verify.py` evaluates four combinations of unequal contracting slopes and two irrational rotation rates. For each it checks all admitted mechanical words through length 16: the number of distinct factors is \(n+1\), the number of high symbols differs by less than one from \(n\rho\), and the product lies in the claimed exponential envelope. It also evaluates a convergent Hecke--Mahler parameter series at 299 terms and verifies a positive branch-image gap. The checker prints `STURMIAN_TWO_SLOPE_LOG_COVERING_CHECKS_OK` on success.

The bounded discrepancy and atom correspondence beyond these finite lengths are justified by the published irrational-rotation/Sturmian framework, and the gap induction is fully analytic. Finite computation does not establish the infinite covering law. Verification is not an independent mathematical audit.
