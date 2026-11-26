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

For the stabilizer H of a proper 6A, put t=|H|. Kneser gives |6A| >= 6|A+H|-5t while properness gives |6A| <= p^a-t. Since |A|>(p-1)p^(a-1)/4, it follows that (p-3)p^(a-1)/2<4t. This contradicts t<=p^(a-1) for p>=11; at p=7 it forces H to be the kernel of reduction modulo 7 (also valid at a=1). The image of A then contains two distinct classes, whose sixfold sums cover the seven classes; H-periodicity lifts coverage to the entire group. The witness {1,2} is a strict majority of Q(7) and has only six fivefold sums. Coverage at any smaller order would imply coverage at order five by adding fixed terms. This is an analytic check for every a; the frozen Python tests are supplementary.

## originality

FAIL

The claimed covering theorem is an immediate specialization of the older exact unrestricted critical-number theorem. It holds without restricting A to squares and even at equality when half the square count is an integer. Sharpness of the uniform six is the elementary two-element obstruction in the group of order seven; the square restriction merely supplies a permissible pair.

## value

FAIL

The local covering constant can be useful when cited as a corollary, but the record adds no nonroutine residue-specific bound or obstruction to the known exact unrestricted theorem. Both the specialization and the sharpness example are immediate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
