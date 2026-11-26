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

Schoenberg gives uniformly convergent nonnegative mixtures of R_m=U_m/(m+1), and the Bernstein operator is bounded in the uniform norm. Expanding by parity and U_k gives the low-degree formulas in RESULT.md. At n=3 the bound 3/(2 sqrt(2)(m+1)) controls both small coefficients after m=0,1. At n=4, U_m(1/2) is periodic with values in {0,±1}; U_m(0) is 0 for odd m and ±1 for even m. The even m≥8 bounds are strictly positive; direct substitution of m=0,2,4,6 and of the odd case m=1 gives the claimed zero sets. For the obstruction, the nth alternating binomial sum on the centered grid annihilates degrees <n. Its (n+2)-moment divided by its nth moment is (n+1)(n+2)/(6n), from the first two nonzero Taylor coefficients of (2 sinh(z/n))^n. Combining the two leading monomials of U_{n+2} and dividing by the leading coefficient of R_n gives the stated strictly negative eta_n for all n≥5. The S² contrast follows from the negative P_4 coefficient −9/256 of B_4 P_6. Fresh replay: python3 /workspace/replay/sphere_bernstein.py (548 exact low-degree basis images and 26 obstructions; the all-index proof is analytic).

## originality

FAIL

A distinct indexed result, 3785c4062726, establishes the same affine operator threshold for every d≥2, with a strictly stronger positive conclusion. The frozen headline is exactly its d=3 specialization. This is statement-level coverage, not a claim that the later-dated entry had historical priority. Its inspected passages do not list the frozen mode-specific zero sets; these are direct coefficient evaluations and do not sustain a separate substantive repaired finding. The antecedent high-degree obstruction is not credited as new to the frozen record.

## value

PASS

As a mathematical question, the exact boundary distinguishes approximation degrees safe for every zonal covariance kernel from those admitting a concrete counterexample; S² failure is not a substitute for the S³ classification. This does not restore originality: with the threshold covered, the remaining zero-set arithmetic alone does not warrant a repaired standalone claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
