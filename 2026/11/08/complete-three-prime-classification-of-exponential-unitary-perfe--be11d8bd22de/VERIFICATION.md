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

The proof uses only elementary divisor inequalities, parity, multiplicativity and integer divisibility. The attached file `artifacts/verify.py` is standalone and uses the Python 3 standard library. From the directory containing this document, execute `python3 artifacts/verify.py`.

The completed script printed:

`VERIFY_OK local_bound=319 squarefull_triples=184320 exact_solutions=[(2, 2, 3, 3, 5, 2), (2, 3, 3, 2, 5, 2)] direct_interval=2..350000 ternary_count=1199 core_36=PASS`

The code tests every squarefull three-prime pattern in its declared finite range; it is not an infinite certificate. The proof, specifically the strict \(39/20<2\) bound and two equality cases, handles all larger parameters. No independent mathematical audit has been performed.
