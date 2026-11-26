---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For one r-set the probability is its internal class probability times q^{r(n-r)}, q=1-p. Distinct sizes rule out any shared vertex in the mixed product. A disjoint pair has independent internal events and the sum of the two separate absent-edge counts minus rs, because the cross edges are counted twice. There are binom(n,r)binom(n-r,s) ordered disjoint pairs; dividing by the positive means gives R q^{-rs}. This is strictly increasing from R<1 to infinity, while r+s>n gives a zero mixed moment and strictly negative covariance. The inverse of R telescopes as the product of (n-i-j)/(n-i-j-1) over 0≤i<r, 0≤j<s. Every factor is at least n/(n-1) and at least one is larger. The logarithmic mean of the same factors is 1/n+(r+s-1)/(2n²)+O(n^-3), yielding the stated threshold expansion on exponentiating. The sample n=6, (r,s)=(1,2) gives R=2/3. VERIFICATION.md and verify.py were inspected, not executed; the recorded finite enumerations are not needed for the proof.

## originality

FAIL

A distinct same-day indexed record already gives the equivalent finite-n covariance bracket, threshold, expansion and the log product implying the strict critical inequality. Summing over isomorphism types recovers the proposed class form exactly. Distinct scientific content is not established; this judgment does not assign chronological priority between the two records.

## value

FAIL

A finite classification about the sign at p=1/n is a natural question. But against the inspected exact distinct-type formula and log product, this version adds only linear summation over types and a direct comparison of the same factors. It supplies no independently useful new invariant or meaningful new threshold phenomenon beyond the existing classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
