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

The complete claim uses an external published classification into 186 isomorphism classes and the explicit filtered-socle lemma in RESULT.md. The standalone `frobenius_socle_checker.py` reconstructs quotient-algebra operations by spanning the two-sided relations inside truncated free associative algebras over \(\mathbb F_2\). It checks that exactly 18 of the 19 characteristic-two rings have a one-dimensional left/right socle, with ring 7 having a two-dimensional socle. It computes all 17 graded presentations for the remaining 184 rings and verifies every complementary top-product matrix has full rank.

Invocation: `python3 frobenius_socle_checker.py` (Python 3 standard library; no downloads, third-party packages or unspecified paths). Expected terminal line: `REVERSIBLE_256_SOCLE_CERTIFICATE_OK`.

The computation is exhaustive over the source's stated graded model list, not an independently complete 186-ring classification. The two-dimensional terminal radical layer of ring 20 is obtained from the source's Hilbert vector, without a direct characteristic-four multiplication-table enumeration. No external validation or independent audit was performed.
