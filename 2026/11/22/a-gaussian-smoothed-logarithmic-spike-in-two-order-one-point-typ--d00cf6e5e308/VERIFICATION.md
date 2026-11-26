---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The repaired headline is the central coefficient asymptotic, not a finite-law originality claim. The two independent rank orders induce independent uniform new-point gaps independent of the reduced old permutation. Given the new coordinates (u,v), each old point disagrees independently with probability u+v−2uv, so the conditional-binomial formula and the factor (n+1)^2 are exact. The product of two uniform variables on [−1,1] gives the stated logarithmic density after transformation; polynomial parity gives the rational sum with denominators (2r+1)^2. The two gamma representations of the beta variable and the delta method give sqrt(n)(2B−1)⇒N(2s,1), including the floor. The maximum beta density is O(sqrt(n)) by Stirling at its mode, so the rescaled density is uniformly bounded; the log singularity contributes at most O(delta(1+|log delta|)), and bounded rescaled second moments control its positive tail. This yields the profile and −E log|Z|=(gamma+log 2)/2. For bulk fractions away from 1/2, the beta log density has a uniform order-n gap between its interior mode and a fixed neighborhood of the singularity, so the logarithmic integral over that neighborhood tends to zero. Independent check: at k=floor(n/2), under the even integral the density of 2B−1 is proportional to (1−x²)^floor(n/2) for either parity (the odd term cancels); the square has Beta(1/2,floor(n/2)+1) law. Thus M/(n+1)=sum_{j=0}^{floor(n/2)}1/(2j+1), checked by enumerating inversion degrees of all vertices of all permutations on n+1 places for n=1–7. This is supporting exact evidence only; the general profile follows analytically. The frozen checker was inspected, not executed.

## originality

PASS

The frozen record presents the finite exact law among its original findings, but that part is directly implied by the published independent-point permutation kernel and its explicit mixing density. The repaired RESULT and SLOGAN credit this implication and limit the originality claim to the fixed-offset central local asymptotic with its O(1) Gaussian-log correction. Best-of-knowledge pass for that remainder only.

## value

PASS

The worthwhile remainder resolves the natural microscopic singular window of a known global degree distribution. It distinguishes the order n log n central coefficient from order n bulk levels and resolves differences within the central window to additive order n, with an explicit nonconstant profile. This precise finite-size information is not supplied by weak convergence, a middle-vertex CLT, or an exact count at a few n. It concerns expectation, not concentration of an individual histogram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
