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

For any putative scalar-shifted monomial the valuation and initial coefficient are forced; normalizing leaves a unit. Removing (1-y^j) factors successively determines unique exponents mod 19 through degree 18. Frobenius gives (1-y^j)^19 = 1 mod y^19, so this test applies to arbitrary integer powers, including negative powers. P0 is trivial in this truncation and each Pa forces equal exponents at a and 19-a. An independent reproduction computes integral colored-partition coefficients through q^379 via n p9(n) = 9 sum_{j=1}^n sigma_1(j) p9(n-j), then reduces mod 19 and removes Euler factors by geometric-series division. It reproduces every row, with valuation 1 only at residues 6 and 13; the pair (1,18) disagrees except at residue 3, where (2,17) gives (10,18). The finite mismatch contradicts any full identity; infinite vanishing at 17 instead follows from Bilgici's dissection, not the computed zero truncation.

## originality

PASS

The surviving distinct result is the unrestricted integer-exponent obstruction for all eighteen nonzero normalized components in the stated alphabet. The dissection and zero component are known; so is the narrower quartic-product observation in the motivating paper. The exact published catalogue match is the same record, not a distinct antecedent. No inspected distinct source covers the unrestricted obstruction.

## value

PASS

This answers a concrete question in Bilgici's Section 8 for the factor alphabet of the dissection. The paired-exponent test covers infinitely many exponent vectors at once and excludes denominator identities as well as quartic products. The value is the complete obstruction, not the known zero progression or another table of dissection terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
