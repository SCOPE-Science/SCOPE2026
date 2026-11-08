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

The standalone `verify.py` is a self-contained ordinary Python 3 checker. Its `val(n)` tests the literal binary zero-run definition independently of the `legal_blocks(m)` generator, which constructs the candidate words by tiling with `1` and `00`.

Executed command: `python3 verify.py`.

Recorded result: `VERIFY_OK: all binary-length layers 1..20, 6765 indices <2^18, 17 distinct return gaps`.

Tests include exact Fibonacci cardinalities and full adjacent-gap multiplicities for all positive binary lengths through 20; direct enumeration of membership for all lengths through 16; and the complete set of direct integer consecutive gaps below \(2^{18}\). The proof in `RESULT.md` handles all larger lengths by the unique tiling representation, rightmost-tile successor lemma, and the Fibonacci identity. Numerical checks do not constitute an independent audit or an infinite proof.
