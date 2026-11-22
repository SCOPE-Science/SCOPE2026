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

The proof gives explicit matrices for all levels, exact rational generating functions, and algebraic closed forms for the zero-residue counts. The nonperiodicity of the nonreal eigenvalue phases is justified by the algebraic-integer obstruction to \(2\cos(2\theta)=-3/2\).

The included `verify.py` uses exact integers and directly enumerates both projective trees through depth \(15\); it also compares the generating-function coefficients with matrix iterates through depth \(80\). Execution of the included script: `PASS: 1138 exact assertions`. This is a finite regression check, not an infinite proof or independent audit.

No computation establishes literature uniqueness. The referenced published residue-pattern studies were compared by their publicly accessible abstracts/summaries, with full-text comparison still a residual priority risk.
