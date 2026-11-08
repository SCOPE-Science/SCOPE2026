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

# Verification

Run `python verify.py` with Python 3 and no external packages. The script uses `fractions.Fraction` for every numerical operation and solves the *uncompressed vertex-level* discounted hitting system by exact Gaussian elimination, independently of the multipartite reduction.

The replay produced:

```
INDEPENDENT_COMPLETE_POLYNOMIALS_OK 27
SHARP_THREE_WAY_PHASE_OK 162 exact independent vertex-level solves
SHARP_m_EQUALS_3_BOUNDARY_OK
VERIFY_OK
```

It exhaustively enumerates all labelled source subsets for nine small complete multipartite part-size lists at three rational discount/threshold pairs, checking 27 complete cardinality polynomials. It also tests all three three-source orbit types on balanced tripartite graphs for nine part sizes and six discount values, along with both rational-difference identities and the sharp part-size-three obstruction. These checks do not replace the all-parameter proof and do not constitute an independent mathematical audit. Parameters remain unrestricted in the proof: integer \(m\ge4\), real \(0<\lambda<1\), and every real threshold in the stated interval.
