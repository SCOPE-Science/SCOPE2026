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

# Reproducibility and mathematical limits

Run `python3 verify_family.py` and `python3 verify_acyclohedron.py` using Python 3 and its standard library, from the extracted package directory. The first script exhausts 1024 edge-cube sign assignments at order five and 32768 at order six and checks the exterior-Gram projection identity, tournament imbalance and outer contact counts. It prints `n=5` with facet shell total 74, inradius squared 3.75, circumsphere squared 12.5 and 24 contacts; `n=6` with facets 394, inradius squared 4.5, circumsphere squared 21 and 2640 contacts. The second independently enumerates all candidate facet normals and exact squared facet distances in the order-five original simplicial-boundary realization, recovering the three shell multiplicities 20, 30, 24. All computations use integer or exact rational arithmetic.

The arbitrary-order theorem requires the exterior-Hodge Gram calculation, minimal circulation supports, tournament imbalance parity and symmetric-group irreducibility proved in RESULT.md. Neither finite enumeration nor a successful run is an infinite proof. Completeness of mathematical-historical priority is not machine certifiable. No independent mathematical audit has been performed.
