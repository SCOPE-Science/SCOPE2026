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

The algebra table and the derivation-equation matrix are specified without external computer-algebra software. `verify.py` carries out integral multiplication checks and exact Bareiss determinant calculations for the two rank certificates. The two minors are critical because a finite sample of field sizes cannot prove an all-characteristic dimension claim. Explicit central maps, together with the two characteristic-two derivations, complete the upper and lower rank arguments.

The script also computes ordinary derivation kernels and all pointwise linear-local constraints over four fields, including the nonprime field \(\mathbb F_4\). The resulting \((\dim\operatorname{Der},\dim\operatorname{LocDer})\) pairs are \((6,7)\) in characteristic two and \((4,4)\) in odd characteristic. The general linear-local classification is established by the direct proof in `RESULT.md`, independently of these tests.

Run `python3 verify.py` and require the final marker `ZINBIEL_LOCAL_MODULAR_OK`. The existence of this check is not a claim of third-party mathematical certification. Historical-priority uncertainty and the restriction to linear local derivations remain.
