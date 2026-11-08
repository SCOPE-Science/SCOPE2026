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

# Reproduction

Execute `python3 joint_verify.py` from the same directory as this document. The script uses only the Python standard library and exact rational arithmetic for all finite identities. It verifies the maximal local-obstruction formula by independent complete enumeration of primitive residue pairs for \(19\) tuples. For \(6860\) choices of tuple and primitive progression parameters, a separate augmenting-path bipartite matching algorithm agrees with the arithmetic criterion. The diagnostic product uses primes below \(60\), with no claim of certified decimal error.

Expected summary:

```
EXACT_SAME_PRIME_EXAMPLES {'4,8': '1/3', '27,81': '1/2'}
CRT_LOCAL_CENSUSES 19
PERFECT_MATCHING_COMPARISONS 6860
JOINT_EULER_PRODUCTS 0.809968275222 0.669351675488 0.564787650891 0.486552441546
POSITIVE_COVARIANCE 0.013303068622
VERIFY_OK exact_rationals=yes independent_augmenting_path=yes
```

Finite enumeration independently tests the boundary cases but does not prove the infinite mean law, the density-zero exceptional set, or the lattice-counting remainder. Those require the logical steps in `RESULT.md`. The published matching theorem is invoked as background, not independently certified here.
