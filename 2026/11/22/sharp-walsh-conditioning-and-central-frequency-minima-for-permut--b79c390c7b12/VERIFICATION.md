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

A two-cycle contributes a minus sign exactly when it crosses the frequency/complement cut; changing its cross-color weight from +uv to -uv multiplies the labelled cycle series by exp(-2uv). Thus the indicated coefficient gives the counting multiplier and division by n! gives the probability multiplier. For n>=4, the first crossing-cycle moment and P(X odd)<=E X give the lower bound (n-2)/(2(n-1)). For the location of the minimum, q(n,k)=[u^k v^(n-k)]F satisfies the Pascal recurrence with central forcing (-2)^j/j! at n=2j. Its first differences in the lower half are at least 2/3 in rows 4–6; elsewhere Pascal addition preserves this, and at the even center two preceding-even differences contribute at least 4/3 against forcing of modulus at most 2/3 for j>=4. Deleting the two-cycle of the newly added character vertex gives Lambda(n,k)-Lambda(n,k+1)=2 k!(n-k-1)! (q(n-2,k)-q(n-2,k-1)). This gives strict descent for n>=6. Direct permutation/Walsh replay through n=8 confirms every frequency against the formula, including the rows (6,2,2,6), (24,12,16,12,24) and (120,72,72,72,72,120); order five has a tie at all intermediate weights. Replay with Python 3 on branches/65fc8914-7d1e-411d-8ebb-566debbe5748/independent_repro.py; the frozen checker was read, not run. Each normalized falling-factorial moment ratio counts an ordered sample event and is bounded by one. Dominated convergence then gives the pointwise exponential limit, compactness upgrades it to uniformity in k/n, and binomial weight concentration gives the empirical limit. The constant multiplier is one; the minimum determines the exact condition number, with the uniform maximum verified at n=3 (n=4 has condition number 2).

## originality

PASS

The distinct supported contribution is the all-order strict central-shell extremum, including its low-order exceptions and sharp finite-order recovery conditioning. The signed generating function is a standard marked cycle-index specialization, and the factorial-moment limit uses classical methods; those ingredients are not credited as new alone. No verified prior statement or stronger implication gives the same finite-order extremum for exactly two-cycle endpoints. Closest related index results and primary-text access limitations are recorded below.

## value

PASS

The endpoint-support observation discards the pairing, so whether and where it erases Fourier information is a natural exact recovery question. The strict finite-order central-shell theorem identifies the least stable channels rather than just furnishing a positivity or asymptotic bound. It gives sharp uniform conditioning, an exceptional order-four shell and a limiting condition number while distinguishing bulk concentration from operator-norm convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
