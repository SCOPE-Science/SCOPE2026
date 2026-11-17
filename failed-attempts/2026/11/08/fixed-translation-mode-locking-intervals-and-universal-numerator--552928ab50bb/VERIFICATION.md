---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The known rational plateau criterion L(λ)<=b<=U(λ) with ceil/floor mechanical word supplies the starting point. Prefix-dominance of initial mechanical factors gives L,U strictly decreasing; L<U inside (0,1), both have endpoints 1 and p/q, hence inverse slope interval. Coprime floor-sum yields S(1)=p, S'(1)=(p-1)(q-1)/2 and L'(1)=-(q-1)/(2q), U'(1)=-(q+1)/(2q); analytic inversion gives width coefficient 4q/(q²-1). Independent exact first-moment arithmetic held for all coprime 1<=p<q<=29. Critically, the identical all-domain proof is also available in two earlier publications.

## originality

FAIL

Previously published October 18 and November 1 exact fixed-translation rational-tongue theorems already prove the same complete inverse-slope interval with identical polynomial endpoints, strict monotonicity and numerator-independent coefficient 4q/(q²-1). The November 1 theorem additionally proves strong-contraction-edge asymptotics, making it strictly broader. The submitted theorem is mathematically covered despite its different monotonicity proof.

## value

FAIL

Exact inverse-slope tongues and denominator-only opening are mathematically useful, but both are already published for the identical class, with a stronger all-edge refinement in November 1 research. A different derivation by a weighted-prefix lemma and a bounded integer checker do not independently provide a motivated new fact beyond those results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
