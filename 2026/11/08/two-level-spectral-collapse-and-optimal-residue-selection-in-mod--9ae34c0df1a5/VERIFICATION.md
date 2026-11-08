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

# Verification details

The exact Gram entries were independently reconstructed from the full Walsh character matrix, not read back from the claimed formula, for \(n=5,6,7,8,9,10\) and each residue \(r=0,1,2\), giving 18 complete direct-matrix comparisons. The executable `artifacts/verify.py` computes the matrix polynomial that annihilates each observed Gram matrix at its predicted exact eigenvalues, and checks the first two trace moments to validate multiplicities. The checker separately verifies the three binomial-count identities and exact positivity/strict ratio inequalities for 408 parameter pairs \(5\le n\le140\), \(r\in\{0,1,2\}\). Expected and observed success marker: `MOD3_WALSH_SPECTRAL_VERIFY_PASS direct=18 exact=408`.

Run from a freshly extracted package root: `python artifacts/verify.py`. Python 3 standard library suffices. This script checks a finite range only. The analytical argument in `RESULT.md` establishes the general spectral identity, exact optimizer comparison, and the asymptotic; no independent human audit or formal proof verification has been performed.
