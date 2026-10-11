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

The 2025 primary paper gives, for the same discretely represented class, the explicit projection \(P\) onto \(c_{0,\mathcal I}\) and states \(\|P\|\le2\). The 2026 follow-up reports the universal lower bound \(2\) for the complementation constant of every proper complemented ideal. Sandwiching those bounds forces the exact constant and the canonical \(P\)-norm to be \(2\). For \(Q=I-P\), the block formula is contractive because every ultrafilter limit has norm one and the blocks partition the coordinates; \(Q\mathbf1=\mathbf1\) forces \(\|Q\|=1\).

## originality

FAIL

The final claim is already a direct logical consequence of two published results on the same object: the 2025 theorem gives a projection of norm at most two on every discretely represented ideal, and the 2026 theorem gives a lower bound of two for every projection onto any proper complemented ideal-null space. Their conjunction immediately yields the exact constant and forces the published projection to have norm two. The complementary norm-one statement is an elementary read-off from the same published block formula. Under the audit rule that a corollary is covered even when the exact wording is absent, this is not an original result.

## value

FAIL

Although the subclass is natural and the exact number answers part of a recent open question, the audited result requires only sandwiching two already-published inequalities plus an immediate norm-one observation for the complementary projection. Under the common value bar, that is a routine corollary rather than a new structural lemma, boundary phenomenon, classification, or independently useful exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
