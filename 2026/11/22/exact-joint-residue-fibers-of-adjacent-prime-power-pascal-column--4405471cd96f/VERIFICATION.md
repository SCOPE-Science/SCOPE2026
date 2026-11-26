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

For h=p^a, Vandermonde increments binomial(hx,h) by 1 modulo p^2: every interior product has both factors divisible by p by Lucas, also for p=2. For x>=1 the exact ratio for inserting r<h factors can be taken in Q_p: each denominator has valuation v_p(i), and only i=p^(a-1)t contributes a nontrivial factor 1+p/t modulo p^2. The x=0 case is zero separately. Applying the congruence at the two neighboring levels gives the joint triangular digit system (2). Its low digits force x0=u0 and x1=v0; the remaining first-coordinate equation is exactly a harmonic fiber query, while the last equation determines x2. This gives the multiplicity p^(a-1) and all supported and excluded cases. Prescribing either single coordinate independently fixes just two index digits after the lower remainder is chosen, yielding the uniform marginals. Translation by p^(a+3) is a period and n=p^(a+2) already differs from n=0 in the second coordinate; since the least period divides every period, no smaller proper divisor works. The reflection H_(p-1-j)=H_j gives the odd-prime bound, and H_0=0,H_1=1 handles p=2. Fresh replay: python3 -B /workspace/reviews/reproduce.py 3; p-adic unit/valuation streaming of both binomial columns in seven full candidate periods checks every cell and both marginals and the nonperiod witnesses, with exact math.comb spot checks. This is finite corroboration only.

## originality

PASS

Pass the evaluated paired fiber law and its harmonic-image obstruction, not the individual congruence or the least period in isolation. Primary sources cover the latter ingredients, whereas the exact simultaneous count requires resolving the overlapping digit constraints and counting their harmonic collisions. No examined prior result supplies this evaluated joint classification; priority is not certified.

## value

PASS

Two adjacent prime-power Pascal columns are naturally coupled by shared index digits. Despite exactly uniform marginals, at most about half the output pairs are attained for odd primes, with a complete exact description in terms of collision counts of finite harmonic sums. This gives a structural and quantitative obstruction rather than just a check of a few primes or another derivation of the known period. The all-exponent scaling and both positive/zero fibers make the exact statistic useful for studying dependence of nearby columns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
