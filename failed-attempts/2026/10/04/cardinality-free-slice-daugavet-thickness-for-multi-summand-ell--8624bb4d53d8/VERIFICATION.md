---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The assigned proof is correct. The coordinate-slice construction gives the upper bound. For the lower bound, finite truncation of the dual \(\ell_q\)-profile is legitimate for arbitrary index sets, coordinatewise Daugavet slices provide near-antipodal vectors, and the scaling lemma converts near distance two into the needed weighted lower bound. Summing \((r+s)^p\ge r^p+s^p\) yields \(2^{1/p}\). The stronger pointwise SCOPE theorem independently confirms the same global infimum.

## originality

FAIL

A stronger published SCOPE finding predates the assigned record and mechanically implies it. That finding proves for every point \(z\) of an arbitrary finite or infinite \(\ell_p\)-sum of Daugavet spaces the exact formula \(\operatorname{dc}(z)=(\lVert z\rVert^p+(1+m)^p-m^p)^{1/p}\), where \(m\) is the infimum of the coordinate norms. Since \(\mathcal T^s(Z)=\inf_{z\in S_Z}\operatorname{dc}(z)\), and a sphere point supported on one coordinate has \(m=0\) while the formula is never below \(2^{1/p}\), the assigned equality follows immediately.

## value

FAIL

As a standalone fact the arbitrary-cardinality equality is natural, but by the time this record was imported it was already an immediate corollary of a strictly stronger published SCOPE theorem computing every pointwise Daugavet constant on the same sums. Repackaging that sphere infimum does not add an independently needed mathematical fact under the shared value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
