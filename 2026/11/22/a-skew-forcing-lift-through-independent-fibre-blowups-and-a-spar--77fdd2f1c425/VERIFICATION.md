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

The transfer is proved by two observations: no forcing process can first color one of two white false twins, and once there is at most one white vertex per fibre, every fibre contains a blue forcing vertex. Counting white neighbors of such a vertex is exactly the skew color-change rule on the base. The full-fibre projection proves both directions and the inclusion-minimal-set correspondence.

For cycles, skew forcing is equivalent to ordinary spread on the distance-two graph, which has one or two components according to cycle parity. The symbolic generating polynomials and the exponential 4-regular vertex-transitive construction follow without exhaustive computation.

Reproducibility: compile `verify.cpp` with `g++ -O2 -std=c++17 verify.cpp -o verify` and execute `./verify`. The program compares independently implemented ordinary and skew closure algorithms on every initial subset of every labelled base graph of order at most five (two-vertex fibres) and order at most three (three-vertex fibres), verifying both generating polynomials and minimality; cycle formulas are also exhaustively verified for the specified small parameters. It prints `ALL_BASE_GRAPHS_AND_ALL_SUBSETS_OK`, `CYCLE ... OK` lines, and `TRANSFER_MINIMAL_AND_CYCLE_CERTIFICATES_OK` on success. Such tests are finite checks, not a replacement for the all-order proof.

The underlying comparison with earlier papers and indexed mathematical results is provisional. Publication-priority uniqueness and independent mathematical validation have not been established.
