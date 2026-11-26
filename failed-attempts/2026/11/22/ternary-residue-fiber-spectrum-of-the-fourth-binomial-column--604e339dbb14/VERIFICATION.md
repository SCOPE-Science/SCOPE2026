---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Completing the square in the falling factorial gives 24F(x)=[(x-3/2)^2-5/4]^2-1. At x=3t this yields the stated center 3/128 and square-times-(9(2t-1)^2-10)/128 identity after dividing the centered value by 3. The multiplier is 1 mod 3, so its Hensel square root congruent to 1 mod 3 exists uniquely; its changes acquire at least two extra factors of 3, so multiplying u by this root preserves distances. The two other branches have unit divided differences mod 3. Each isometry permutes all finite quotients and is onto Z_3. The regular branches therefore contribute two finite lifts in total; the singular branch contributes three times the number of square roots at one lower modulus. For zero, the square roots are exactly multiples of 3^ceil(m/2); for nonzero squares of valuation 2j there are two unit roots with 3^j free lifts each. This handles m=0 and shows the exceptional count cannot equal a nonzero-square count. The shift by 3^k changes the output at n=1 by valuation k-1, and all branches descend to the claimed period 3^(k+1), proving leastness. In characteristic zero the derivative vanishes only at x=3/2: the other possibility is (x-3/2)^2=5/4, a nonsquare mod 3. Each sufficiently small output ball in a nonzero-square shell has probability divided by Haar volume equal to 2/3+2*3^j by the finite counts; on nonsquare targets the ratio is 2/3. The critical singleton has finite preimage and hence no atom. The shell volumes 3^(-2j-2) sum to 1/8, and their added density integrates to 1/3. The independent integer enumeration checked all target residues and shifts through k=9 against literal modular squares, giving, for example, the claimed k=5 histogram.

## originality

FAIL

A distinct same-object catalogue record has the same exact finite fiber law and normal form. A separate all-odd-prime theorem implies the finite and three-adic claims by specialization, including the density by the elementary square-map law. Material coverage is demonstrated; the shared date does not establish chronological precedence. Sun–Zhang's older theorem alone would only cover surjectivity.

## value

FAIL

The ramified fourth-column distribution is naturally motivated, and its global square form is useful as mathematics. As a distinct frozen contribution, however, its exact counts are already covered and the remaining density phrasing and three-adic preimage numbers follow mechanically from the covered isometric normal form. Reprinting this same specialization with the square-shell densities evaluated does not supply a new worthwhile gap or a surviving repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
