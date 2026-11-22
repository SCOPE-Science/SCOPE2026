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

# Reproducibility and verification

Run `python square_torus_verify.py` using Python 3. The executable script constructs a direct path-concatenation product, enumerates all nonzero degree-two target fibers for a specified list of finite fields and cycle lengths, compares these fibers to a separately implemented theorem formula, and checks exact relative image counts. The script's recorded output is in `verify_output.txt`. A successful replay ends with `NAKAYAMA_SQUARE_TORUS_OK`.

The tested sizes are cyclic lengths 3 to 6, field orders 2, 3, 4 and 5 in the configurations recorded in the output; an irreducible-polynomial model supplies genuine extension-field arithmetic at order 4. The free length-three coefficients contribute a known factor of \(q^n\) and are accounted for analytically rather than brute-forced. The proof itself works in all finite fields with \(n\ge3\), irrespective of whether they occur in the tests.

Verification limitations: finite tests do not establish the general theorem, and there is no independent audit or external proof certification. The paper's proof establishes generality by a cyclic scalar recurrence and an exact rank/kernel analysis.
