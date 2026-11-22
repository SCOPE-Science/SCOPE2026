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

Execute `python3 kummer_frobenius_verifier.py kummer_frobenius_certificate.json` (Python standard library). The program reconstructs all 256 entries of the Kummer incidence matrix, verifies the \((16_6)\) design identity and the automorphism property for all eleven \(S_6\) classes, builds every rectangular integer presentation from the 31-node reduced Laplacian and Frobenius action, and replays the complete collection of elementary unimodular row/column operations. It checks zero off-diagonals, positive invariant factors, their integer divisibility chain and all eleven exact orders. Expected output: `KUMMER_FROBENIUS_ALL_ELEVEN_INTEGRAL_FIXED_GROUPS_OK`.

Each matrix is exact and full rank; no finite sample is used to infer the classification. The identity order is additionally checked against the known spanning-tree formula. Proof of the fixed/coinvariant invariant-factor equality is via the canonical automorphism-invariant perfect graph monodromy pairing, not via an unverified identification of the two groups as subsets. The geometric incidence references do not constitute independent priority certification. Independent mathematical audit has not been performed.
