---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

White-side first-force obstruction gives at most two uncolored vertices in each part. A two-white side requires a missing matched endpoint; if both sides have two whites, the nonempty matched index sets must differ. Direct case reduction completes forcing. Counting pairs with matched endpoints and exclusion of equal index sets gives coefficient C=A2*B2-t(a-t)(b-t)-binom(t,2); every initial white has at least b-3 or a-3 black neighbours, hence domination. An independent graph bitmask full-subset enumeration for 15 profiles corroborated. The all-parameter proof is combinatorial rather than empirical.

## originality

FAIL

FAIL: An October 18 published zero-forcing-polynomial theorem for the same graph family proves the identical five-term expression over the stronger parameter domain a,b>=3 and the exact characterization of all zero-forcing sets. The claimed dom-forcing equality for a,b>=4 follows immediately since every white vertex is adjacent to all but at most one of at least two black opposite-side vertices. A separate October 12 publication already gives the scalar dom-forcing thresholds.

## value

FAIL

FAIL: All substantive coefficients, cutoff and minimum count were published previously. The remaining domination observation is a one-line minimum-neighbour bound within the covered white-set classification and does not justify a separate novel scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
