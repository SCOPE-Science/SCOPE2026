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

The published run weights match the two parity counts, including the empty product and leading zeros. Partitioning a word by its initial 1-run and the next zero gives H=A/(1-zA). For the three quadratic weights the Fibonacci Binet modes are φ², -1, and φ^{-2}, giving the common 1-2z-2z²+z³ denominator for A; the coefficients at degrees 0,1,2 give the three numerators. This reconstructs the five stated functions. Merging adjacent runs after a bit flip makes U nondecreasing and V strictly increasing by the Fibonacci addition laws. Condition on all but a specific bit: the conditional covariances are nonnegative and strictly positive when its adjacent bit is one and the rest are zero. The conditional means are increasing in the remaining bits, so their covariance is nonnegative by Harris; this supplies the strictness step and shows both variances nonzero for L≥2. U is constant for L=0,1. The nine root brackets isolate three distinct roots of each cubic, with the stated dominant root. Rational upper bounds 2.41422 and 2.73206 for the first-moment growth roots verify all three second-moment domination comparisons. Partial fractions then give each positive pole amplitude and the Pearson asymptotic; the rational bound on r_UV² gives rho<1. Independent exact parity enumeration on ten complete blocks and rational endpoint checks agree; high-precision evaluation gives C=0.9980884128685269… and rho=0.9865717478180131…. Replay `python3 /workspace/audit_checks/frozen_reconstruction.py`; only the argument, not enumeration, proves the universal result.

## originality

PASS

The two run laws, their single-variable averages and the numerical UU series are known. The mixed generating function is also a routine consequence of the published linear representations, not a sufficient originality basis by itself. The supported distinction is the positive-at-every-nondegenerate-length yet vanishing Pearson correlation, with a strict exact exponential rate for this specific pair. That conclusion uses an actual dominance and radius comparison and a strict association argument, not just identifying tensor matrices.

## value

PASS

This is a natural pair from the literature, not a pair selected to manufacture a root comparison. Its known separate averages do not explain its joint fluctuations. Strict covariance for every nondegenerate block coexists with asymptotically vanishing normalized dependence, and the exact algebraic rate quantifies the slow approach. The result is for complete uniform dyadic prefixes only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
