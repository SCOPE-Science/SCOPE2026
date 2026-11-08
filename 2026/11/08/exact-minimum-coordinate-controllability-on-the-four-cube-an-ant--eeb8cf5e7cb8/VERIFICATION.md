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

# Exact proof and independent finite enumerator checks

The theorem's infinite-dimensional inference is not based on sampling; this is a *finite graph classification*. Its conceptual proof uses Walsh eigenspaces, the PBH rank criterion, Jacobi's complementary-minor identity and a simple zero-counting argument. The orbit number is an exact finite group-action result.

The accompanying `verify.py` is a standalone Python 3 program. It computes all 8,008 six-vertex subsets and checks their exact PBH-rank condition at the five eigenvalues against the parity criterion. It then constructs all automorphism images under the 16 coordinate-bit translations and 24 coordinate permutations and partitions the 1,024 admissible subsets into eight complete orbits. The run established exact agreement for every subset and the orbit-size list `32,32,96,96,192,192,192,192`. The canonical representatives are printed by the program.

The rank calculation uses arithmetic modulo 257, not floating-point tolerance. All relevant square subdeterminants have entries \(\pm1\) and order at most six; Hadamard's inequality bounds their absolute values by \(6^3=216\). Since \(257>216\), every determinant is zero modulo 257 if and only if it is zero over the rationals. Therefore the computed ranks are exact, not probabilistic.

Executed check: `python3 verify.py` — all assertions passed and the program ended with `EXACT VERIFICATION PASS`.

The result is limited to independent coordinate inputs on the unweighted full four-cube; no external mathematical validation or proof-assistant certification was performed.
