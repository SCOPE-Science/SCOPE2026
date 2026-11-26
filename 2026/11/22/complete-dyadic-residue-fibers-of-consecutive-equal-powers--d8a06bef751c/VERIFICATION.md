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

For odd k≥3 and equal-parity inputs the odd-base difference has valuation s=ν₂(x−y) by the odd sum of monomials; the even-base difference has valuation at least s+k−1. This gives two bijective parity branches onto 1+2Z₂. The linear k=1 case is a single branch. For k=2, f₂=1+4T with T(x)−T(y)=(x−y)(x+y+1)/2, yielding two parity branches after normalization. For even k≥4, set t=ν₂(k); the odd unit power is 1 mod 2^(t+2), and k≥t+2 kills the even-base term at that precision. On one input class modulo four the odd bases have sum of valuation one, giving a power difference of valuation s+t by binary lifting, strictly below the even-base valuation s+k−1 or higher. Thus the four normalized maps are isometries. In all cases an isometry induces finite permutations and hence a compatible inverse and normalized Haar preservation. Above depth h, each of the 2^b branches modulo 2^b contributes 2^(h−b) preimages per attained target; at or below depth h everything reduces to 1. This also distinguishes finite residue multiplicities from the exact numbers of 2-adic roots. Independently computed all target counts at n=1 through 9 for 64 exponents, including powers of two through 1024, using exact integer powers (python3 /workspace/branches/independent_checks_2_5.py). The frozen checker was read, not run; the valuation proof, not the finite range, establishes the quantifiers.

## originality

PASS

Best-of-knowledge pass for the complete dyadic fiber law and exact 2-adic multiplicities for the constrained polynomial across all exponents. Its lifting and isometry techniques are standard. None of the compared dependent-input, independent-input or general-map results supplies the exponent-dependent dyadic branches and valuation offsets without map-specific analysis.

## value

PASS

Adjacent powers impose the natural one-variable dependence missing from unrestricted power-sum representation laws. The uniform theorem gives exact solvability and congruence counts for every exponent and precision, identifies the quadratic exception, and shows why a finite residue count can differ from the number of genuine 2-adic roots. This supplies a usable local obstruction and inverse-branch structure, not an isolated elementary modulus computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
