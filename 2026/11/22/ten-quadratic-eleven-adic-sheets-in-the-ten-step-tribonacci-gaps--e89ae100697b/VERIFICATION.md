---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Write the gap as the x^2 coefficient of x^n h in Z[x]/(x^3-x^2-x-1), with h=x^10-1. Independent ring arithmetic gives h=(43,68,81), xh=7h mod 11, h^2=0 mod 11 and h^3/11=7h mod 11. For t on sheet r the normalized nonconstant Mahler series has quadratic leading coefficient 3*7^r mod 11. In the remainder after dividing by 121 the coefficient valuations of term i are at least floor((i+1)/2)-2-v_11(i!), nonnegative for i>=3 and tending to infinity. Hensel gives one derivative zero; translation and division by the square of the displacement yields a unit factor congruent to 1, with integral square root. Multiplication of the displacement by that factor's square root preserves all distances and is surjective by finite-quotient bijectivity. The ten mod-11 residues differ, and each fiber is a shifted square fiber at one lower depth. The normalized series is 1-Lipschitz; the unit quadratic coefficient excludes nonzero shifts mod 11 and a point with unit derivative detects exactly v_11(q) for q divisible by 11. Modulo 11 itself the ten disjoint classes give the least period directly. Counting units at even valuations gives the stated images; summing Haar measures gives 5/12. Standalone replay: python3 /workspace/branches/tribonacci_reproduction.py. It independently lifts critical roots, compares full shifted-square multiplicity tables (rather than just multiplicity bounds), and tests the recurrence periods through depth five: 10, 60, 560, 6110, 67110 image residues. Those finite checks are not the infinite proof.

## originality

PASS

The distinct contribution is the complete lag-ten gap image and square-root fibers at 11. The generalized recurrence period theorem is credited prior context. No compared statement supplies the ten shifted-square gap sheets; this is a qualified finding, not a historical priority certificate.

## value

PASS

The lag-ten difference probes the first return of a natural recurrence at the exceptional prime. Exact periods alone leave the support and the number of preimages undetermined. The ten critical-value sheets provide exact all-depth membership and multiplicity tests and explain the positive-measure omission (image Haar measure 5/12). This is an arithmetic classification, not a table of a few moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
