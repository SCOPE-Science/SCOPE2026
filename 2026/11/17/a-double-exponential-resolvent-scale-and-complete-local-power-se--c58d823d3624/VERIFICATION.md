---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For B e_j=(log(j+e))^-1 e_(j-1) on complex l^p (1<=p<infty) or c0, decreasing weights imply exact ||B^k||=P_k=exp(-F(k)); F(k)/k->infinity gives compactness and spectral radius zero. Maximizing k log t-F(k)-a k/log(k+e) places log k=t-a+o(1) and yields H_a(t)~e^(t-a)/t, by summation/integration of loglog and logarithmic-integral residual. Max-term versus sum has at most O(t) logarithmic overhead using cut K=e^(2t), negligible on this scale. Neumann expansion gives the uniform-in-argument global upper, and the e_k zeroth coordinate lower gives log||R||~e^t/t. For x^a_j=e^(-a j/log(j+e)), positive real lambda gives lower via zeroth output and l^p/c0 tails give matching upper, hence exponent e^-a. e0 gives 0, y_j=e^(-j/log^2(j+e)) gives 1, and the universal norm bounds confine exponents to [0,1]. The bundled finite saddle diagnostic was read; the asymptotic follows from the infinite saddle argument rather than finite sampled t.

## originality

PASS

Powers and local resolvent exponents are standard, and Ignatev has a full-power-set result under an explicit some-finite-l^q weight hypothesis. Here weights 1/log(j+e) are in no finite l^q, so that stated condition does not cover this example. The additional exact e^t/t and e^(t-a)/t logarithmic growth also are not derived from the abstract theorem. Full text of the closest recent paper inaccessible; this is a qualified best-of-knowledge PASS, not a claim of global historical priority.

## value

PASS

The exact local spectral exponent set in a natural just-nonsummable compact shift is a motivated boundary of summability-based results; the explicit doubly exponential resolvent growth and tunable concrete tail witnesses are directly useful in local spectral theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
