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

## Reproducible checks and scope
Run `python3 verify_trinomial_residues9.py` with standard-library Python 3. The program independently derives exact central trinomial numbers from the integer recurrence \((n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}\), validates all \(6561\) residues for \(0\le n<3^8\), and tests all nine frequency counts at each \(L\in\{0,\ldots,8\}\). Expected executed output: `VERIFY_OK exact_terms=6561 block_censuses=0..8 digit_formula=PASS`.

The infinite result depends on the exact modulo-nine Laurent-coefficient recurrences, the binary sentinel-transition bijection, and a roots-of-unity computation. None of the finite enumerations proves an unbounded claim. Published literature supplies the zero-residue census and general modular-automatic methods; originality of the remaining explicit classes and sharp error has only a literature-supported, self-review, with residual priority uncertainty. No external audit or certificate is represented.
