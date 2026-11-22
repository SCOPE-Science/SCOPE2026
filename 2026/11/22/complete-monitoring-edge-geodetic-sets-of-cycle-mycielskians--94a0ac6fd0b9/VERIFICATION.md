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

# Reproducibility checks and limits

The self-contained executable `verify.py` uses only Python 3 standard-library modules. It constructs \(H_n\) from its explicit original, shadow and apex vertex definition. For each edge deletion, a fresh breadth-first-search table tests whether the distance of a selected vertex pair strictly increases; this test is independent of the symbolic classification and uses no precomputed monitoring tables from the proof.

At all five orders \(5\le n\le9\), it evaluates each of the total \(698{,}368\) possible selected-vertex subsets and compares the actual monitoring predicate to the criterion that all shadows be selected and the selected originals form a cycle vertex cover. It reconstructs complete size distributions, all inclusion-minimal sets, all minimum sets, and their one-token jump and slide adjacencies. At \(10\le n\le15\), it additionally tests the exact claimed detector pairs for each shadow-edge type, including all rotations, using deleted-edge distances. The executable returns `VERIFY_OK` after these assertions succeed. To replay, run `python3 verify.py` in the directory containing the extracted artifact.

The infinite-order claim is established by the symbolic detour, unique-geodesic, and cyclic-gap arguments in `RESULT.md`, not by finite enumeration. The checker does not verify every subset at orders beyond nine and does not constitute independent mathematical or publication-priority certification.
