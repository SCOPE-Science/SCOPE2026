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

Reassessed the corrected theorem. With the conic class at zero, E_i at the five weight-four words u_i and H−E_i−E_j at u_i+u_j, the integral pairing agrees exactly with adjacency at binary distance four. A vertex and its five-neighbor permutation determine a graph automorphism, giving the even-affine W(D5) group. In any four-cycle the directions must repeat in opposite pairs because the only nonempty relation among distinct u_i is the sum of all five. This gives 10·4=40 squares. The sum D of the four components has D²=D·(−K)=(−K)²=4; the Hodge index theorem and the free blowup Picard lattice give D∼−K. Thus both finite Galois sets descend to finite étale schemes of the indicated degrees, also in characteristic two. Independent `python3 /workspace/reviews/reproduce_2_3_5.py` builds every square from the integral lattice, classifies all 1920 elements by signed cycle data (no splitting because an odd coordinate cycle allows adjustment of the conjugating translation to even parity), and matches all 18 class sizes, both spectra and six counts against the CSV. It gives 12 line spectra, 16 square spectra, 18 joint spectra, and 13,17,18 signatures at the three cutoffs. The unique degree-two collision is ((0,1),(4,1)); the 80-element class has square spectrum 1¹3¹6⁶ and third-degree pair (0,4), and the 160-element class has spectrum 1¹3⁵6⁴ and pair (0,16). The total finite étale zeta functions follow from the cycle factors. Neither the proof nor the repair asserts realization of all abstract types over a fixed field.

## originality

PASS

The repaired classification is for the joint square/line arithmetic of a quartic del Pezzo, not the known configuration of forty geometric four-line sections or the already computed line-only spectrum count. The strongest verified broader classification uses a different output invariant (all Zariski chambers); the cubic-surface six-count version uses a different group and actions. Direct comparison did not establish coverage of the exact joint inverse statement; this is a bounded priority judgment.

## value

PASS

The two low-degree schemes are defined by canonical geometry rather than selected after computing class separation. The exact sharp cutoff explains how combining genuinely insufficient individual zeta functions identifies the Weyl type, and identifies the precise two-degree obstruction. This is useful for replacing full incidence permutations with point counts and remains valuable with the corrected orbit-class size, without claiming new geometry of the 40 squares or field-by-field sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
