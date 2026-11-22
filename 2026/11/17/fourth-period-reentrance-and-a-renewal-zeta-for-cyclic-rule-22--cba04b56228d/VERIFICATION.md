---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Reconstructed the temporal t-column constraint graph D_t for Rule 22, with edge (a,b)->(b,c) iff for every time j the unique-one rule gives b_(j+1). For t=2, recurrent SCC sizes [4,2,1]; for t=4, [18,18,4,2,1]. Two 18-state components are temporal shifts, while the smaller recurrent components are doubled period-two subgraphs; hence 4C4(n)=2tr(A^n). Independently generated all nine simple cycles of one 18-state SCC with length multiplicities 8:1,9:2,10:3,11:2,12:1, all meeting at the four stated vertices. Thus the determinant expansion has only singleton cycle terms: det(I-zA)=1-z^8-2z^9-3z^10-2z^11-z^12. The log determinant proves the exact generating series, and intersecting cycles prove the exact support semigroup {8..12} ∪ {n>=16}, not just finite enumeration. Independent exhaustive binary state iteration for n=3..16 agrees with 4C4 counts, and symbolic 18x18 determinant yields all displayed coefficients. Perron-Frobenius primitivity (lengths 8,9) gives λ^n/2, not a conjectural numerical fit.

## originality

PASS

The source-specific labelled primitive temporal-four enumeration and its all-n rational zeta, 13–15 gap, and renewal growth are not implied by the inspected finite representative cycles or by other-rule period zeta classifications. The exact transfer determinant, common-cycle structure and semigroup classification supply the missing global statement.

## value

PASS

An all-circumference exact labelled orbit enumeration for a canonical nonlinear elementary CA, including a genuinely missing length window and a sharp exponential rate, is a motivated dynamical invariant not mechanically implied by finite tables. The common-simple-cycle bottleneck turns a finite transfer graph into a usable complete renewal classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
