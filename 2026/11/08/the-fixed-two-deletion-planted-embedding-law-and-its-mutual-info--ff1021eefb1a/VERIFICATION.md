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

The proof uses the run-separation lemma and an iid two-site neighborhood coupling. `checker.py` independently enumerates all deletion pairs of small q-ary words, verifying the local run product identity and the exact entropy identity by summing the induced output probabilities. Run `python3 checker.py` using Python 3.10+ standard library. These checks are finite corroboration, not certification of the infinite total-variation or entropy-limit claims. The bound C_q is not optimized; external validation has not been carried out.
