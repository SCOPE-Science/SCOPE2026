---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

De Cataldo's product formula gives \(F(q)=\prod_{m\ge1}(1-q^m)^{-e}\). Formal logarithmic differentiation yields \(qF'(q)=eF(q)\sum_{j\ge1}\sigma_1(j)q^j\), hence \(n a_n=e\sum_{j=1}^n\sigma_1(j)a_{n-j}\). Therefore \(e\mid n a_n\), and cancelling \(\gcd(|e|,n)\) gives \(|e|/\gcd(|e|,n)\mid a_n\). The \(e=0\) case follows from \(F=1\). The argument also works for negative Euler characteristic because it is an identity of formal power series. The bundled finite expansion is consistent but is not needed for the proof.

## originality

FAIL

The arithmetic statement is a routine direct corollary of de Cataldo's already-published Euler product. Under the required implication standard, a result need not be printed verbatim to be covered: the known product determines the coefficients, and one standard logarithmic-derivative step gives the exact recurrence from which the divisor follows by Euclid's lemma. Fresh exact-form and Resultary searches did not locate the divisor as a separately named theorem, but that absence cannot restore originality against this decisive prior implication.

## value

FAIL

Although the divisor is a neat arithmetic observation on a natural geometric sequence, the entire proof is a standard one-line logarithmic-derivative recurrence plus gcd cancellation from a known exact generating function. Under the shared value standard this is a routine textbook deduction, not a sufficiently motivated new structural lemma or classification. The K3 specialization is just substitution into the same corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
