---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

Run `python3 verification.py` using Python 3.9 or later. No external libraries are required. The program evaluates the two generating-function identities using rational arithmetic, enumerates all signed permutations and actual subgroup generator pairs, checks subgroup conjugacy via explicit conjugation at small degrees, and enumerates all faithful profiles through degree twelve.

Observed successful output:

```
A4_HYPEROCTAHEDRAL_PROFILE_NORMALIZER_AND_SUBGROUP_CENSUS_VERIFIED n<=12; brute B_n n<=6
```

The coefficient checks are exact through degree twelve; direct permutation-group checks are exhaustive through degree six and direct subgroup conjugacy checks through degree four. A generator pair \((a,b)\) satisfying \(a^3=b^2=(ab)^3=1\) with nonidentity \(a,b\) generates \(A_4\); each embedded subgroup produces exactly 24 such pairs. The proof, not the finite computations, establishes the theorem for all degrees. The verification code does not provide an independent scientific audit.
