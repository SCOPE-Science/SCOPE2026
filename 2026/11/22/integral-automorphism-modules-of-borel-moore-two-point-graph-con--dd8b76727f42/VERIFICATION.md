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

# Reproducible verification

Run `python3 verify_bm.py` with Python 3 and SymPy. The script constructs a relative symmetric-square cellular chain model for six small graphs, checks \(\partial_1\partial_2=0\), rational second Betti numbers, and first mod-two Betti numbers. It additionally computes exact Smith normal forms for four graphs and compares alternating cellular Lefschetz traces of six graph automorphisms to the exterior-square trace formula. The expected terminal line is `VERIFY_OK`.

These are exact finite checks with no unreported numerical approximations. They do not prove the asserted theorem for all graphs; the compact-pair homotopy reduction, multiplication-by-two diagonal and natural cross-product construction in RESULT.md provide that proof. Published first Betti/torsion group values are credited separately; the new claim concerns integral naturality and automorphism actions. There has been no independent mathematical audit.
