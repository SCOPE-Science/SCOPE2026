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
# Verification

The proof in RESULT.md supplies the unrestricted algebraic chart isomorphism, not merely numerical tests. `verify.py` is a standalone Python 3 standard-library checker: `python3 verify.py`. It enumerates every nonempty disjoint pair of row and column supports for matrix sizes \(m=3,4,5,6\), constructs the exact Jacobian linearization of every zero-diagonal two-by-two minor, reduces the integer 0/1 Jacobian mod 2, and compares the resulting tangent dimension with \(m-1+c\). Because the predicted answer is confirmed modulo 2 for each tested point, the check is a finite supporting test, not a proof of the complex ranks in all sizes. It also verifies the distinct codimension-one component count and a Segre-degree sum identity.

Actual invocation: `python3 verify.py`. Actual final output: `EXACT_JACOBIAN_AND_COMPONENT_COUNTS_OK 844`. The four per-size counts were 12, 50, 180 and 602, totaling 844. Reproducibility depends only on the embedded script and Python 3.

No independent audit has been performed. The origin completed local ring, nonreduced singular subscheme and global conductor at the origin remain outside the claim. The source's origin Hilbert--Samuel multiplicity is only a consistency check.
