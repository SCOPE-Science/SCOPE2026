---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Write h=b-k for the red count in the second class. Same-color swaps cannot make both strictly better, and swaps within a class leave the opposite class and each moved agent's payoff unchanged. For a red in the first class and blue in the second, the pre-swap own fractions are h/n and (n-k)/n; the post-swap fractions, after relocating both agents, are (k-1)/n and (n-h-1)/n. Squaring the exact distance comparisons yields (k-h-1)(b-n-1)<0 and (k-h-1)(b-n+1)>0. The strict inequalities require the last factors to have opposite signs, which for integer b-n forces b=n; then they hold just when k-h>1, ensuring both participants exist. Reversing classes yields h-k>1. Thus the equilibrium test is exactly the stated one, including the ties at abs(2k-n)=1 and the endpoint population values. Counting labeled red subsets with fixed k gives binom(n,k)binom(n,b-k); at b=n only one even or two odd central values survive. The central binomial asymptotics give the factors 2/sqrt(pi*n) and 4/sqrt(pi*n). An independent finite enumeration over binary masks relocated each candidate red–blue pair and recomputed both open-neighbor integer distances. For n=2 through 6 it found respectively 4,18,36,200,400 balanced equilibria and no nonbalanced exceptions; the unbounded result is algebraic.

## originality

FAIL

The distinct October 25 Resultary record 35b4a89b1bc4 gives an open-neighborhood profitable-swap theorem for equal-size complete multipartite graphs. Its two-part specialization has precisely this phase diagram under the same strict payoff ordering. The binomial parity census and its asymptotics are mechanical consequences of the already determined stable values of k. No distinct remainder is supported.

## value

FAIL

The exact population-instability comparison is meaningful for this model, but as a distinct result the frozen record only instantiates a known multipartite criterion and counts its central values using standard binomial asymptotics. The parameter substitution and census leave no independent new invariant or phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
