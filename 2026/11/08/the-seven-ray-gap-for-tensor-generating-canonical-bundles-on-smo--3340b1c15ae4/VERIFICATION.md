---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact checks and their scope

Run `python3 verify.py` with Python 3 and no dependencies. It prints three `*_OK` or `EXACT` markers and exits successfully. The certificate works with cyclic sequences of integer-affine functions \(c n+d\) rather than substituting a finite collection of Hirzebruch parameters. It enumerates the exact self-intersection replacement rule for every admissible star subdivision from the two minimal classes, using four steps after \(\mathbb P^2\) and three after \(\mathbb F_n\).

It yields \(13\) cyclic/dihedral sequence classes from \(\mathbb P^2\), all containing \(-2\); the \(21\) formal classes from \(\mathbb F_n\) all contain \(-2\) for \(n=0,1,2,3,4\), and all contain a constant \(-2\) term for \(n\ge5\). The latter argument is symbolic over all integers \(n\ge5\), not merely over the checked small values.

The checker also verifies cyclic determinant-one conditions and self-intersections for the displayed eight-ray fan, verifies the nine-ray subdivision, and repeats the two-subdivision growth operation twelve times for each base. The unrestricted growth theorem is the algebraic local identity in `RESULT.md`, not an inference from twelve tests. The categorical equivalence relies on the published toric criterion, and the minimal fan classification is standard. No independent external audit was performed.
