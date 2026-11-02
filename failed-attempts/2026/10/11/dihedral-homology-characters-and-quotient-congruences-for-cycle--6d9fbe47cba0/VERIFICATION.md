---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The infinite proof is internally valid: established Ind(C_n) suspension recurrence fixes the sole homology degree q_n and its rank for n>=3, including initial n=3,4,5. For any group element, each invariant independent face with t labels and u occupied vertex orbits contributes (-1)^(u-1) to the reduced simplicial Lefschetz trace, including the empty face -1, so L(g)=-I(B_g,-1). Rotations produce C_d with d=gcd(n,a), with d=1,2 handled separately. Reflections produce P_((n-1)/2), P_(n/2+1), P_(n/2-2) according to parity and axis type. The exact P recurrence P_m=P_(m-1)-P_(m-2) yields period six, the cycle polynomial produces Q, and rational invariant averaging over D_n after barycentric subdivision gives the cyclic and dihedral congruences. This is a uniform analytic proof, not a finite-experiment inference. Independently reimplemented signed face traces agreed with 150 group elements n=3..12; the sign-twisted prior representation agreed with all 360,594 rotations/reflections n=3..600 and quotient averages n=3..24. These experiments supplement, not replace, the all-n derivations.

## originality

FAIL

Decisive 2014 prior coverage via exact D_n-equivariant combinatorial Alexander duality. The minimal nonfaces of Ind(C_n) are the n adjacent edge-label pairs. Their complements are exactly the cyclic length-(n-2) facets of N(n,n-3), so Ind(C_n)^vee = N(n,n-3) as D_n-simplicial complexes, not merely up to homotopy. The signed complement chain map of Björner–Tancer yields over Q a natural sign-of-permutation twist of the dual nerve cohomology. The 2014 nerve homology-representation classifications then imply the submitted complete rotation/reflection traces in all dimensions. In the divisible-by-3 case the nerve top module is the 2-dimensional augmentation representation of the three cyclic generators, with rotation traces 2 or -1 and reflection trace zero; in the other two congruence classes its one-dimensional character has trivial rotations and reflection sign (-1)^(floor(n/3)). Tensoring by the ambient n-vertex permutation sign reproduces all stated period-six P/Q character formulas and cyclic/dihedral invariant averages. Thus the full result is a prior corollary even without identical cycle-matching terminology. Originality is FAIL regardless of exact database string matches.

## value

FAIL

Complete natural dihedral-character and orbit-space homology tables are intrinsically motivated invariants. However, here all of those tables follow from published 2014 parametric nerve representations via classical signed combinatorial Alexander duality. The submitted signed Lefschetz proof may be useful as an independent exposition, but it proves no new invariant, classification, or structural obstruction once the exact prior implication is recognized. Correctness, finite verification and alternative proof presentation do not establish an original mathematical contribution. No viable novel final claim or substantive repair was supplied; rejecting the original must preserve all original science.

The dated certificate retains the supplied scientific assessment, sources and limitations.
