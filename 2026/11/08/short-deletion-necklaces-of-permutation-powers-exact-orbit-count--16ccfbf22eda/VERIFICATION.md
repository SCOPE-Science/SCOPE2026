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

# Reproducible checks

The accompanying `verify.py` uses only the Python standard library. Run `python verify.py`. Its exhaustive checks cover every integer \(2\le q\le6\), \(2\le k\le4\), and \(0\le t\le q\). For each deletion mask it constructs the distinct cyclic output by canonical rotation and independently constructs the orbit of the mask under whole-period rotations. It verifies the divisor-sum formula, injectivity for \(t<q\), and that the sole non-singleton orbit fiber at \(t=q\) is \([P^{k-1}]\) of size \(q\). The executed output was: `PASS configurations=75 deletion_masks=255038`.

The proof is purely combinatorial and applies to unbounded \(q,k\) in the declared range. The above finite verification tests code-level fidelity and boundary examples; it neither exhausts all parameters nor independently establishes novelty. Independent audit has not been performed.
