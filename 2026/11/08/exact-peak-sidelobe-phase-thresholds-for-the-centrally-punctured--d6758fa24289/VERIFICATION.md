---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The eight-site centrally punctured 3x3 support and three-root gauge yield exactly q^5 normalized arrays for each q=2,...,8. All 12 aperiodic half-plane displacements are exhaustively scored. Inspected check_psl.py represents q=5,7,8 squared magnitudes in exact quadratic/cubic rings and distinguishes q=7 values by a rational isolating interval, not by rounded floating-point ties. Independent reimplementation enumerated all 61,775 normalized assignments and reproduced every minimum and optimizer count: 4/20, 3/8, 2/24, (3+sqrt(5))/2 /240, 1/2, 4cos²(2pi/7)/28, and 2/114. The corner displacement (2,2) forces PSL>=1 for every phase; exhibited q=6 vector attains it. This proves exactly q<=8, not all alphabets.

## originality

PASS

New exact max-norm finite phase-alphabet census; same punctured support had earlier sum-of-squares/fourth-moment results, but maximum is not their sum and optimizer counts differ sharply. q=6 optimizer overlap expressly credited.

## value

PASS

Peak aperiodic sidelobe minimization on a sparsely supported square is a natural array-design invariant, distinct from integrated fourth moment. Full optimizer census and the first six-phase exact floor with q7/q8 nonmonotonicity give motivated finite cutoffs and explicit usable witnesses; q<=8 is intentionally a finite theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
