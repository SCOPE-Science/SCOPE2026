---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The same synchronous update F(x)_v=x_v+sum_{w~v}sgn(x_w-x_v) and same translation equivalence are used throughout. For F²(x)=x, signs on each edge must reverse (or remain zero), as shown by the nonnegative edge-sum identity and its converse. On a tree, all integer oriented edge gaps can be independently chosen after fixing one hub. Leaf rigidity forces each active pendant group to one sign; enumerate the three admissible signed hub-bridge classes, both sign-negated copies, and the equal-bridge class (a=b). This yields current N_states=1+2[B_ab] for all a,b>=1, including boundaries a=1, b=1, and balanced arms; direct orientation checks at (1,1),(1,2),(2,2),(2,3),(3,3) gave 27,145,879,7169,60851. All nonconstant states are primitive period two, and fixed class is unique.

## originality

FAIL

A publication dated 2026-11-02 proves exactly B_ab as the orbit count for the SAME labelled double-star, SAME update and SAME unrestricted integer translations, together with a stronger fixed-total classification. Current N_states=1+2B_ab is an immediate restatement of that prior theorem, including the balanced bridge-tie family; no distinct novelty survives.

## value

FAIL

The underlying exact census is a natural and meaningful diffusion invariant, but in this submission the WHOLE formula and tied-hub contribution already follow algebraically from the earlier, stronger all-bistar orbit classification. No additional motivated unknown exact fact remains; reproducibility of known counts is not a new valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
