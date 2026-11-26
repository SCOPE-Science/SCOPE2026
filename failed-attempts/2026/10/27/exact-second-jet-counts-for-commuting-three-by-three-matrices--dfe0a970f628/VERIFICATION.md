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

For 3×3 matrices, rational canonical form gives scalar, cyclic, or scalar plus rank one. The scalar shift in the last case is unique by the rank inequality. For C(N) with rank N=1, the nonzero-trace form splits as M2(k)⊕k. The trace-zero form N=E12 gives the displayed five-parameter algebra, and its commutator matrix on the three noncentral coordinates has determinant zero and a nonzero square minor off the center. This gives common centralizer dimensions 3, 5, 9 in all characteristics. Trace duality for the linearized commutator gives tangent dimension 9+d; the underlying dimension 12 at geometric points makes d=3 smooth for the equation scheme. The reduced nonsmooth support is parametrized by scalar translations and nonzero decomposable 2×3×3 tensors, with scalar pairs as limits. The rank-one minor on the open set where suitable off-diagonal entries are nonzero recovers the scalar shifts rationally; this confirms birationality, dimension 8, and irreducibility, not a scheme structure assertion. The projective rank-one directions count L, giving U and the noncyclic single-matrix count S; summing partner counts gives T. Every smooth fiber has q^24 lifts. At (N,0) the trace obstruction for A1 at fixed B1∈C(N) has rank dim[B1,C(N)], 0 or 2, and any admissible first-order pair has q^14 completions. Scalar-base lifts are Tq^18 per pair. These give the stated formula. An independent bit-matrix enumeration over F2 gives strata (6864,588,4), T=7456, and for both E11 and E12 exactly 4 choices of B1 with 512 admissible A1 and 28 choices with 128 admissible A1. It gives J2(2)=177234509824. The frozen VERIFICATION.md and verify_jet3.py were inspected, not executed; their other-field tests are bounded recorded corroboration.

## originality

FAIL

The earlier Avni–Klopsch–Onn–Voll shadow and branching tables mechanically determine the ordered all-matrix count at every length, not just invertible commuting pairs or simultaneous-similarity orbits. Their actual tables also mechanically determine the putatively new d=5 per-base count. The same arithmetic written via second-jet obstruction is a different proof, not a distinct exact invariant; the base stratification is covered by earlier centralizer classification. The failure is demonstrated implication, not an unavailable source or a claim of verbatim duplication.

## value

FAIL

This is a natural arithmetic invariant and the direct proof explains the exceptional lifts well, but both the claimed numerical invariant and the exceptional fiber are elementary weights of known stronger exact tables. The remaining geometric description is a direct repackaging of the known base centralizer types via nondegenerate trace duality and rank-one tensor parametrization. No independently useful new geometric or arithmetic remainder is established: in particular, there is no singular scheme calculation, new higher-order law, or distinct obstruction result beyond the existing centralizer ranks. No repair is warranted for the stated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
