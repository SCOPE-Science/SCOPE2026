---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The positive root solves a²+c(d+1)a/sqrt(d)+c²=1, and b²-a²=ca sqrt(d). For unit u with first coordinate t, completing the square in the farther of the two ball distances gives exactly 1-ca sqrt(d)(|t|-1/sqrt(d))². Convexity gives containment and the equality condition gives the entire contact set. At each contact u the active transformed-ball gradient is 2b²u, so u·v<=1 is a support inequality. The stated 4(d-1) contacts with equal weight d/[4(d-1)] have zero first moment and identity second moment: sign sums cancel cross terms, their weighted squared first coordinates sum to one, and each transverse coordinate contributes one. To verify unrestricted uniqueness directly, express any normalized competitor as y+A B_d with A symmetric positive definite. The support inequalities give u·y+||Au||<=1; summing with the contact weights and using u·Au<=||Au|| gives tr A<=d, hence det A<=1. Equality forces A=I by AM–GM, then the zero first moment and spanning contacts force y=0. The strict axis inequalities follow from (d+1)/sqrt(d)>2 and b²+c²=1-ca/sqrt(d). The root gives a=O(d^-1/2) and c(d+1)a/sqrt(d) tends to 1-c², yielding both limits. The volume and common-radius scaling follow from the determinant.

## originality

FAIL

The main finding is already covered exactly by two distinct earlier indexed results, 02e413e91d3d and 10a8defe3ad4. They give the same unrestricted John ellipsoid and the same complete normalized contact set on the identical lens; the second even gives the same finite contact certificate. The other claims are stated there or are immediate scale, volume, inequality, or dimension consequences of the identical formulas. The rejection is for demonstrated mathematical coverage, not for unavailable sources or correctness.

## value

FAIL

The exact John invariant and universal contact locus of this natural body are meaningful, but they are already available in the checked literature at the exact stated generality. The record repeats the existing finite certificate as well. Volume, equal-radius dilation and the fixed-c limit are direct consequences of the available formulas, not a distinct contribution or a motivated new refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
