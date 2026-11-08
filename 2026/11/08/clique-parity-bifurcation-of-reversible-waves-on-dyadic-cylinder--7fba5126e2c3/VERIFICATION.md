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

The algebraic proof is given in `RESULT.md`, Steps 1–5. The programs in this package provide finite checks and do not constitute an infinite proof.

Run `python3 verify_algebra.py` and `python3 verify_direct.py`. Captured standard output is provided respectively in `verify_algebra.out` and `verify_direct.out`.

`verify_algebra.py` constructs exact binary adjacency and two-row wave matrices independently of the symbolic decomposition. It checks the predicted adjacency annihilating polynomial, exact global order by testing the two prime factors of the proposed order, and 438 exact fixed-space nullities for \(r=3,4,5\), \(m=3,4,5\).

`verify_direct.py` updates states by iterating graph neighbors instead of using matrix powers. It exactly enumerates the 65,536 paired states of an eight-vertex boundary graph, then checks 60,000 deterministic pseudorandom states on four in-scope graphs. These finite checks do not cover every parameter or state. The proof covers all integers \(r\geq3\), \(m\geq3\), every finite \(q=2^f\), and every positive integer time.

The rational cyclic-module description remains valid even when \(X^2+X+1\) splits over the larger characteristic-two field. No test is described as independent expert validation.
