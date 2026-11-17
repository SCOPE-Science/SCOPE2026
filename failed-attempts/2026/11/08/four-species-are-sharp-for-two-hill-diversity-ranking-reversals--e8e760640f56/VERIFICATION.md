---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The power-sum difference for (1,9,12,18)/40 versus (3,5,16,16)/40 has exact integer numerator values F(0)=F(1)=0 and 40^q F(q)=(4,-54,496) at q=(2,3,4). For q>1 Hill order reverses the sign of power sums. The ordered combined exponential coefficients (+1,-2,+1,+1,-1,-1,+1) have exactly four sign changes, so the zeros q=0,1 and two crossings between (2,3),(3,4) exhaust all real zeros. Common-component padding preserves the roots for all S>4. These calculations and the majorization/zero-count argument support correctness, but not novelty.

## originality

FAIL

FAIL: a complete earlier publication dated 2026-10-13 already proves for every s the stronger bound of at most s-2 ties for two distinct Hill-diversity profiles and exhibits an exactly double-crossing four-species pair with the same q2,q3,q4 alternation and extension to larger S. It directly implies the submitted sharp threshold and exact-two existence; a different numerical witness cannot establish originality of the covered principal theorem.

## value

FAIL

FAIL: The scientifically motivated question of the least number of species allowing two Hill-diversity reversals has already been answered in full, with a stronger s-2 bound. The submitted smaller-denominator rational witness and a standard exponential-polynomial proof repeat the established sharp threshold without an independently useful new constraint, algorithm or exact enumeration. Correctness, reproducibility and alternative numerics do not create mathematical value for a covered original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
