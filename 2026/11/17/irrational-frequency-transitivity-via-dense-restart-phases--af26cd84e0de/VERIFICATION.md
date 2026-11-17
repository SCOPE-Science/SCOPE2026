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

# Verification and reproducibility
The proof is in `RESULT.md`. Its central tests are (i) nonzero discrepancy at each tested finite prefix for irrational beta, (ii) exact closed-run formula \(e_m=\{e+eta m\}-1\), and (iii) density of irrational rotations, which permits the two target-prefix restart cases.

The included `checker.py` is standalone Python 3 and runs enumerations of admissible prefixes of lengths one through six for four irrational constants. Output observed: 1,849, 2,401, 1,849, and 1,369 successful ordered-pair connections, respectively; total 7,468. It performs finite floating-point numerical corroboration, not a proof of the density theorem or a verification for all irrational parameters. The strict-sign proof, not the script, handles the infinite quantifiers.

Published predecessor full text was not accessible through the inspected public sources, and independent checking has not been performed.
