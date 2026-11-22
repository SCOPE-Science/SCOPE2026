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

# Verification record

The accompanying standalone `verify.py` was run with the standard Python interpreter and returned `PASS: 631 exact rational comparisons`. It also returned the independent five-cycle example value `378/95` at perturbation \(\epsilon=1/2\). The executable makes independent exact Fraction evaluations using (a) electrical parallel-resistance sums and (b) direct rational linear solves of Markov-chain first-hitting-time equations; these agree on the tested finite graphs.

The tested one-edge families cover every integer length \(3\le n\le23\) with eight rational positive conductances; the five-cycle descent uses eleven rational perturbations, and the triangle/four-cycle boundary cases use further rational examples. The proof in `RESULT.md`, not these finite runs, establishes the assertions for arbitrary positive real conductances and all integer cycle lengths in their claimed ranges.

No external or independent mathematical validation has been performed. The artifact's calculations assume exact arithmetic and strictly positive conductances; they do not establish a globally optimal nonuniform design for five or more vertices.
