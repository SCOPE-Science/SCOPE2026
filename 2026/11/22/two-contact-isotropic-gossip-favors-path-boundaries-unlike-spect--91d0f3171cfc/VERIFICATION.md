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

With centered covariance C=I−11ᵀ/n, the conditional two-contact loss for ordered edges e,f is tr(CP_eP_fP_e)=tr(P_eP_f)−1=n−3+(v_eᵀv_f)². The squared inner products are 1, 1/4 and 0 for identical, incident and disjoint edges. Equivalently the loss is tr((I−L_p/2)²)−1=n−3+tr(L_p²)/4. The unsigned incidence Gram matrix gives B_G≽I/2; the simplex KKT signs and normalization are correct. On the path the tridiagonal recurrence with zero exterior coordinates yields the displayed product of factors 1−r^i and 1−r^(m+1−i), all strictly positive; summing shows S_m/m→2/3 and hence both boundary and bulk limits. Subtraction gives q_1−q_2 proportional by a positive factor to r^(m−1)−r>0 for m≥3. For the separate gap benchmark the centered ramp gives an upper Rayleigh bound; the parabolic law attains it because its weighted Laplacian is triangular on polynomial-degree flags, with eigenvalues c k(k+1). Equality forces the centered ramp eigenvector and recursively determines the weights. At m=1 the only law gives loss zero, and m=2 is reflection-symmetric. At m=3 direct substitution gives losses 23/16 and 13/9, difference 1/144, with center-edge masses 1/4 and 2/5 for the two objectives.

## originality

PASS

The exact two-contact isotropic path optimizer and its alternating boundary profile relative to the spectral-gap benchmark are the distinct supported finding. Neither independent averaging projections nor weighted spectral-gap design are new. The strongest indexed match explicitly treats a prior two-contact path calculation with this same objective and a path-specific optimum as a supplied input, and describes its own contributions as the broader support threshold and resolvent. The passage does not give the exact prior title, but the specified objective and path optimum, together with its exact P4 benchmark, point to the assigned result; there is no separate closed-form boundary classification in the matched finding. Same-day dates do not establish order. No verified independent anticipation of the path boundary finding was found in the bounded comparison.

## value

PASS

The design distinction is structural, not the small numerical gain on P4: the unique finite-budget optimum reverses the first-two-edge ordering of the gap optimum on every path with at least three edges and has an explicit alternating, exponentially decaying boundary correction. That supplies a precise regime where standard spectral design uses the wrong spatial bias for the stated risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
