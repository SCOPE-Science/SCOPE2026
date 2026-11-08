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

# Analytical and finite verification

The analysis proves: (i) the normalized angular beta-moment identity for all integer degrees; (ii) orthogonality and invariance of the axial/ideal decomposition for the three canonical boundary measures; (iii) exact shift weights and the positive self-commutator eigenvalues; (iv) the trace, sharp \(S_q\) cutoff for all real \(q>0\), and exact critical counting/logarithmic constants; (v) the generating-function differential equation and the axial kernel asymptotics. No finite search substitutes for any of these proofs.

The included Python 3 standard-library checker `pentablock_axial_check.py` was executed with the expected output `PENTABLOCK_AXIAL_EXACT_CHECKS_OK 3723`. It performs 3,723 exact-rational and supplementary floating-point assertions, checking moment identities, weight differences, trace telescoping and the first 350 generating-function coefficients. It checks finitely many parameters only and cannot certify a general theorem by itself. Reproduce with `python3 pentablock_axial_check.py`.

No independent mathematical audit or literature-priority certification has been performed. The paper's individual-coordinate commutator on the full Hardy space is not addressed; the restriction to the reducing axial summand is explicit and essential.
