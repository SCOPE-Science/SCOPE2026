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

Run `python check_density.py` with standard Python 3. The included `density_check_output.txt` is its actual result. Exact rational calculations verify the prime-block minimality inequality at eleven sample prime indices, and a direct subset-sum algorithm verifies the Zumkeller partition property for the odd seed \(945\) and twenty-one multiples \(945(1+945t)\).

The full theorem does not follow from the finite checks. It depends on the published Somu–Kukla–Tran Lemma 3.3 that sufficiently late minimal prime blocks are Zumkeller, on the fixed-modulus prime number theorem, and on an exact Chinese-remainder-density calculation. The existence and positivity of the natural density do not require any unproved prime-density hypothesis. No independent mathematical audit has been performed.
