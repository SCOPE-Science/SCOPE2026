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

# Verification evidence and limits

For each integer \(N\) from 2 through 7, the file `verify.py` constructs the two explicit Bloch-vector layers and checks unit row norms, each centroid, and every off-diagonal sum of dot products against \(-2/(N-1)\). It additionally checks the three matrix identities \(U^{\mathsf T}U=V^{\mathsf T}V=(7/3)I_3\) and \(U^{\mathsf T}V=0\) for the seven-point configuration. Command executed: `python3 verify.py`. Observed output: `PASS: 229 assertions for N=2,...,7; seven-point orthogonal 2-design split.`

The standard-library checker uses floating-point arithmetic and \(10^{-12}\) tolerance. It is not an exhaustive search of arbitrary frames, and it does not prove the dimension bound or the converse classification. The universal conclusions instead follow from the exact Pauli trace identity, the rank of the centered regular-simplex Gram matrix, the explicit trigonometric sums in RESULT.md and the rank/trace positive-semidefinite argument.

Prior-mathematics comparison is relative to the accessible primary manuscript and targeted record searches described in REVIEW.md and AUDIT.json. A prior equivalent formulation may exist in older geometric frame theory. This is a self-review, not an independent mathematical audit.
