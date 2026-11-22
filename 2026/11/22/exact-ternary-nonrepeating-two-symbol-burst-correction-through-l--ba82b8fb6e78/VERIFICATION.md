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

# Reproduction of the finite capacity bounds

Place `codebooks.json`, `verify_balls.py` and `verify_structure.py` together in one directory. Run:

```sh
python3 verify_balls.py
python3 verify_structure.py
```

The first program directly enumerates all outputs of every listed word under all overwrite windows; `VERIFY_OK` reports no pairwise collisions. The second independently checks all difference-support conflicts, proper-input source counts and upper-bound interior fibers for lengths two through seven; it reports `ALTERNATE_OK`. The scripts are standalone and depend only on the standard Python library. Codewords are in `codebooks.json` and are reproduced verbatim.

The interior-projection theorem for unbounded word length and alphabet is proved algebraically in `RESULT.md`, not inferred from a finite computation. The short-block matching upper bounds are theoretical. There is no solver dependency, proof-assistant certificate or external validation. The source restriction is checked for every codeword, but outputs are deliberately unrestricted and include words with neighboring equal letters.
