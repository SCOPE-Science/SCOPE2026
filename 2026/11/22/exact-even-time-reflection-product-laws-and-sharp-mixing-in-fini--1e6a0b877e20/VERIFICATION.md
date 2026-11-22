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

# Verification record

The supplied `verify.py` enumerates the complete general- and special-linear matrix sets directly over the prime fields of orders \(3,5,7,11\) and over the extension field \(\mathbb F_9\), represented as \(\mathbb F_3[z]/(z^2+1)\). It checks all reflection matrices, pairwise product counts against the conic formula for every target, then forms explicit repeated pair convolutions and checks the complete pointwise distribution, total variation and chi-square as exact rational numbers. The length ranges checked are \(k=1,\ldots,4\) for \(q=3\), \(k=1,\ldots,3\) for \(q=5\), \(k=1,2\) for \(q=7,9\), and \(k=1\) for \(q=11\).

The complete captured output is `verification_output.txt`, ending in `ALL TESTS PASSED`. These checks do not certify all prime powers and all lengths; the general claim is proven separately using direct two-involution fibers and the complete complex character table for \(\operatorname{GL}_2(\mathbb F_q)\). The use of the character table is a mathematical premise from cited literature, not an independent validation. No independent audit has been performed.
