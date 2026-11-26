---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The lambda maps are exactly the left multiplications by I+A, so the orbit at B is B+R_n(q)B. Row i of AB ranges independently over the span of rows i+1 through n of B. Thus the orbit exponent is the sum of the tail ranks. Adding row j gives q^d choices preserving dimension and q^(n-j)-q^d increasing it, with the updated dimension added to the exponent. Row 1 contributes a free factor q^(n-1); division of each point count by its orbit size is valid. Rank zero forces all other rows to vanish. The maximal profile increases at every stage; its point fraction is (1-1/q)^(n-2), giving the stated maximal count and bounding the normalized collision probability between that fraction and 1. The n=2 empty recurrence and the four row cases agree. An independent BFS on actual matrix-unit lambda maps for (n,q)=(4,2), cross-checked against B+R_n(q)B, produced 8,12,4,2 orbits of sizes 1,2,4,8, respectively, and collision probability 31/512. No uploaded script was executed.

## originality

FAIL

Yan's earlier adjoint-template theorem and double-orbit size lemma mechanically imply the complete numerical census for the same one-sided action. This is stronger evidence than a thematic resemblance to coadjoint orbit theory. The weighted deduction is given below. The specific row-state implementation need not have appeared there; it is an alternate evaluation of that invariant. Two later catalogue records also contain exact same-action censuses, but their dates are not used to infer historical priority.

## value

FAIL

The canonical component spectrum and collision probability are naturally motivated, and the state recurrence is a convenient way to compute them. But the submitted exact-invariant advance is mechanically available from the earlier template theory and the collision identity; the extremes and fixed-n large-field estimate result from the same maximum profile. The frozen claim does not establish a distinct complexity, structural or asymptotic result that would turn this alternate enumeration into a separate advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
