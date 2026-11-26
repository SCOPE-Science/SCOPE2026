---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

After one iteration every point is integer, so a primitive pair can be written x,x+k with x an integer and k>0. Putting d=2-epsilon, the two floor inequalities intersect exactly at mu-k-1+epsilon k < d x <= mu-k. This both proves the strict cutoff k<1/epsilon and gives at most one pair for each k. Conjugacy by integer translation gives period d. Put p=k mod 2. Modulo one in v={mu/d}, the allowed interval starts at p/2+epsilon k/(2d) and ends, exclusively, at p/2+(1-epsilon k/2)/d; the latter is at most (p+1)/2 since k>=1. Hence there is no wrap, only matching parity is possible, and intervals nest within each half. The mth interval in each half gives the survival length; adding lengths and summing over k=1 through ceil(1/epsilon)-1 gives the stated mean, including reciprocal-integer cutoffs. For w equal to phase within a half, the matching parity lattice with mesh 2 epsilon is cut off by epsilon k<=2dw and epsilon k<2(1-dw). The smaller cutoff is at most one, and if it equals one the strict inequality excludes the potential endpoint. Counting either lattice differs from cutoff divided by its mesh by at most one, including when an endpoint is excluded. Thus epsilon times the count differs from min(dw,1-dw) by at most epsilon; replacing d by 2 adds at most epsilon/2. Under uniform phase the four linear branches yield F uniform on [0,1/2], with CDF Lipschitz constant two, so the coupled CDF error is at most 3 epsilon. At epsilon=1/4 and k=3 the lower offset 5/4 indeed admits {-1,2}, while at offset 3/2 the strict upper test excludes this gap. This is a closed argument for all stated real parameters, not an inference from the finite frozen check.

## originality

PASS

Fixed-offset cycle enumeration is already known for the exact family and directly gives the same positive-gap floor differences. The distinct result is the exact law and uniform singular-limit profile over offset. This uses an analytical reduction of correlated gap events to two disjoint nested families, not a claim of a new classification of periodic points. The strongest indexed same-family overlap concerns the distribution of basins over states and settling from remote initial states, rather than the distribution of the number of primitive cycles over offsets.

## value

PASS

Near a unit negative slope, the known fixed-parameter counts alone do not show how typical or uniform the growth is as offsets are varied. The nested-window description gives all finite survival probabilities and a deterministic phase profile distinguishing offsets with very different growth. A uniform error also controls every discontinuity and implies a quantified distributional limit. These results characterize meaningful parameter sensitivity of a standard quantized dynamical system beyond reenumerating its periodic points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
