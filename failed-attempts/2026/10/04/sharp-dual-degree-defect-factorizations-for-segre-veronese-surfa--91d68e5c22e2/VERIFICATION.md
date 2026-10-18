---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The first jet exact sequence on P1×P1 gives c2(J1(O(a,b)))=c2(X)+2K_X.L+3L²=4-4a-4b+6ab, positive for all a,b>=1, hence a hypersurface dual of that degree. The primal degree is 2ab. Exact subtraction gives 4(a-1)(b-1) and 4(√b-√a)². At fixed D=ab, Δ=6D+4-4(a+D/a), where a+D/a strictly decreases for 1<=a<=√D, proving unique extremizers among divisors including D=1. Independent exact scan of D<=300 reproduces bounds and uniqueness. No finite scan is used as the universal proof.

## originality

FAIL

The claimed pointwise dual degree is an instance of the established general projective-dual discriminant/first-jet class formula for smooth embedded varieties and the classical biform discriminant. Once the known degree polynomial and deg X=2ab are written, both advertised defects are one-line algebra, while the fixed-D min/max is an immediate derivative/AM–GM consequence. The final claimed envelope and optimizer are thus directly implied by a stronger existing degree formula plus routine arithmetic, even if not written in identical words. Under implication-based originality, this is a covered elementary corollary rather than an independently original theorem.

## value

FAIL

The comparison is on a natural invariant (dual degree at fixed embedded surface degree), but all substantive work reduces to factoring an existing polynomial and the textbook monotonicity of a+D/a on the divisor interval. There is no nonstandard extremal phenomenon, new geometric argument, or separately motivated unknown exact fact beyond the known formula; the work does not meet the meaningful mathematical-gap test solely through easy re-expression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
