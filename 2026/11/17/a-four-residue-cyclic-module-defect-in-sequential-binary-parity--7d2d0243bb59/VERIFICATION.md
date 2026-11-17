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

# Verification and scope

The included `checks/verify.py` requires only Python 3 and its standard library. Run `python3 checks/verify.py` from the package root. The program builds the actual hub-first sweep from its binary adjacency graph rather than calling the symbolic determinant proof, checks exact matrix polynomials and fixed-power nullities, and enumerates all states for small rim lengths.

The stored output `checks/verification_output.txt` was produced from this code. The checker reports 22 determinant comparisons for rim sizes 4–25, 77 minimal-polynomial comparisons for 4–80, 1,078 fixed-power kernel comparisons, and full functional graphs for n=4–10 (4,064 labelled initial states). All reported checks passed. The all-parameter assertions are deduced instead from the symbolic three-row determinant elimination and elementary-divisor proof in `RESULT.md`.

No independent mathematical validation or certification has been performed. The historical-originality search was finite and cannot rule out unindexed equivalent results. The finding applies to a fixed scan order and does not cover arbitrary scans or synchronous dynamics.
