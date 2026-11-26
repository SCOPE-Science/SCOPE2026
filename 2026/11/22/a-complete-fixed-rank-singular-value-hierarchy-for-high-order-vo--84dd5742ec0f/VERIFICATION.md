---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The fixed-rank theorem is unchanged. The input/output changes of variables absorb the factor alpha and give the kernel (1-(u+v)/alpha)_+^(alpha-1). The exterior kernel on ordered tuples is the determinant without 1/j!, and its norm is the product of the leading j singular values. The repaired proof bounds the individual u- and v-degrees at epsilon-order r by r, with equality in both possible in the mixed logarithm only for -epsilon uv. Thus any determinant term using distinct degree lists a and b through a matching sigma starts at sum max(a_i,b_{sigma(i)}); at J=j(j-1)/2 only identical consecutive lists starting at zero and the diagonal matching qualify. The coefficient is (-1)^J Delta(U)Delta(V)/prod_{k<j}k!. To pass from local analyticity to Hilbert–Schmidt convergence, the Cauchy disc of radius 1/[8(1+R)^2] bounds the mixed determinant uniformly and yields remainder O_j(epsilon^(J+1)(1+R)^(2J+2)). With R=C_j log(alpha), the inside scaled error times the extracted exponential tends to zero in L², and the outside squared scaled tail is O_j(alpha^(2J) exp(-R)). The ordered Gram determinant is prod_{k<j}(k!)²/2^(j²) by monic Laguerre norms; division of the product limits gives (j-1)!/2^(2j-1) for all fixed j, including 1/16 and 3/64 at j=3,4. Independent exact finite checks of the Vandermonde coefficient and Gram constants through rank 8 corroborate these steps; the analytic proof, not a finite quadrature or the uploaded checker, proves the limit. No growing-rank uniformity is claimed.

## originality

PASS

On the inspected evidence the surviving contribution is the sharp hierarchy from rank 3 onward. This is not a priority claim for the boundary-layer model, rank-one or rank-two consequences, or exterior powers. Search is nonexhaustive; abstract-only comparisons are recorded as such.

## value

PASS

At each fixed rank the next singular value is the exact optimal finite-rank approximation error in operator norm. The hierarchy determines its scale and sharp coefficient, rather than just convergence to rank one or an upper tail bound after rank two. The exterior-power Vandermonde limit explains why successively smaller scales occur for this natural family and supplies all higher fixed ranks in one argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
