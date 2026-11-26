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

Riemann–Hurwitz gives 2g−2=6 and the three-branch-point bound d≥2g+1 is attained. For a fixed labeled target, connected covers correspond to simultaneous conjugacy of triples of full cycles with product one; one full cycle already implies transitivity. Fixing σ reduces equivalence and deck groups to the action and stabilizers of C₉. The full-cycle character sum uses only hooks and evaluates to 8064 admissible choices. For σ³, the centralizer acts on three residue blocks by a block permutation and three translations mod 3; both τ and στ require the forward block cycle, and the total shift must be neither 0 nor −1. The nine translation triples summing to 1 give exactly nine fixed choices. For any generator of C₉ the fixed choices are σ¹, σ⁴, σ⁷. Thus the orbit counts for deck orders 9,3,1 are respectively 3, (9−3)/3=2 and (8064−9)/9=895. In the independent replay each admissible second cycle is represented by its displacement word, with simultaneous conjugation reduced to cyclic word rotations. Canonical words yielded exactly 900 and the same order split.

## originality

FAIL

Giorgetti–Walsh (2018), Appendix B.5, explicitly tabulates 900 unrooted sensed hypermaps of genus 4 with 9 darts and 1 vertex, 1 hyperedge, 1 face. Their ordered-permutation equivalence is precisely the frozen fixed-branch correspondence. The deck split is then forced by that table and Djounvouna's exact mass 896 and three cyclic covers, since deck orders divide nine. The submitted calculation is correct but its stated output is covered.

## value

FAIL

The exact census of this extremal passport is intrinsically motivated, but the frozen finding recomputes a published census. Its apparent refinement is a two-equation consequence of existing mass and cyclic counts, and the proof does not claim any new arbitrary-degree result or other noncovered invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
