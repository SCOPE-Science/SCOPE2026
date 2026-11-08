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

The mathematical argument in RESULT.md establishes the infinite-family claim. The computations here are finite reproducibility and model-consistency checks, not a substitute for the proof.

From the directory containing all embedded artifacts, run `python3 exhaustive_check.py` and `python3 local_check.py`. Expected success markers are `EXHAUSTIVE_OK` and `LOCAL_CHECK_OK`, respectively. The first checker exhausts all size-four subsets for \(5\le n\le12\), plus size-three subsets through \(n=9\). The second checker generates only the symmetry-orbit templates for \(5\le n\le60\), checks their closures and all legal token slides, and verifies the proposed token-jump paths for representatives.

The input graph is always the undirected Cartesian prism with \(2n\) labeled vertices and three neighbors per vertex. Each candidate move replaces exactly one selected vertex by a previously unselected vertex. All graph operations use the exact integer alphabet and no floating-point arithmetic.

The file content was checked for scientific scope and neutral publication wording. There is no external independent audit or scholarly certification.
