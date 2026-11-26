---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With w=c+d>0, W_t=tw+c(t−2), so the artificial independent categorical draw assigning w/W_t to each existing label and the rest to a dummy outcome is well defined, including at t=2 and for d<0 in the stated range. Conditional on any current leaf set, singleton deletions and no deletion have exactly the probabilities in the true process; adding the new leaf gives equality of leaf-set histories, not of whole trees. Independent draws then give the joint survival product on the deterministic active intervals, and inclusion-exclusion recovers the finite law. An increasing test function restricted to one-hot support has nonnegative increments from its all-zero value; for disjoint test blocks, cross-products of the increments vanish. Conditioning proves concatenation of independent negative-associated families, and negating both composed tests gives the decreasing-block closure used here. Distinct vertex labels give disjoint input blocks even for overlapping calendar intervals. Factoring the exponential moments for either sign and applying the bounded Bernoulli inequality gives Hoeffding. For every positive kernel at size three the two seed indicators are complementary. For size four the size-three shape fixes total weight b+2, where b=f(2)/f(1); the seed/third-leaf joint probability is b/[2(b+2)] and their marginals are (b+1)/[2(b+2)] and (b+1)/(b+2), giving the stated negative covariance; the two seeds cannot both survive. At size five, the three equally likely size-four branches (attach to center, other seed leaf, or vertex 2) directly give the stated marginals and joint law. Subtraction gives g²−8g−41 over the positive denominator, and the unique positive root is 4+√57. Exact independent enumeration confirms all six nontrivial pair formulas and the affine survival product on two mixed observation schedules. The frozen checker itself was inspected, not executed.

## originality

PASS

The distinct contributions are the mixed-observation labeled leaf-status law for affine ordinary-degree weights, its resulting negative association, and the sharp earliest-size nonlinear reversal with an exact threshold in the displayed family. Aggregate leaf-count processes, deterministic parent-choice survival products, and allocation negative association are established and are not credited as new. Plane-recursive slot survival is a particularly close common-horizon mechanism, but is not the same seed normalization or the full stated result.

## value

PASS

The categorical reduction makes an entire labeled and mixed-time law accessible despite degree reinforcement, a stronger input than aggregate count dynamics for questions about birth cohorts or specified labels. The earliest-size nonlinear witness then identifies where even pairwise repulsion can fail, with a natural one-parameter boundary that can be used exactly. The finite result is motivated by the structure of the affine theorem rather than an arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
