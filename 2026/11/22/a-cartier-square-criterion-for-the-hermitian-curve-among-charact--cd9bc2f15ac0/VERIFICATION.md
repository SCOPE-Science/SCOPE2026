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

# Reproducible scientific checks

Run `python3 verify_cartier.py` with the Python 3 standard library. The script rederives the Cartier operator from the plane-quintic mixed-partial formula over \(\mathbb F_4\), rather than simply entering the matrix from the proof. For every one of the \(256\) monic quartics it checks exact squarefreeness and, on the \(192\) smooth models, the semilinear matrix ranks. The expected distribution is \(180\) smooth coefficient tuples with Cartier ranks \((3,1,0)\) and \(12\) tuples with ranks \((3,0,0)\). The script also verifies that \(v^5=u^4+u\) has \(65\) points over \(\mathbb F_{16}\), using explicit binary-field arithmetic.

The coefficient-independent proof is the six-basis-vector calculation in `RESULT.md`; field enumeration serves as a separate finite consistency check, **not** a proof of all algebraically closed-field cases. The proof derives the genus from a smooth plane quintic, computes Cartier by mixed partials, uses the semilinear square and cube, and classifies the additive-quartic branch locus up to projective equivalence. No assertions about full generic Newton polygons or independent external certification are made.

Scientific status: the symbolic argument and finite verifier have received a self-review. Independent audit: not yet performed.
