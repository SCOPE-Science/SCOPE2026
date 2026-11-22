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

The theorem's infinite assertion is proved by a singular-chain comparison and two long exact sequences in `RESULT.md`, not by a search over curve coefficients. Reconstructible steps are: (1) the real and complex normalization-circle exact sequence, (2) the order-two torsion image derived from one real bounding chain and one complex normalization hemisphere, (3) the parity of the kernel and the index of the free boundary image, and (4) the cokernel quotient exact sequence. The key nonstandard equality is the absolute homology identity that complex conjugation sends the class \(k[\ell]\) of the closed difference chain to \(-k[\ell]\) while the two conjugate hemispheres differ by the degree-\(d_i\) fundamental cycle. It forces \(2k=-d_i\).

To reproduce the supplementary integer-module checks, run `python checker.py` with Python 3 and no external dependencies. The script enumerates a total of 1,290 compatible Smith-determinantal-divisor module models, verifies that the half-degree torsion classes generate exactly the order-two subgroup, and checks the proposed cokernel indices. The model tests do **not** independently verify the topology of all real arrangements or decide the unresolved extension structure for the nontrivial embedding-character case.

The examples with two conics are sourced from Yoshinaga's Example 4.2, but the integral conclusions follow from the present general theorem. Existing work on the rational chamber map is credited; no publication-priority guarantee is asserted. There has been no independent audit.
