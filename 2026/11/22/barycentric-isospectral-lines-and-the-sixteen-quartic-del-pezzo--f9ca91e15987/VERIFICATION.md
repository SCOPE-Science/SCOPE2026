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

For n≥5 and any simple complex spectrum, Lagrange interpolation cancels moments through degree 3, so the skew matrix N=u(Du)^T−(Du)u^T has N²=NDN=0. Orthogonal conjugation by I+tN gives the exact commutator direction for all t. A three-column Vandermonde factorization gives rank 3 and the degree-4 residue gives Q²=uu^T for n=5 and Q²=0 for n≥6, with Qu=0 in both cases. Nonzero off-diagonal entries and a triangle comparison rule out projective sign coincidences other than global reversal. Distinct eigenvalues imply smoothness of the two-quadric surface; its classical sixteen lines already exhaust the sixteen distinct barycentric images, and commutation by D is an invertible diagonal rescaling in Plücker coordinates. No classification of the whole isospectral cone is needed. The rational and modular evidence was inspected, not run, and is supplementary.

## originality

PASS

The strongest inspected prior results give generic higher-dimensional existence and classical common-isotropic geometry, including the degree-four del Pezzo line count and sign action. They do not supply the stated all-simple-spectrum symmetric isospectral orbit, its precise Jordan-type transition, or the Plücker-commutator realization. The pass is for this spectral construction and its refinements, not for generic existence or the sixteen-line classification.

## value

PASS

For the natural rigidity-versus-existence problem this gives a uniform, directly computable nontrivial orbit even at nongeneric simple spectra. The exact rank and abrupt change from Jordan type (3,2) to square-zero distinguish the affine direction itself, and the geometric realization explains the distinguished sixteen in the first nonrigid dimension. This supplies more than generic existence or a routine enumeration of del Pezzo lines.

The dated certificate retains the supplied scientific assessment, sources and limitations.
