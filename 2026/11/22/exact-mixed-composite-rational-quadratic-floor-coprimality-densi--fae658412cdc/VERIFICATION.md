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

For n=bq+r the floor differs from arq+c_r by aqn, and multiplying the reduced second gcd argument by b gives ar n-t_r. When t_r>0 every shared prime divides t_r. For a prime dividing b, shared divisibility occurs exactly when the prime divides both r and c_r; otherwise a prime dividing t_r forbids just one q class. CRT gives weight w_r and a period bQ, not necessarily the least. When t_r=0, b divides n². Write n=gm, b=gh, g=gcd(n,b), so gcd(m,h)=1, h divides g, and g=hj. Then gcd(n,an²/b)=jm because h divides b and is coprime to am. It equals one exactly when j=m=1, i.e. n²=b. The r=0 fibers give no hits for b>=6. A putative period starting at or before d=sqrt(b) is a global period for H because it agrees with H on a tail and H is already periodic; it therefore cannot repeat the isolated spike. CRT yields the density, and the remainder of an incomplete period plus the spike yields the stated real-X error. For a'≡au² mod b match r≡ur' mod b: t=t', and c'−c=mr'²−2aukr'−abk² when a'=au²+bm, r=ur'+bk. This vanishes modulo each prime dividing both b and r, so admissibility and the weights match. Independent finite diagnostics (python3 /workspace/branches/independent-reproduction/arithmetic_review.py) made 207600 raw floor/gcd checks across ten mixed denominators including squares and numerators above b, and recovered 1/2 and 23/30 at b=6. They corroborate but do not replace the uniform argument. Frozen checker inspected, not run.

## originality

PASS

The supported distinct claim is the mixed-composite quadratic case, not rational-floor periodicity in general, known prime and prime-square classifications, or the spike by itself. The inspected same-day prime-square theorem has exact least periods in its own family and the identical quadratic p-square spike, but it does not allow mixed nonunit fibers with a nonzero remainder. CRT applied to that statement is not a reduction: the remainders modulo the whole denominator and the local obstructions from the whole-denominator floor quotient are required. The irrational and linear results have incompatible hypotheses. No equivalent mixed-composite result was established from the bounded evidence.

## value

PASS

A researcher studying fixed rational quadratic floor indicators needs the local exclusions even in fibers that are nonunits but not zero-remainder. The formula settles the entire mixed-denominator regime, with an explicit finite density and square-class symmetry despite genuine numerator dependence, and distinguishes one globally located spike from periodic obstructions. Its period is explicit, not claimed minimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
