---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The positive tent vector makes the Rayleigh quotient universally 1/S_n (or (1-p_middle)/S_n). The exhibited p solves Mv=v/S_n; a path ground-state sum-of-squares proves it is the bottom eigenvalue; the node equations characterize all optimal faces. Direct newly constructed numpy matrices checked n=2..13 and 24 theta cases. This is a one-step objective, not an exact multi-step exponent.

## originality

PASS

Best-of-knowledge PASS: retrieved prior work establishes the row-sampling SDP and exact annealed exponent, but not this extra-endpoint tent-vector optimal face; indexed mirrored adjacent-coordinate theorem has different frame and objective structure. The complete historical E-optimal design literature was not fully inspected.

## value

PASS

PASS: the exact best expected one-step contraction and complete optimizer face are a motivated E-optimal row-selection problem for calibrated path measurements; the sharp parity-forced central omission is a structural phenomenon, not a routine SDP restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
