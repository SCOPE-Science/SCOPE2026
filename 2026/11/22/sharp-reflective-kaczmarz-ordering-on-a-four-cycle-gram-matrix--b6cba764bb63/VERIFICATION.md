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

The Gram eigenvalues are 1±2t and two copies of 1, so the row basis is legitimate. Independently, with G=I+L+Lᵀ ordered by the sweep and L strictly lower triangular, old and new coefficients a,b obey (I+2L)b=−(I+2Lᵀ)a, since the update in row i uses already updated coefficients for earlier rows and old coefficients for later rows. Thus the characteristic determinant is det[(z+1)I+2zL+2Lᵀ]. In its expansion the identity and four single edge swaps contribute (z+1)^4−16t²z(z+1)². The two disjoint-matchings terms contribute +32t⁴z², and the two full cycle terms give −16t⁴(z+z³) if the order runs along the cycle, or −32t⁴z² otherwise. The former occurs exactly for the four starting vertices and two directions. Taking z+z⁻¹=2c yields the stated cosines; c_other−c_+=4t²(1−t²−t√(2+t²))>0 exactly in the specified positive domain by squaring. c_+ is increasing and c_+(1/2)=1; endpoint derivatives 32/3 and 8 give the square-root gap ratio 2/√3. Normality gives the uniform averaging bound, not pointwise optimality of the finite average. Reversal and cyclic shift exhaust the three-factor case up to inverse and similarity, establishing minimality. Replay: `python /workspace/replay_checks.py 4` independently expanded the sweep determinant for all 24 orders and checked the endpoint slope; the supplied scripts were inspected, not executed.

## originality

PASS

Credit the reflection-product spectral framework and general characteristic determinant to prior work, not to this record. The supported distinct contribution is the exact eigengap ordering of every permutation for this weighted positive four-cycle, with strict comparison on the full admissible interval and the limiting performance ratio. The closest distinct indexed order-comparison hit uses a different iteration and objective. The judgment is bounded by the source access described below.

## value

PASS

The positive cycle is a natural minimal four-row geometry where order matters. The classification answers an a priori solver question about an established bound constant with no tuning except row order, and quantifies the advantage near loss of rank. It does not imply better finite-horizon error or runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
