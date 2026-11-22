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

# Computational and mathematical verification

The complete proof is in `RESULT.md`. Brandt multiplication is checked directly, and the two normal-form families exhaust all maximal commuting sets. The weighted polynomial is an exact sum over disjoint parametrizations; the maximum follows from the sharp rectangular bound. For the probability statement, the two distinguished color-counts have an exact multinomial distribution before an exponentially rare conditioning event, so the law of large numbers and ordinary multivariate central limit theorem apply with the stated covariance. The derivative of the product map yields the recorded nonzero variance.

Run `python CHECK.py` (Python standard library only). It enumerates actual maximal cliques in the nonzero commuting graph and compares all sets against the asserted normal forms. Product-closure is checked for every enumerated family. `CHECK_OUTPUT.txt` contains ten `PASS` records and ends with `VERIFY_OK`.

Tested input pairs of structure group and index count are \((C_1,1),(C_1,2),(C_1,3),(C_1,4),(C_2,2),(C_2,3),(C_3,2),(C_3,3),(S_3,2),(S_3,3)\). In the \(S_3\) case, the code independently recovers its four inclusion-maximal abelian subgroups. Exhaustive *small* cases cannot certify arbitrary groups, indices, or the asymptotic limit. No external or independent audit was performed.
