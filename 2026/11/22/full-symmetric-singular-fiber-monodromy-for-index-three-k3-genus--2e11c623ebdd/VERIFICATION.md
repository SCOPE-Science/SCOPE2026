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

# Verification record

The mathematical argument is in `RESULT.md`. The independent tasks within the argument are: (i) degree 12 of the reduced ternary-cubic discriminant and pullback to degree 24; (ii) transversality and nodalness on a nonempty coefficient open; (iii) irreducibility of one- and two-marked singular-point incidences; (iv) a simple quadratic collision producing one transposition; (v) the group-theoretic inference; (vi) rank-two intersection-lattice divisibility for the index-three pencils.

`verify.py` runs without external data using Python and SymPy, checking the intersection numbers, primitive isotropic rays, fiber-degree gcds, 24-degree arithmetic, a sample independent binary-quadratic evaluation matrix, and the simple critical-value local model. The checker is diagnostic for finite symbolic identities, not a certificate of universal irreducibility, Picard genericity or publication novelty. The universal geometric steps rely on the explicit proofs in `RESULT.md` and on the cited source's Picard-lattice identification. Independently verified formal certificates have not been produced.
