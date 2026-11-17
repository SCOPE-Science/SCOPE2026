---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The check map L(c)=Σc_jα^j is onto and satisfies L(Tc)=αL(c). For proper d|q^r−1, every ambient T^d-fixed word therefore has zero syndrome. The coordinate permutation has gcd(N,d) cycles, and T^{dN/g}=λ^{d/g}I determines the fixed-weight binomial polynomial. For d=M the dual simplex has all nonzero words of weight q^{r−1}, so the q-ary MacWilliams transform gives W_M. Weight-preserving Möbius inversion on divisors of M yields the exact orbit-by-period-by-weight count. Checked q=2,r=3 directly in independently constructed GF(8), including full fixed-weight polynomials; finite checks are not the infinite proof.

## originality

PASS

No inspected earlier source yields the simultaneous two-parameter exact period–weight spectrum for the specified constacyclic Hamming action; preexisting constacyclic representation, total orbit counts, and MacWilliams formula are excluded from novelty.

## value

PASS

The joint period–weight coefficients of a natural perfect-code family, including composite repunit lengths, resolve which orbit types/weights appear and in what multiplicities; their exact refinement cannot be reconstructed from the known separate total-orbit or global weight marginals and can inform covering-sequence constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
