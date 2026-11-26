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

For p>d, the exponential ratio is at most one, and splitting according to which of r,s is larger bounds the polynomial ratio by 2^p times (1+min(r,s))^(−p). Each resulting sum is controlled by the summable cubical shells, uniformly in n. On the axis, the defect vanishes exactly when 0≤j≤N and the transverse radius is at most min(j,N−j); this gives the displayed (2min(j,N−j)+1)^(d−1) slice count with counting measure. On the inner half 0≤j≤N/2 off this region, transverse radius j+h gives defect at least h and far factor (N+1)/(1+s)≤2. Summing h≥1 with e^(−ah) gives an O((1+j)^(d−2−p)) bound per j, whether the exponent is positive or negative. On the outer half-line j=−h the defect is at least h+max(h,‖z‖∞), so that sum is uniformly bounded; reflection gives the other half. The complete off-region bound is therefore lower order subcritically and O(1) at p=d. The bulk equality-region Riemann sum has the stated integrand; near 0 or 1 the normalized sum on an interval of width ε is O(ε^(d−p))+o(1). At p=d the summand on 1≤j≤N/2 differs from 2^(d−1)/j by O(j^−2)+O(N^−1), so both ends give exactly 2^d log N+O(1), without dependence of the leading coefficient on a. The packaged checker was treated as finite evidence, not used to prove an infinite tail or limit.

## originality

PASS

The strongest inspected family-level result treats only finite norm exponents and expressly excludes the cube, and the closest continuous density result has different norm geometry and normalization. The abstract RKHS/subconvolutivity criteria apply but do not evaluate this weight family. The supported distinct claim is the cubical iff threshold together with the exact axis leading orders and constants, not the general subconvolution criterion.

## value

PASS

The cube is the natural nonsmooth endpoint of the ℓ^q family. Its equality slices have full transverse size, changing the threshold and making the leading constants independent of the exponential scale. The proof turns that mechanism into an exact subcritical coefficient and a critical logarithmic residue, not merely a summability test or an illustrative truncated computation. The scope of the residue is axis directions and fixed parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
