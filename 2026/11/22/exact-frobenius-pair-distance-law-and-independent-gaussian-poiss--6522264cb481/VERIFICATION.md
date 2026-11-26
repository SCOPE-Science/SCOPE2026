---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Two changes are reflected in the complete affected files under /workspace/repairs/4/: the raw residual is 2C_n and converges to 2 times a Poisson variable, not itself to Poisson, and the finite enumerator is credited as a direct reweighting of an available component census rather than claimed as an independent new invariant. For fixed ranks k and l, row and column permutation symmetries give the probability (k)_r/(n)_r² of containing a specified ordered nonattacking r-list; independence gives the stated conditional moment of C_n and the falling-factorial expansion gives the polynomial. No exponent is actually negative, since r≤min(k,l). The mean follows from each cell having occupancy probability E[K_n]/n². Independently, deleting rows and columns of r specified shared cells gives the unnormalized polynomial sum over r of A_{n,r}(1-z²)^r times (sum_k A_{n-r,k}z^k)². /workspace/evidence/reproduce_other_checks.py verifies it by exact enumeration through n=4; a separate truncated expansion of the distance-marked component series also agreed through n=4. For the joint limit, the ordinary Laguerre Perron estimate at a=exp(u n^(-1/4)) gives the centered log-mgf u²/4+o(1) for each deficiency, thus both normalized ranks tend to one. The conditional characteristic function of C_n tends in probability and L¹ to exp(exp(iv)-1), since each fixed factorial ratio tends to one and the majorants |exp(iv)-1|^r/r! are summable. Multiplying by the two-deficiency characteristic factor proves the full joint product limit. Slutsky and rationalization yield the Gaussian squared- and ordinary-distance limits of variance 1 and 1/8 respectively. The residual has even support and limit 2Z independent of both Gaussian variables. The asymptotic arguments are not extrapolations from the finite tests.

## originality

PASS

Only the repaired distinct claim is passed: the joint Gaussian rank-deficiency and Poisson occupied-cell law for independent uniform vertices over all ranks, with its metric residual. The comparable Gaussian–Poisson product law counts omitted intermediate labels, and the finite distance law is already implied by a same-day component census; neither is passed as a distinct new result here.

## value

PASS

The repaired claim separates fluctuating ranks from actual common-cell geometry in the standard metric on the square partial-matching polytope. Gaussian distance alone blends the two ranks and discards the overlap entirely; the additional independent unscaled limit determines overlap after subtracting measured ranks, including its exact lattice factor. This is a natural two-scale metric statistic of independent uniform vertices. Its value does not rest on reprioritizing the finite census or on novelty of the classical one-sample limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
