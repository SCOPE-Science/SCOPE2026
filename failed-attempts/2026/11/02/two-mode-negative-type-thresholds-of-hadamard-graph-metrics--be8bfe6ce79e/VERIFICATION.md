---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An independent sign decomposition gives the powered-distance spectrum. Orthogonality gives distance two between different indices on the same bipartite side, distance four between antipodes, and distance three for opposite-side nonedges. On the sign-even subspace A₂ acts as 2(J_k−I_k) separately on the two sides, A₃=A₁ and A₄=I. On the sign-odd subspace A₂=0, A₃=−A₁, A₄=−I; the off-diagonal block of A₁ is H with all singular values sqrt(k). This yields the stated eigenvalues and multiplicities on the zero-sum subspace. On [0,1], G is strictly increasing, and F for k≥8 is strictly concave with F(0)=−1, F(1)=0 and F′(1)<0, yielding the claimed first crossings. The zero sector excludes p>1. At k=4 and p=1 only the +sqrt(k) sector is negative; below 1 the bipartition eigenvalue is the fourth forward difference of x^p at zero and is strictly negative by the positive integral representation of x^p as a mixture of 1−exp(−tx). Centered Gram ranks give all endpoint dimensions. Independent rational bounds confirm the switch at k=8 and 12, and high-precision bisection confirms the reported decimals. Substituting p=x/k or x/sqrt(k) in the first-root equations and bracketing by strict limiting signs yields the respective asymptotics. The strict statement at p=0 uses the usual convention D₀=J−I.

## originality

FAIL

A distinct earlier published Resultary result explicitly gives both powered-distance inequalities for every positive exponent and the full equality-sector dimension formula for the same graph family and all the same existing orders. The frozen root law and dimensions restate that classification; the order-8 and order-12 checks and large-order expansion are elementary consequences of its explicit inequalities, not an independent coverage gap.

## value

FAIL

The graph-metric boundary and competition are mathematically natural, but the central quantitative invariant and endpoint ranks are already available from the matched all-exponent result. The surviving numerical comparisons are two substitutions and the asymptotic is a first-order expansion of those explicit inequalities; the record does not offer a separate nonmechanical structural result that would justify the old claim on value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
