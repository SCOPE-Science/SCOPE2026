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

The theorem is proved by reducing the labelled crown adjacency in characteristic three to the two modules \(J-I\) and \(I-J\). When the matched-pair count is divisible by three, the all-ones matrix is nonzero square-zero, giving two size-two spatial Jordan blocks. The eigenkernel calculation proves their lifted time modules are size-four Jordan blocks at the two signs, rather than two size-two blocks. The normal forms determine every fixed power and the exact global order. Möbius inversion gives every primitive temporal orbit count.

`verification/verify_matrix.py` is standalone Python 3 using only its standard library. Run from the root with `python3 verification/verify_matrix.py`. `verification/verified_output.txt` records the actual successful execution: 216 modular rank/nullity checks for graph sizes 5 through 10 at all times 1 through 36, strict global-order checks, and 360 separately coded direct neighborhood trajectories. Field extensions inherit the prime-field Jordan decomposition. The finite checks are sample corroboration, **not** a substitute for the all-parameter mathematical argument.

Independent mathematical assessment has not been performed; residual literature-priority risk is described in the scientific review.
