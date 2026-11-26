---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Final assessment of /workspace/repairs/1/RESULT.md. Frozen line 45 wrongly allowed a double inverse-map root at q=−1/4. The complete corrected RESULT.md replaces that assertion by the factorization: q−r contributes t−r(1+t)² with discriminant 1−4r, product of roots 1, and sum 1/r−2. These signs give two distinct negative roots for r<0, and a nonreal r cannot correspond to real t (t=−1 is not a root of this quadratic). The extra (1+t) factor power from a degree drop handles m=1; the double gamma root at m=2 yields real roots with multiplicity. Checked the corrected identities algebraically and with rational arithmetic including r=−1/4; the actual inverse-map double-root parameter is +1/4. No theorem statement, coefficient, or certificate changed. By Zhong's endpoint-pair formula and Hall, each j≥2 source-target choice matches: individual neighborhoods have size at least j−1, and two distinct sources have union of neighborhoods equal to all j targets. Only m singleton choices are lost. Independent exact rational Sturm replay gives (V(−∞),V(0))=(m,0) for m=3,…,11 and (11,1) for m=12, whose chain ends in a nonzero constant. The positive coefficients rule out nonnegative roots; the remaining two roots at m=12 are nonreal conjugates. Replay files: /workspace/review-evidence/1/independent_sturm.py and independent_sturm.txt in that directory. Frozen verification files were inspected, not executed. The conclusion does not classify m≥13 or minimal failure among all posets.

## originality

PASS

Reassessed after the proof correction with the same scope. The gamma formula is a direct application of the broader prior matching theorem and Hall's criterion, not an independent novelty claim. The exact first loss of real-rootedness in the standard examples is the supported increment. Neither the known complete two-level case, the smaller general counterexample, nor the nearby crown-cycle family covers that cutoff. The accessible comparisons do not settle universal priority.

## value

PASS

Reassessed after correction: the standard examples are a canonical height-two sequence and a uniform diagonal deletion of a known real-rooted family. Knowing the precise first failure at order 12 and the ten-real/two-nonreal split isolates a natural stability boundary for that deformation. The value rests on the sharp nontrivial boundary, not the routine application of Hall to the coefficient formula. Neither all larger orders nor the smallest failure among general posets is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
