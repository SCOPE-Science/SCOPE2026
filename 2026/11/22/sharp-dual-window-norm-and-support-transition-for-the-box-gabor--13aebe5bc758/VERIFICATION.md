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

For a.e. x in [−1,0), the Bessel cross-duality identity at alias n has the sum over integers k with −1<x+k+n/beta<1 (the sign of n and conjugation convention do not affect this real box condition). At n=0 it is h_0+h_1=beta. For delta=1/beta−1, on I=(delta−1,−delta) the ±1 equations force h_(−1)=−h_0 and h_2=−h_1; the +1 equation still couples −1,0 on the left, and the −1 equation still couples 1,2 on the right. Thus the l1 costs and nonzero coordinate counts are at least beta and 1 on the outer intervals, 2beta and 2 on I. Tonelli gives 4beta−2 and 4−2/beta without any preliminary support restriction. Equality in the l1 bound eliminates all uncounted coordinates and fixes a common phase in the triangle inequality, hence h_0,h_1 are nonnegative real where they can coexist. Equality in support instead forces exactly one nonzero pair on I and one coordinate on each outer interval, fixed in value by the equations. Every displayed candidate is bounded with compact support and therefore Bessel. Directly, the remaining ±1 equations on the tails involve only vanishing entries. At n=2 only k=−1 from the displayed range can contribute, and only for x<−2delta; at n=−2 only k=2 can contribute, and only for x>2delta−1. These ranges miss I by delta>1/3. For |n|>=3 the shifted box misses the whole supported index range. This verifies actual reconstruction and attainment, also for irrational beta. A mixed 0<u<beta fiber adds two nonzero sites to the minimal count; precisely endpoint choices of u (not a claim that h itself only takes two values) minimize support globally. The explicit two-block h_* is obtained from u=beta and has the stated measure and norm.

## originality

PASS

The joint exact minima and global equality classes of the discontinuous box on this open interval are not stated or implied by the inspected supported-window theorems. General l1 reduction and the compact-dual parametrization method are established; the distinct mathematical work is the exact two-alias optimization and unrestricted support-minimizer classification. The cited Lemvig–Nielsen title should end in ‘optimal smoothness’; for the general l1 reduction in the retrieved 2026 preprint use pp. 19–20 rather than the frozen ‘Remark 3.4’ label. These bibliographic details do not change the claim.

## value

PASS

The density interval is the natural first phase in which both neighboring aliases constrain a positive-measure set of fibers. Exact cost and support laws for this canonical generator and the full minimizer family, especially the distinction between l1 optimality and sparsity, are useful benchmarks not provided by compact-support existence or a generic LP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
