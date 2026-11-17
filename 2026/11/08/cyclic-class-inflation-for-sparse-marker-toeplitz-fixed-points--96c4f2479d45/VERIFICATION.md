---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For every k>=2, each factor of length kn in the fixed point of 0 -> 0^(k-1)1, 1 -> 0^k is a rotation by r<k of phi_k(u) for a length-n factor u, because each image block has k-1 leading zeros. All nonempty one markers in phi_k(u) have indices congruent k-1 mod k. Every input factor n>=2 contains zero since the fixed point avoids 11, so rotating images of two such factors to coincide forces a multiple-of-k shift, hence conjugacy of source factors. Different residues give k|C| target members and Parikh complement t -> n-t; handle two singleton classes at n=1 separately. Independent direct factor-set/class enumeration matched k=2..4, n=1..7 including class sizes.

## originality

PASS

The 2014 general cyclic-complexity paper establishes the number of length-k^j classes, not the all-length bijection and exact class-size lift. However a published November 2, 2026 theorem already proves the k=2 all-length factor-class bijection for the binary period-doubling word; credit this precisely. The new surviving all k>=3 sparse-marker generality, uniform k-fold class-size spectrum, exceptional n=1 lift, and Parikh iterates are absent from the read prior k=2 paper.

## value

PASS

Beyond the already-known dyadic class-count invariant, the exact factor-representative multiplicities and weight transport give a natural fine cyclic-complexity classification of a uniform substitution family. The marker-residue proof provides a reusable recognizability mechanism rather than a few isolated counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
