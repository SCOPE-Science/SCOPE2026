---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The claimed minimum is correct. Equal-length squares are distinct and cannot contain each other. In any linear host, successive selected starts are separated by at least the least consistent positive overlap shift. Conversely, appending by those shifts preserves the whole new square at the suffix and all previously embedded factors. Adding the dummy creates a tour with cost 10 plus the shifts. Independently regenerated all costs and checked the literal 82-bit witness against all 32 factors. Rather than using the frozen numerical-optimality check as a proof, generated an independent binary branch certificate with valid directed cut inequalities. Each split fixes an arc bit to 0 or 1 and covers both cases. At each leaf, priced degree equalities and directed cut inequalities with the valid signs, then bounded each adjusted arc term by its exact minimum on its fixed value or on {0,1}. The standard-library replay verifies the result in integers: 557 splits, 558 leaves, 113 valid cuts, weakest rational lower bound 50659721/625000 > 81. Thus integral tour length is at least 82, and the witness attains it.

## originality

FAIL

A distinct Resultary finding b1c706b65373 covers the exact same optimum 82 for all 32 five-bit-root squares as ordinary factors in a linear host, with an exhaustive exact lower-bound argument and a matching witness. This is demonstrated equivalent coverage, not an assertion that the later-dated catalogue path proves earlier priority or derivation from either record. Au's earlier Algorithm E also yields a length-82 construction on direct evaluation, though it does not establish exact optimality. The two exact records' different verification methods do not make their stated invariant different.

## value

FAIL

The fifth value of this natural sequence is a motivated exact invariant, and closing its gap would be worthwhile if it were not already covered. A separate solver approach and witness in the frozen record provide corroboration, but the finding states the same covered finite fact and no independently useful new mathematical consequence or sharper invariant. Au's earlier algorithm already provides an attaining construction, so that part is not a surviving result on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
