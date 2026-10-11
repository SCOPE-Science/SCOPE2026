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

Prime ℓ has exponent divisors {1,ℓ}, while every prime in squarefree m has exponent one, so d_e=2, σ_e=mp(1+p^{ℓ-1}), and S_e=1+p^{ℓ-1}. Type 1 would force 1+p^{ℓ-1}|2p^{ℓ-1}; coprimality with p reduces this to divisibility by 2, impossible. Type 2 reduces exactly to 1+p^{ℓ-1}|2m. Cancelling its gcd with 2 yields M|m; since m is squarefree this is equivalent to M squarefree and the stated coprime factorization. An independent direct-definition sweep checked 5,700 small admissible triples with no discrepancy. The argument is complete for all stated parameters.

## originality

PASS

Sándor's full primary paper introduces the two exponential-harmonic notions and proves squarefree and exponential-perfect related results, while Laugier–Saikia–Sarmah give two further criteria only under multiplicatively e-perfect/e-superperfect hypotheses. Neither inspected source states the prime-exponent/squarefree-cofactor necessary-and-sufficient criterion. Current OEIS entries A348961, A348964 and A348965 tabulate the relevant sequences and examples but do not give the submitted stratum classification.

## value

FAIL

Although the exponent pattern is a natural first mixed layer and the classification appears unstated, the entire theorem follows by inserting the prime-exponent/squarefree pattern into the defining multiplicative formulas and cancelling one coprime factor. It introduces no additional structural lemma, difficult boundary, or nontrivial classification mechanism beyond this direct textbook-level specialization. Under the stated bar excluding routine definitional deductions, correctness and best-of-knowledge novelty are not enough for acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
