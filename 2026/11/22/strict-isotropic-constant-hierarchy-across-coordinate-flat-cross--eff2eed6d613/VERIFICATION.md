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

For a sector with j positive coordinates, integration against √m δ(sum y_i) gives mass density √m s^(m−2)/[(j−1)!(m−j−1)!] on 0≤s≤1/2. With multiplicity binom(m,j), the sum of the weights without √m equals binom(2m−2,m−1)/(m−2)! by Vandermonde. The weighted mean of 1/(j+1) equals (2m−1)/[m(m+1)], since dividing binom(m,j) by j+1 gives binom(m+1,j+1)/(m+1) and the second Vandermonde sum is binom(2m−1,m). The two independent simplex blocks and E(s²)=(m−1)/[4(m+1)] therefore give the claimed trace of B_m. Permutations make the covariance scalar on the zero-sum space. For k=n−m>0 the free block has norm radius Beta(k,m), by the shell density R^(k−1) times (1−R)^(m−1); the norm fractions of its k signed coordinates have Dirichlet(1,…,1) magnitudes. Its Beta second moments scale the two blocks exactly as claimed and independent sign symmetry kills the cross terms. The volume integral and the covariance reduce directly to the asserted ratio, also at k=0 by using B_m itself. Writing f_{m+1}/f_m=1+δ_m, the coefficient bound binom(m,j)≤m(m−1)^(j−1) gives a geometric majorant; 1−(m−1)δ_m=(2m²+1)/[(2m−1)(m+2)]>0. The positive margin displayed in RESULT.md exceeds that majorant and 1−r_m²=(3m−1)/(4m³)>0. These are proofs for every admissible m, not finite extrapolation. Replayed both margins and the denominator identity in `python3 /workspace/checks/independent_01_05.py` (check 2). The 1,058 checks in frozen VERIFICATION.md are recorded, not independently rerun.

## originality

PASS

The supported distinction is the strict intermediate-rank covariance-determinant/volume ordering with exact adjacent certificate, not the type-A base moments, the endpoint comparison or the general methodology of polytope integration. The volume-only companion has independent elementary mechanisms and does not carry the originality verdict by itself.

## value

PASS

Support rank is a canonical indexing of the flat-normal sections. The exact inequality completes their order by an affine invariant, beyond static endpoint classes or Euclidean volume comparisons. The dimension-separated adjacent ratio and short strict certificate provide a reusable comparison across ambient dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
