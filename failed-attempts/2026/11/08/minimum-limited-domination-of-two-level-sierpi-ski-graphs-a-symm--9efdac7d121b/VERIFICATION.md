---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

The main classification and formulas are correct. The diagonal vertex forces selection in every row; each selected vertex bounds its row's omissions by k; the symmetric circulant construction attains equality, with no duplicated offsets because k<m. At equality every selected vertex has exhausted its allowance within its own row, so no cross-row edge splits selected from omitted. This is exactly symmetry of the omission matrix, and the converse follows because each row is nonempty and all cross-row partners of selected vertices are selected. The coefficient, complementation and involution arguments follow. But under the standard edge-count meaning of path length, the frozen Finding and Proof falsely require paths of length at least two in the k=2 component description. For m=4, take a block diagonal omission matrix with two 2-by-2 all-ones blocks. It is valid and represents two single-edge paths, each with both endpoints looped. Paths must have at least two vertices, not at least two edges. The printed generating function already counts the two-vertex components correctly.

## originality

FAIL

The earlier Resultary finding a700d19c9c6e gives exactly the same complete labelled extremal classification and enumerations on the same parameter range. Its selected-vertex matrix is J minus the frozen omission matrix. Applying this bijection changes the common row sum from m−k to k and derives every mathematical counting and classification assertion, with the k=2 path-order wording corrected. This is verified coverage, not a priority inference from similarity or an unavailable paper.

## value

FAIL

An all-minimizer structural classification beyond a scalar extremum is intrinsically useful, but the frozen switch from selected to omitted entries is just complementation of an already complete classification on the same domain. It adds no distinct structural, enumerative or application result. Fixing the path-length wording would restore the intended mathematics, not leave a substantive new result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
