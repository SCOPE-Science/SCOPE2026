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

Shor's classification and formulas give q=floor(g/a), r=g−qa in [1,a−1], conductor 2g−r+1, and e=a or a−1 according as r=a−1 or not. The nongap count below the conductor is qa+1, so the two surplus formulas follow by multiplication and subtraction. When a≤g, qa≤g and a≤g give the claimed 4/g error against q(a/g)^2. The second case has a≥3 and nonnegative additive term, and W is nonnegative and at most qa²≤g² on ordinary entries; the a=g+1 entry has W=0. Each open mesh interval of f has variation O(q⁻²) and the jumps are summable; f(0)=0 is continuous at zero. For every fixed Lipschitz test, the integral versus endpoint-sum error is bounded by variation/g, and replacing the uniform mesh by the admissible set changes the tested mean by O((1+τ(g))/g). On (1/(q+1),1/q] the sublevel set is cut off at sqrt(t/q); each level set is countable and adjacent image closures overlap since q/(q+1)^2<1/(q+1), giving atomlessness and full support. Integrating each branch to power m and shifting the second sum yields [q^m−(q−1)^m]/q^(2m+1), whose binomial expansion gives the stated zeta moments and positive variance. An independent finite check generated all semigroups through genus 10 by deleting a minimal generator above the Frobenius number, then tested gaps modulo g and recalculated W from each reflected gap set. It reproduced the admissible multiplicities and the surplus in every case; the finite check is not the proof of convergence.

## originality

PASS

The Wilf surplus, reflective classification, cardinality and structural formulas are prior inputs, as is Wilf nonnegativity in this class. The prior isolated-gap and pivot-run results overlap substantially in sampling and divisor arithmetic, but neither gives this surplus law, its distribution, or its complete zeta moment sequence. The bounded originality decision concerns that distributional result rather than the elementary substitution into Shor's formulas.

## value

PASS

The Wilf surplus measures the magnitude of a central inequality rather than merely testing its sign. In a classified natural ensemble, its g² scale, nondegenerate atomless law, variance and full zeta moment sequence give a quantitative benchmark for typical behaviour and comparison to other semigroup ensembles. The divisor-sensitive rate makes the benchmark testable at finite genus. This goes beyond restating the known positivity result or listing a few surplus values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
