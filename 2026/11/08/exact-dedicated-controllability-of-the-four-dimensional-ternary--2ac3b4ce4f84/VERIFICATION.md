---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The 81x108 incidence matrix N has NN^T=4I+A_{H(4,3)}, hence eigenvalues 12(1),9(8),6(24),3(32),0(16) by tensor decomposition, rank N=65. Laplacian eigenspaces at eigenvalues 4 and 3 lie entirely on the point and line shores and have respective dimensions 16 and 43, so PBH requires at least 16 distinct point-actuated and 43 distinct line-actuated vertices. The proposed lexicographic pivot complement picks exactly 43 lines, and the binary-corner set has 16 points. Independent finite-field F101 elimination gives exact observation ranks for N, P_0 and each P_lambda (16,32,24,8,1); nonzero mod101 minors imply nonzero rational minors, with eigendim upper bounds, proving PBH for all modes. Also directly checked no initial marked vertex has one unmarked neighbor, so standard zero forcing stalls. All 5 ranks and source tree independently rebuilt, not relying on saved VERIFY_OK.

## originality

PASS

General results of Burgarth et al establish sufficiency of zero forcing, not necessity; Yuan et al max geometric eigenvalue multiplicity 43 concerns unrestricted B and does not imply 59 for dedicated point/line columns. The ordinary 54-vertex Gray graph is dimension three and 3-regular, unlike the 4D 189-vertex incidence network. Related precise controller classifications for affine plane incidence graphs and triangular graphs use different base graphs and spectra. No prior exact 59 count for this 4D ternary point–line graph found.

## value

PASS

Dedicated coordinate controllability is an independently meaningful graph invariant. The 43 versus 59 separation displays an orthogonal two-shore obstruction invisible to a single unrestricted-input multiplicity bound; the explicit rank-certified optimum and its stalled zero-forcing behavior provide a useful exact small structural benchmark rather than an arbitrary parameter variant. A fixed finite natural Hamming incidence graph may have an exact valuable invariant without a whole higher-dimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
