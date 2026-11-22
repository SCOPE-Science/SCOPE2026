---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and exact checks

Run `python CHECK.py` from this package; it uses SymPy. It checks substitution of the invariant quotient equation into the elliptic model, the exact swap action, the quotient invariants, the factorization and orders at finite and infinite discriminant zeros, smoothness at the two fixed fibers, and the rational two-torsion sections. The checker has been run successfully on the embedded copy of the script.

The infinite/geometric assertions are justified by the explicit field identities plus the separate proof of minimal K3 identification, Kodaira valuations, two smooth branch fibers, rationality, full constant-curve descent, and the Nikulin fixed-locus theorem. The algorithm does not claim to enumerate all complex points or certify external sources.

The four points of the two-elliptic fixed-locus cross-check are the four simple roots of \(zw(z^2+w^2)\). Riemann–Hurwitz gives elliptic quotients of each genus-three plane section; they become disjoint after resolving the quotient nodes, independently confirming the model's two fixed fibers.

The statement is new work on this explicitly named surface, not a reclassification of all extremal rational elliptic surfaces. No independent audit has been performed.
