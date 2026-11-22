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

# Verification record

Run `python3 verify.py` in the same directory as the other files. The checker uses only the Python standard library and reconstructs crossing events from cyclic endpoint alternation, rather than calling the formulas being tested to determine graph statistics.

The execution of the standalone checker passed 311,034 exact assertions: all perfect matchings with up to seven chords were enumerated and compared to the complete binomial-moment formula, while every permutation with up to seven letters was enumerated as a matching conditioned on one specified universal diameter. The code checked the conditional crossing and additional-hub identities and independently calculated exact means and variances. Each matchings family was also checked against its double-factorial population.

The general count identity rests on the opposite-sector pairing bijection in `RESULT.md`. The normal limit uses the independent inversion-sequence representation and Lindeberg's theorem; the existence-conditioned transfer uses a proven total-variation bound. Finite enumeration verifies small cases, not the asymptotic statements.

Potential limitations include historical priority under older equivalent permutation enumeration and the absence of an explicit quantitative normal-approximation error bound. No claim of external or independent certification is made.
