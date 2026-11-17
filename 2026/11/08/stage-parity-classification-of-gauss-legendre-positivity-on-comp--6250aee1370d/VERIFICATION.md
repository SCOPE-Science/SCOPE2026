---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Verified functional calculus on exact orthogonal multipartite Laplacian projectors (constant, part-constant, within-part) and derived all three entry types. Padé Q_s(z) has positive coefficients; writing E_s(z²)+z O_s(z²), coefficient-ratio q_(2j+1)/q_(2j) decreases with j and yields nonnegative numerator E′O-EO′, hence f_s(z)=(1-r_s(z))/z decreases strictly for all s. For even s, exact positive-integral Padé remainder makes Q_s(-z)>0, giving diagonal positive; for odd s r_s(z)->-1 and diagonal ->2/N-1. For N=2, |r_s(z)|<1. Actual symbolic verifier read and finite stages 1..14 independently checked; all-stage conclusion derives from coefficient argument, not finite enumeration.

## originality

PASS

Best-of-knowledge all-stage parity classification and scalar Padé monotonicity for unbalanced multipartite graphs. Earlier general scalar positivity test and stage-two case are PRIOR, but do not by themselves prove higher-stage scalar properties or odd-stage classification.

## value

PASS

Natural all-stage sharp classification of the positivity behavior of a major collocation method on a motivated graph family; unexpected parity-only answer across all multipartite sizes, with a structural coefficientwise monotonicity proof. Extends beyond the known s=2 example, not just a one-number substitute.

The dated certificate retains the supplied scientific assessment, sources and limitations.
