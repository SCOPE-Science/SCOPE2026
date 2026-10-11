---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For the rearrangement-invariant Lorentz plane, signed permutations make the optimal Euclidean pullback circular. On the Euclidean unit circle in the first octant, F(s)=(1+omega s^q)^(1/q)/sqrt(1+s^2), and F'/F has the sign of s(omega s^(q-2)-1). For 1<q<2 this gives the unique interior maximum s_*=omega^(1/(2-q)). The endpoint minimum switches exactly when (1+omega)^(1/q)/sqrt(2)=1, i.e. omega=2^(q/2)-1, yielding the two stated branches. Boundary agreement is exact.

## originality

FAIL

The exact profile is a routine implication of a broader planar distance-ellipsoid theorem. Grundbacher's Corollary 2.11 makes the distance ellipse unique for every planar symmetric body; the Lorentz unit ball is invariant under all signed coordinate permutations, so that ellipse must be a circle. The remaining calculation is the direct one-variable radial profile of the defining norm, with a single derivative and endpoint comparison. The exact-object literature already studies precisely this radial family and its critical quantities for other geometric constants. Under the required implication standard, a special-family radial evaluation mechanically following a dominating optimizer theorem is covered even if the Banach–Mazur formula was not printed verbatim.

## value

FAIL

The family is mathematically natural, but after the general uniqueness/symmetry result the submitted theorem is a straightforward one-variable derivative and endpoint switch. Under the stated value bar this is a routine specialization rather than a new structural lemma or difficult exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
