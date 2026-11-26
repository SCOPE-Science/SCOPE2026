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

The unique word decomposition into initial, internal and terminal b-gaps gives avoidance exactly when the total k in internal gaps is at most r−1: the first and last a witness any sufficient total. An internal b in gap i contributes i to the ab-count and a terminal b contributes A. Sorting the k internal gap indices and subtracting one from each gives partitions in a k by (A−2) rectangle, verifying the Gaussian factor and exponent offset, including k=0. Reversal sends C to AB−C; putting all b after the a achieves degree AB. At r=2, the k=0 and k=1 cases partition the residue classes modulo A (only k=0 when B=0). When r>B avoidance is vacuous. In the unrestricted model the weakly sorted counts of b following successive a are partitions in an A by B rectangle, with every area possible by filling rows plus one partial row; the ratio is for uniform sampling in the class. For A=2, e=(C−k)/2 and k+e≤B give the stated parity and cutoff. For even r the saturated cutoff contains equal counts of the two parities; for odd r=2s+1 the three coefficients at r−1,r,r+1 are s+1,s,s+1, also when B=r. The universal proof suffices; the packaged finite checks were inspected, not rerun.

## originality

FAIL

The October 18 catalogue record states the entire same enumerator for r≥3 and uses the same interior-gap proof. The two-a unimodality boundary is read directly from its coefficients. The remaining r=1 and r=2 cases are respectively the zero-gap and at-most-one-gap cases; the already acknowledged r=2 singleton boundary does not distinguish the claim.

## value

FAIL

An exact fixed-composition avoidance law could be useful, but that law is already available. The additional parity observation is obtained by reading the earlier enumerator at A=2, and the only extra parameter endpoints are immediate gap counts. No distinct, independently useful remainder is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
