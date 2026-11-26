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

At each top-row extension of a suffix of rank r, the rows modulo its span are the orbit choices: one coset gives no rank increase, and q^(m-r)-1 increase rank. Equivalently the point transfer divides by q^r in both cases since the new row adds r to the affine orbit dimension. Suffix ranks and exponents are invariant under invertible unitriangular suffix operations. This yields the stated joint weight and exponent, not point-weighted counts. Moving each rank increase left of its latest possible stage gives the rectangle partition and the nonnegative defect. The weight divided by q^{k(n-k)} is at most q^{-defect}; both the partition series and its first moment converge for q>1. The latest centered pattern contributes at least half of q^{floor(n²/4)} by Bernoulli's inequality, including n=2. The centered Gaussian lattice estimates then bound both requested expectations uniformly in n, and the elementary bound on binom(R,2) yields the linear expected exponent error. Independent enumeration via elementary row-addition generators corroborated the joint census at (n,q)=(3,2),(4,3),(5,2),(6,2), and the two reported sample means follow from independent profile weights.

## originality

PASS

The supported distinct claim is fixed-q concentration under equal weighting of distinct left-action orbits, including the bounded mean defect and the 1/8 exponent. It does not claim the exact finite transfer, unrefined counts, unitriangular action, or the uniform-point exponent as new.

## value

PASS

The change from point weighting to equal orbit weighting changes the leading exponent by a factor of four. The result also locates the typical rank to bounded mean error and the orbit exponent to bounded mean defect relative to that rank, information beyond an unrefined orbit census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
