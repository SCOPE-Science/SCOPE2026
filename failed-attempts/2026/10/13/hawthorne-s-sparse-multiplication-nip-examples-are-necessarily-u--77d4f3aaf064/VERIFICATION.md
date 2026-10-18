---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

In either sparse power set P={b^i:i>=0} for b=d>=2 or b=t, the restricted multiplication graph R(b^i,b^j,b^k) holds exactly when k=i+j. Thus x != y and exists z in P with R(x,z,y) defines i<j on powers and has the order property, proving instability. The Hawthorne NIP theorems (integer all d>=2 and polynomial prime p>=7) are confirmed in the primary PDFs. Domain and orientation are correct; the issue is prior coverage, not correctness.

## originality

FAIL

DECISIVE ORIGINALITY FAILURE: Hawthorne, arXiv:2007.00070 PDF Section 6.2 p.18, explicitly notes that the order on d^N is definable, that the exact integer expansion is not stable, and then Theorem 6.9 that it is NIP. This directly covers the submitted central integer claim with identical d>=2 hypotheses. The polynomial p>=7 corollary follows mechanically from Theorem 7.8 in arXiv:2011.12405 which writes the relation as (t^i,t^j,t^(i+j)); it is the same one-line order formula. Resultary failure to surface it cannot establish novelty.

## value

FAIL

The only new-seeming component is the identical definable exponent-order exercise applied to powers of t rather than d. With the explicit integer conclusion already published and the polynomial premises/graph explicitly stated, no independent new mathematical invariant, structural classification or motivating gap remains; another restatement of the elementary order property does not satisfy scientific-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
