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

# Reproducible checks

Run `python3 verify.py` from the folder containing the extracted files. The checker uses only Python's standard library. It reconstructs the sextic polynomial, derives its derivatives, checks all six singular-representative Hessians, enumerates every point of projective three-space over \(\mathbb F_5\) and two presentations of \(\mathbb F_{25}\), and reproduces the relevant point counts. Its expected final line is `VERIFY_OK`.

For the extra degree-three extension check, compile and run `g++ -std=c++17 -O2 verify_f125.cpp -o verify_f125 && ./verify_f125`. The C++ code constructs \(\mathbb F_{125}\) as \(\mathbb F_5[t]/(t^3+t+1)\), enumerates all normalized projective points, and must report `F125 count 17251 predicted 17251`. The nonzero determinant list in the polynomial verifier is the finite calculation needed for the ordinary-node assertion.

The supplied `verification_results.txt` records the actual successful executions. These finite checks cover projective point enumeration for the stated extension fields, not infinity of all extensions. The all-extensions statement additionally requires the proof from rational double points, Noether's formula, Weil purity, and the Lefschetz trace formula. The bibliographical comparison does not constitute an independent scientific audit.
