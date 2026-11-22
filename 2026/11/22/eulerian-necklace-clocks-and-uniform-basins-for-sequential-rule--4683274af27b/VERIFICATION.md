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

The proof uses an exact symbolic copy-source correspondence for every sequential update order, followed by the finite-dimensional rotation conjugacy, uniform one-sweep fibers, Möbius inversion and Eulerian permutation enumeration. For random schedules, cyclic ascents satisfy a standard one-dependent central limit theorem and proper binary subperiods are exponentially rare.

Run `python3 verification/verify_formula.py` to check all scan permutations through eight sites, including source map and cyclic-ascent enumeration; successful output ends in `FORMULA_CHECK_OK`. Run `python3 verification/check_exhaustive.py` to independently classify the entire functional graph of every scan permutation through seven sites; successful output ends in `BRUTE_FUNCTIONAL_GRAPH_OK`. The recorded output text is supplementary. These checks were executed from the exact packaged paths, and finite computation is not substituted for the all-size proof. No independent external validation has been performed.
