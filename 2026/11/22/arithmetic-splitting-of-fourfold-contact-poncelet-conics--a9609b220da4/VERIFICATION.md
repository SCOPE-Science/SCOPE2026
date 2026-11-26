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

The unique geometric contact point is rational by Frobenius. Normalize the smooth conic with that point to the Veronese model; restriction of the other quadratic form is a nonzero multiple of s⁴, and the restriction kernel is exactly the defining line of quadratic forms for C. Smoothness makes the coefficient of that defining form nonzero. This gives D=XZ−Y²+λX², λ≠0, with determinant 1/4. Every projectivity preserving C and P induces an affine map w↦aw+b; the restriction to C is faithful (four points on a conic form a projective frame), and the displayed Veronese action realizes these maps. It scales the defining form by a², giving exactly two square classes and stabilizer order 2q. Independently, a finite chord has Z=(u+v)Y−uvX; on X=1 its intersection with D has discriminant (u−v)²+4λ. A chord through P has Y=wX, and restriction of D to it is X[Z+(λ−w²)X], with two distinct intersection points. Thus the graph is edgeless or exactly the coset cycles of h𝔽_p for h²=−4λ, with P isolated. This includes p=3, rationality of the unique tangency on a rational tangent line, and counting modulo the two orientations and rotations. The sign over extension is the n-th power of the original sign, since 1+q+⋯+q^(n−1) has parity n. Orbit–stabilizer gives the claimed sizes and equal census. The frozen verification file and both scripts were inspected, not executed; their finite graphs supplement the all-fields argument.

## originality

PASS

The supported distinction is the classification and exact census of ordered rational projective pair-orbits and the identification of their graph/count behavior as an arithmetic orbit invariant. The ground-field normal form, geometric additive porism and incidence discriminant are prior ingredients, and the rational graph count can be extracted from the known incidence equation plus elementary finite-field descent. It is not credited as an independent new tangency equation or porism. The closest finite-field pencil table does not refine the ordered pairs by rational projective orbit. No claim of historical priority is made.

## value

PASS

The invariant of interest is the rational projective type of the ordered pair. A fixed known geometric p-period can arise both from pairs with no rational edge and from pairs with all affine points in rational cycles. Counting the two classes of pairs and identifying that invariant with the graph and its extension behavior gives a useful arithmetic refinement of geometric porism and the finite-field pencil census. Value is not assigned merely for rederiving the geometric period or the known pencil table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
