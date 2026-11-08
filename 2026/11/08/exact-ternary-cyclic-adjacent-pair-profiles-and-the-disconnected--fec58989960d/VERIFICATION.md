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

The exact generating function follows from an exhaustive split of balanced ternary directed frequency matrices by their common three-cycle flow and by the positive reciprocal edge pairs. The Eulerian-circuit criterion determines which balanced matrices are realized by a single circular word. This establishes the unbounded count independently of finite enumeration.

To check finite coefficients, run `python3 verify_words.py` and `python3 verify_matrices.py` using Python 3 and the standard library only. The first enumerates all indexed ternary words through length ten. The second enumerates all nine-entry nonnegative matrices of weights one through twelve and independently checks balance and connectivity, including every disconnected case. The programs assert exact matching counts and print `WORDS_VERIFY_OK n=1..10` and `MATRICES_VERIFY_OK n=1..12`.

These programs are finite consistency checks, not an unbounded proof. No claim is made that the listed asymptotic leading coefficient, general Markov-type framework, or the Eulerian-circuit criterion is new. Priority against unavailable full texts has not been independently established.
