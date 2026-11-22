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

# Reproducibility and verification

The proof is in `RESULT.md` and takes established integral chessboard-complex results as explicit premises. These standalone scripts check the new optimizer and shattering classification in finite cases.

1. Run `python3 VERIFY_PYTHON.py` (independent brute-force support enumeration and direct domination tests on the smaller boards). Compare with `CHECK_PYTHON_OUTPUT.txt`.
2. Compile `g++ -std=c++17 -O2 VERIFY_CPP.cpp -o check` and run `./check`. It checks every selected support of size at most five on the \(5\times5\) board, comparing traces of all optimum dominating sets against the stated row/column criterion. Compare with `CHECK_CPP_OUTPUT.txt`.
3. Run `python3 VERIFY_CHESSBOARD.py` with NumPy installed. It constructs the actual signed boundary maps for the \(5\times5\) chessboard matching complex, row-reduces over three prime fields, and reports field Betti numbers; compare with `CHECK_CHESSBOARD_OUTPUT.txt`.

The appearance of a characteristic-three anomaly is consistent with the *known* integral \(3\)-torsion theorem but does not by itself prove integral torsion, rule out other primes, or prove statements at untested orders. The all-order homological statement depends on Mayer--Vietoris plus Jonsson's published exact integral results. The Python/C++ checks are finite and do not replace the all-parameter proof.
