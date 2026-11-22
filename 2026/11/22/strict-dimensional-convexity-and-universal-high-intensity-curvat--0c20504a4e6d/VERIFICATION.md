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

The exact operator is \(H_{d,\beta}=A_d+\beta\lvert\delta_0\rangle\langle\delta_0\rvert\). The key analytic checks are the rank-one resolvent identity, the probability-density normalization implicit in the positive eigenvalue equation, the nonaffinity test \(a''(0)=-v\), and the four-step closed-walk moment expansion. All four are proved in `RESULT.md`; no infinite conclusion depends on a finite program run.

Run `python CHECKER.py` with Python 3, SymPy and SciPy installed. Its stored output is `CHECKER_OUTPUT.txt`, reporting 84 passed symbolic, integer-enumeration and numerical assertions. The numerical root-solving used quadrature tolerances \(3\times10^{-12}\), and verifies only representative nearest-neighbor parameters. No sample-path Monte Carlo, formal proof assistant, or independent validation is claimed.

Scientific limitations: only fixed-dimension high-intensity asymptotics, only product generators, and potentially uninspected earlier priority evidence. Independent audit remains unperformed.
