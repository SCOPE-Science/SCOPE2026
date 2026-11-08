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

# Reproduction and limits

Run `python verify.py` in a Python 3 environment with NumPy. The program independently constructs full discrete Fourier transforms of rank-at-most-two indicator arrays on binary \(3	imes3\), binary \(4	imes4\), and ternary \(3	imes3\) matrix groups. All coefficients and the endpoint norm are compared with the closed theory at those finite parameters. It separately enumerates every rank-at-most-two matrix in binary \(5	imes5\) and \(5	imes6\) spaces and checks the full frequency-rank representative spectrum, including the sign transition. Exact-integer rank orbit and sign tests cover \(q=2,3,4,5,7,8,9\), \(3\le m\le17\), and \(n=m,m+1,m+3\).

Expected marker: `ALL_RANK_TWO_BALL_CHECKS_PASS`. These exhaustive finite-space tests and exact integer parameter grids corroborate the symbolic all-field proof. The tests alone do not prove any unbounded quantifier. The standalone file is included verbatim with the theorem. Independent mathematical review was not performed.
