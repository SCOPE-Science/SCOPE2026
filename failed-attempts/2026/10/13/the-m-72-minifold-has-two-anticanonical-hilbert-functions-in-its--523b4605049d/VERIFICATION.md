---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With column coordinates and χ(x,y)=xᵗAy, Serre duality gives AS*=Aᵗ, and the shift by 3 gives T*=−A⁻ᵗA. The geometric-helix input is substantive: Loginov–Orlov give the periodic standard helix and state in the proof of Proposition 3.7 that the right dual of a full geometric helix also generates a geometric helix. For p>0 this kills the nonzero-degree Hom terms; for p=0 exceptionality suffices. Independent exact matrix replay from both printed matrices, without running the uploaded script, computed N=T*−I and found N⁴=0 for each. For the four right-dual terms the diagonals of ANᵏ, k=0,1,2,3, give the tuples (1,38,108,72), (1,146,432,288), (1,146,432,288), (1,38,108,72); they give (1,38,108,72) for every standard term. The binomial identity therefore proves the cubics for every integer p≥0, not just samples. Multiplying the resulting series by (1−t)^4 gives the displayed numerators (1,35,35,1) and (1,143,143,1). Both functions equal 1 at p=0; the claim is two distinct functions. Reviewed frozen RESULT.md lines 85–150, VERIFICATION.md, verify.py and VERIFY.txt; the matrix replay verifies pairings and does not replace the geometric-helix input.

## originality

FAIL

The right-dual cubics are not printed verbatim, but the same primary paper gives this exact right-dual matrix, the geometric-helix input and an exact general Hilbert-function formula, including how to form its matrix coefficients. The frozen result is the direct finite evaluation of those published results on their published example, rather than a new invariant requiring a further mathematical argument. This is implication coverage, not a claim that the authors tabulated the two right-dual cubics.

## value

FAIL

The distinction between Hilbert dimension and the full Hilbert polynomial is meaningful, but this exact narrow example is mechanically determined by already published matrices and the authors' explicit Hilbert-function formula. The record evaluates and compares those outputs; it does not supply a further obstruction, general criterion, or mathematically new input that would make the calculation an independently valuable exact finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
