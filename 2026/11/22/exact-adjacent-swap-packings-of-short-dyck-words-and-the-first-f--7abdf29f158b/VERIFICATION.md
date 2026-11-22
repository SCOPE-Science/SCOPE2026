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

The two standalone Python programs use only the standard library. Invoke them from the directory containing `certificates.json`:

```sh
python verify_rational.py
python verify_classification.py
```

`verify_rational.py` regenerates Dyck words by exhaustive binary tuples, constructs all outputs from the identity and one adjacent swap of unlike symbols, and checks every stored rational primal and dual inequality for semilengths one through five. It also checks each listed codebook and that the two rational objectives agree. `verify_classification.py` uses a different recursive Dyck generator and direct set-intersection compatibility test, enumerates all maximal cliques, verifies the entire eleven-codebook list, and checks the nine reflection-complement fixed cases and the noncontainment of the deletion and adjacent-swap conflict graphs.

The finite domain, exact rational certificates, and exhaustive clique enumeration substantiate the claimed results. No claim is made about semilength six or greater, nor about external mathematical certification.
