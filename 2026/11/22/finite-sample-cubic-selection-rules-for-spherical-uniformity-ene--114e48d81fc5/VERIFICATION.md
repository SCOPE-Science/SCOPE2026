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

# Reproduction and scope

Run `python3 check_harmonic.py` with the Python 3 standard library. The executable computes each triple Legendre integral in exact rational arithmetic by a separately implemented recurrence and compares it with the Wigner factorial expression at degrees one through eight, including all vanishing/parity cases. It also enumerates all vertex-tuples of a regular icosahedron with two, three, and four draws and checks means, second moments, and the selected mixed and pure third moments numerically. A regular icosahedron is a spherical five-design, and the checked integrands have degree at most four per sampled position. The run passed 1,562 assertions; design computations use a floating-point tolerance of \(2\cdot10^{-9}\).

The general theorem for arbitrary degrees and sample sizes follows from the kernel identities, graph classification and Gaunt integral proved in RESULT.md, not from finite tests. No external independent audit or empirical sample-level calibration was performed.
