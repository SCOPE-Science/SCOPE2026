---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

By signed rearrangement the support function is sum_j(2j-1)|u|_(j), and central symmetry doubles it for width. On a stratum with >=2 distinct positive magnitude levels, the restricted support is a positive linear functional on a sphere of block levels: nonstationary points descend and the only stationary point is a strict maximum on that stratum; hence no other minima. At a single positive level with support k, for tan(theta)<1/(2sqrt(k)) the perturbed positive coordinates stay above all formerly-zero absolute coordinates, so the width separates exactly into base width cos(theta) plus active block A_k(a)=sum_{i<j}|a_i-a_j| and inactive C_m(z)=sum_j(2j-1)|z|_(j). Zero-mean upper-step decomposition gives A_k(a)>=sqrt(k(k-1))||a|| (k>=2); nonnegative sorted upper-step decomposition gives C_m(z)>=min(2m-1,m sqrt(m))||z||. Pure one-coordinate-split or inactive indicator rays attain sharp slopes, and orthogonality forces the smaller term. Integer comparisons yield strict switch k<2m vs k>=2m for 2<=k<n without ties. In open signed Weyl chambers the support is linear and all local maxima are its normalized signed-weight gradients; zero/tie perturbations increase support to first order, excluding boundary maxima. Sharp global minimum is axes for n>=3 and equal full-support vectors for n=2. Independently verified squared step inequalities, attaining rays and switch for n<=29; universal classification uses the analytic step decomposition, not those finite checks.

## originality

PASS

The concrete external and published-record searches compared mathematical statements, operator domains, norms and implied subcases, not simply titles. Closest strong antecedents were read to their stated scope. No earlier theorem subsuming the final exact result was established. This is a best-of-knowledge conclusion, not priority certification; disclosed archival and nomenclature risks remain.

## value

PASS

The fixed type-B orbit body's complete spherical width critical-point landscape and exact angular stability slope are natural quantitative geometric invariants. The support-level classification and new active-coordinate-splitting versus zero-activation threshold give precise robustness information absent from existing fan/facet counts and the different type-B roundness optimization. All dimensions and supports are handled by a uniform structural formula rather than isolated numerical cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
