---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In RESULT.md lines 21–65, iteration of the incoming AND yields exactly the AND over length-t predecessors of each target. Thus the surviving nonempty initial zero sets are the distinct nonempty subsets of the complements of these predecessor sets. With α the distance to the hub and β the distance from it, any length ≥a² walk must pass through the hub: a walk avoiding it lies on one of the two open arms and cannot last even a steps. Between the first and last hub visits it makes complete circuits, so a walk exists exactly when t−α−β belongs to ⟨a,a+1⟩. For n=ha+r with 0≤r<a, membership means h≥r: at least r copies of a+1 are needed for this residue, and r such copies suffice. Hence above or at c−a=a(a−2), the sole gap is c−1 (the last residue in the block h=a−2); c=a(a−1). For t=E−k the residual length is at least c−a, so missing predecessors of a target at distance β are exactly the source level α=2a+1−k−β. The nonempty levels run from a+1−k to a: a singleton at a and k−1 two-vertex levels. Duplicate targets with the same β make no new subsets. Counting singles and whole pairs yields (2k−1)z+(k−1)z². At E all residual lengths are at least c, and at E−1 the α=β=a pair is still missing. Subtracting survivor polynomials therefore gives 2z+z² at E−a+1 through E−1 and z at E; includes a=2. Inspected the two frozen checkers without executing them. Independent `python3 /workspace/replay/check_assignments.py 2` shifts the two arm bitfields and directly updates the hub for every labelled non-all-one state at 2≤a≤7, verifying extinction and zero weights in every claimed shell. This is corroboration, not the all-size proof.

## originality

PASS

The supported distinct claim is the complete late-time initial-zero-weight profile for consecutive shared-hub cycles. The walk/AND correspondence, numerical semigroup conductor and constant attractors are not new. Neither attractor results on the identical graph nor bounds on the exponent determine the missing-predecessor sets with their source multiplicities. The closest indexed comparison for a=2 agrees at the terminal count but has inaccessible full text and only 2/3-cycle topology in its summary. The available one-bridge result treats a different dynamics and gives different shell counts. No checked statement implies the infinite-family refinement; priority is not asserted.

## value

PASS

For a standard strongly connected conjunctive network, the exact population and zero weights of the longest-delay states are information not supplied by an exponent or attractor theorem. The result explains why only a small number of configurations can attain those times and why the late population is restricted to specific singletons and pairs. The uniform terminal size-three shells and sharp last singleton are meaningful natural transient invariants, not just measurements at a small size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
