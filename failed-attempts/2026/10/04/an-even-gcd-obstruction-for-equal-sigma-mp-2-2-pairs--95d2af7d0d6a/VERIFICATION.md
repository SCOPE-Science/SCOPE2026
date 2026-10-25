---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For positive m,n let c=σ(m)=σ(n); the stated two squared equalities mean m²+n²=c². For every integer r=2^e∏p_j^{a_j}, σ(2^e) is odd and σ(p_j^{a_j}) has parity a_j+1, so σ(r) odd iff all odd-prime exponents are even, i.e. r is a square or twice a square. If c is odd, m²+n²≡1 (mod 4) implies exactly one leg is odd, so write the odd one x². The even one is y² or 2y². The former gives x⁴+y⁴=c², forbidden by Fermat descent; the latter yields a right triangle with square area (x²)(2y²)/2=(xy)², also impossible. Hence c is even and m²+n²=c²≡0 (mod 4) forces m,n even. Positive m,n exclude zero-area and trivial zero-fourth-power exceptions. Equal m=n gives 2m²=c², already impossible over positive integers, but does not require a separate case. An independent divisor-sum sieve through 200000 found zero parity discrepancies and zero equal-σ Pythagorean pairs and reproduced all five named MP(2,2) examples. The entire assigned eight-blob native Git tree was independently SHA-1 reconstructed and matched.

## originality

FAIL

The equal-divisor-sum hypothesis with odd common value implies, by the classical multiplicative divisor-sum parity criterion, that each leg is a square or twice a square. The pre-existing general Fermat-descent result that no integer Pythagorean triangle can have two such sides rules out that case outright. The Pythagorean identity then forces even common value and both legs even modulo 4. This is an immediate corollary of two standard antecedent statements plus a routine mod-4 step, not a mathematically new obstruction under the required implication-based originality bar. Dimitrov 2024/2025 and OEIS still pose the equal-sigma question and do not explicitly articulate this corollary; that absence does not defeat the decisive prior mathematical implication. The published Resultary hit is a posting of the very same assigned record, not an independent earlier theorem.

## value

PASS

Irrespective of originality, excluding every primitive/coprime candidate in the exact named Dimitrov equal-σ MP(2,2) existence problem is a motivated all-integer structural boundary; it changes the admissible search/construction regime from arbitrary pairs to even-even ones, rather than merely expanding a finite search. A future researcher investigating that problem could need this precise restriction. However the argument is very short and entirely assembled from standard classical tools, limiting its standalone contribution; that simplicity is independently decisive for the originality assessment, not falsely converted into a correctness defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
