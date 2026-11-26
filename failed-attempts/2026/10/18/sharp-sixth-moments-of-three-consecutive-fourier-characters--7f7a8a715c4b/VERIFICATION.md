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

Probability Haar orthogonality squares the cube coefficients grouped by character order, and the triangle inequality in each residue bounds the complex polynomial by its coefficient magnitudes. /workspace/replay.py (three_modes, Python 3 + SymPy) independently expands the cube and verifies the five multivariate identities and derivative numerators. With fixed endpoint energy u>0 and middle energy v≥0, each alias correction is nondecreasing in the endpoint product p and the unaliased positive p² coefficient gives strict increase, so both endpoints must have equal nonzero magnitude. The u=0 quotient is 1 and not maximal. The normalized derivatives change sign once from + to − on t>0: for m=5 Descartes plus opposite endpoint signs gives exactly one positive root, and for orders 6 and ≥7 the equations are increasing quadratics in t² with negative constants. Orders 3 and 4 give t=1; the endpoint t=0 and limit 1 at ∞ are not maxima. Strictly positive optimal moduli mean the triangle condition in cube degree 2 is ac/b² positive, forcing affine phases. All cube coefficients are then nonzero with degree-k phase factor ζ^k; a pair separated by m for 3≤m≤6 forces ζ^m=1, and that condition suffices for all pairs. At order at least seven or infinite there is no such pair. Zero is trivially equality outside the listed nonzero cases. The argument holds for disconnected compact groups too. The packaged checker was inspected, not executed.

## originality

FAIL

Resultary 382775ed6a3d treats a stronger finite Fourier-coset problem; its H={1} specialization gives every finite character-order case including all equality phases. Passing to arbitrary compact groups produces no distinct regime: Haar pushforward along χ is uniform on the finite image or Haar on the circle, and at infinite order the degree-six cube norm is exactly its seven-point quadrature for every coefficient vector. The compact-group extension and all nonzero equality cases therefore follow directly. This is coverage, not a conclusion about authorship or priority.

## value

FAIL

The torsion-sensitive classification would be a natural exact invariant if uncovered, but is present in a stronger statement. Compact-group pushforward and a degree-six quadrature identity give the full extension without an independent extremum or rigidity result. There is no distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
