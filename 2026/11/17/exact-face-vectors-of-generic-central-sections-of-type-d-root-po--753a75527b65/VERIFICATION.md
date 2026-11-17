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

# Verification and reproducibility

The unrestricted proof uses the support-function description of \(D_n\), a complete three-type face classification, chamber sign invariance, and explicit binomial counts. None of these arguments assumes that finitely many dimensions establish the general theorem.

Run the embedded `verify_droot_sections.py` using standard Python 3, without downloads or nonstandard packages. Its checks independently generate all vertices \(\pm e_i\pm e_j\), obtain the complete face lattice from intersections of defining facet vertex sets, and find each face's dimension by exact rational elimination. For \(n=4,5,6\) it compares formula and face-crossing counts for six generic normals per dimension; it also checks the Euler relation. The command completed successfully with terminal marker `VERIFY_OK`, giving, respectively, section face vectors \((32,48,18)\), \((80,200,156,36)\), and \((160,560,756,424,70)\).

The \(n=4\) case is an already-known control and is not claimed new. Higher ranks, nongeneric normals, section volumes, and metric congruence are not covered by the finite verifier, nor asserted by the theorem where outside the hypotheses. This is same-model reproducibility evidence only; independent audit has not been performed.
