---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The 15-edge labelled Petersen orientation model and unnormalized binary Fourier transform are defined without quotient. Kahn topological peeling independently enumerated all 32768 masks, finding exactly 16680 acyclic; a complete integer FWHT found 19112 zero coefficients (16384 from global edge reversal plus 2728 additional even-weight zeros), rank 13656. Independently recomputed all 105 pair correlations by graph line distance: 30 pairs absolute multiplier 1944, 60 pairs 1080, 15 pairs zero. Fourier support projector has inverse Walsh kernel absolute sum 1113888 and norm 1113888/32768=34809/1024. Its norm is optimal even among non-translation-equivariant projections by averaging arbitrary projections over translations. Source verify_petersen.cpp was inspected with two acyclicity predicates, direct even-frequency sums, exact certificate comparisons; original CSVs were not independently regenerated from a downloaded source tree. The reported numbers were also independently recomputed.

## originality

PASS

No examined accessible primary theorem, exact table, or prior published mathematical result implies the complete specific final claim. This is best-of-knowledge originality, with the separately recorded plausible historical risks.

## value

PASS

The graph is a canonical nontrivial finite test object and the full signed Walsh nullity, two-edge correlation shells, and optimal unrestricted endpoint projection norm give exact structural/recovery information not implied by the familiar unsigned 16680 count. Self-contained exhaustive finite theorem with a mathematically motivated invariant, no extrapolation to all cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
