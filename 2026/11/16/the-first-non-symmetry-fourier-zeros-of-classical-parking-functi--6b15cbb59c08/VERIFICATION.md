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

The finite classification was checked with two separate exact-integer algorithms. `check_orbits.py` enumerates 252 sorted frequency representatives for five cars using distinct permutations of 42 nondecreasing parking functions, and reduces residue-count polynomials modulo cyclotomic polynomials. Its 252 exact pairs at modulus six reproduce the included `ORBIT_CERTIFICATE.tsv`. `check_tensor.py` independently computes every character coefficient by repeated one-dimensional transforms in integer cyclotomic quotient rings, including all 7776 characters in the five-car case.

Both were run with Python 3 and passed all built-in assertions. The cases with one through four cars also passed, with no extra zeros. The arithmetic and orbit coverage are exact; this is a bounded computation, not a general theorem for larger sizes. The algebraic proof of symmetry-forced zeros is included in `RESULT.md`. External independent validation has not been performed.
