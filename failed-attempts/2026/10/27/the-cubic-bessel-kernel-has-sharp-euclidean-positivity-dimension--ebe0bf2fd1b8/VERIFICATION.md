---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The assertion and certificates are correct. The circular characteristic function is J0(a|x|), and the threefold convolution gives planar positive definiteness. For a=1, a hypothetical 3D radial law has one-coordinate characteristic function J0(r)^3, the transform of the law of the sum of three independent cosines of uniform angles. This coordinate is supported in [−3,3]. Conditional on radius t in 3D the coordinate is uniform on [−t,t]; thus the radius cannot exceed 3 with positive probability. The same bounded-support argument holds in 4D, since a conditional coordinate has positive density on (−t,t). All required Taylor moments therefore exist, and the sinc series in 3D or the series of 2J1(r)/r in 4D gives the stated hypothetical moments. Independently replayed with python3 /workspace/audit_bessel.py: the twofold binomial sum from Vandermonde gives A_k; scaling the 3D Hankel by the diagonal 4^i makes it integral for fraction-free elimination. Dividing the resulting determinant by 4^42 gives −59778222499952939497463042623250744763/302231454903657293676544; the 4D determinant is −27756. Both negative polynomial-square evaluations also match, including −10794 in 4D. This contradicts a necessary positivity condition for an actual measure. Dilation handles every a>0 and restriction handles higher dimensions. In arXiv:1502.07179v1 Remark 4.4 the conjectural lower inclusion at n=2,k=3 is indeed in Phi4, not a theorem. This review does not claim that the later literature stated the counterexample in the same terminology.

## originality

FAIL

Earlier exact results imply the sharp cutoff in an equivalent formulation. The one-coordinate law with transform J0^3 is the nearest-neighbour simple-cubic density of states after rescaling. Igoshev–Irkhin report its maximum at the off-centre X energy for the small-next-neighbour regime that includes zero. The known moment recurrence implies that this density is not constant on the intervening central interval. It therefore cannot be the nonincreasing uniform-mixture density forced by a 3D radial extension. Earlier planar density results also imply the weaker Phi4 obstruction separately. The independently reproduced Hankel calculations supply a different certificate, not a new sharp cutoff.

## value

FAIL

Sharp extension bounds for radial kernels and testing a published conjecture are motivated. But here the sharp bound is already implied by prior exact results for the equivalent law, and the weaker refutation of Phi4 follows even more directly from the known planar singularity. The frozen result's alternative valid computation does not establish a separately motivated exact invariant such as a minimal certificate order or a bound on finite witnessing configurations. No independently valuable surviving claim was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
