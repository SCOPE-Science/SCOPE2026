---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The calculation is correct. From the normal bundle sequence, c_1=(5-a-b)H and c_2=(10-5(a+b)+a^2+ab+b^2)H^2, so p_1=(5-a^2-b^2)H^2 and integrating H^2=ab gives sigma=ab(5-a^2-b^2)/3. At fixed S and gap g=b-a, minus three times the signature equals (S^4-10S^2+10g^2-g^4)/8. On even allowed gaps, g=2 uniquely maximizes the variable term; on odd gaps, g=1 and g=3 tie and every g at least five is lower. A fresh exact check for every S from 6 through 40 reproduced both formulas and all equality cases; the symbolic quartic argument proves all S.

## originality

FAIL

Originality fails under the implication standard. The exact tangent-bundle formula for complete intersections is classical and gives the pointwise signature formula for every bidegree by the standard Chern-to-Pontryagin calculation and Hirzebruch signature theorem. Once that stronger all-bidegree formula is known, imposing a+b=S and writing g=b-a reduces the claimed extremum to maximizing the elementary quartic 10g^2-g^4 on the allowed parity lattice. The gap-two even optimum and gap-one/gap-three odd tie are therefore routine corollaries of already-known complete-intersection characteristic-class data, even though no source with those extremal words was found.

## value

FAIL

Fixing a+b is geometrically motivated because it fixes the adjunction exponent, but the final extremal theorem is obtained by substituting into a classical pointwise signature formula and maximizing a one-variable quartic over parity-constrained integers. Under the required value bar this is a routine deduction from known characteristic-class data, not an independently worthwhile exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
