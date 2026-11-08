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

# Reproduction and limits

The standalone `verify_nodes.py` requires only Python 3's standard library. Run `python3 verify_nodes.py` from the directory containing the extracted file. It computes each intersection of the nine Lucas parameter lines, checks exactly twelve double intersections and eight triple intersections, constructs all eight base support vectors, and verifies that each yields thirty-two projective sign lifts. Using exact rational elimination, it computes each parity-character evaluation block of every homogeneous degree through five and confirms ranks \(1,9,39,109,206,256\), with missing degree-three supports `BMG` and `DME`. The run printed `PROJECTIVE_NODE_HILBERT_FUNCTION_OK` and `SATURATED_IDEAL_REGULARITY 6` with no assertion failures.

The rank calculation is an exhaustive finite computation over \(\mathbb Q\) of explicitly defined matrices, not a probabilistic experiment or evidence for an unbounded extrapolation. The proof of all higher degrees uses multiplication by a linear form avoiding the finite node set. The local ordinary-double-point classification is prior geometry; the computation concerns the reduced support. The cited primary paper establishes the surface and singularity count, not the postulation now calculated. Independent validation has not been performed.
