---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The full RESULT.md at blob df7941008788d9053b5a342e35b935422bc1872a derives t+u=-2cos(theta) for any primitive noncentral 2-cycle and a positive quadratic Q(P)=P²+(2+alpha²−4cos²(theta))P+(1−alpha²)=0. The positive-root/discriminant test gives exactly the half-width arcsin((1−sqrt(1−alpha²))/2); at theta=pi two cycles are classified separately. Differentiating arg normalization gives multiplier factor (q−P²)(q+3P)/(4P³). Independent reconstruction for alpha=.2,.5,.8 with interior fractions .5,.99 yielded two cycles and at 1.01 exterior zero; finite tests do not replace discriminant proof.

## originality

PASS

Best-of-knowledge PASS: 2022/2024 Choudhuri–Faraco–Yadav Proposition 8 asserts a neighborhood of -1 with four period-two points and a coarse nonexistence region, while Proposition 10 handles precisely theta=pi; neither gives the exact boundary formula and saddle-node multiplier. Earlier 2016 Shah–Yadav article and 2022 erratum remain priority risks.

## value

PASS

The sharp mode-locking tongue boundary, complete multiplicity, and attractive/repulsive versus neutral transition are natural dynamical phase-diagram invariants of an explicitly studied analytic family; not merely reproducing its known center example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
