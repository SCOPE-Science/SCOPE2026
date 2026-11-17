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
# Reproducible verification

`check_sg_gini.py` is the standalone, standard-library-only checker. Its complete integer enumeration covers every cut of the four finite base rings (\(n=5,6,7,8\)), so those finite calculations can be independently inspected or rerun. The code derives the Gini pair sums directly, not through a floating-point matrix norm or a borrowed output table.

It verifies the kernel's constant, linear and quadratic reproduction; each of the exact norms \(6/7\), \(101/105\), \(69/70\), and \(251/245\); all 472 binary cuts; and the general singleton formula in the first 96 allowed sizes. The unrestricted singleton identity and the asymptotic envelope are proved symbolically in `RESULT.md` and are not claimed to follow from checking 96 examples. Every real input is covered by the analytical layer-cake lemma.

The displayed numerical and finite-cut outputs are reproducible same-model evidence, not independent audit or proof of historical originality.
