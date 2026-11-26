---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructed for the stated d>p+2 and p not dividing B=d−1. At s=1/u=0 the equation is v^p+sv=sf(1/s). Any root has negative valuation, so the p-th power term uniquely dominates sv and v has s-valuation −B/p. The denominator forces local degree and ramification p; this also proves irreducibility and leaves one place above infinity. The affine derivative in v is 1. For finite u and a pole of v, b=1/v gives u+b^(p−1)=f(u)b^p, which forces u=0 and has one smooth formal solution with u=−b^(p−1)+O(b^p). Both places map to [0:1:0]; losing the affine chart requires a pole of u or v, so the list is exhaustive. In (a,b)=(u/v,1/v) the orders are (p,1) and (A,B), A=B−p>1. Extraction of an A-th root of a unit yields a=t^A; in the cusp branch's Weierstrass basis 1,b,…,b^(A−1) over k[[a]], the summands have distinct valuation classes mod A. Thus the cusp semigroup is exactly <A,B>; the smooth branch equation a=−b^p+O(b^(p+1)) has order A on it. Its semigroup gaps number (A−1)(B−1)/2. The intersection adds A to delta and to each intrinsic conductor exponent, since elements supported on one component are the other component's equation times elements of the branch ring, and the maximal normalization ideal contained there is that factor times the branch conductor. This gives total delta, genus, the stated (3,2) example and the two rational places over the prime field (both individually Frobenius-fixed). Reviewed the integer checks as limited corroboration, not a source of the branch proof.

## originality

FAIL

A distinct indexed record, a243edd42b3d, explicitly proves the same embedded calculation for arbitrary polynomial f under hypotheses containing the entire assigned range, and states the same maximal-family data in its Finding. This is demonstrated scientific coverage, not a finding of earlier chronological priority. Both records have the same displayed date. The independently verified formulas are not false, but no distinct substantive remainder is left in the assigned claim.

## value

FAIL

The ordinary plane model and conductor multidegree are well motivated and would be useful for adjunction or normalization computations. But the assigned exact classification, including its general-f range and maximal-family examples, is covered by the existing indexed uniform calculation. An alternative elementary verification does not leave a new exact invariant or gap for this record to fill.

The dated certificate retains the supplied scientific assessment, sources and limitations.
