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

The mathematical proof uses the orbit-complex identification and the affine-coset lemma, not a bound on finite enumeration. `verify_general.py` exhaustively enumerates the subgroup lattices and complete orbit nerves of fourteen Hamming products with unequal and composite factors. It tests 200 nontrivial subgroups, checks their connected components, and ensures that each is a full simplex of the predicted size. `verify_prime.py` separately tests 500 nontrivial vector-subspace actions in Hamming products over prime alphabets. Both programs use the Python standard library only.

Run `python3 verify_general.py` and `python3 verify_prime.py` after extracting the package. Their exact recorded outputs appear in `verify_general_output.txt` and `verify_prime_output.txt`. These tests are finite corroborations. They do not establish the assertion for unbounded parameters: the proof in `RESULT.md` does.

Full-text comparison with the motivating 2026 preprint was unavailable; the accessible abstract and two directly inspected closely related published mathematical findings support only a qualified originality assessment.
