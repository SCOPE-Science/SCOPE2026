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

# Verification of the stated theorem

The proof in `RESULT.md` checks existence, interiority, the one-large-habitat structure of global maxima, the complete comparison with equal splitting, and both habitat-count boundaries. In particular, the variational representation is derived from the unique positive crossing for each fixed asymmetric fraction; the positive-parameter minimizer for at least three sites is proved to exist by its small- and large-parameter asymptotics. The strict local optimality of equality near total stock \(s=2\) justifies \(s_m>2\).

Run `python3 verify.py` in a directory containing the companion script. The script uses the Python 3 standard library only and issues 3,186 diagnostic assertions in the tested environment. It checks sample formulas, finite habitat counts, scalar minimizations, and example configurations. It does not perform interval-certified global optimization and does not substitute for the mathematical proof or establish untested parameter values.

The quantitative examples use dimensionless stock and a normalized local recruitment law; they are not measured field outcomes. The historical literature comparison is bounded by actual material examined. Self-review passed. Independent audit has not been performed.
