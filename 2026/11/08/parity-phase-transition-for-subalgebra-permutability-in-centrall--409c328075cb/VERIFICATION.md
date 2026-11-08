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

# Verification summary

Run `python3 artifacts/verify.py` from the extracted research-artifact directory. The program requires only the Python standard library and independently enumerates all ambient vector subspaces in reduced row-echelon form; each candidate is tested against the bilinear Lie bracket, and every pair of resulting subalgebras is tested by direct linear-algebra rank. It then compares with the Gaussian-binomial expression. It includes an explicit representation of \(\mathbb F_4\) and checks configurations \((r,q)\) equal to \((0,2),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(3,2)\).

The observed output is embedded in `artifacts/verification_output.txt` and ends in `VERIFY_OK cases= 9 subspaces_examined= 1339`. For the new domain's first instance, \((r,q)=(3,2)\), the exhaustive direct calculation gives \(220\) subalgebras and \(6636\) nonpermuting ordered pairs. The exact formulas for all \(r\ge3\) and their fixed-rank asymptotic limits depend on the symbolic proof, not extrapolation from these finite tests.

These are self-review results; no independent mathematical audit has been performed.
