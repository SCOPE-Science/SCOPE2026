---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The actual RESULT.md at frozen blob ff2af828... defines F_n correctly, degree d=n/2 for n=2^m. Setting c_j=binom(n,j)^2 binom(2(n-j),n), for 1<=j<=d the inner binomial is even, so 4|c_j. Legendre binary digit sums give v_2(c_0)=1 and v_2(c_d)=2. Thus G_n(X)=X^dF_n(1/X)/2 has integral coefficients, odd leading coefficient, all other coefficients even, and constant coefficient exactly divisible by 2, not 4. It is Eisenstein at 2. Because c_0!=0, reciprocal irreducibility transfers to F_n. Applies for every m>=1, not other indices. Independent exact binomial-valuation checks covered n=2..128, not used for all m.

## originality

PASS

The 2013 Sun irreducibility conjecture at OEIS A000172 is the true antecedent; this explicit infinite n=2^m Eisenstein subfamily was not in the inspected OEIS statement or the ranked prior findings. Earlier Franel power polynomials and fourth-Franel recurrence papers use different coefficients and cannot cover this polynomial without a proven transformation. Priority remains best-of-knowledge because the 2-adic trick is elementary enough to have appeared unindexed.

## value

PASS

Proves an infinite arithmetically distinguished subfamily of an explicit named all-n irreducibility conjecture, not a routine rebranding of a different polynomial. The proof is short, but a rigorous infinite family with no extrapolation is a reusable obstruction and a definite conjectural advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
