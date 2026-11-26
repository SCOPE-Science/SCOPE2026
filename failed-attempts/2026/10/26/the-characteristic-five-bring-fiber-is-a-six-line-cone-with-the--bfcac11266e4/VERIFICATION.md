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

PASS

For the fiber of the specified equations (not stable reduction), the affine cone ring is k[a,b,c,t]/(Q,T), with Q the nonsingular ternary quadratic and T the product of the three displayed linear forms up to a unit. They have no common factor, and the six rational directions exhaust their degree-six transverse intersection. The complete intersection has no embedded components and is generically reduced, hence reduced including at the apex. Independently, Newton's identities give the coordinate-root polynomial U^5+e4 U-e5; either e4=0 and all coordinates coincide, or its five distinct roots are a translate of an F5 line. This recovers precisely the permutation directions modulo affine changes. Away from the vertex the lines are disjoint and smooth; at the vertex the cone has multiplicity six and six normalized branches. The Hilbert polynomial is 6n-3, and the normalization sequence gives delta=4+6-1=9; the rational point count is 1+6q. The permutations preserve the quotient conic and act transitively with affine order-20 stabilizer. The kernel is trivial (no nontrivial S5 normal subgroup fits inside it), so the conic action is the full PGL2(F5), sharply three-transitive. Direct small-field reproduction at /workspace/branches/independent_bring.py enumerated 31 points in the original coordinates and 120 ordered triple images; the universal and scheme-theoretic assertions use the proof, not the enumeration. The phrase 'literal integral closure' in the assumptions is technically inapt; the displayed equations and explicit base change unambiguously define the intended model.

## originality

FAIL

A distinct earlier-catalogued Resultary record treats the same power-sum special fiber over Z5, proving the same reduced concurrent F5 lines, genus, normalization defect and component stabilizer, and additionally determines the conductor. All-extension counts, vertex multiplicity and the description as the sharply three-transitive conic action follow from this coverage. This is a failure of distinct mathematical content, not a claim to know authorship or exact priority from catalogue dates.

## value

FAIL

The degeneration and component action are intrinsically useful, but the frozen result adds no substantive invariant to the matching scheme, singularity and action calculation. Its additional all-extension count and multiplicity are direct consequences of the known union of rational lines through a single vertex; sharp transitivity just makes explicit the already identified degree-six action.

The dated certificate retains the supplied scientific assessment, sources and limitations.
