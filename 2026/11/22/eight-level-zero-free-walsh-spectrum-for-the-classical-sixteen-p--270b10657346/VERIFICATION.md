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

Run `python3 verify.py` with Python 3 and no third-party packages. Two independent affine-plane constructions must coincide with exactly 140 blocks. Gaussian elimination establishes an eleven-dimensional incidence code span. An exact integer length-65536 Walsh–Hadamard transform checks every signed multiplier, the analytic class multiplicities and all zeros (there are none). Applying a second integer Walsh transform to the reciprocal multipliers, scaling by 3360, checks the complete inverse kernel and its absolute sum.

Expected final line: `PASS: inverse l1/linfty norm = 3617/840`.

The generator parameterization covers all 65,536 characters, not sampled characters. The completeness of the binary transform is a deterministic finite theorem: at each stage, pairwise sum and difference replace the two-point Walsh transform along one coordinate; induction through all sixteen coordinates computes every character sum exactly. Walsh involution yields the reciprocal inverse. This verifies the stated finite sixteen-point claim only. No higher-dimensional existence, asymptotic behavior or independent audit is certified.
