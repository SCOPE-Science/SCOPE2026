---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Any two vertices in the same independent part have distance two and a shortest path via any outside vertex. Thus X dual iff Y=V\X meets outside each part i having x_i≥2 or y_i≥2. Inclusion–exclusion for bad Y⊂V_i yields D_i=z^N+z^{N−2} when n_i=2, D_i=z^(N−n_i)(1+z)^n_i when n_i≥3; bad families intersect only for Y=∅, so correction (p−1)z^N. Two-color constructions and star-center obstruction yield exact χ. Independent direct subset enumeration checks representative multipartite profiles and all coefficients, finite check only corroborative.

## originality

FAIL

FAIL: previously published 2026-10-04 Resultary/SCOPE full RESULT titled "Dual, outer, and total mutual-visibility colorings of complete multipartite graphs" explicitly states/proves the IDENTICAL criterion in the notation B=V\X and IDENTICAL dual chromatic classification incl K1,2 and K1,n≥3. Remaining dual polynomial follows mechanically by counting Y⊂V_i using that complete prior set criterion, including only the n_i=2 boundary and trivial common empty complement intersection. This is strong prior implication, not mere title similarity. Do not salvage via a numerical reprint/certificate.

## value

FAIL

FAIL for this final claim’s proposed novelty: the key structural dichotomy and all chromatic content are already published. The remaining polynomial is immediate routine inclusion-exclusion over fully classified bad subsets and no separate independently motivated new invariant mechanism or extremal result is established. The polynomial itself is a natural count, but originality/value together cannot pass as a distinct new contribution from this package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
