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

## Analytic checks
1. Floquet/positive-vector comparison: the periodic half-line Jacobi norm equals the largest zero-phase cycle eigenvalue. At period four this is half the top singular value of the displayed two-by-two block.
2. At fixed normalized mean one, the entrywise sum is four and the squared Frobenius norm is \(4(1+v)\). The uniform singular-vector Rayleigh quotient is two.
3. Nuclear triangle inequality gives \(s+t\le4\). For \(v\ge1\), \(4(1+v)\le s^2+(4-s)^2\) forces the claimed square-root boundary.
4. Equality of nuclear and entrywise norms forces support on a diagonal or antidiagonal. Equality of the uniform Rayleigh bound forces alternating coefficients. These conditions classify all cases.
5. Sample exact quadruples \((1,1,1,1)\), \((3/2,1/2,3/2,1/2)\), \((2,0,2,0)\), and \((3,0,1,0)\) match the four claimed phase values.

## Limits
No finite enumeration or numerical approximation underwrites the proof. Independent audit is not performed. Exact-historical-priority comparison is limited by the available literature and by inaccessible published complete texts.
