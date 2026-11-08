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

Run `python check_scroll_dual.py` using Python 3.10+ and SymPy. The included `verification_output.txt` is a captured successful execution, ending in `ALL_CHECKS_PASSED`.

The script verifies all coefficient derivatives and the factorization when the prime divides the degree for `n=2,...,8` and primes `2,3,5,7`, verifies the expected generic graded length formula, checks the existence of irreducible residue-field polynomials in six sample cases relevant to the conductor argument, and exhaustively counts projective rational points for `(q,n)=(2,2),(2,3),(3,2),(3,3),(5,2)`.

The exact source is in `check_scroll_dual.py`, with no hidden inputs or downloads. Finite computations do not establish irreducibility of the universal polynomial or the arbitrary-degree conductor formula; those are proved directly in `RESULT.md`. They also do not prove originality. In particular the full text of Piene–Sacchiero (1984), a plausible historical antecedent, was unavailable.

Independent scientific validation: not performed.
