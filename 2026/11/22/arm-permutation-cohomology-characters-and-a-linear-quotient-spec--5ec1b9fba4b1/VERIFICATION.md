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

The simultaneous arm permutation preserves the stated lattice and acts naturally on the Nomizu model after extension to real coefficients. In the splitting by the presence of a, d is precisely a wedge the degree-zero replacement z_i -> x_i; image subtraction gives equal kernel and cokernel characters. For each sl_2 isotypic component the permutation acts on the multiplicity space, and that same space occurs once both in ker E and in the sum of weights 0 and 1. A length-l cycle contributes the stated two determinants. Independently, on arm invariants let X=sum x_i, Z=sum z_i, W=sum x_i z_i. For degrees 2j the invariant basis is W^j (0<=j<=n), with XZW^{j-1} also when 1<=j<n; in degrees 2j+1 it is XW^j,Z W^j for 0<=j<n. This follows by symmetrizing the empty, double and two single local wedge types, with each odd type usable at most once; over Q the symmetrized two-single component of XZW^{j-1} is nonzero for j<n. E vanishes on the even space and sends the second odd generator to the first, proving the stated plateau and 6n total after the (1+t) factor, including n=1. Barycentric subdivision of an equivariant triangulation removes simplex inversions so invariant cochains compute ordinary rational orbit-space cohomology. Inspected RESULT.md, VERIFICATION.md and checker.py; the latter checks modular traces only and was not run. No integral, ring or Borel claim is verified.

## originality

PASS

Pass applies to the graded arm-permutation characters at arbitrary cycle type and the resulting ordinary rational orbit-space Betti formula, not to the cohomology dimensions of the covering star nilmanifold. The strongest inspected published work with the same stars gives those covering-space dimensions, while the closest ancillary symmetry calculations concern other graphs. No equivalent or stronger covering theorem was established on the evidence searched.

## value

PASS

The automorphism group is intrinsic to the star and its explicit symmetric lattice. The cycle formula answers the naturally equivariant cohomology question for every permutation and, by restriction and averaging, for all arm-permutation subgroups. The 6n total with its exact degree plateau contrasts with exponential covering-space cohomology and is not obtained from the known nonequivariant dimensions or a single small graph computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
