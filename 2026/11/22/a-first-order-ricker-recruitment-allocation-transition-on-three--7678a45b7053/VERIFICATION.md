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

# Verification protocol and limits

The analytic proof in `RESULT.md` is the justification of the infinite-family theorem. The independent downloadable `checker.py` uses standard Python 3 and reconstructs the critical scalar equations by bisection. Run `python checker.py`; the reviewed execution reported 35,028 supplementary assertions for habitat numbers 2 through 10 and dense budget ranges. Separately, 245 multistart constrained optimization runs were compared against its predicted optimum, finding no objective excess beyond roundoff. Those finite tests do not prove global optimization for untested stocks or all integers.

The proof-critical chain is as follows: strictly positive allocation coordinates by the marginal return at zero; KKT and curvature imply either equality or exactly one higher-density coordinate; the difference of levels is parameterized by a strictly convex scalar stock map; a fixed-stock second variation excludes the descending branch; the reward difference has a derivative with a uniquely controlled sign; a positive cubic perturbation at mean density 2 establishes positive reward difference at that endpoint. Uniqueness of the global transition then follows by the intermediate value theorem and strict increase on the remaining branch. The continuous two-habitat limit follows separately.

Numerics are reported only as checks and rounded example values. The model assumes identical uncoupled Ricker habitats, assignment of the entire continuous stock, and maximization of a single generation of expected recruitment. No stochastic persistence, real-world management calibration, or broad priority certification is established. The 2022 spawner-habitat paper's supplementary Appendix S1 remained unavailable for full inspection; this and general nonconcave allocation literature remain originality risks.
