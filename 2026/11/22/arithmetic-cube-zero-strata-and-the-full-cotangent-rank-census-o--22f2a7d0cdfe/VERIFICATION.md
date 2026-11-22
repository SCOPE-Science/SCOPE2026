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

# Verification procedure and limits

Run `python3 verify.py` in the extracted package directory. The script uses the standard library only, enumerates all degree-two coefficient sextuples for fields of orders \(2,3,4,5,7,8\), directly cubes 950 seeded general ring elements, and checks the complete cotangent-rank count identities. For the two binary extension fields, multiplication is defined by irreducible polynomials, not by integer modular arithmetic. The captured output file is `verification_output.txt`; its final line is `VERIFY_OK direct_quadratics=6 sampled_powers=950 rank_profiles=6`.

The infinite-family theorem depends on the written proof's coefficient identifications and binary-quadratic zero-count, not on finite enumeration. The program checks only a bounded sample of rings and cube-zero elements, and does not independently verify historical priority. The only mathematical assessment recorded is the self-review; no independent audit has been performed.
