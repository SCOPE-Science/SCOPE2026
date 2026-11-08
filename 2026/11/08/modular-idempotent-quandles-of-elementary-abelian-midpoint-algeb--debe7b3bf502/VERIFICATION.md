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

# Reproducibility checks and limitations

Run `python3 check_idempotents.py` in the extracted artifact directory. The checker directly evaluates the structure constants of \(e_xe_y=e_{(x+y)/2}\) for every coefficient vector over specified small finite fields. It does not reuse the formula being checked to choose which vectors to test.

Exact exhaustive checks: \((p,r,q)=(3,1,3),(5,1,5),(3,2,3),(7,1,7),(3,1,9)\). Their total idempotent counts are \(4,6,82,50,10\). For prime-field cases the script also verifies the split into one augmentation-zero idempotent and the remaining augmentation-one idempotents. For \(p=3,r=1; p=5,r=1; p=3,r=2\), all ordered pairs of augmentation-one idempotents were tested for closure under the quandle-algebra product. For \(q=9\), the script uses the explicit multiplication in \(\mathbb F_3[t]/(t^2+1)\).

The file `verification_output.txt` is the actual recorded program output and ends in `VERIFY_OK`. The unbounded-rank and arbitrary-field assertions are derived symbolically via the group-ring filtration and cyclic representation splitting, not certified by finite enumeration. No independent external validation is claimed.
