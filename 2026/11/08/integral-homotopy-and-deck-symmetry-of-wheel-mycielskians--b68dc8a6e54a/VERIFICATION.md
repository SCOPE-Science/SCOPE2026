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

# Verification and limits

Run `python3 verify.py` with the Python 3 standard library. The script constructs the graph edges from definitions, enumerates all independent faces, constructs reduced simplicial boundary matrices over \(\mathbb F_2\), and computes their exact ranks without external symbolic libraries or network access. It verifies the cone-cover Betti splitting for all 75 labeled simple graphs on one to four vertices, checks wheel covers for \(n=5,6,7,8,9\), and checks six small direct Mycielskian constructions. Successful output ends with `ALL_VERIFY_OK wheel_covers=5 coned_graphs=75 mycielskians=6` and is saved in `verification_output.txt`.

The program checks finite mod-two Betti numbers only. It does not establish infinite-parameter formulas, integral torsion-freeness, attaching-map vanishing, or deck-module actions; these require the mathematical proof in `RESULT.md` and the cited general Mycielskian theorem. The deck-sign argument is an exact orientation calculation in an integral relative chain complex. A separate independent audit has not been performed.
