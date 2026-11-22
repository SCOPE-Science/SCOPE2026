---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For n>=3 regular sites at equatorial azimuth 2jπ/n, uniform latitude z∈[-1,1] and longitude φ imply that at 0<r<π/2 a site covers precisely an interval of azimuth halfwidth L_r(z)=acos(cos r/√(1−z²)), for |z|<sin r. Counting lattice points in a random interval of length 2L gives P(K>=k|z)=clip(L/α−k+1,0,1) with α=π/n. The z-level endpoints are z_j=√(1−cos²r/cos²(jα)) if jα<r, else zero. Integrating and using primitive zL+B_r(z) yields T_k=(B(z_{k−1})−B(z_k))/α; p_k=T_k−T_{k+1}. Hemispherical parity and r↔π−r antipodal complement follow from lattice geometry. At r_k=(k−1)α, 2<=k<=ceil(n/2), L=r_k+ε−(cot r_k)z²/2+..., so integrating clipped parabola gives (2n/(3π))√(2tan r_k) ε^(3/2)+O_n(ε^(5/2)); p0 near π/2 closes with n tan(π/n)/(2π) ε²+O_n(ε⁴). Independent split-at-endpoints numerical integration checked n=3,4,7,12 and radii .45,.95,1.4. The first ordinary adaptive integration for n=12,r=1.4 had a narrow endpoint sampling error; split integration fixed it, not a theorem correction.

## originality

PASS

The closest published coverage results involve tetrahedral four-center caps and pair-contact exponents, or extremal dispersion/coverage of arbitrary spherical point sets. The n equatorial regular point set has a different latitude–longitude lattice structure; no inspected source gives simultaneous exact multiplicity p_0...p_n at all radii and every contact threshold. The two-level uniform lattice count is elementary and not claimed as novel; its all-depth integral, parity/complement laws and onset coefficients are the specific contribution.

## value

PASS

For a natural deterministic spherical design of any size, the full coverage-depth distribution is a precise geometric statistic with identifiable phase transitions and exact constants, beyond an elementary union-area special case. The all-k classification is reusable for coverage and discrepancy calculations; it is not an arbitrary truncated numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
