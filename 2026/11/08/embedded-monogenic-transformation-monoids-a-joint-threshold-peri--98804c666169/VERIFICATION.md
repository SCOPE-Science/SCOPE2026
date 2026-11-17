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

PASS. Each full transformation decomposes uniquely into a permutation of s cyclic vertices with exact order p and n−s labeled rooted forest vertices of maximal depth h. Ordered distance-layer parent assignments give E_(n−s,s,h); Möbius inversion of permutation orders gives Q_(s,p). A monogenic embedded submonoid has φ(p) generating maps at h=0 or1, unique generator for h≥2; these preserve s. Thus the joint quotient C(n,s)Q_(s,p)E_(n−s,s,h)/c(h,p) is exact, including m=0 and p=1. Counting the h≤1 overcounts produces M_n=n^n−∑_s C(n,s)(s!−C_s)s^(n−s), with bound n exp(1/2−n/3) for relative error. Independent enumeration of all functions n=1..5 produced total embedded counts 1,4,26,237,2842 and checked nonzero triple classes (1,3,7,14,26); finite sample does not prove all degrees.

## originality

PASS

PASS only for joint stable-cyclic-rank s refinement with h and p: Resultary 2026-11-02 gives EXACT same bivariate (h,p) embedded count, same generator correction c(h,p), same unrefined totals and an even sharper exponential O(√n(2/e)^n) overcount bound. Those parts of this package are fully covered and are not novel. Earlier published bivariate EGF does not state the stable-rank resolved fiber M_(n;h,p,s); obtaining it requires keeping cycle-support cardinality in the rooted-forest combinatorics. The extra rank is a natural invariant, although the extension is short and there is substantial implicit-coverage risk.

## value

PASS

PASS narrowly. The joint maximal-depth, eventual-cycle-period and stable-rank distribution is an exact natural embedding statistic for finite transformation dynamics; knowing h,p alone does not recover the distribution of the eventual image size s. It permits conditional counts by image size and separates maps with identical power semigroup type but different embedding ranks. Its component forest formula is explicit and independently useful. The prior total and asymptotic, and the elementary generator lemma, add no value here; ranking this as a modest finite combinatorial refinement rather than a new global monoid classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
