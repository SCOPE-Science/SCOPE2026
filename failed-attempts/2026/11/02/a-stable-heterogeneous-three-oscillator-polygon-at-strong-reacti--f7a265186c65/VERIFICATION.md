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

Sum(w)=0 and the squared radii are (1,3/2,2); the mean-field form then gives frequency ω−3 Im(C)=1 and no radial drift. The strict triangle inequality holds along the ray since the largest squared radius is less than the sum of the two smaller squared radii. At ε=1 the real co-rotating Jacobian is the block diagonal matrix with blocks −2v_j v_j^T plus a rank-two mean term (v_j=(Re w_j, Im w_j)). The determinant lemma reduces its characteristic polynomial to a 2×2 determinant and gives the exact frozen polynomial. The Routh first column is (1, 15/2, 4063/240, 353677/16252, 2996769579/90541312, 3519/64); only common phase is neutral. Along the small-ε branch, the three zero-coupling phase directions are semisimple and split at first order by the projected phase coupling. Its kernel includes collective rotation, its trace is 3/4, and its second elementary symmetric sum is |1/4+i|² times the sum of squared pairwise phase sines, which is strictly positive by noncollinearity. Hence exactly two eigenvalues have positive real parts at sufficiently small ε and the three radial eigenvalues stay negative. Orbital exponential attraction at ε=1 is local in the full state space. Independent bounded replay: python3 /workspace/review-evidence/reproduce.py 5 (SymPy). The uploaded script and saved outputs were inspected, not executed.

## originality

FAIL

The headline existence claim that three active oscillators with strictly increasing, linearly spaced growth rates can support an attracting zero-mean triangle, with weak-reactive instability, is already established in the same dynamical model by Resultary 3e86ca58217e, with an exact global transition on a different coupling path. The fixed-ray qualitative claim is also not a new mechanism: the exact three-node homogeneous window of 807118a3b756 applies at the frozen coupling and the mean growth rate, hence ensures attracting heterogeneous triangles on nearby strictly spaced triples by hyperbolic continuation. The elementary small-coupling phase instability persists for these triples by the two nontrivial first-order phase eigenvalues. This comparison does not claim that another record states the exact rates (7/4,9/4,11/4) or certifies the exact same full ray. It credits equivalent qualitative coverage without making a priority inference from same-day dates.

## value

FAIL

Three-active heterogeneous stabilization and weak-to-strong changes are meaningful but already demonstrated. The surviving exact quintic at one finite parameter tuple supplies no independently motivated spacing, boundary, uniform criterion, or unresolved benchmark: the selected spacing d=1/2 is not identified as structurally distinguished, and ratio four already belongs to an open stable example class. A different parameter tuple plus an exact certificate does not answer a new scientific question of comparable scope. No corrected valuable claim is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
