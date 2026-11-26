---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed all 49 support histories from the simultaneous rule, computing recurrence by repetition and, separately, the color permutation around each recurrent support cycle. A full state cannot be periodic before support recurrence. At support entry the lap map on each support is onto, hence a permutation; because each supported color occurs, its order gives the exact multiple of the support period required to restore every labelled vertex. The recurrent cases have (support period, lap order) (1,1), (1,3), and (2,2), as claimed. Weighting support cardinalities by the numbers of surjections onto the prescribed colors verified every coefficient, including all zero classes, for positive shore sizes. The sole t=4 class is all-rest with coefficient 2u+2U+v+V, positive outside K_(1,1); the singleton-only restriction has two states of depth three. Replay: python3 /workspace/audit_evidence/excitation.py. This is an exact proof of the uniform census, not extrapolation from the recorded direct tests.

## originality

FAIL

A distinct indexed result gives the same ten labelled first-entry/least-period populations on precisely the same graph family and rule, as well as the sharp cutoff, the extinction-only fourth layer and absence of transient approaches to three-cycles. Its formulas are exactly equivalent under renaming and expansion. A second distinct catalogue item also includes the same census as its GHM half. This establishes statement-level coverage independent of any claim about authorship or chronological priority.

## value

FAIL

The labelled depth of a dynamical basin is a meaningful invariant, but this frozen claim computes exactly the joint table already explicitly available. Presenting the table as a two-variable polynomial is a direct re-encoding and does not supply a new calculation or structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
