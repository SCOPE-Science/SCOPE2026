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

# Reproducibility and scope of verification

Run `python verify.py` in an environment with Python 3 and SymPy. The checker constructs all \(4ab\) signed rays and \(2^a+2^b\) maximal cones for parameter pairs \((1,2),(1,3),(1,4),(2,2),(2,3),(3,3)\), independently computes rational Cartier compatibility ranks, and computes the integer Smith invariants of the normal-ray matrix and its all-one augmentation. It also obtains the top self-intersection by exact finite differences of lattice point counts, independently of the beta-integral volume proof. Successful execution ends with `COMPLETE_BIPARTITE_TORIC_LATTICES_OK`.

The finite checks are sanity checks only. The all-parameter proof is the independent facet/maximal-cone construction, the integral Cartier-support calculation (including one-element part cases), the two mod-two Smith arguments, and the volume integral in RESULT.md. The case \((1,1)\), alternative lattice saturations, nonnormal projective embeddings, and singular-locus classification are outside the theorem. No independent audit has been carried out.
