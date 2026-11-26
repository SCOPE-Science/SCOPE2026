---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The six exceptional, fifteen line-transform and six conic-transform classes have pairwise intersection zero or one. Each line has ten neighbors in the double-six presentation; distinct lines through the same point have distinct tangent directions, and Eckardt-freeness excludes triple concurrence, so the 135 intersections give distinct transverse nodes. The connected rational-component divisor has genus 109. The class sum is 27H−9∑E_i=−9K. A separately built double-six graph gives exact Laplacian spectrum 0^1,9^20,15^6 and rooted Smith diagonal 1^7,9^13,45,135^5 at two deletions, with the exact determinant 5129015115539641837921875. The frozen local algorithm correctly clears a minimum-valuation pivot by dividing out its p-power and inverting the unit part; the precision-five runs described by the record resolve all nonzero pivots, and sorting the local valuations aligns the integral invariant factors. Since −K is very ample, the second pencil member can be smooth and avoid the finite node set. In the formal neighborhood of a node the family is given by xy+t·u=0 with u a unit; away from nodes the special fiber is smooth and so is the family there. The pencil is proper and flat over the formal DVR, with smooth geometrically connected generic fiber (Bertini and connectedness for an ample divisor). Thus the regular split thickness-one graph description applies.

## originality

FAIL

The exact group is a straightforward specialization of Ducey et al., Critical group structure from the parameters of a strongly regular graph, Theorems 3.1 and 3.3, with a rank forced by the classical line-class marking. That is implication by a relevant prior theorem, not a claim that its Example 3.6 gives the target factors verbatim. The example there is the 16-regular nonintersection graph, whereas both the specialization and the frozen claim concern its 10-regular complement. The divisor and smoothing interpretation use classical geometry and the general component-group theorem.

## value

FAIL

This is a natural degeneration and the exact invariant is potentially useful. But the central numerical result is mechanically implied by earlier strongly regular graph theorems, with the required 3-rank an immediate unimodular-minor fact from the classical double-six marking. The genus, pencil regularity and component-group application here are standard deductions from this same configuration, not a distinct conclusion that sustains the frozen finding on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
