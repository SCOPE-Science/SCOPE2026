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

# Reproducibility and scope

The accompanying standard-library-only program `check_flux.py` uses a boundary-seam construction of periodic link phases, computes every oriented plaquette directly, and compares the total plaquette energy against the closed form in `RESULT.md`. Execute `python check_flux.py`. The actual output was:

```
PASS: 5892 oriented plaquettes; exact global energies for all tested dimensions and flux choices
```

Tested side triples are `(2,2,2)`, `(3,3,3)`, `(3,3,4)`, `(3,4,5)`, `(2,3,5)`, `(5,5,3)`, `(2,2,3)`, `(2,3,3)`, and `(3,5,7)`. Every eligible odd-plane sign assignment was tested. Arithmetic checks use complex double precision and a maximum absolute tolerance of \(4\times10^{-10}\) on the total energy.

The proof is fully analytic. Its indispensable points are exact cancellation of link factors around the periodic plane; the odd-plane angle-product and strict averaging lemma; a seam-gauge construction compatible with all three fluxes; a bounded-increment Bianchi argument for transverse rigidity; and the classification of flat holonomies. The finite checks confirm conventions and seam signs only; they do not exhaustively prove the theorem. No independent audit has been carried out.
