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

Three standalone Python 3 programs substantiate the exact formula and its finite cases. Run them in a directory containing the three scripts, without third-party dependencies:

```
python verify_words.py
python verify_flows.py
python verify_identity.py
```

`verify_words.py` enumerates every binary word of lengths 1 through 16 and compares distinct cyclic trigram count vectors to the closed coefficient formula; it printed `WORDS_VERIFY_OK lengths=1..16`.

`verify_flows.py` independently enumerates balanced integer multiplicities on the four-vertex de Bruijn graph, tests actual support connectivity, and compares the count at each length 1 through 40; it printed `FLOWS_VERIFY_OK lengths=1..40`.

`verify_identity.py` performs integer polynomial multiplication to check equality of the four-support-case rational sum and the reduced rational function by cross multiplication; it printed `RATIONAL_IDENTITY_OK exact integer polynomial cross-multiplication`.

The proof in RESULT.md is not based on a finite cutoff: balanced and connected integral multigraphs admit Eulerian circuits for all positive lengths, and the support cases exhaust the possible parameters. The programs independently guard against combinatorial and algebraic transcription errors. No independent scientific audit or independent historical-priority certification has occurred.
