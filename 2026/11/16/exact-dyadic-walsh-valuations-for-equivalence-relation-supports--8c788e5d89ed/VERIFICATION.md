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

Run `python verify_equivalence_walsh.py` (standard-library Python 3.9+). This script:

1. Reconstructs the modulo-eight Stirling residue-state transition and verifies \(M^{24}e_0-e_0=4(e_0+e_4)\), the closed six-step difference orbit, the 24 Bell residues and the class table.
2. Independently lists all set partitions for each \(2\le n\le7\); forms binary equivalence-relation edge vectors; performs integer Walsh butterflies over all \(2^{\binom n2}\) frequency graphs; checks each modular prediction and the rank conditions. The aggregate is 2,131,018 exact Fourier coefficients.
3. Computes 1,026 additional signed sums at \(n=8\) via a separate first-block signed-partition recurrence without enumerating those partitions or using Walsh butterflies.

Observed verification marker: `EQUIVALENCE_PARTITION_FOURIER_MOD8_PASS coefficients= 2131018 independent_n8_samples= 1026`.

The finite checks do not constitute proof of the infinite classification. The proof is the exact component-collapse expansion and eight-state modular-matrix argument recorded in `RESULT.md`. In particular no numerical experiments are used to claim anything about the unresolved odd-frequency multipliers when \(n\equiv2\pmod{12}\).
