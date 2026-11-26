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

Besides the published binary two-read criterion, one can check the key uniqueness directly. For distinct words with first and last differences L,R, a common deletion word made by deleting i in the first word and j>i in the second requires i≤L≤R≤j. Equality of the shifted substrings and equality of letters before L and after R allow these deletions to move within constant runs to L and R. The reverse orientation is the only other possibility (deleting the same index only covers a single mismatch). Both orientations when L<R force the opposite alternating phases. Mark the representative starting with D and its unique mismatch factor. The mark requires initial height h≥1; flipping raises odd intermediate heights by two, leaves even ones unchanged, and at the end either preserves height (even length) or raises it by two (odd length), preserving ballot legality. Excursion decompositions give P_h=C(z²)T^h and the first-passage exclusion F_h=(1−T^{h+1})/(1−2z). The even factors contribute z²/(1−z²) times ΣP_hF_h over h≥1 and the odd factors z³/(1−z²) times ΣP_hF_{h−1}; the geometric sums give the two displayed rational expressions in T. Expanding T at z=1/2 gives (3√2)⁻¹(1−2z)^(−3/2) and (6√2)⁻¹(1−2z)^(−3/2) for the leading terms. The only other circle singularity is z=−1/2, where 1−2z is nonzero and 1−T² vanishes at square-root order. Algebraic transfer and Γ(3/2)=√π/2 give the constants and O(2^n) total remainder; the central binomial asymptotic gives average degree n to leading order.

## originality

PASS

The distinct result is the edge enumeration by height change for the graph induced on all ballot prefixes and its two-to-one asymptotic split. Credit the two-read alternating characterization, the unrestricted composition-refined edge calculation and the Dyck-only edge calculations. Neither unrestricted counts by total composition nor counts for words ending at zero count legal suffixes at the two different heights arising here. The fixed-pattern Dyck and ballot sources inspected have different outcome statistics, endpoints or pattern classes.

## value

PASS

The constrained confusability graph is a natural object in sequence reconstruction; the equality versus adjacency of endpoint layers is not an arbitrary slice. A boundary-sensitive edge count with explicit generating functions determines an asymptotic density split and average degree for the full family. This supplies testable graph-scale constraints beyond the generic two-deletion-output criterion or the balanced Dyck-only graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
