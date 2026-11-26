---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the specified initial conditions and windows starting at n+1, the gcd valuation is the least valuation of any window. The recurrence gives the linear forms y, x+2y, 2x+5y, 5x+12y and the step-four matrix M with rows (5,12), (12,29). Expanding their fourth powers gives the stated coefficients, all divisible by 6. M is I modulo 4; replacing each form L by L+4L' changes L^4 by a multiple of 16 coefficientwise, and each further difference gains a factor 4. For 3 use -M, equal to I modulo 3 and giving identical evaluations on the homogeneous quartic F; each difference gains 3. In the sum of m operator iterates the coefficient of the l-th difference is binom(m,l+1). The loss in its valuation is at most v_p(l+1) relative to v_p(m). For l>=1 the remaining gain over v_p(m) is at least 3 for p=2 and 2 for p=3, so only mF(v) matters modulo the two claimed powers. F(0,1)=21378 has both valuations one; F(1,3)=2911764 has 3-valuation one. The Q terms are odd, and any four Q fourth powers sum to 4 mod 16, establishing exact 2-valuation two for the base block. Thus for k=4m the minima are as claimed. The fourth-power patterns mod 3 have one zero in four, at index 0 mod 4 for P and 2 mod 4 for Q, by the signed four-step period; the stated starts give nonzero remainders for lengths 1,2,3 mod 4. For other lengths at 2, the alternating P parity gives an odd window for either k odd or k=2 mod 4, and every Q sum equals k mod 16. Independent bounded replay: python3 /workspace/independent_checks.py 5 checked exact gcds over 64 positive-start windows in each of 778 sequence/length cases, including selected high powers of 2 and lengths 4 times powers of 3. This finite replay does not prove the universal divisibility. No claim is made for primes >=5.

## originality

PASS

The closest Pell literature defines this sliding gcd generally and treats first powers and squares; the nearest distinct indexed research treats Pell cubes, or quartic windows for different recurrences and prime regimes. The exact quartic two-prime formula for this pair survives these comparisons. This is a bounded judgment, not historical-priority certification.

## value

PASS

The prior Pell work motivates powered sliding gcds as exact invariants. This result determines two unbounded prime-primary parts for all window lengths, explains the common sharp 3-adic threshold at k divisible by four, and distinguishes the two companion normalizations at 2. The proof moves beyond a finite table or a first-power identity, while leaving the full gcd and other primes open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
