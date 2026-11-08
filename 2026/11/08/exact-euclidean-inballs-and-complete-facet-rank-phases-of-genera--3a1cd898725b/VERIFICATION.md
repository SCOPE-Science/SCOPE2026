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
# Verification

The analytic argument in `RESULT.md` relies on the cited primary facet theorem for the exact arbitrary-parameter polytope. The distance inequalities, optimal-center construction, redundancy exclusion, and uniqueness are symbolic for all positive integer parameters in every dimension at least two. The nontrivial phase-realization step is separately proved using a derivative with one strict minimum, continuity under perturbation and integer scaling.

The bundled checker `verify.py` constructs the original full system of lower and subset-sum upper halfspaces, without assuming that the center is uniform. It numerically solves the largest-ball linear program via SciPy HiGHS in 121 parameter cases: twenty independent integral realizations of every target upper rank in dimensions two through six, one hundred two-parameter examples, and the explicit middle-rank witness. Every recovered radius matches the formula and the centers match the analytically unique center within documented numerical tolerances. It prints `ARBITRARY_PARKING_INBALL_CHECKS_PASSED trials=121 distinct_rank_phase_witnesses=20` on success.

Run `python -m pip install -r requirements.txt` and then `python verify.py` using the embedded files. Numerical optimization is finite corroboration, not an independent all-dimensional proof or an independent mathematical audit. The verification does not determine unrelated Euclidean invariants or establish exhaustive historical novelty.
