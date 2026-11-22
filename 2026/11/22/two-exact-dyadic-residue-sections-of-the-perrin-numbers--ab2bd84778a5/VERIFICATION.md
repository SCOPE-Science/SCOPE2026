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

# Verification of the residue-section theorem

The proof uses exact matrices with entries in \(\mathbb Z\), not floating-point estimates. The two nonstandard certificates are the odd trace pairs \((5,17)\) and \((7,29)\) for the matrices \(B=(M^7-I)/2\) and \(C=(M^{14}-I)/4\). Repeated squaring proves that the normalized matrix after \(2^r\) powers retains \(C\pmod2\) for all \(r\ge1\). This gives the exact valuation for every positive index difference; negative differences follow by sign symmetry.

Run the embedded `check_perrin.py` using Python 3 without external dependencies. It verifies exact matrix products, trace identities, 9,900 parameter-pair comparisons, and both complete subsequence images for all moduli \(2^k\) with \(1\le k\le10\), alongside matrix-period checks. Its successful run reported 11,956 grouped checks. Exhaustive finite checks are used only as independent arithmetic corroboration: the all-depth claim is established by the proof in RESULT.md.

The result does not provide all full-period residue multiplicities; the full period can have multiple representations from other index classes. Only the two designated progressions are one-to-one. Complete historical priority and independent validation remain unestablished.
