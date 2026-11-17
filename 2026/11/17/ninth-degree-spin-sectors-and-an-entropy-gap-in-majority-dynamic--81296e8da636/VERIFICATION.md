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

Execute `python verify_spectrum.py` with SymPy. It deterministically constructs the complete \(256\)-state directed transfer for \(GP(n,2)\), verifies its \(320\) edges, Tarjan strong components, the two \(12\)-state characteristic polynomials and the exact integer Collatz–Wielandt inequalities. It also constructs the prism transfer and checks its complete characteristic polynomial. The power-trace output through \(n=15\) is captured in `verify_spectrum.out`.

Execute `python verify_direct.py` with NumPy. It independently builds all twenty or fewer explicit three-neighbor bit-update equations and enumerates every configuration on \(GP(n,2)\) and \(GP(n,1)\), \(5\le n\le10\). All \(2{,}795{,}520\) exhaustive checks passed; output is in `verify_direct.out`. The direct checker is not used to infer the all-size theorem.

The finite transfer construction, SCC and characteristic computations are proved to encode the infinite family by the exact cyclic-window bijection in RESULT.md. The asymptotic theorem uses primitivity and a rational positive-vector spectral certificate; no floating-point approximation is used in any logical implication. Independent expert validation has not been performed.
