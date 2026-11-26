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

FAIL

The displayed theorem is correct, but the Finding calls the tested shift the largest proper divisor and the title and SLOGAN call it a half-period. In fact h_r=2·3^(r−2) is T/3 and is the maximal even proper divisor. The largest proper divisor, T/2=3^(r−1), is odd, and its shift changes the residue modulo 3 on both parities; the stated even-only defect cannot describe that shift. Independently checked the actual formulas: substitution of y=e^t−1 gives integral g_k and coefficients g_k k! S(n,k); for n≥3r powers k≥3r vanish modulo 3^r by factorial divisibility. The low-degree certificate gives c_j modulo 9 equal to (2,7,0,0,2,8), hence 7+7^(n/2) for even n≥6 and 1 for odd n≥6. Cubing j²=1+3b repeatedly lifts the difference from shift 2 by a factor 3^(r−2), while 3-divisible j contribute zero. Euler gives T and eventual periods are closed under gcd; the odd and maximal-even proper divisors fail by the two separate obstructions. An independent inclusive-exclusion power-sum replay checked all residues of a tail cycle at each of r=1,…,8, including the defects and proper-divisor obstructions. It is finite corroboration only. The frozen verifier was inspected, not executed.

## originality

FAIL

The earlier 2026-10-13 Resultary record a513a62dd452 states the identical EGF, least eventual period at every ternary level, and the identical parity-selective defect with n≥3r. This is verified direct coverage, not an inference from the earlier all-moduli Carmichael upper bound. Correcting the divisor terminology leaves the duplicate theorem unchanged.

## value

FAIL

The least-period question is natural, but this submission repeats the known all-level classification and same-onset parity obstruction. Re-expanding the same integral coefficients in Stirling powers supplies no improved onset, modulus range, new invariant, or distinct proof consequence. A wording correction would not restore independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
