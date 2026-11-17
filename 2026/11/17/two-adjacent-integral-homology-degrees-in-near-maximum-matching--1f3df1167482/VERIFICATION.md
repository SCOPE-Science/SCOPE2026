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

The proof is an integral Mayer--Vietoris argument comparing three canonical joins. The critical map \(\widetilde H_{2s-8}(R;\mathbb Z)\to\widetilde H_{2s-8}(P;\mathbb Z)\) is an isomorphism by naturality of the connecting homomorphisms on the common intersection, not inferred from finite experiments.

To reproduce the five finite-field sanity checks, run `python3 verify_homology.py` in the extracted package directory; it uses only the Python standard library. The output is preserved in `verify_homology_output.txt`. The code enumerates all permitted simplicial faces, forms all simplicial boundary matrices, and reduces them over \(\mathbb F_2\). It checks five even/odd cycle pairs. These tests verify only finite-field ranks for those five instances. They do not constitute integral torsion tests, all-length proof, or independent certification.
