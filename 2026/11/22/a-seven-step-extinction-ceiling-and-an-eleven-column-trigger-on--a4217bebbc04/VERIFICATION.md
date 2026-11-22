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

The self-contained exact verifier is `verify_bdd.py`. Run `python3 verify_bdd.py`; all 13 lengths from 1 through 13 have a zero decision-diagram root for the assertion that excitation persists to time six. The program obtains sharp times `3,3,4,4,5,5,6,6,6,6,7,7,7`, replays each witness directly, enumerates every initial coloring for the first three lengths to cross-check Boolean population counts, verifies the exact critical eleven-column count `1265544`, and checks that time-five excitation on eleven columns is confined to the middle column in the two outside rows. All assertions were executed successfully.

An independently encoded SAT verifier is `verify_smt_optional.py`, using a system installation of libz3. Running `python3 verify_smt_optional.py` successfully reproduced the same thirteen sharp times and excluded excitation at time six. This secondary tool is optional: the full finite certificate needs only the standard Python library and `verify_bdd.py`.

The all-length deduction uses a separate formal locality argument: a time-six state on any three-row strip depends only on a horizontal radius-six window, including its true endpoint status. The finite lengths up to 13 cover every possible local endpoint geometry. The lower-bound eleven-column witness is immune to arbitrary extensions outside its radius-five cone. Thus finite checks are used only as exhaustive local lemmas, not as evidence that enumerating thirteen graph sizes automatically proves a theorem about all sizes.

Neither independent outside audit nor a machine-certified formal proof is claimed. The output excludes other strip widths, other thresholds and other refractory lengths.
