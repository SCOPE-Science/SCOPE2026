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

Run `python3 verify_coupon.py` with Python 3 and no third-party packages. Its exact dynamic program independently conditions on the next sampled type, includes all self-loops when the type's multiplicity exceeds the tracked level, and computes both terminal exact-frequency count and its mixed stopped-draw moment. It agrees with the exponential-moment formula for all \(2\le n\le8\) and \(1\le r\le6\), checks strictly increasing moment ratios for \(2\le n\le32\) and \(1\le r\le12\), and checks the \(n=2,r=2\) equality boundary.

Expected output: `PASS: 457 exact assertions; independent truncated-count state recursion versus Poissonized moments`.

The checker corroborates finitely many instances only. The arbitrary-size exact formula is proved by independent Poisson processes and a beta-transform density, and the asymptotic location of the sign transition is established analytically by exponential-moment bounds and uniform integrability. No numerical result is used as an infinite proof, and no external or independent audit was performed.
