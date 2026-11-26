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

The primary paper's Algorithm 2.1 and practical estimator (2.2) in arXiv v1 give the frozen update, including the shorter startup product. On the invariant lower ray, q₁=1−a and [ (1−a)², 1−a ] is invariant because the geometric mean is between its inputs. This closes the signed-multiplier induction and ensures the ratios never divide by zero. For the stationary q*=(1−a)/(1+a), the distance from a geometric mean to q* is at most the greatest input distance, even without a Euclidean Lipschitz estimate. Each complete block of ℓ new entries then reduces the maximum deviation by a factor at most a; the limit of α is 2/(1+a). The Jacobian's first row is −a/ℓ in every position and the rest shift the lags. Its ℓth power has sup-norm at most a by the same block argument; the root-product identity gives the other radius bound. The ℓ=2 discriminant is negative on 0<a<1 and the conjugate modulus is √(a/2), with equality to a only at 1/2. These are all-window analytical checks; the packaged finite check was inspected as evidence only. The paper labels in the frozen text should read Algorithm 2.1, (2.2), Lemma 2.4 and Theorem 2.5 in the cited v1. These are pinpoint-citation errors, not a different method or hypotheses. No assertion that the prescribed startup attains the linearized worst-case rate is needed.

## originality

PASS

The single-sample rate and identified step are covered by a stronger earlier one-sample result. The original already treats that result as antecedent, not as a novel isolated case. The distinct joint claim is the finite-window feedback classification beyond one sample, including exact radius crossover and degeneration as the chosen fixed window grows. Neither the source framework nor the strongest earlier matched result establishes or implies that claim at the stated scope.

## value

PASS

The lower-eigenray is a natural test where one can isolate the curvature-identification dynamics from transient spectral mixing. The exact crossover shows that adding just one observation can improve or worsen that response depending on curvature; the fixed-window limit rules out a memory-uniform linearized contraction factor even though every chosen window converges. This is a concrete limitation of interpreting residual memory as uniformly beneficial, not a claim about slower optimization iterates. The known one-sample result serves as a motivated baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
