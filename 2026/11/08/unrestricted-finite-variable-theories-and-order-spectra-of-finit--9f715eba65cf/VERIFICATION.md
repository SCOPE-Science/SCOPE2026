---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

For each i, the two-name formula P_i(x) recursively asserts i strict predecessor levels; local shadowing makes the recursion legitimate at arbitrary depth and L_i(x)=P_i∧¬P_{i+1} isolates level i. With k variables, requiring t≤k distinct elements satisfying L_i distinguishes different capped multiplicities. Conversely a perpetual k-pebble injection preserving level indices and equality always has a reply: after lifting one pebble at most k−1 remain, and either an unsaturated level has exact matching size or each saturated level has ≥k elements. This proves equivalence for every finite depth, not merely sampled tests. Capped words give unique family-relative minimum models, k^h at fixed height and exact defining width M+1. Splitting capped words with and without a k letter yields both rational generating functions and exact-order realisability. Width one distinguishes no two nonempty pure strict orders; boundary cases h=1, k=2 and n_i=1 are covered. Independently constructed tuple-colour refinement on all 63 compositions of 1..6 vertices gave 0 disagreements across all 1953 unordered pairs for k=2,3 (1725 and 9549 tuples, respectively); direct independent compositions gave u2 through N=12 and u3 through N=10. The finite computation only corroborates the analytic argument.

## originality

PASS

Resultary semantic searches, a full reading of related published chain-union findings, and primary articles on pure linear orders, finite-coloured-order EF ranks, total preorders with additional relations, and general finite-variable pebble games show no identified predecessor that entails the ordered truncated-level theorem together with the distinct exact-order spectrum. The basic pebble characterization and composition algebra are classical. Priority is qualified by the possibility of an unindexed general composition/interpretation theorem.

## value

PASS

The object is the full natural class of finite strict weak orders (rankings with ties), not an arbitrary numerical slice. Complete unrestricted-depth FO^k classification sharpens exactly which tie multiplicities are observable at any fixed variable budget while height remains visible, yields canonical minimum models and sharp width, and separates two distinct natural order spectra (minimum sizes versus theories actually realised by N elements). This is a motivated reusable exact classification, not a mere verifier output or a single tiny-case negative check. The formulas and counting follow elementarily after the structural insight; no major general theorem or downstream application is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
