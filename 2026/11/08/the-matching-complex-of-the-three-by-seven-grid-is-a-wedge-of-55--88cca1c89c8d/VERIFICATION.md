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

Run `python3 verify_grid7.py` in a directory containing only that script. It uses standard-library modules and no network, hidden data or earlier artifacts. Output generated from the exact graph is saved in `grid7_verify_output.txt`.

Checks performed: 32 graph-edge construction, exhaustive enumeration of 196785 simplices including the empty one, 98361 augmented face pairs, 196785-node matched Hasse DAG topological sorting, 196784-node nonempty DAG topological sorting, 59 critical degree-six cells and four degree-seven cells, complete signed integer Morse boundary, explicit determinant-one minor on rows (5,9,15,16), a separate mod-two elimination obtaining rank four, and reduced Euler characteristic 55. Every assertion must succeed before the `GRID7_MORSE_OK` output.

The computation is exact and exhaustive for this finite simplicial complex. It is not evidence of an all-length grid classification. The public scientific claims receive self-review only; independent audit has not been performed.
