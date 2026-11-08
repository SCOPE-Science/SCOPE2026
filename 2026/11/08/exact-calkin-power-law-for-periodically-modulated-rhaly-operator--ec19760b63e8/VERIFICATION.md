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

The standard-library-only checker `check_periodic_cesaro.py` was executed directly with Python 3 and reported 2,884 successful finite identities and diagnostics. Its direct rational-arithmetic matrix calculations verify the formulas for finite Cesàro-sandwich entries and weighted Gram entries, using five periodic coefficient patterns and five finite matrix sizes. Four lower-bound Cesàro packet norms were checked numerically.

The universal statements do not follow from finite testing. Independently inspect the explicit infinite sums and their summability in the proof: a periodic mean-zero cancellation estimate produces the Hilbert–Schmidt identity \(CD_cC-mC^2\in\mathcal S_2\); the same argument applies to the Gram sandwich. The weakly null packet argument proves the essential norm of the ordinary Cesàro operator, and the direct selfcommutator estimate proves its essential normality. The quotient algebra identities then imply the stated power law and the square-zero example.

Boundary conditions checked in the proof: \(q\ge2\); complex periodic coefficients, including zeros; nonzero mean-square \(\mu\); integer power \(p\ge1\); and the separate interpretation of \(|m|^0\) at \(p=1\) when \(m=0\). No full essential-spectrum formula for \(m\ne0\), no nonperiodic extension and no independent audit are claimed.
