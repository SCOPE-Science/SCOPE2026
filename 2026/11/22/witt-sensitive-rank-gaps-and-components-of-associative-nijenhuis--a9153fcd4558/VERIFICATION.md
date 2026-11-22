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

# Reproducibility and proof boundaries

Run the bundled `verify.py` using Python 3.10 or newer (standard library only); the expected terminal marker is `ISOTROPIC_NIJENHUIS_VERIFIED`.

The program exhaustively evaluates the original associative Nijenhuis identity on all linear endomorphisms of two explicitly specified three-dimensional algebras over \(\mathbb F_3\) and one over \(\mathbb F_5\). It independently checks every candidate three-by-three generator block over \(\mathbb F_3\), matching the theoretically derived rank polynomial, and checks the isotropic subspace numbers for split and nonsplit four-dimensional quadratic forms. It directly checks 3,000 further higher-dimensional original identities. All tested comparisons passed.

The general classification is proved by forcing annihilator preservation and reducing to the total-isotropy condition. The exact polynomial follows from subspace Möbius inversion; the reduced component count follows from the orthogonal-Grassmannian incidence map. The finite tests do not certify algebraic-geometric reducedness, infinite quantifiers, claims of priority, or any independent mathematical validation. The result explicitly limits its geometry to the reduced solution variety and excludes characteristic two.
