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

PASS. Reviewed the complete dipole potential, cross-part sign accounting, h_N(s) algebra, partition extremality derivative and exceptional N=2..7 cases in actual RESULT.md and verify.py. L phi=delta_u-delta_v follows by the partwise Laplacian formula, and absolute potential differences over interpart edges sum to h_N(a)+h_N(b). Convexity p=ab<=((N-c)/2)^2 and monotonic F_N(c), with odd integer balance, establish the stated maximizers; small orders are finite enumerations. Independent grounded-Laplacian calculations for ten representative partitions confirmed K11 1, K111 4/3, K22 3/2, K221 26/15, K34=K331=2, K44 17/8. Finite checks corroborate but do not replace the all-N proof.

## originality

PASS

Unbalanced h_N and integer maxima are not implied by older balanced exact constants.

## value

PASS

PASS. Arbitrary unbalanced multipartite electrical networks are a natural symmetric graph family and precise edgewise error amplification is a meaningful stability invariant of least-squares gradient reconstruction. The new two-part-size formula and sharp global maximizer over all integer partitions determine nontrivial transitions, including K331 co-maximization at N=7. Earlier balanced subfamily formulas do not supply these heterogeneous-row and partition results; this is more than a parameter substitution or a table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
