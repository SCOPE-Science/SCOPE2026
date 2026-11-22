---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and exact domain

**Claim domain.** Every finite simple nonempty undirected graph; each probe marginal independently uniform across all \(2^n\) sign vectors, with arbitrary dependence between probes; a matrix-adversarial real symmetric off-diagonal coefficient vector of squared Euclidean norm one on the known graph; worst-case variance of the equal-weight two-quadratic-form trace estimator.

**Analytic checks.** (1) Each probe marginal is uniform, so individual edge monomials have mean zero. (2) For arbitrary dependence between probes, testing a single edge produces error variance \(4\Pr(D_i=D_j)\), giving the universal lower bound. (3) An independent uniform base signing and graph-optimal random cut makes all distinct edge monomials orthogonal, producing a diagonal covariance and the matching upper bound for every matrix. (4) Scaling probability distributions and fractional cut covers in both directions gives \(\alpha_G=1/\operatorname{fcc}(G)\), with finite attainment. (5) Automorphism averaging gives the edge-transitive reduction, while exact maximum-cut counts prove odd-cycle and complete-graph values. (6) A triangle with a pendant edge demonstrates why the formula using an unweighted maximum cut is not valid on every graph. These steps give the full infinite-family proof without extrapolating numerical evidence.

**Reproduction.** Install `requirements.txt`, then run `python verify.py` in the same directory. A completed invocation passed 594 checks: independent primal/dual LP formulations on listed graph families and 60 sampled further graph instances, exact-rational sign covariance enumeration of chosen cut mixtures, 240 randomized nonlinear coupling tests, and exact complete-graph combinatorics. The script prints the count and fails on any assertion. Its floating-point LP tolerances are specified in code. The LP experiments cannot certify a general optimization theorem or historical novelty; they only independently stress-test the formula. The proof does not depend on numeric solvers.

**Unproved and excluded.** No finite-polynomial-time construction of optimal cut laws is claimed; exact cut enumeration can be exponential. No comparisons of finite-sample tails, adaptive algorithms, more than two probes, nonuniform probe marginals, or unknown graph structure are established. Independent audit has not been performed.
