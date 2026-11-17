---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: Bonsall Poisson variance identity yields F_(m,c)(r)=c²(1-r²)+1-r^(2m)+2c r^(m-1)(1-r²); phase alignment gives m-1 off-center angles. Comparing F(r) with F(0) reduces to quadratic roots c±(r), whose upper branch has maximum C_m, with unique positive equality R_m at m>=4. Cubic derivative has one positive maximizer for c<2, continuous at threshold; higher-degree origin remains locally strict and maximizing off-center radii converge to positive R_m. Singular value of the finite Hankel reversal-plus-corner matrix gives the stated full operator norm. Exact finite algebraic comparison with the earlier general n=1 binomial threshold and radii passed for m=4..15. Infinite m conclusion follows from derivatives, not finite checks.

## originality

FAIL

FAIL: The public November 2 generalized binomial Hankel-kernel theorem for z^m+c z^n covers n=1 with the same threshold, unique center optimizer, critical coexistence radius, m>=4 jump and m=3 continuous case, with the precise cubic formula. A separate published November 8 z+t z^m theorem gives the reciprocal-amplitude normalization and same optimizer constellation. The submitted theorem is a direct specialization; the ancillary full Hankel norm and degree asymptotics are also in those sources.

## value

FAIL

FAIL as a new claim: The exact localization phase diagram is worthwhile but has already been derived in greater generality and independently in the same restricted two-term form. Reexpressing c=|a|/|b| or supplying additional finite diagnostics does not fill a distinct mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
