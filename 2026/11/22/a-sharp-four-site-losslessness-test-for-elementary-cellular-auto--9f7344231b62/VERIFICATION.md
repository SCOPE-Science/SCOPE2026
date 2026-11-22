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

The proof identifies the five effective truth-table bits from the forbidden-factor constraint. The three necessary conditions each have a literal two-, three-, or four-site periodic collision witness. Exactly 10 of 32 effective masks survive; each original Wolfram rule has eight assignments to the three local inputs that cannot occur.

The positive direction is independently checked by the 13 admissible five-bit input windows and the listed radius-one decoder identities. Their locality proves correctness for arbitrarily large rings and for bi-infinite inputs. The attached `verify.py` uses only Python's standard library and prints four `PASS` lines when all enumerations, identities, direct finite-ring checks and sharpness assertions succeed.

Verified test coverage: all 32 restricted tables; all 256 ordinary rules via table equivalence; all ten surviving decoders; all 22 excluded-table witnesses; every indexed admissible ring through 12 sites; sharp short exceptions. The bounded ring census is corroborating evidence only, not an infinite proof. Historical originality was evaluated against the cited papers and relevant published mathematical records. Independent audit is not performed.
