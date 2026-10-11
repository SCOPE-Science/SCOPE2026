---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

After setting \(x_i=1-2p_i\), fixing the number of negative factors and their total magnitude reduces each sign class to two AM--GM blocks. The product magnitude is monotone in the transferred magnitude, so the optimum lies at the stated endpoint and yields exactly the displayed \(M_r\). The small-mean lower bound follows from \(\prod_i(1-2p_i)\ge1-2\sum_i p_i\), and complementing trials handles \(\lambda>n/2\). The discrete phase monotonicity follows from differentiating the logarithm of the candidate expression. A fresh exact grid replay over \(3905\) small parameter vectors found every bias inside the claimed interval.

## originality

FAIL

Hoeffding's 1956 theorem is decisively broader: for an arbitrary real-valued function \(g(S)\) of a Poisson-binomial sum at fixed mean, Corollary 2.1 states that both extrema are attained with the Bernoulli probabilities taking at most three values, only one of them different from \(0\) and \(1\). Parity is the specialization \(g(s)=(-1)^s\). Evaluating that published extremal normal form gives a deterministic shift plus a homogeneous binomial block; the submitted \(M_r\) candidates are exactly those evaluations after elementary one-variable monotonicity. Under the required implication rule, the exact displayed parity formulas are therefore a routine corollary of a theorem that already covers every objective \(g\), not an original extremal principle.

## value

FAIL

Parity is a natural statistic, but once Hoeffding's arbitrary-objective extremizer theorem is applied, the remaining work is evaluation of a one-parameter binomial block and elementary monotonicity. Under the common value bar this is a useful worked specialization rather than a new structural lemma, boundary phenomenon, or classification beyond the stronger prior framework.

The dated certificate retains the supplied scientific assessment, sources and limitations.
