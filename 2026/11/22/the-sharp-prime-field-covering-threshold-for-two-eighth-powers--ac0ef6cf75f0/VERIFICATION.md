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

For p odd and target a nonzero, the derivatives of X^8+Y^8-aZ^8 cannot vanish together in projective space over the algebraic closure. The smooth plane curve is geometrically integral (distinct components would meet) and has genus 21. The at-most-eight points on Z=0 leave at least p-7-42 sqrt(p) affine points by Hasse–Weil. At 1778 the squared margin (1778-7)^2-42^2*1778 is 49 with 1778-7 positive, and the unsquared lower bound increases for p>441. Thus the asserted large-prime range is covered with no gap above the census cutoff 1777. The target zero is immediate and F_2 has both elements as eighth powers. A separately written replay used trial-division primality, eight repeated modular multiplications for each x and a residue bitmap for all pairs of distinct power values as sets (including diagonal pairs). It checked all 275 primes through 1777 and exactly reproduced p:count = 5:3, 13:10, 17:5, 29:22, 41:21, 73:46, 89:56, 97:73, 113:85, 137:86, 233:204, 257:225, 337:295, 761:666. The replay checks the power-image size 1+(p-1)/gcd(8,p-1) in the three odd-prime branches, 769 primality, and compositeness of all integers between 761 and 769. This proves the least prime threshold. The uploaded verifier was inspected, not executed; the exact replay can be repeated with python3 /workspace/evidence/5/independent_two_eighths.py.

## originality

PASS

Best-of-knowledge pass for the sharp prime-field octic classification, the eleven p=1 mod 8 obstructions and their counts, and the last obstruction at 761. The three quartic-branch exceptions and their counts are already known, and eventual coverage and the general geometric/counting methods are not new. The best relevant full texts inspected do not give the octic finite classification or its sharp threshold. The 2022 thesis and the unread portion of the 2021 graph paper remain access risks, not evidence of noncoverage.

## value

PASS

The largest exception for a fixed exponent is a natural question explicitly raised in the two-power coverage literature. For the prime-field case at exponent eight, the result gives the sharp onset of permanence and all genuinely octic exceptions with exact coverage deficits. The theorem combines a certified universal cutoff and an exhausted finite complement, rather than proposing a table from sampled primes. Its specific finite counts are useful independently of a new general method, and the already-known quartic branch is not credited as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
