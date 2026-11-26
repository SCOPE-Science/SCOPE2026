---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The filled-hub equation eliminates b for eigenvalues below q. On the full leaf cube the eliminated operator is H_leaf−μI+(μ−λ)P_star, with μ=λ(1−λ)/(q−λ). For 0<λ<λ* the second eigenvalue is positive by min–max and the constant Rayleigh quotient is negative, so the operator cannot have a kernel. At λ* the pairing with the centered sum of leaf occupations forces g(star)=0, because the evaluation of the sum is nq and its product weight is p^n. The degree-one leaf spectrum then gives precisely the n−1 sum-zero contrasts; reconstruction is one-to-one and leaf averaging vanishes. The three-state n=1 chain has eigenvalues 0,q,2−q. Eighteen independently assembled symmetric matrices (n=1 through 6, q=0.16,0.5,0.84) agreed in first nonzero eigenvalue and multiplicity at tolerance 1e−10; the proof does not rely on them.

## originality

PASS

After removing the novelty claim for the gap value and the existence of the contrast family, the supported distinct claim is the exhaustion of the gap eigenspace, ruling out any other slow modes at that exact eigenvalue. The closest exact source does not show this. This is not a priority claim.

## value

PASS

Identifying the whole gap space, rather than giving a single slow branch, determines which observables can decay at that rate. In particular every permutation-invariant observable misses all gap modes at finite n; this distinguishes radial relaxation from arbitrary relaxation without a total-variation claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
