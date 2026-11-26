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

Re-audited repaired RESULT.md and SLOGAN.txt. For the frozen fixed-box interpretation, the exact unrestricted count cannot be asserted: requiring every entrance point inside [0,L]^2 imposes n-w(L-n-1)≤z≤L+w, from the maximum event x=max(n,z-w) and maximum event y=max(n,n+1+(n-z)/w). The independent rational check gives 24 rather than 30 at n=6 for L=7, and a gap already at n=5 for L=6 (14 rather than 16). The corrected Finding explicitly uses full-line entrance orders for both exact counts and first gap, and retains only the upper bound and the obstruction uniformly under clipping. For an explicit padded box it correctly gives 30 in [0,37]^2: verified the CSV witnesses have event x≤37/4 and y≤36. The closed-prefix proof is sound for every L>n in the family and arbitrary interior grades in general: every event location dominates its prefix maxima, and every new grade in a closed-prefix chain raises a coordinate maximum, ensuring that the straight segment to the new maximum introduces that grade only at its endpoint and no unlisted grade. Antidiagonal closure is interval hull, giving the sum of endpoint-interleavings 2^(n-1). The sphere filtration is one-critical and its persistent homology has one essential bar per distinct positive degree; under the repaired explicit shared entrance indexing these degrees decode the entire order. For i<j, the strict sign of t_i-t_j is the sign of z-j-wi, so each strict order is constant in an open chamber of the M tie lines, and the standard intersection-count argument gives the quartic bound. The independent exact slab enumeration samples each open chamber, also covering any strict order realized at a slab boundary by openness. It yields 1,2,4,8,16,30 through n=6, with exactly the two displayed reflected obstructions, and confirms 638 at n=13. The analytic six-grade contradiction gives w>1 from the middle trio and w<1 from the last requirement. Any full-line witness fits in some padded square and hence has closed prefixes, so all first-gap comparisons are with the stated path-order sets. The uploaded checker was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the repaired joint path-versus-line theorem: the graded-barcode realization, the quartic-versus-exponential comparison and the exact six-grade full-line cutoff. The raw antidiagonal strict simplicial order count is directly covered by a matching catalogue theorem, and neither that count nor the general idea of line arrangements is claimed as new.

## value

PASS

The repaired theorem answers a natural finite-order question in the extended fibered setting and quantifies the information positive-slope probes lose in a canonical family. It gives a complete path-realizability criterion with a construction, then an explicit barcode family and a sharp first failure for full lines, rather than an arbitrary finite sample or an overstated resolution of the general counting question. This remains a substantive gap under sufficient padding, and the upper bound alone gives a gap for clipped restrictions as well.

The dated certificate retains the supplied scientific assessment, sources and limitations.
