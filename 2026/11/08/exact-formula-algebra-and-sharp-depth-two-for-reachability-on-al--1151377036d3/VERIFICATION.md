---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The pinned proof derives both pointwise gamma cases by finite-Alexandrov comparability components, then proves structural induction on profiles (root color b, nonempty leaf color support S, pointed leaf color a or root marker). Distinct profiles have explicit depth-two characteristic formulas using E(C)=gamma(top,C), R=d(top), so all 2^N subsets occur with N=Q Σ_{j=1}^{min(m,Q)} binom(Q,j)(j+1), Q=2^k. The m=Q saturation and k>=1,m>=2 lower bound use explicit depth-one indistinguishable valuations; the k=0,m=1 edge cases are covered. Independent finite direct graph comparison checked 5,456 (A,B) pairs on m=1..5 and all asserted small profile counts. No finite test substitutes for the induction.

## originality

PASS

Best-of-knowledge original, qualified. General path logic and finite-poset reachability are established; no inspected theorem computes the exact fixed-star semantic algebra or its sharp variable-dependent saturation. Originality depends on fixed-space arbitrary-valuation quotient, not on rediscovering the global modality.

## value

PASS

This determines a natural exact formula algebra and sharp expressive depth for a fixed Alexandrov family. It distinguishes support from leaf multiplicity and identifies an exact Q=2^k stabilization threshold; the universal closed form is not a routine renaming of a known count. A researcher analyzing topological reachability expressivity on finite spaces could use precisely this classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
