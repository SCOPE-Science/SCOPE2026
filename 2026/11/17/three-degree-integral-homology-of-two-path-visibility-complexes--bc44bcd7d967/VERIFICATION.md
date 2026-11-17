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

# Verification

The standalone `verify.py` uses two different finite constructions: a direct graph-neighbor count of disjoint clear shortest paths for every vertex subset, and an independent explicit Alexander-dual simplicial cover. They agree exactly for shore sizes 5 and 6. It computes all mod-two simplicial boundary ranks and compares every reduced Betti number to the claimed formulas. The checked complexes contain respectively 750 and 2076 nonempty Alexander-dual faces. `verification_output.txt` records the actual executable output and is reproduced by `python3 verify.py`.

The proof of integral torsion-freeness is structural: the Mayer–Vietoris map is explicitly identified with a primitive augmentation sublattice. Finite mod-two calculations do not constitute integral or infinite certification. The theorem does not assert a wedge-of-spheres homotopy type.
