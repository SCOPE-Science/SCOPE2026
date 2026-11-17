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

# Reproducibility
Run `python3 checks/verify.py` from the directory containing the extracted embedded files. Python 3 standard library suffices; no external data or generated intermediate files are required. The verified output is `checks/verify_output.txt`.

The exhaustive checker independently constructs the voltage-derived covers; for every tested deck subgroup it enumerates the orbits of edges and **all** choices of orbit sets, and tests acyclicity both before and after taking the graph quotient. For each cyclic-deck element it additionally sums signed traces on all invariant oriented forest simplices, including the augmented empty face, then compares with the signed quotient Tutte value. A Klein-four cover independently exercises a noncyclic full subgroup and its three order-two subgroups.

These finite checks do not prove the general PL/homeomorphism theorem; the proof uses covering-path lifting and matroid shellability. The source theory of matroid shellability is arXiv:1410.3870. All computations are exact integers. The one-vertex case uses augmented reduced homology in degree \(-1\).
