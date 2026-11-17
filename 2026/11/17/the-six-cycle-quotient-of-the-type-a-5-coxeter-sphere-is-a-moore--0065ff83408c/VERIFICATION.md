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

Run `python verify_cyclic6.py` with standard Python 3. The included `VERIFIER_OUTPUT.txt` is the recorded output of the exact program in this package. The program generates every nonempty chain of proper nonempty six-set subsets, forms orbits under all six rotations, checks the integer identity \(\partial^2=0\) on every quotient cell, and computes modular boundary ranks by column elimination for characteristics two, three, five and seven.

Expected dimensions of quotient chains: \((12,91,260,300,120)\). Expected Betti vectors: \((1,0,0,1,1)\) over \(\mathbb F_2\), and \((1,0,0,0,0)\) over each of \(\mathbb F_3,\mathbb F_5,\mathbb F_7\). Expected final line: `CYCLIC_SIX_SIMPLEX_QUOTIENT_CHECK_PASS`.

These modular calculations cannot exclude torsion of other prime orders or establish the homotopy type by themselves. The integer proof instead uses the explicitly defined lens-space quotient and the mapping-cone maps, with \(f_*\) equal to an isomorphism on \(\pi_1\) and multiplication by two on \(H_3\). No independent external audit has been performed.
