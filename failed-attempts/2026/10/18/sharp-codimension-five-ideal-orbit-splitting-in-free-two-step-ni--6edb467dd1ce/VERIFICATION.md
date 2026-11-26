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

An ideal with projection U and central part W must and need only satisfy U∧V⊆W. The quotient of the exterior square by U∧V is Λ²(V/U), so the two Gaussian factors count U and W, and each graph of U→Z/W contributes one lift, giving q^((d−k)δ). Codimension is k+δ. An automorphism induces g on the abelianization, Λ²g on the derived algebra, and an arbitrary central shear on V. Such shears realize every difference of graph maps, and the stabilizer of U induces the full GL(V/U). For k≤2 there is no nontrivial subspace choice within a fixed defect; for k=3 the exterior square is the dual up to a determinant twist and is transitive on subspaces of fixed dimension; δ=0 is always transitive. Enumerating admissible pairs for k+δ≤5 leaves only (4,1) to check. Its annihilator is a one-dimensional subspace of alternating forms, and splitting off a pair with nonzero pairing gives the rank-2/rank-4 normal forms in every characteristic. A rank-2 projective form is the pullback of the unique projective area form on the quotient by its two-dimensional radical, so precisely [4 choose 2]_q have rank 2, with [6 choose 1]_q−[4 choose 2]_q of rank 4. Multiplication by the number of U and graph lifts proves the orbit sizes. The two other codimension-five profiles (5,0) and (3,2) are transitive, yielding the stated counts. The bundled checker covers small prime-field cases, not a proof over every finite field.

## originality

FAIL

The frozen fixed-defect enumerator is stated in equivalent parameters in distinct Resultary record 6f754a2fffbb. The first split and low-codimension orbit list are direct consequences of the classical low-dimensional class-two quotient classification: for this free algebra, two embedded ideals with isomorphic quotients are conjugate by lifting an isomorphism on generators. The embedded sizes then follow from the covered graph-lift count and a Gaussian count of possible radicals for alternating forms. The verified overlap and these implications leave no distinct mathematical claim established at the stated scope. The later catalogue date of the exact enumerator is not a finding of historical precedence.

## value

FAIL

The embedded counting question is natural and the account is useful exposition, but the proposed cutoff in this free presentation is read off from the low-dimensional quotient classification after the generator lift. The embedded sizes require only the standard radical and graph counts, and the exact refined enumerator is already available in the compared corpus. The submission does not isolate an independently needed exact invariant beyond those mechanically implied ingredients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
